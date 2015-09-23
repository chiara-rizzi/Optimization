import argparse
import subprocess
import os


'''
TO DO:
  - automatically grab the parsers from optimize.py instead of copying them over...
'''

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter):
  pass

__version__ = subprocess.check_output(["git", "describe", "--always"], cwd=os.path.dirname(os.path.realpath(__file__))).strip()
__short_hash__ = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=os.path.dirname(os.path.realpath(__file__))).strip()

parser = argparse.ArgumentParser(description='Author: G. Stark. v.{0}'.format(__version__),
                                 formatter_class=lambda prog: CustomFormatter(prog, max_help_position=30))
parser.add_argument('files', type=str, nargs='+', metavar='<file.root>', help='ROOT files containing the optimization ntuples')
parser.add_argument('--supercuts', required=True, type=str, dest='supercuts', metavar='<file.json>', help='json dict of supercuts to generate optimization cuts to apply')
parser.add_argument('--output', required=False, type=str, dest='output', metavar='', help='name of directory to keep all generated outputs', default='n-1')

parser.add_argument('--tree', type=str, required=False, dest='tree_name', metavar='<tree name>', help='name of the tree containing the ntuples', default='oTree')
parser.add_argument('--eventWeight', type=str, required=False, dest='eventWeightBranch', metavar='<branch name>', help='name of event weight branch in the ntuples. It must exist.', default='event_weight')

# parse the arguments, throw errors if missing any
args = parser.parse_args()

import json
from itertools import combinations
import operator
import optimize
import ROOT

supercuts = json.load(file(args.supercuts, 'r'))

differences = []
level = 0
c = ROOT.TCanvas("canvas", "canvas", 500, 500)
for subercuts in combinations(supercuts, len(supercuts)-1):
  level += 1
  # hold the differences and create a text file with them later for reference
  # use integers to denote them
  differences.append([x for x in supercuts if x not in subercuts][0])
  # now that we have a sub-supercuts, let's actually do_cuts
  subercutsFile = os.path.join(args.output, '{0:d}.json'.format(level))
  with open(subercutsFile, 'w+') as f:
    f.write(json.dumps(subercuts, sort_keys=True, indent=4))

  # get the tree
  tree = optimize.get_ttree(args.tree_name, args.files, args.eventWeightBranch)

  # get the selection we apply to draw it
  selection = optimize.cuts_to_selection(subercuts)
  # get the branch we need to draw
  selection_string = differences[-1]['selections']

  branchesSpecified = set(optimize.selection_to_branches(selection_string, tree))
  # get actual list of branches in the file
  availableBranches = optimize.tree_get_branches(tree, args.eventWeightBranch)
  # remove anything that doesn't exist
  branchesToUse = [branch for branch in branchesSpecified if branch in availableBranches]

  # more than one branch, we skip and move to the next
  if len(branchesToUse) != 1:
    print("Warning: selection has multiple branches.\n\tSelection: {0}".format(selection_string))
    level -= 1
    del differences[-1]
    continue

  # draw with selection and branch
  tree.Draw(branchesToUse[0], '{0:s}*{1:s}'.format(args.eventWeightBranch, selection))

  # write to file
  c.SaveAs('{0}_{1}.pdf'.format(os.path.join(args.output, str(level)), branchesToUse[0]))
  c.Clear()