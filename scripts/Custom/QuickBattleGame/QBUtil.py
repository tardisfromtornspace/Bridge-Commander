import App

class QBDatabase (App.TGLocalizationDatabase):
	def GetString(*args):
		if (args[0] == "test"):
			return App.TGString("test")
		else:
			return App.TGString()
			
def writeInfo():
	import nt
	import Appc
	
	f = nt.open('test.txt', nt.O_RDWR | nt.O_CREAT)
	a = dir(Appc)
	for s in a:
		nt.write((f, s+'\n'))
			
	nt.close(f)
	
def GetShipList(dir = None):
	import nt
	import strop
	
	if (not dir is None):
		loaddir = dir
	else:
		loaddir = "scripts\Custom"
		
	ships = []
	
	f = nt.open(loaddir + "\ships.txt", nt.O_RDONLY)
	l = nt.lseek((f, 0, 2))
	nt.lseek((f, 0, 0))
	s = nt.read((f, l))
	list = strop.split(s)
	nt.close(f)
	
	for ship in list:
		s = strop.split(ship, '.')
		if (len(s)>1) and ((s[-1] == 'pyc') or (s[-1] == 'py')):
			shipname = s[0]
			pModule = __import__('ships.'+shipname)
			
			if (hasattr(pModule, 'GetShipStats')):
				stats = pModule.GetShipStats()
			
				if (shipname != '__init__') and (ships.count([shipname, stats["Name"]]) == 0):
					ships.append([shipname, stats["Name"]])
	
	ships.sort()

	return ships

def GetSystemList(dir = None):	
	import nt
	import strop
	
	if (not dir is None):
		loaddir = dir
	else:
		loaddir = "scripts\Custom"
		
	systems = []
	
	f = nt.open(loaddir + "\systems.txt", nt.O_RDONLY)
	l = nt.lseek((f, 0, 2))
	nt.lseek((f, 0, 0))
	s = nt.read((f, l))
	list = strop.split(s)
	nt.close(f)

	for system in list:
		s = strop.split(system, '.')
		if (len(s)==1):
			systemname = s[0]
			
			if (systemname == "Starbase12"):
				continue # Starbase12 will only crash us
				pModule = __import__('Systems.Starbase12.Starbase')
			elif (systemname == "DryDock"):
				pModule = __import__('Systems.DryDock.DryDockSystem')
			elif (systemname == "QuickBattle"):
				pModule = __import__('Systems.QuickBattle.QuickBattleSystem')
			else:
				pModule = __import__('Systems.'+systemname+'.'+systemname)
			
			if (hasattr(pModule, 'CreateMenus')):
				systems.append(systemname)
	
	systems.sort()
	return systems

#def GetShipList(dir = None):
#	import nt
#	import strop
#	
#	if (not dir is None):
#		nt.chdir(dir)
#	
#	list = nt.listdir('scripts\Custom\ships')
#	
#	ships = []
#	
#	for ship in list:
#		s = strop.split(ship, '.')
#		if (len(s)>1) and ((s[-1] == 'pyc') or (s[-1] == 'py')):
#			shipname = s[0]
#			pModule = __import__('Custom.ships.'+shipname)
#			
#			if (hasattr(pModule, 'GetShipStats')):
#				stats = pModule.GetShipStats()
#			
#				if (shipname != '__init__') and (ships.count([shipname, stats["Name"]]) == 0):
#					ships.append([shipname, stats["Name"]])
#	
#	ships.sort()
#	return ships
	
#def GetSystemList(dir = None):
#	import nt
#	import strop
#	
#	if (not dir is None):
#		nt.chdir(dir)
#	
#	list = nt.listdir('scripts\Custom\systems')
#	
#	systems = []
#	
#	for system in list:
#		s = strop.split(system, '.')
#		if (len(s)==1):
#			systemname = s[0]
#			
#			if (systemname == "Starbase12"):
#				pModule = __import__('Systems.Starbase12.Starbase')
#			elif (systemname == "DryDock"):
#				pModule = __import__('Systems.DryDock.DryDockSystem')
#			elif (systemname == "QuickBattle"):
#				pModule = __import__('Systems.QuickBattle.QuickBattleSystem')
#			else:
#				pModule = __import__('Custom.Systems.'+systemname+'.'+systemname)
#			
#			if (hasattr(pModule, 'CreateMenus')):
#				systems.append(systemname)
#	
#	systems.sort()
#	return systems
#

def GetSystemPlanets(systemname):
	
	planets = []
	
	i = 1
	while (1):
		try:
			__import__('Systems.'+systemname+'.'+systemname + repr(i))
		except ImportError:
			break
		else:
			planets.append(systemname + repr(i))
			i = i + 1		
	planets.sort()
	return planets