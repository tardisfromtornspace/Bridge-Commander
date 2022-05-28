from bcdebug import debug
################################################################
#######  LoadGravityFX Script ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# This is where it all begins... lol
# Here's the script that will load GravityFX and it's handlers, start up the Gravity Sensor Menu GUI and the System Map GUI
# And a bunch of some other stuff too that needed to happen upon starting BC.
####################################################################
##########################################################################################################################
##### reuniting the imports      #########################################################################################
##########################################################################################################################
import App
import Foundation
import MissionLib
import Custom.GravityFX.GravityFXmain
import Custom.GravityFX.GravityFXlib
import Custom.GravityFX.GravityFXgui
import Custom.GravityFX.Logger
##########################################################################################################################
##### A little something-something that usefull in the future it will be     #############################################
##########################################################################################################################
App.Planet.GetMass = Custom.GravityFX.GravityFXmain.GetMass
App.Planet.IsAtmosphereObj = Custom.GravityFX.GravityFXlib.IsAtmosphereObj
App.Planet.GetDensity = Custom.GravityFX.GravityFXmain.GetDensity
App.Planet.SetDensity = Custom.GravityFX.GravityFXmain.SetDensity
App.Planet.GetClass = Custom.GravityFX.GravityFXlib.GetClass
App.PoweredSubsystem.IsSystemOnline = Custom.GravityFX.GravityFXlib.IsSystemOnline
##########################################################################################################################
##### SAY HELLO TO MY LITTLE FRIEND!!!     ###############################################################################
##########################################################################################################################
mode = Foundation.MutatorDef("USS Frontier's GravityFX")

Foundation.SystemDef('PsiBlackhole', 0, dict = { 'modes': [ mode ] } )
##########################################################################################################################
##### Hiring the Manager - very important to have a organized company    #################################################
##########################################################################################################################
App.g_kGravityManager = Custom.GravityFX.GravityFXmain.GravityManager()
##########################################################################################################################
##### Debugging Power!      ##############################################################################################
##########################################################################################################################
Logger = None
if Custom.GravityFX.GravityFXlib.GetConfigValue("LogLoadGravityFX"):
	Logger = Custom.GravityFX.Logger.LogCreator("LoadGravityFX Logger", "scripts\Custom\GravityFX\Logs\LoadGravityFXLOG.txt")
	Logger.LogString("Initialized LoadGravityFX logger")
else:
	Logger = Custom.GravityFX.Logger.DummyLogger()
##########################################################################################################################
##### the main trigger: ENTERED SET       ################################################################################
##########################################################################################################################
class GravityFXTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.CreateGUIs = 1
	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
		
		try:
			pPlayer = App.Game_GetCurrentPlayer()
			pDestShip = App.ShipClass_Cast(pEvent.GetDestination())
			if pDestShip:
				#pShipProp = pDestShip.GetShipProperty()
				if pPlayer and pDestShip.GetObjID() == pPlayer.GetObjID():
					###
					#import Systems.PsiBlackhole.PsiBlackholeSys
					#Systems.PsiBlackhole.PsiBlackholeSys.CreateMenus()
					###
					if self.CreateGUIs == 1:
						Custom.GravityFX.GravityFXgui.StartGSOGUI()
						Custom.GravityFX.GravityFXgui.StartSystemMapGUI()
						Custom.GravityFX.GravityFXgui.StartGravGenGUI()
					self.CreateGUIs = 0
					CreateGravWells()
				else:
					#now Refresh the GravityManager ship list and try to create a grav well plugin for the ship.
					App.g_kGravityManager.CreateGravWellPlugin(pDestShip)
					App.g_kGravityManager.RefreshShipList()
			if pObject and pEvent:
				pObject.CallNextHandler(pEvent)
		except:
			LogError("GravFX Trigger Call")
	def Deactivate(self):
		debug(__name__ + ", Deactivate")
		print "GravityFX has been deactivated."
		# BC, or Foundation or other mod causes some mutators to be deactivated when you abort your mission (normally 
		# QB) and start a new one.  And that is a pain in the ass... 
		# I've came up with the following line of code to solve this problem, at least with GravityFX.
		# But as i couldn't test it for sure to see the fix worked, i will just comment the line out.
		#mode.Enable()
		App.g_kGravityManager = Custom.GravityFX.GravityFXmain.GravityManager()
		self.CreateGUIs = 1

GravityFXTrigger('GravityFX Trigger', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )

##########################################################################################################################
##### the update handler "Delete": EXITED SET and OBJECT DESTROYED    ####################################################
##########################################################################################################################
class GravityFXDeleteShipHandler(Foundation.TriggerDef):
	def __init__(self, name = "GravityFX Exit Set Trigger", EventKey = App.ET_EXITED_SET,
			 name2 = "GravityFX Obj Destroyed Trigger", EventKey2 = App.ET_OBJECT_DESTROYED, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, EventKey, dict)
		Foundation.TriggerDef.__init__(self, name2, EventKey2, dict)
	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
			
		try:
			pDestShip = App.ShipClass_Cast(pEvent.GetDestination())
			if pDestShip:
				#pPlayer = App.Game_GetCurrentPlayer()
				#if pPlayer and pPlayer.GetObjID() == pDestShip.GetObjID():
				#	print "Player Exited Set or was Destroyed"
				App.g_kGravityManager.DeleteGravWellPlugin(pDestShip)
				App.g_kGravityManager.RefreshShipList()
				SMGUI = __import__('Custom.GravityFX.SystemMapGUI')
				if SMGUI.pGUICreator and SMGUI.pGUICreator.GetElement("System Map"):
					SMGUI.pGUICreator.IconCreator.DeleteIcon(str(pDestShip.GetObjID()))
					SMGUI.Logger.LogString("LGFX: Deleted icon for object: "+pDestShip.GetName()+" "+str(pDestShip.GetObjID()))
					SMGUI.pGUICreator.IconCreator.DeleteIcon("GravWell"+str(pDestShip.GetObjID()))
					SMGUI.pGUICreator.IconCreator.DeleteIcon("GravWellPluginMarker"+str(pDestShip.GetObjID()))
					SMGUI.pGUICreator.IconCreator.DeleteIcon("FriendMarker"+str(pDestShip.GetObjID()))
					SMGUI.pGUICreator.IconCreator.DeleteIcon("EnemyMarker"+str(pDestShip.GetObjID()))
					SMGUI.pGUICreator.IconCreator.DeleteIcon("NeutralMarker"+str(pDestShip.GetObjID()))
			if pObject and pEvent:
				pObject.CallNextHandler(pEvent)
		except:
			LogError("GravFX Delete Trigger Call")
GravityFXDeleteShipHandler(dict = { 'modes': [ mode ] } )
##########################################################################################################################
##### STARTER FUNCTION        ############################################################################################
##########################################################################################################################
def CreateGravWells():
	debug(__name__ + ", CreateGravWells")
	App.g_kGravityManager.CreateGravWells()
	if Custom.GravityFX.GravityFXlib.GetConfigValue("SetStockPlanetsDensity") == 1:
		SetStockSystemPlanetsDensity()
	SMGUI = __import__('Custom.GravityFX.SystemMapGUI')
	if SMGUI.pGUICreator and SMGUI.pGUICreator.GetElement("System Map"):
		SMGUI.PurgeSystemMap()
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer:
		App.g_kGravityManager.CreateGravWellPlugin(pPlayer)

##########################################################################################################################
##### RANDOM DENSITY GENERATOR        ####################################################################################
##########################################################################################################################
StockSystemsList = ['Albirea1', 'Albirea2', 'Albirea3', 'Alioth1', 'Alioth2', 'Alioth3', 'Alioth4', 'Alioth5', 'Alioth6', 'Alioth7', 'Alioth8', 'Artrus1', 'Artrus2', 'Artrus3', 'Ascella1', 'Ascella2', 'Ascella3', 'Ascella4', 'Ascella5', 'Belaruz1', 'Belaruz2', 'Belaruz3', 'Belaruz4', 'Beol1', 'Beol2', 'Beol3', 'Beol4', 'Biranu1', 'Biranu2', 'Cebalrai1', 'Cebalrai2', 'Cebalrai3', 'Chambana1', 'Chambana2', 'Geble1', 'Geble2', 'Geble3', 'Geble4', 'Itari1', 'Itari2', 'Itari3', 'Itari4', 'Itari5', 'Itari6', 'Itari7', 'Itari8', 'Nepenthe1', 'Nepenthe2', 'Nepenthe3', 'OmegaDraconis1', 'OmegaDraconis2', 'OmegaDraconis3', 'OmegaDraconis4', 'OmegaDraconis5', 'Ona1', 'Ona2', 'Ona3', 'Poseidon1', 'Poseidon2', 'Prendel1', 'Prendel2', 'Prendel3', 'Prendel4', 'Prendel5', 'Riha1', 'Savoy1', 'Savoy2', 'Savoy3', 'Serris1', 'Serris2', 'Serris3', 'Tevron1', 'Tevron2', 'Tezle1', 'Tezle2', 'Vesuvi1', 'Vesuvi4', 'Vesuvi5', 'Vesuvi6', 'Voltair1', 'Voltair2', 'XiEntrades1', 'XiEntrades2', 'XiEntrades3', 'XiEntrades4', 'XiEntrades5', 'Yiles1', 'Yiles2', 'Yiles3', 'Yiles4']
StockPlanetsDensityDict = {}
def SetStockSystemPlanetsDensity():
	debug(__name__ + ", SetStockSystemPlanetsDensity")
	global StockPlanetsDensityDict
	print "Setting Stock System Planets Random Density."
	try:
		DensityDict = __import__('Custom.GravityFX.DensityDict')
		pPlayer = App.Game_GetCurrentPlayer()
		if not pPlayer:
			return
		pSet = pPlayer.GetContainingSet()
		if not pSet:
			return
		sSetName = pSet.GetName()
		if sSetName in StockSystemsList:
			for pGravWell in App.g_kGravityManager.GravWellList:
				if pGravWell.CLASS == "Gravity Well":
					pPlanet = pGravWell.Parent
					sClass = pPlanet.GetClass()
					if StockPlanetsDensityDict.has_key(pPlanet.GetName()):
						pPlanet.SetDensity(StockPlanetsDensityDict[pPlanet.GetName()])
					else:
						DenRange = DensityDict.GetDensityRange(sClass)
						if DenRange == None or DenRange == [0,0]:
							DenRange = [0.1, 10.0]
						nDensity = Custom.GravityFX.GravityFXlib.GetRandomInRange(DenRange[0], DenRange[1])
						pPlanet.SetDensity(nDensity)
						StockPlanetsDensityDict[pPlanet.GetName()] = nDensity
					pGravWell.UpdateRadius()
	except:
		LogError("Set Random Density For Stock System Planets/Suns")

##########################################################################################################################
##### HELPER FOR LOGGING        ##########################################################################################
##########################################################################################################################
def LogError(strFromFunc = None):
	debug(__name__ + ", LogError")
	import sys
	et = sys.exc_info()
	if strFromFunc == None:
		strFromFunc = "???"
	if Logger:
		Logger.LogException(et, "ERROR at "+strFromFunc)
	else:
		error = str(et[0])+": "+str(et[1])
		print "ERROR at "+strFromFunc+", details -> "+error
