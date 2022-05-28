import App

g_pShips = []
g_pShipListData = {}
g_pSystem = []
g_pRegionListData = []
g_sBridge = ''

def LoadSetup(sModule):
	try:
		pModule = __import__('Custom.QuickBattleGame.Missions.'+sModule)
	except ImportError:
		try: # Yes, two try's...Maybe we can make it without them in the future?
			pModule = __import__('Custom.QuickBattleGame.'+sModule)
		except ImportError:
			print("Error importing file ", sModule, ".")
			return
	
	global g_pSystem
	g_pSystem		=  pModule.gSystem
	
	global g_sBridge
	g_sBridge	=  pModule.gBridge
	
	if (g_sBridge == "Sovereign" or g_sBridge == "Galaxy"):     # old configs are still using only the short string
		g_sBridge = g_sBridge + "Bridge"                    # we fix that here for downward compatibility.

	import QBGUI
	QBGUI.SetBridge(g_sBridge)

	global g_pShips
	g_pShips = []

	if (float(pModule.gVersion) < 2.3):
		AddOldShips(pModule)

	g_pShipListData.clear()
	
	if (hasattr(pModule, "gShips")):
		for s in pModule.gShips:
			g_pShips.append(s)

	for ship in g_pShips:
		g_pShipListData[ship["name"]] = ship
				
	global g_pRegionListData
	g_pRegionListData = []
	for system in g_pSystem:
		AddSystem(system[0]+'.'+system[1])
		
	import plugin
	try:
		plugin.gPluginData = pModule.gPluginData
	except:
		plugin.gPluginData = {}
		
	return -1
		
def AddSystem(system):
	if (g_pRegionListData.count(system)==0):
		g_pRegionListData.append(system)

def AddOldShips(pModule):	# compatibility to older setups
	data = GetDefaultShipData(pModule.gPlayer[0])
	data['name'] = pModule.gPlayer[1]
	data['system'] = pModule.gPlayer[2]
	data['pos'] = pModule.gPlayerLoc
	data['ailevel'] = 0.0
	data['ai'] = ''
	data['warp'] = 0
	data['group'] = 'player'
	try:
		data['mindamage'] = pModule.gPlayer[3][0]
		data['maxdamage'] = pModule.gPlayer[3][1]
	except:
		pass
	
	g_pShips.append(data)
	
	AddGroup(pModule.gEnemy, pModule.gEnemyLoc, "enemy", 0)
	AddGroup(pModule.gFriendly, pModule.gFriendlyLoc, "friend", 0)
	AddGroup(pModule.gNeutral, pModule.gNeutralLoc, "neutral", 0)
	AddGroup(pModule.gEnemyStarbases, pModule.gEnStLoc, "enemy", 1)
	AddGroup(pModule.gFriendlyStarbases, pModule.gFrStLoc, "friend", 1)
	AddGroup(pModule.gNeutralStarbases, pModule.gNeStLoc, "neutral", 1)

def AddGroup(list, poslist, group, bStarbase):
	i = 0
	for ship in list:
		data = GetDefaultShipData(ship[0])
		data['name'] = ship[1]
		data['system'] = ship[2]
		data['pos'] = poslist[i]
		data['ailevel'] = 0
		if (not bStarbase):
			data['ai'] = ship[4]
			data['ailevel'] = ship[5]
			data['warp'] = ship[3]
			if (len(ship)>6):
				data['mindamage'] = ship[6][0]
				data['maxdamage'] = ship[6][1]
		else:
			data['ai'] = ship[3]
			data['warp'] = 0
			if (len(ship)>4):
				data['mindamage'] = ship[4][0]
				data['maxdamage'] = ship[4][1]
		data['group'] = group
		data['starbase'] = bStarbase
		g_pShips.append(data)
		i = i + 1

def WriteSetup(filename):
	gBridge = g_sBridge
	gSystem = []
	gShips = []
	
	for system in g_pRegionListData:
		import strop
		s = strop.split(system, '.')
		gSystem.append([s[0], s[1], ''])
	
	keys = g_pShipListData.keys()

	for key in keys:
		gShips.append(g_pShipListData[key])
		
	import nt
	try: 
		if (filename == "QBSetup"):
			nt.remove("scripts\Custom\QuickBattleGame\\" + filename + ".py")
		else:
			nt.remove("scripts\Custom\QuickBattleGame\Missions\\" + filename + ".py")
	except OSError:
		pass
		
	import QuickBattle

	try:
		if (filename == "QBSetup"):     # We have to save the mainsetup in the main directory
			file = nt.open('scripts\Custom\QuickBattleGame\\' + filename + '.py', nt.O_CREAT | nt.O_RDWR)
		else:                           # rest here.
			file = nt.open('scripts\Custom\QuickBattleGame\Missions\\' + filename + '.py', nt.O_CREAT | nt.O_RDWR)
	
		nt.write(file, "gVersion=" + repr(QuickBattle.g_version) + "\n")
		nt.write(file, "gSystem=" + repr(gSystem) + "\n")
		nt.write(file, "gBridge=" + repr(gBridge) + "\n")
	
		nt.write(file, "gShips=" + repr(gShips) + "\n")
	
		import plugin
		nt.write(file, "gPluginData=" + repr(plugin.gPluginData) + "\n")
				
		nt.close(file)
	except:
		return 0
		
	return -1

def GetDefaultShipData(classname):
	pShipData = {
		'class': 	classname,
		'name':  	classname,
		'system':	'',
		'pos':		[0, 0, 0],
		'ailevel':	0.5,
		'ai':		'',
		'warp':		1,
		'group':	'neutral',
		'starbase':	0,
		'mindamage':	1,
		'maxdamage':	1,
		'minETA':	0,
		'maxETA':	0,
		'missioncritical': 0
	}
	
	return pShipData

def DeleteSetup(filename):
	import nt
	try:
		nt.remove('scripts\Custom\QuickBattleGame\Missions\\' + filename + '.py')
		nt.remove('scripts\Custom\QuickBattleGame\Missions\\' + filename + '.pyc')
	except:
		print("Cannot remove", filename)
