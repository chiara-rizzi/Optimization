import json
import glob
import os
import re
import copy
import numpy

# write scalefactor in ifb
scaleFactor = 10

# edit with the path to the files you're looking at, so we can figure out did to group mapping
pathToFiles = r'/faxbox2/user/mleblanc/multib_ichep2k16/hf_tag2.4.11-0-0/optin/'
#pathToFiles = r'/home/mleblanc/Optimization/input/temp/'

# this holds a list of various subset of counts
count_types = ['raw', 'weighted', 'scaled']

# this holds a structure of a group with the control region counts and signal region counts
groups = {}

# get the did to group mapping
files = glob.glob(os.path.join(pathToFiles, "*.root"))
#p = re.compile(os.path.join(pathToFiles, r'.*(\d{6}).*root'))
did_to_group = {}

#for f in files:
#  group, did = p.search(f).groups()
#  if 'ttbar' in group: group = 'ttbar'
#  did_to_group[did] = group

did_to_group['361081'] = 'diboson'
did_to_group['361082'] = 'diboson'
did_to_group['361083'] = 'diboson'
did_to_group['361084'] = 'diboson'
did_to_group['361085'] = 'diboson'
did_to_group['361086'] = 'diboson'
did_to_group['361087'] = 'diboson'
did_to_group['361091'] = 'diboson'
did_to_group['361092'] = 'diboson'
did_to_group['361093'] = 'diboson'
did_to_group['361094'] = 'diboson'
did_to_group['361095'] = 'diboson'
did_to_group['361096'] = 'diboson'
did_to_group['361097'] = 'diboson'

did_to_group['361300'] = 'Wjets'
did_to_group['361301'] = 'Wjets'
did_to_group['361302'] = 'Wjets'
did_to_group['361303'] = 'Wjets'
did_to_group['361304'] = 'Wjets'
did_to_group['361305'] = 'Wjets'
did_to_group['361306'] = 'Wjets'
did_to_group['361307'] = 'Wjets'
did_to_group['361308'] = 'Wjets'
did_to_group['361309'] = 'Wjets'
did_to_group['361310'] = 'Wjets'
did_to_group['361311'] = 'Wjets'
did_to_group['361312'] = 'Wjets'
did_to_group['361313'] = 'Wjets'
did_to_group['361314'] = 'Wjets'
did_to_group['361315'] = 'Wjets'
did_to_group['361316'] = 'Wjets'
did_to_group['361317'] = 'Wjets'
did_to_group['361318'] = 'Wjets'
did_to_group['361319'] = 'Wjets'
did_to_group['361320'] = 'Wjets'
did_to_group['361321'] = 'Wjets'
did_to_group['361322'] = 'Wjets'
did_to_group['361323'] = 'Wjets'
did_to_group['361324'] = 'Wjets'
did_to_group['361325'] = 'Wjets'
did_to_group['361326'] = 'Wjets'
did_to_group['361327'] = 'Wjets'
did_to_group['361328'] = 'Wjets'
did_to_group['361329'] = 'Wjets'
did_to_group['361330'] = 'Wjets'
did_to_group['361331'] = 'Wjets'
did_to_group['361332'] = 'Wjets'
did_to_group['361333'] = 'Wjets'
did_to_group['361334'] = 'Wjets'
did_to_group['361335'] = 'Wjets'
did_to_group['361336'] = 'Wjets'
did_to_group['361337'] = 'Wjets'
did_to_group['361338'] = 'Wjets'
did_to_group['361339'] = 'Wjets'
did_to_group['361340'] = 'Wjets'
did_to_group['361341'] = 'Wjets'
did_to_group['361342'] = 'Wjets'
did_to_group['361343'] = 'Wjets'
did_to_group['361344'] = 'Wjets'
did_to_group['361345'] = 'Wjets'
did_to_group['361346'] = 'Wjets'
did_to_group['361347'] = 'Wjets'
did_to_group['361348'] = 'Wjets'
did_to_group['361349'] = 'Wjets'
did_to_group['361350'] = 'Wjets'
did_to_group['361351'] = 'Wjets'
did_to_group['361352'] = 'Wjets'
did_to_group['361353'] = 'Wjets'
did_to_group['361354'] = 'Wjets'
did_to_group['361355'] = 'Wjets'
did_to_group['361356'] = 'Wjets'
did_to_group['361357'] = 'Wjets'
did_to_group['361358'] = 'Wjets'
did_to_group['361359'] = 'Wjets'
did_to_group['361360'] = 'Wjets'
did_to_group['361361'] = 'Wjets'
did_to_group['361362'] = 'Wjets'
did_to_group['361363'] = 'Wjets'
did_to_group['361364'] = 'Wjets'
did_to_group['361365'] = 'Wjets'
did_to_group['361366'] = 'Wjets'
did_to_group['361367'] = 'Wjets'
did_to_group['361368'] = 'Wjets'
did_to_group['361369'] = 'Wjets'
did_to_group['361370'] = 'Wjets'
did_to_group['361371'] = 'Wjets'

did_to_group['363102']='Zjets'
did_to_group['363103']='Zjets'
did_to_group['363104']='Zjets'
did_to_group['363105']='Zjets'
did_to_group['363106']='Zjets'
did_to_group['363107']='Zjets'
did_to_group['363108']='Zjets'
did_to_group['363109']='Zjets'
did_to_group['363110']='Zjets'
did_to_group['363111']='Zjets'
did_to_group['363112']='Zjets'
did_to_group['363113']='Zjets'
did_to_group['363114']='Zjets'
did_to_group['363115']='Zjets'
did_to_group['363116']='Zjets'
did_to_group['363117']='Zjets'
did_to_group['363118']='Zjets'
did_to_group['363119']='Zjets'
did_to_group['363120']='Zjets'
did_to_group['363121']='Zjets'
did_to_group['363122']='Zjets'
did_to_group['363361']='Zjets'
did_to_group['363362']='Zjets'
did_to_group['363363']='Zjets'
did_to_group['363364']='Zjets'
did_to_group['363365']='Zjets'
did_to_group['363366']='Zjets'
did_to_group['363367']='Zjets'
did_to_group['363368']='Zjets'
did_to_group['363369']='Zjets'
did_to_group['363370']='Zjets'
did_to_group['363371']='Zjets'
did_to_group['363372']='Zjets'
did_to_group['363373']='Zjets'
did_to_group['363374']='Zjets'
did_to_group['363375']='Zjets'
did_to_group['363376']='Zjets'
did_to_group['363377']='Zjets'
did_to_group['363378']='Zjets'
did_to_group['363379']='Zjets'
did_to_group['363380'] = 'Zjets'
did_to_group['363381'] = 'Zjets'
did_to_group['363382'] = 'Zjets'
did_to_group['363383'] = 'Zjets'
did_to_group['363384'] = 'Zjets'
did_to_group['363385'] = 'Zjets'
did_to_group['363386'] = 'Zjets'
did_to_group['363387'] = 'Zjets'
did_to_group['363388'] = 'Zjets'
did_to_group['363389'] = 'Zjets'

did_to_group['363331']='Wjets'
did_to_group['363331']='Wjets'
did_to_group['363332']='Wjets'
did_to_group['363332']='Wjets'
did_to_group['363333']='Wjets'
did_to_group['363334']='Wjets'
did_to_group['363334']='Wjets'
did_to_group['363335']='Wjets'
did_to_group['363336']='Wjets'
did_to_group['363336']='Wjets'
did_to_group['363337']='Wjets'
did_to_group['363337']='Wjets'
did_to_group['363338']='Wjets'
did_to_group['363338']='Wjets'
did_to_group['363339']='Wjets'
did_to_group['363340']='Wjets'
did_to_group['363341']='Wjets'
did_to_group['363342']='Wjets'
did_to_group['363343']='Wjets'
did_to_group['363344']='Wjets'
did_to_group['363345']='Wjets'
did_to_group['363346']='Wjets'
did_to_group['363347']='Wjets'
did_to_group['363348']='Wjets'
did_to_group['363349']='Wjets'
did_to_group['363350']='Wjets'
did_to_group['363351']='Wjets'
did_to_group['363352']='Wjets'
did_to_group['363353']='Wjets'
did_to_group['363354']='Wjets'

did_to_group['363400'] = 'Zjets'
did_to_group['363401'] = 'Zjets'
did_to_group['363402'] = 'Zjets'
did_to_group['363403'] = 'Zjets'
did_to_group['363404'] = 'Zjets'
did_to_group['363405'] = 'Zjets'
did_to_group['363406'] = 'Zjets'
did_to_group['363407'] = 'Zjets'
did_to_group['363408'] = 'Zjets'
did_to_group['363409'] = 'Zjets'
did_to_group['363410'] = 'Zjets'
did_to_group['363411'] = 'Zjets'
did_to_group['363412'] = 'Zjets'
did_to_group['363412'] = 'Zjets'
did_to_group['363413'] = 'Zjets'
did_to_group['363414'] = 'Zjets'
did_to_group['363415'] = 'Zjets'
did_to_group['363416'] = 'Zjets'
did_to_group['363417'] = 'Zjets'
did_to_group['363418'] = 'Zjets'
did_to_group['363419'] = 'Zjets'
did_to_group['363420'] = 'Zjets'
did_to_group['363421'] = 'Zjets'
did_to_group['363422'] = 'Zjets'
did_to_group['363423'] = 'Zjets'
did_to_group['363424'] = 'Zjets'
did_to_group['363425'] = 'Zjets'
did_to_group['363426'] = 'Zjets'
did_to_group['363427'] = 'Zjets'
did_to_group['363428'] = 'Zjets'
did_to_group['363429'] = 'Zjets'
did_to_group['363430'] = 'Zjets'
did_to_group['363431'] = 'Zjets'
did_to_group['363432'] = 'Zjets'
did_to_group['363433'] = 'Zjets'
did_to_group['363434'] = 'Zjets'
did_to_group['363435'] = 'Zjets'
did_to_group['363436'] = 'Wjets'
did_to_group['363437'] = 'Wjets'
did_to_group['363438'] = 'Wjets'
did_to_group['363439'] = 'Wjets'
did_to_group['363440'] = 'Wjets'
did_to_group['363441'] = 'Wjets'
did_to_group['363441'] = 'Wjets'
did_to_group['363442'] = 'Wjets'
did_to_group['363443'] = 'Wjets'
did_to_group['363443'] = 'Wjets'
did_to_group['363443'] = 'Wjets'
did_to_group['363444'] = 'Wjets'
did_to_group['363445'] = 'Wjets'
did_to_group['363446'] = 'Wjets'
did_to_group['363447'] = 'Wjets'
did_to_group['363448'] = 'Wjets'
did_to_group['363449'] = 'Wjets'
did_to_group['363450'] = 'Wjets'
did_to_group['363451'] = 'Wjets'
did_to_group['363452'] = 'Wjets'
did_to_group['363453'] = 'Wjets'
did_to_group['363454'] = 'Wjets'
did_to_group['363455'] = 'Wjets'
did_to_group['363456'] = 'Wjets'
did_to_group['363457'] = 'Wjets'
did_to_group['363458'] = 'Wjets'
did_to_group['363459'] = 'Wjets'
did_to_group['363460'] = 'Wjets'
did_to_group['363461'] = 'Wjets'
did_to_group['363462'] = 'Wjets'
did_to_group['363462'] = 'Wjets'
did_to_group['363463'] = 'Wjets'
did_to_group['363464'] = 'Wjets'
did_to_group['363465'] = 'Wjets'
did_to_group['363466'] = 'Wjets'
did_to_group['363467'] = 'Wjets'
did_to_group['363468'] = 'Wjets'
did_to_group['363468'] = 'Wjets'
did_to_group['363469'] = 'Wjets'
did_to_group['363470'] = 'Wjets'
did_to_group['363471'] = 'Wjets'
did_to_group['363472'] = 'Wjets'
did_to_group['363472'] = 'Wjets'
did_to_group['363473'] = 'Wjets'
did_to_group['363474'] = 'Wjets'
did_to_group['363475'] = 'Wjets'
did_to_group['363476'] = 'Wjets'
did_to_group['363477'] = 'Wjets'
did_to_group['363478'] = 'Wjets'
did_to_group['363479'] = 'Wjets'
did_to_group['363480'] = 'Wjets'
did_to_group['363481'] = 'Wjets'
did_to_group['363482'] = 'Wjets'
did_to_group['363483'] = 'Wjets'
did_to_group['363390'] = 'Zjets'
did_to_group['363391'] = 'Zjets'
did_to_group['363392'] = 'Zjets'
did_to_group['363393'] = 'Zjets'
did_to_group['363394'] = 'Zjets'
did_to_group['363395'] = 'Zjets'
did_to_group['363396'] = 'Zjets'
did_to_group['363396'] = 'Zjets'
did_to_group['363397'] = 'Zjets'
did_to_group['363398'] = 'Zjets'
did_to_group['363399'] = 'Zjets'
did_to_group['361372'] = 'Zjets'
did_to_group['361373'] = 'Zjets'
did_to_group['361374'] = 'Zjets'
did_to_group['361375'] = 'Zjets'
did_to_group['361376'] = 'Zjets'
did_to_group['361377'] = 'Zjets'
did_to_group['361378'] = 'Zjets'
did_to_group['361379'] = 'Zjets'
did_to_group['361380'] = 'Zjets'
did_to_group['361381'] = 'Zjets'
did_to_group['361382'] = 'Zjets'
did_to_group['361383'] = 'Zjets'
did_to_group['361384'] = 'Zjets'
did_to_group['361385'] = 'Zjets'
did_to_group['361386'] = 'Zjets'
did_to_group['361387'] = 'Zjets'
did_to_group['361388'] = 'Zjets'
did_to_group['361389'] = 'Zjets'
did_to_group['361390'] = 'Zjets'
did_to_group['361391'] = 'Zjets'
did_to_group['361392'] = 'Zjets'
did_to_group['361393'] = 'Zjets'
did_to_group['361394'] = 'Zjets'
did_to_group['361395'] = 'Zjets'
did_to_group['361396'] = 'Zjets'
did_to_group['361397'] = 'Zjets'
did_to_group['361398'] = 'Zjets'
did_to_group['361399'] = 'Zjets'
did_to_group['361400'] = 'Zjets'
did_to_group['361401'] = 'Zjets'
did_to_group['361402'] = 'Zjets'
did_to_group['361403'] = 'Zjets'
did_to_group['361404'] = 'Zjets'
did_to_group['361405'] = 'Zjets'
did_to_group['361406'] = 'Zjets'
did_to_group['361407'] = 'Zjets'
did_to_group['361408'] = 'Zjets'
did_to_group['361409'] = 'Zjets'
did_to_group['361410'] = 'Zjets'
did_to_group['361411'] = 'Zjets'
did_to_group['361412'] = 'Zjets'
did_to_group['361413'] = 'Zjets'
did_to_group['361414'] = 'Zjets'
did_to_group['361415'] = 'Zjets'
did_to_group['361416'] = 'Zjets'
did_to_group['361417'] = 'Zjets'
did_to_group['361418'] = 'Zjets'
did_to_group['361419'] = 'Zjets'
did_to_group['361420'] = 'Zjets'
did_to_group['361421'] = 'Zjets'
did_to_group['361422'] = 'Zjets'
did_to_group['361423'] = 'Zjets'
did_to_group['361424'] = 'Zjets'
did_to_group['361425'] = 'Zjets'
did_to_group['361426'] = 'Zjets'
did_to_group['361427'] = 'Zjets'
did_to_group['361428'] = 'Zjets'
did_to_group['361429'] = 'Zjets'
did_to_group['361430'] = 'Zjets'
did_to_group['361431'] = 'Zjets'
did_to_group['361432'] = 'Zjets'
did_to_group['361433'] = 'Zjets'
did_to_group['361434'] = 'Zjets'
did_to_group['361435'] = 'Zjets'
did_to_group['361436'] = 'Zjets'
did_to_group['361437'] = 'Zjets'
did_to_group['361438'] = 'Zjets'
did_to_group['361439'] = 'Zjets'
did_to_group['361440'] = 'Zjets'
did_to_group['361441'] = 'Zjets'
did_to_group['361442'] = 'Zjets'
did_to_group['361443'] = 'Zjets'
did_to_group['361444'] = 'Zjets'
did_to_group['361445'] = 'Zjets'
did_to_group['361446'] = 'Zjets'
did_to_group['361447'] = 'Zjets'
did_to_group['361448'] = 'Zjets'
did_to_group['361449'] = 'Zjets'
did_to_group['361450'] = 'Zjets'
did_to_group['361451'] = 'Zjets'
did_to_group['361452'] = 'Zjets'
did_to_group['361453'] = 'Zjets'
did_to_group['361454'] = 'Zjets'
did_to_group['361455'] = 'Zjets'
did_to_group['361456'] = 'Zjets'
did_to_group['361457'] = 'Zjets'
did_to_group['361458'] = 'Zjets'
did_to_group['361459'] = 'Zjets'
did_to_group['361460'] = 'Zjets'
did_to_group['361461'] = 'Zjets'
did_to_group['361462'] = 'Zjets'
did_to_group['361463'] = 'Zjets'
did_to_group['361464'] = 'Zjets'
did_to_group['361465'] = 'Zjets'
did_to_group['361466'] = 'Zjets'
did_to_group['361467'] = 'Zjets'

did_to_group['370100'] = 'Gtt'
did_to_group['370101'] = 'Gtt'
did_to_group['370102'] = 'Gtt'
did_to_group['370103'] = 'Gtt'
did_to_group['370104'] = 'Gtt'
did_to_group['370105'] = 'Gtt'
did_to_group['370106'] = 'Gtt'
did_to_group['370107'] = 'Gtt'
did_to_group['370108'] = 'Gtt'
did_to_group['370109'] = 'Gtt'
did_to_group['370110'] = 'Gtt'
did_to_group['370111'] = 'Gtt'
did_to_group['370112'] = 'Gtt'
did_to_group['370113'] = 'Gtt'
did_to_group['370114'] = 'Gtt'
did_to_group['370115'] = 'Gtt'
did_to_group['370116'] = 'Gtt'
did_to_group['370117'] = 'Gtt'
did_to_group['370118'] = 'Gtt'
did_to_group['370119'] = 'Gtt'
did_to_group['370120'] = 'Gtt'
did_to_group['370121'] = 'Gtt'
did_to_group['370122'] = 'Gtt'
did_to_group['370123'] = 'Gtt'
did_to_group['370124'] = 'Gtt'
did_to_group['370125'] = 'Gtt'
did_to_group['370126'] = 'Gtt'
did_to_group['370127'] = 'Gtt'
did_to_group['370128'] = 'Gtt'
did_to_group['370129'] = 'Gtt'
did_to_group['370130'] = 'Gtt'
did_to_group['370131'] = 'Gtt'
did_to_group['370132'] = 'Gtt'
did_to_group['370133'] = 'Gtt'
did_to_group['370134'] = 'Gtt'
did_to_group['370135'] = 'Gtt'
did_to_group['370136'] = 'Gtt'
did_to_group['370137'] = 'Gtt'
did_to_group['370138'] = 'Gtt'
did_to_group['370139'] = 'Gtt'
did_to_group['370140'] = 'Gtt'
did_to_group['370141'] = 'Gtt'
did_to_group['370142'] = 'Gtt'
did_to_group['370143'] = 'Gtt'
did_to_group['370144'] = 'Gtt'
did_to_group['370145'] = 'Gtt'
did_to_group['370146'] = 'Gtt'
did_to_group['370147'] = 'Gtt'
did_to_group['370148'] = 'Gtt'
did_to_group['370149'] = 'Gtt'
did_to_group['370150'] = 'Gtt'
did_to_group['370151'] = 'Gtt'
did_to_group['370152'] = 'Gtt'
did_to_group['370153'] = 'Gtt'
did_to_group['370154'] = 'Gtt'
did_to_group['370155'] = 'Gtt'
did_to_group['370156'] = 'Gtt'
did_to_group['370157'] = 'Gtt'
did_to_group['370158'] = 'Gtt'
did_to_group['370159'] = 'Gtt'
did_to_group['370160'] = 'Gtt'
did_to_group['370161'] = 'Gtt'
did_to_group['370162'] = 'Gtt'
did_to_group['370163'] = 'Gtt'
did_to_group['370164'] = 'Gtt'
did_to_group['370165'] = 'Gtt'
did_to_group['370166'] = 'Gtt'
did_to_group['370167'] = 'Gtt'
did_to_group['370168'] = 'Gtt'
did_to_group['370169'] = 'Gtt'
did_to_group['370170'] = 'Gtt'
did_to_group['370171'] = 'Gtt'
did_to_group['370172'] = 'Gtt'
did_to_group['370173'] = 'Gtt'
did_to_group['370174'] = 'Gtt'
did_to_group['370175'] = 'Gtt'
did_to_group['370176'] = 'Gtt'
did_to_group['370177'] = 'Gtt'
did_to_group['370178'] = 'Gtt'
did_to_group['370179'] = 'Gtt'
did_to_group['370180'] = 'Gtt'
did_to_group['370181'] = 'Gtt'
did_to_group['370182'] = 'Gtt'
did_to_group['370183'] = 'Gtt'
did_to_group['370184'] = 'Gtt'
did_to_group['370185'] = 'Gtt'
did_to_group['370186'] = 'Gtt'
did_to_group['370187'] = 'Gtt'
did_to_group['370400'] = 'Gtt'
did_to_group['370401'] = 'Gtt'
did_to_group['370402'] = 'Gtt'
did_to_group['370403'] = 'Gtt'
did_to_group['370404'] = 'Gtt'
did_to_group['370405'] = 'Gtt'
did_to_group['370406'] = 'Gtt'
did_to_group['370407'] = 'Gtt'
did_to_group['370408'] = 'Gtt'
did_to_group['370409'] = 'Gtt'
did_to_group['370410'] = 'Gtt'
did_to_group['370411'] = 'Gtt'
did_to_group['370412'] = 'Gtt'
did_to_group['370413'] = 'Gtt'
did_to_group['370414'] = 'Gtt'
did_to_group['370415'] = 'Gtt'
did_to_group['370416'] = 'Gtt'
did_to_group['370417'] = 'Gtt'
did_to_group['370418'] = 'Gtt'
did_to_group['370419'] = 'Gtt'
did_to_group['370420'] = 'Gtt'
did_to_group['370421'] = 'Gtt'
did_to_group['370422'] = 'Gtt'
did_to_group['370423'] = 'Gtt'
did_to_group['370424'] = 'Gtt'
did_to_group['370425'] = 'Gtt'
did_to_group['370426'] = 'Gtt'
did_to_group['370427'] = 'Gtt'
did_to_group['370428'] = 'Gtt'
did_to_group['370429'] = 'Gtt'
did_to_group['370430'] = 'Gtt'
did_to_group['370431'] = 'Gtt'
did_to_group['370432'] = 'Gtt'
did_to_group['370433'] = 'Gtt'
did_to_group['370434'] = 'Gtt'
did_to_group['370435'] = 'Gtt'
did_to_group['370436'] = 'Gtt'
did_to_group['370437'] = 'Gtt'
did_to_group['370438'] = 'Gtt'
did_to_group['370439'] = 'Gtt'
did_to_group['370440'] = 'Gtt'
did_to_group['370441'] = 'Gtt'
did_to_group['370442'] = 'Gtt'
did_to_group['370443'] = 'Gtt'
did_to_group['370444'] = 'Gtt'
did_to_group['370445'] = 'Gtt'
did_to_group['370446'] = 'Gtt'
did_to_group['370447'] = 'Gtt'
did_to_group['370448'] = 'Gtt'
did_to_group['370449'] = 'Gtt'
did_to_group['370450'] = 'Gtt'
did_to_group['370451'] = 'Gtt'
did_to_group['370452'] = 'Gtt'
did_to_group['370453'] = 'Gtt'
did_to_group['370454'] = 'Gtt'
did_to_group['370455'] = 'Gtt'
did_to_group['370456'] = 'Gtt'
did_to_group['370457'] = 'Gtt'
did_to_group['370458'] = 'Gtt'
did_to_group['370459'] = 'Gtt'
did_to_group['370460'] = 'Gtt'
did_to_group['370461'] = 'Gtt'
did_to_group['370462'] = 'Gtt'
did_to_group['370463'] = 'Gtt'
did_to_group['370464'] = 'Gtt'
did_to_group['370465'] = 'Gtt'
did_to_group['370500'] = 'Gtt'
did_to_group['370501'] = 'Gtt'
did_to_group['370502'] = 'Gtt'
did_to_group['370503'] = 'Gtt'
did_to_group['370504'] = 'Gtt'
did_to_group['370505'] = 'Gtt'
did_to_group['370506'] = 'Gtt'
did_to_group['370507'] = 'Gtt'
did_to_group['370508'] = 'Gtt'
did_to_group['370509'] = 'Gtt'
did_to_group['370510'] = 'Gtt'
did_to_group['370511'] = 'Gtt'
did_to_group['370512'] = 'Gtt'
did_to_group['370513'] = 'Gtt'
did_to_group['370514'] = 'Gtt'
did_to_group['370515'] = 'Gtt'
did_to_group['370516'] = 'Gtt'
did_to_group['370517'] = 'Gtt'
did_to_group['370518'] = 'Gtt'
did_to_group['370519'] = 'Gtt'
did_to_group['370520'] = 'Gtt'
did_to_group['370521'] = 'Gtt'
did_to_group['370522'] = 'Gtt'
did_to_group['370523'] = 'Gtt'
did_to_group['370524'] = 'Gtt'
did_to_group['370525'] = 'Gtt'
did_to_group['370526'] = 'Gtt'
did_to_group['370527'] = 'Gtt'
did_to_group['370528'] = 'Gtt'
did_to_group['370529'] = 'Gtt'
did_to_group['370530'] = 'Gtt'
did_to_group['370531'] = 'Gtt'
did_to_group['370532'] = 'Gtt'
did_to_group['370533'] = 'Gtt'
did_to_group['370534'] = 'Gtt'
did_to_group['370535'] = 'Gtt'
did_to_group['370536'] = 'Gtt'
did_to_group['370537'] = 'Gtt'
did_to_group['370538'] = 'Gtt'
did_to_group['370539'] = 'Gtt'
did_to_group['370540'] = 'Gtt'
did_to_group['370541'] = 'Gtt'
did_to_group['370542'] = 'Gtt'
did_to_group['370543'] = 'Gtt'
did_to_group['370544'] = 'Gtt'
did_to_group['370545'] = 'Gtt'
did_to_group['370546'] = 'Gtt'
did_to_group['370547'] = 'Gtt'
did_to_group['370548'] = 'Gtt'
did_to_group['370549'] = 'Gtt'
did_to_group['370550'] = 'Gtt'
did_to_group['370551'] = 'Gtt'
did_to_group['370552'] = 'Gtt'
did_to_group['370553'] = 'Gtt'
did_to_group['370554'] = 'Gtt'
did_to_group['370555'] = 'Gtt'
did_to_group['370556'] = 'Gtt'
did_to_group['370557'] = 'Gtt'
did_to_group['370558'] = 'Gtt'
did_to_group['370559'] = 'Gtt'
did_to_group['370560'] = 'Gtt'
did_to_group['370561'] = 'Gtt'
did_to_group['370562'] = 'Gtt'
did_to_group['370563'] = 'Gtt'
did_to_group['370564'] = 'Gtt'
did_to_group['370565'] = 'Gtt'
did_to_group['370239'] = 'Gtt'
did_to_group['370240'] = 'Gtt'
did_to_group['370241'] = 'Gtt'
did_to_group['370242'] = 'Gtt'
did_to_group['370243'] = 'Gtt'
did_to_group['370244'] = 'Gtt'
did_to_group['370245'] = 'Gtt'
did_to_group['370246'] = 'Gtt'
did_to_group['370247'] = 'Gtt'
did_to_group['370248'] = 'Gtt'


did_to_group['373421'] = 'Gtt'
did_to_group['373422'] = 'Gtt'
did_to_group['373423'] = 'Gtt'
did_to_group['373424'] = 'Gtt'
did_to_group['373425'] = 'Gtt'
did_to_group['373426'] = 'Gtt'
did_to_group['373427'] = 'Gtt'
did_to_group['373428'] = 'Gtt'
did_to_group['373429'] = 'Gtt'
did_to_group['373430'] = 'Gtt'
did_to_group['373431'] = 'Gtt'
did_to_group['373432'] = 'Gtt'
did_to_group['373433'] = 'Gtt'
did_to_group['373434'] = 'Gtt'
did_to_group['373435'] = 'Gtt'
did_to_group['373436'] = 'Gtt'
did_to_group['373437'] = 'Gtt'
did_to_group['373438'] = 'Gtt'
did_to_group['373439'] = 'Gtt'
did_to_group['373440'] = 'Gtt'
did_to_group['373441'] = 'Gtt'
did_to_group['373441'] = 'Gtt'
did_to_group['373442'] = 'Gtt'
did_to_group['373443'] = 'Gtt'
did_to_group['373444'] = 'Gtt'
did_to_group['373445'] = 'Gtt'
did_to_group['373446'] = 'Gtt'
did_to_group['373447'] = 'Gtt'

did_to_group['410000'] = 'ttbar'
did_to_group['407009'] = 'ttbar'
did_to_group['407010'] = 'ttbar'
did_to_group['407011'] = 'ttbar'
did_to_group['407012'] = 'ttbar'
did_to_group['407019'] = 'singletop'
did_to_group['407021'] = 'singletop'
did_to_group['410011'] = 'singletop'
did_to_group['410012'] = 'singletop'
did_to_group['410013'] = 'singletop'
did_to_group['410014'] = 'singletop'
did_to_group['410025'] = 'singletop'
did_to_group['410026'] = 'singletop'
did_to_group['410080'] = 'topEW'
did_to_group['410111'] = 'topEW'
did_to_group['410112'] = 'topEW'
did_to_group['410113'] = 'topEW'
did_to_group['410114'] = 'topEW'
did_to_group['410115'] = 'topEW'
did_to_group['410116'] = 'topEW'
did_to_group['341177'] = 'topEW'
did_to_group['341270'] = 'ttH'
did_to_group['341271'] = 'ttH'
#did_to_group['407021'] = 'singletop'
#did_to_group['410011'] = 'singletop'
#did_to_group['410012'] = 'singletop'
#did_to_group['410013'] = 'singletop'
#did_to_group['410014'] = 'singletop'
#did_to_group['410025'] = 'singletop'
#did_to_group['410026'] = 'singletop'

did_to_group['410066'] = 'ttbarW' # ttW Np0
did_to_group['410067'] = 'ttbarW' # ttW Np1
did_to_group['410068'] = 'ttbarW' # ttW Np2
did_to_group['410069'] = 'ttbarZll' # ttZllonshell Np0
did_to_group['410070'] = 'ttbarZll' # ttZllonshell Np1
#did_to_group['410071'] = 'ttbarV' # doesn't exist ?
#did_to_group['410072'] = 'ttbarV' # doesn't exist ?
did_to_group['410073'] = 'ttbarZnnqq' # ttZnnqq Np0
did_to_group['410074'] = 'ttbarZnnqq' # ttZnnqq Np1
did_to_group['410075'] = 'ttbarZnnqq' # ttZnnqq Np2
#did_to_group['410076'] = 'ttbarV' # doesn't exist ?
did_to_group['410080'] = '4topSM' # 4tops SM
did_to_group['341177'] = 'ttH' # ttH

for regionID in range(0, 5):
  for fname in glob.glob("cuts_ICHEP/0L/VR0L{0:d}Cuts/*.json".format(regionID))+glob.glob("cuts_ICHEP/0L/VR1L{0:d}Cuts/*.json".format(regionID)):
    did = os.path.basename(fname).split('.')[0]

    # figure out if we're using VR0L or VR1L
    region='VR0L'
    if 'VR0L' in os.path.basename(os.path.dirname(fname)): region='VR1L'

    with open(fname) as f:
      data = json.load(f)
      # add in the group
      group = did_to_group[did]

      # no signal allowed
      if group == 'Gtt': continue
      # if we haven't added the group yet, set up defaults
      if group not in groups:
        nullregion = dict((count_type, 0) for count_type in count_types)
        nulldict = {0: copy.deepcopy(nullregion),
                    1: copy.deepcopy(nullregion),
                    2: copy.deepcopy(nullregion),
                    3: copy.deepcopy(nullregion),
                    4: copy.deepcopy(nullregion)}
        groups[group] = {'VR0L': copy.deepcopy(nulldict), 'VR1L': copy.deepcopy(nulldict)}

      # we just need the subset which is often first item (look at an example json)
      data = data[data.keys()[0]]
      for count_type in count_types:
        sf = 1
        # scale by 2ifb
        if count_type == 'scaled': sf = scaleFactor*1000
        value = data[count_type]*sf
        #groups[did_to_group[did]][region][regionID][count_type] = data[count_type]*sf
        groups[did_to_group[did]][region][regionID][count_type] += data[count_type]*sf

def getValues(group, groups):
  return [group] + [groups[group][region][i][index] for region in ['VR0L', 'VR1L'] for i in range(0, 5)]

for index, typeBkgd in zip(count_types, ['raw', 'weighted', 'scaled ({0:0.2f} ifb)'.format(scaleFactor)]):
  sumValues = [0]*10
  print("{0: ^150s}".format(typeBkgd))
  printStr = "{{0:12}}{0:s}0{0:s}1{0:s}2{0:s}3{0:s}4{1:s}0{1:s}1{1:s}2{1:s}3{1:s}4".format("\t{1:>9}", "\t{2:>9}")
  print(printStr.format("GROUP", "VR1L", "VR0L"))
  for group in sorted(groups):
    values = getValues(group, groups)
    valueStr = "{{0:12}}\t{{1:{0:s}}}\t{{2:{0:s}}}\t{{3:{0:s}}}\t{{4:{0:s}}}\t{{5:{0:s}}}\t{{6:{0:s}}}\t{{7:{0:s}}}\t{{8:{0:s}}}\t{{9:{0:s}}}\t{{10:{0:s}}}".format("10.4f")
    print(valueStr.format(*values))
    sumValues = [sum(x) for x in zip(sumValues, values[1:])]
  print("\t"+("-"*100))
  sumValues = ["total"] + sumValues
  print(valueStr.format(*sumValues))
  # add ttbar fraction
  ttbarFrac = getValues('ttbar', groups)
  ttbarFrac[0] = '%ttbar'
  for i in range(1, len(ttbarFrac)):
    ttbarFrac[i] = numpy.float64(ttbarFrac[i])/sumValues[i]
  print(valueStr.format(*ttbarFrac))
  print("="*100)
