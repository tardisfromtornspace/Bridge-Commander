import App
import MissionLib
import Lib.LibEngineering
import Bridge.BridgeUtils
from Libs.LibQBautostart import chance

pMain = None
PLAY = "Yes"

#############################################################################################
#                                                                                           #
#  This Section Handles the Detroyed System Repair Interface,                               #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def init():
	global pMain, pButton7, pButton8, pButton9

	if not Lib.LibEngineering.CheckActiveMutator("Repair Destroyed Systems"):
		return
	
	pPlayer = MissionLib.GetPlayer()
	pName = pPlayer.GetName()
	pShip = MissionLib.GetShip(pName)
	
 	pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
 	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet('bridge')
	Brex = Bridge.BridgeUtils.GetBridgeMenu('Engineer')
	pMain = App.STMenu_CreateW(App.TGString("Repair Destroyed Systems"))
	Brex.InsertChild(1, pMain, 0, 0, 0)
	
	pHeavyWeapons = pPlayer.GetPulseWeaponSystem()
	if (pHeavyWeapons == None):
		pHeavyWeaponsName = "Heavy Weapons"
	else:
		pHeavyWeaponsName = pHeavyWeapons.GetName()
	
	pTorpedoes = pPlayer.GetTorpedoSystem()
	if (pTorpedoes == None):
		pTorpedoesName = "Torpedoes"
	else:
		pTorpedoesName = pTorpedoes.GetName()
	
	pPhaserSys = pPlayer.GetPhaserSystem()
	if (pPhaserSys == None):
		pLightWeaponsName = "Light Weapons"
	else:
		pLightWeaponsName = pPhaserSys.GetName()

	pButton10 = Lib.LibEngineering.CreateMenuButton("Replicate Tractor Beam parts requires 10% battery power", "Engineering", __name__ + ".TractorBeams", 0, pMain)
	pButton9 = Lib.LibEngineering.CreateMenuButton("Replicate " + str(pHeavyWeaponsName) + " parts requires 20% battery power", "Engineering", __name__ + ".PulseWeapons", 0, pMain)
	pButton8 = Lib.LibEngineering.CreateMenuButton("Replicate " + str(pTorpedoesName) + " parts requires 10% battery power", "Engineering", __name__ + ".Torpedoes", 0, pMain)
	pButton7 = Lib.LibEngineering.CreateMenuButton("Replicate " + str(pLightWeaponsName) + " parts requires 4% battery power", "Engineering", __name__ + ".Phasers", 0, pMain)
	pButton4 = Lib.LibEngineering.CreateMenuButton("Replicate Shield Generator parts requires 20% battery power", "Engineering", __name__ + ".Shields", 0, pMain)
	pButton3 = Lib.LibEngineering.CreateMenuButton("Replicate Sensor Array parts requires 10% battery power", "Engineering", __name__ + ".Sensors", 0, pMain)
	pButton5 = Lib.LibEngineering.CreateMenuButton("Replicate Impulse Engine parts requires 10% battery power", "Engineering", __name__ + ".Impulse", 0, pMain)
	pButton11 = Lib.LibEngineering.CreateMenuButton("Replicate Cloak parts requires 20% battery power", "Engineering", __name__ + ".CloakingSubsystem", 0, pMain)
	pButton2 = Lib.LibEngineering.CreateMenuButton("Replicate Warp Engine parts requires 20% battery power", "Engineering", __name__ + ".WarpE", 0, pMain)
	pButton1 = Lib.LibEngineering.CreateMenuButton("Replicate Warp Core parts requires 10% battery power", "Engineering", __name__ + ".CoreA", 0, pMain)
 
#############################################################################################
#                                                                                           #
#  This Section Handles Repairs to the Destroyed Cloaking Subsystem,                        #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def CloakingSubsystem(pObject, pEvent):

	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/5):
		return
	
	pCloak = pPlayer.GetCloakingSubsystem()
	
	if (pCloak == None):
		return

	if pCloak:
		pCloakHealth = pCloak.GetCondition()

		if  (pCloakHealth > 0):
			 return

	Response(pObject, pEvent)
	
	AvailCloakingSubsystemParts(pObject, pEvent)
	pShipSet = pPlayer.GetPropertySet()
	pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	iNumItems = pShipList.TGGetNumItems()
	pShipList.TGBeginIteration()
	for i in range(iNumItems):
		pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
		pSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)

		pCloak.SetCondition(pSubsystem.GetMaxCondition())
		pCloak.SetCondition(1)

def AvailCloakingSubsystemParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower() 
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/5))

###############################################################################################
#                                                                                             #
#  This Section Handles Repairs to the Destroyed Tractor Beams,                               #
#                                                                                             #
#                                                                                             #
#                                                                                             #
###############################################################################################

def TractorBeams(pObject, pEvent):
	global pTractorBeamsChildRepair 
	
	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/10):
		return

	pTractorBeamsSys = pPlayer.GetTractorBeamSystem()
	
	if (pTractorBeamsSys == None):
		return
	
	if pTractorBeamsSys:
		iNumTractorBeams = pTractorBeamsSys.GetNumChildSubsystems()
		for iEng in range(iNumTractorBeams):
			pTractorBeamsChild = pTractorBeamsSys.GetChildSubsystem(iEng)
			if (pTractorBeamsChild.GetCondition() == 0):
				pTractorBeamsChildCondition = pTractorBeamsChild.GetCondition()
				pTractorBeamsChildRepair   = pTractorBeamsChild.SetCondition(1)
				if (pTractorBeamsChildCondition == 0):
					TractorBeamsB(pObject, pEvent)
					return

def TractorBeamsB(pObject, pEvent):

	AvailTractorBeamsParts(pObject, pEvent)
	Response(pObject, pEvent)
	pTractorBeamsChildRepair
		
def AvailTractorBeamsParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/10))
 
###############################################################################################
#                                                                                             #
#  This Section Handles Repairs to the Destroyed Pulse weapons,                               #
#                                                                                             #
#                                                                                             #
#                                                                                             #
###############################################################################################

def PulseWeapons(pObject, pEvent):
	global pPulseWeaponChildRepair 
	
	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/5):
		return

	pPulseWeaponSys = pPlayer.GetPulseWeaponSystem()
	
	if (pPulseWeaponSys == None):
		return
	
	if pPulseWeaponSys:
		iNumPulseWeapon = pPulseWeaponSys.GetNumChildSubsystems()
		for iEng in range(iNumPulseWeapon):
			pPulseWeaponChild = pPulseWeaponSys.GetChildSubsystem(iEng)
			if (pPulseWeaponChild.GetCondition() == 0):
				pPulseWeaponChildCondition = pPulseWeaponChild.GetCondition()
				pPulseWeaponChildRepair   = pPulseWeaponChild.SetCondition(1)
				if (pPulseWeaponChildCondition == 0):
					PulseWeaponsB(pObject, pEvent)
					return

def PulseWeaponsB(pObject, pEvent):

	AvailPulseWeaponsParts(pObject, pEvent)
	Response(pObject, pEvent)
	pPulseWeaponChildRepair
		
def AvailPulseWeaponsParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/5))

##############################################################################################
#                                                                                            #
#  This Section Handles Repairs to the Destroyed Torpedoes,                                  #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################

def Torpedoes(pObject, pEvent):
	global pTorpedoChildRepair 
	
	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/10):
		return

	pTorpedoSys = pPlayer.GetTorpedoSystem()
	
	if (pTorpedoSys == None):
		return

	if pTorpedoSys:
		iNumTorpedo = pTorpedoSys.GetNumChildSubsystems()
		for iEng in range(iNumTorpedo):
			pTorpedoChild = pTorpedoSys.GetChildSubsystem(iEng)
			if (pTorpedoChild.GetCondition() == 0):
				pTorpedoChildCondition = pTorpedoChild.GetCondition()
				pTorpedoChildRepair  = pTorpedoChild.SetCondition(1)
				if (pTorpedoChildCondition == 0):
					TorpedoesB(pObject, pEvent)
					return

def TorpedoesB(pObject, pEvent):

	AvailTorpedoesParts(pObject, pEvent)
	Response(pObject, pEvent)
	pTorpedoChildRepair
		
def AvailTorpedoesParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower() 
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/10))
 
##############################################################################################
#                                                                                            #
#  This Section Handles Repairs to the Destroyed Phasers,                                    #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################

def Phasers(pObject, pEvent):
	global pPhaserChildRepair 
	
	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/25):
		return

	pPhaserSys = pPlayer.GetPhaserSystem()
	
	if (pPhaserSys == None):
		return
	
	if pPhaserSys:
		iNumPhaser = pPhaserSys.GetNumChildSubsystems()
		for iEng in range(iNumPhaser):
			pPhaserChild = pPhaserSys.GetChildSubsystem(iEng)
			#pPhaserChildMaxCondition = pPhaserChild.GetMaxCondition()
			if (pPhaserChild.GetCondition() == 0):
				pPhaserChildCondition = pPhaserChild.GetCondition()
				pPhaserChildRepair = pPhaserChild.SetCondition(1)
				if (pPhaserChildCondition == 0):
					PhasersB(pObject, pEvent)
					return

def PhasersB(pObject, pEvent):

	AvailPhasersParts(pObject, pEvent)
	Response(pObject, pEvent)
	pPhaserChildRepair
		
def AvailPhasersParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower() 
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/25))
 
#############################################################################################
#                                                                                           #
#  This Section Handles Repairs to the Destroyed Warp Core,                                 #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def CoreA(pObject, pEvent):

	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	else:
		Core(pObject, pEvent)

def Core(pObject, pEvent):
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	BackupBattery = pBattery.GetBackupBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	MaxBackupBattery = pBattery.GetBackupBatteryLimit()
	
	if (MainBattery < (MaxMainBattery/10)) and (BackupBattery < (MaxBackupBattery/10)):
		return
 
	pPowerSys = pPlayer.GetPowerSubsystem()
	
	if (pPowerSys == None):
		return

	if pPowerSys:
		pPowerHealth = pPowerSys.GetCondition()

		if  (pPowerHealth > 0):
			 return

	Response(pObject, pEvent)
	
	AvailCoreParts(pObject, pEvent)
	pShipSet = pPlayer.GetPropertySet()
	pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	iNumItems = pShipList.TGGetNumItems()
	pShipList.TGBeginIteration()
	for i in range(iNumItems):
		pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
		pSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)

	 	pPower = pPlayer.GetPowerSubsystem()
		pPower.SetCondition(1)

def AvailCoreParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	BackupBattery = pBattery.GetBackupBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	MaxBackupBattery = pBattery.GetBackupBatteryLimit()

	if not MainBattery < (MaxMainBattery/10):
		pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/10))
	else:
		pBattery.SetBackupBatteryPower(BackupBattery - (MaxBackupBattery/10))

#############################################################################################
#                                                                                           #
#  This Section Handles Repairs to the Destroyed Shield Generators,                         #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def Shields(pObject, pEvent):
       
	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/5):
		return
 
	pShieldSys = pPlayer.GetShields()
	
	if (pShieldSys == None):
		return

	if pShieldSys:
		pShieldHealth = pShieldSys.GetCondition()

		if  (pShieldHealth > 0):
			 return

	Response(pObject, pEvent)
	
	AvailShieldParts(pObject, pEvent)
	pShipSet = pPlayer.GetPropertySet()
	pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	iNumItems = pShipList.TGGetNumItems()
	pShipList.TGBeginIteration()
	for i in range(iNumItems):
		pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
		pSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)

		pShield = pPlayer.GetShields()
		pShield.SetCondition(1)

def AvailShieldParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower() 
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/5))

#############################################################################################
#                                                                                           #
#  This Section Handles Repairs to the Destroyed Sensor Array,                              #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def Sensors(pObject, pEvent):

	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/10):
		return
	
	pSensors = pPlayer.GetSensorSubsystem()
	
	if (pSensors == None):
		return

	if pSensors:
		pSensorHealth = pSensors.GetCondition()

		if  (pSensorHealth > 0):
			 return

	Response(pObject, pEvent)
	
	AvailSensorParts(pObject, pEvent)
	pShipSet = pPlayer.GetPropertySet()
	pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	iNumItems = pShipList.TGGetNumItems()
	pShipList.TGBeginIteration()
	for i in range(iNumItems):
		pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
		pSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)

		pSensors.SetCondition(pSubsystem.GetMaxCondition())
		pSensors.SetCondition(1)

def AvailSensorParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower() 
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/10))

#############################################################################################
#                                                                                           #
#  This Section Handles Repairs to the Destroyed Impulse Engines,                           #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def Impulse(pObject, pEvent):
	global pImpulseChildRepair 
	
	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/10):
		return

	pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
	
	if (pImpulseSys == None):
		return
	
	if pImpulseSys:
		iNumImpulse = pImpulseSys.GetNumChildSubsystems()
		for iEng in range(iNumImpulse):
			pImpulseChild = pImpulseSys.GetChildSubsystem(iEng)
			if (pImpulseChild.GetCondition() == 0):
				pImpulseChildCondition = pImpulseChild.GetCondition()
				pImpulseChildRepair  = pImpulseChild.SetCondition(1)
				if (pImpulseChildCondition == 0):
					ImpulseB(pObject, pEvent)
					return

def ImpulseB(pObject, pEvent):

	AvailImpulseParts(pObject, pEvent)
	Response(pObject, pEvent)
	pImpulseChildRepair
		
def AvailImpulseParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower() 
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/10))

#############################################################################################
#                                                                                           #
#  This Section Handles Repairs to the Destroyed Warp Engines,                              #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def WarpE(pObject, pEvent):
	global pWarpChildRepair 
	
	Check(pObject, pEvent)
	
	AreYouKazon(pObject, pEvent)
	if (REPLICATORS == "No"):
		return
	
	Core(pObject, pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower()
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	
	if MainBattery < (MaxMainBattery/5):
		return

	pWarpSys = pPlayer.GetWarpEngineSubsystem()
	
	if (pWarpSys == None):
		return
	
	if pWarpSys:
		iNumWarp = pWarpSys.GetNumChildSubsystems()
		for iEng in range(iNumWarp):
			pWarpChild = pWarpSys.GetChildSubsystem(iEng)
			if (pWarpChild.GetCondition() == 0):
				pWarpChildCondition = pWarpChild.GetCondition()
				pWarpChildRepair = pWarpChild.SetCondition(1)
				if (pWarpChildCondition == 0):
					WarpEB(pObject, pEvent)
					return

def WarpEB(pObject, pEvent):

	AvailWarpEParts(pObject, pEvent)
	Response(pObject, pEvent)
	pWarpChildRepair
		
def AvailWarpEParts(pObject, pEvent):

	pPlayer = MissionLib.GetPlayer()
	pBattery = pPlayer.GetPowerSubsystem()
	MainBattery = pBattery.GetMainBatteryPower() 
	MaxMainBattery = pBattery.GetMainBatteryLimit()
	pBattery.SetMainBatteryPower(MainBattery - (MaxMainBattery/5))

#############################################################################################
#                                                                                           #
#  This Section checks if certain weapon systems changed their names should the player      #
#  board a new ship,																        #
#                                                                                           #
#                                                                                           #
#############################################################################################

def Check(pObject, pEvent):
	global pButton7, pButton8, pButton9
	
	pPlayer = MissionLib.GetPlayer()

	pHeavyWeapons = pPlayer.GetPulseWeaponSystem()
	if (pHeavyWeapons == None):
		pHeavyWeaponsName = "Heavy Weapons"
	else:
		pHeavyWeaponsName = pHeavyWeapons.GetName()
	pButton9.SetName(App.TGString("Replicate " + str(pHeavyWeaponsName) + " parts requires 20% battery power"))
	
	pTorpedoes = pPlayer.GetTorpedoSystem()
	if (pTorpedoes == None):
		pTorpedoesName = "Torpedoes"
	else:
		pTorpedoesName = pTorpedoes.GetName()
	pButton8.SetName(App.TGString("Replicate " + str(pTorpedoesName) + " parts requires 10% battery power"))
	
	pPhaserSys = pPlayer.GetPhaserSystem()
	if (pPhaserSys == None):
		pLightWeaponsName = "Light Weapons"
	else:
		pLightWeaponsName = pPhaserSys.GetName()
	pButton7.SetName(App.TGString("Replicate " + str(pLightWeaponsName) + " parts requires 4% battery power"))

#############################################################################################
#                                                                                           #
#  The Kazon don't have replicators so if you are flying the Kazon Rider you're 			#
#  out of luck,																       		    #
#                                                                                           #
#                                                                                           #
#############################################################################################

def AreYouKazon(pObject, pEvent):
	global REPLICATORS

	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pShipName = pPlayer.GetShipProperty().GetShipName()
	
	if (pShipName == "Predator") or (pShipName == "SFRD_Promellian") or (pShipName == "Workerbee") or (pShipName == "Escape Pod"):
		REPLICATORS = "No"
	else:
		REPLICATORS = "Yes"

#############################################################################################
#                                                                                           #
#  This Section handles Brexs response.	There is also a timer to prvent Brex				#
#  responding too often, 																	#
#                                                                                           #
#                                                                                           #
#############################################################################################

def Response(pObject, pEvent):
	global PLAY

	if (PLAY == "Yes"):
		PLAY = "No"
		pGame = App.Game_GetCurrentGame() 
		pEpisode = pGame.GetCurrentEpisode() 
		pMission = pEpisode.GetCurrentMission()
		pDatabase = pMission.SetDatabase("data/TGL/Bridge Crew General.tgl")
		
		pSequence = App.TGSequence_Create()
		pSet = App.g_kSetManager.GetSet("bridge")
		pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
		if chance(33):
			pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "BrexYes3", None, 1, pDatabase))
		elif chance(50):
			pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "BrexYes4", None, 1, pDatabase))
		else:
			pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "ge007", None, 1, pDatabase))
		
		if chance(50):
			pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "ge151", None, 1, pDatabase))
		pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_PLAY_ANIMATION, "PushingButtons", None, 0))
		pSequence.Play()
		
		MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".Play", App.g_kUtopiaModule.GetGameTime() + 30, 0, 0)
		
def Play(pObject, pEvent):
	global PLAY

	PLAY = "Yes"
	
#############################################################################################
#                                                                                           #
#  This Section handles a Quick Battle start or end,				                        #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def Restart():
	
	EnableTimer = MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".Check", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)
