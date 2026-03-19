import App
import Foundation
import FoundationTech
import MissionLib
import loadspacehelper
import Bridge.BridgeUtils
import Lib.LibEngineering
import math
import traceback
from bcdebug import debug

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.1",
            "License": "LGPL",
            "Description": "Read info below for better understanding"
            }

"""
Based on AdvArmorTechThree version 1.941 BY Alex SL Gato, made for Greystar. Basically a weird combination between AdvArmorTechThree and some concepts from techs that also affect hull properties, like MEShields.
PLEASE NOTE THIS IS STILL A VERY EARLY-VERSION

Sample Setup:
# In scripts/Custom/ships/yourShip.py
# NOTE: replace "AMVoyager" with your abbrev
# NOTE: "Energy Subsystems" is a dictionary entry that provides a list, that list indicates the order where the properties used for the energy-side of these armor calculations are used (invincible but can be harmed) - only the first of those listed will be actually considered. By default (not mentioned/cannot find any of the lsited properties) it's the primary hull property.
# NOTE: "Armor Subsystems" is a dictionary entry that provides a list, which indicates what subsystems are used for the "armor" stuff (these are set to "invincible" but can be harmed and actually destroyed according to the damage absorbed by the first "Energy" subystem (not the actual energy systems)). By default (not mentioned/cannot find any of the lsited properties) this is set to the Power property.
Foundation.ShipDef.AMVoyager.dTechs = {
	'Adv Armor Tech EX': {"Energy Subsystems": [], "Armor Subsystems": []}
}

# In scripts/ships/yourShip.py

def GetArmorRatio(): # Strength of the armor, in a way
      return 2.5

def GetDamageStrMod(): # visual damage strength
	return 0

def GetDamageRadMod(): # visual damage radius
	return 0

def GetForcedArmor(): # If everyone is forced to wear it once it loads
	return 1

def GetArmouredModel(): # OPTIONAL: Select another scripts/ships/yourShip2.py with a adifferent model so when you are armored you change to this
	return "DiamondsArmorVoyager"

def GetOriginalShipModel(): # Should be the same script scripts/ships/yourShip2.py, but for more flexibility, here you can change it to never return when the armor drops
	return "DiamondsAMVoyager"
# In scripts/ships/Hardpopints/yourShip.py
# Add armored hull property, optional if you added GetArmorRatio above
#################################################
ArmourGenerator = App.HullProperty_Create("Armored Hull")

ArmourGenerator.SetMaxCondition(295000.000000)
ArmourGenerator.SetCritical(0)
ArmourGenerator.SetTargetable(1)
ArmourGenerator.SetPrimary(0)
ArmourGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ArmourGenerator.SetPosition2D(0.000000, 0.000000)
ArmourGenerator.SetRepairComplexity(1.000000)
ArmourGenerator.SetDisabledPercentage(0.500000)
ArmourGenerator.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ArmourGenerator)

# on the Property load function.
	prop = App.g_kModelPropertyManager.FindByName("Armored Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)

"""
TECH_NAME = "Adv Armor Tech EX"
REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

global sNewShipScript
sNewShipScript = {}
global sOriginalShipScript
sOriginalShipScript = {}
global AdvArmorRecord
AdvArmorRecord = {}
global vd_rad_mod
vd_rad_mod = {}
global vd_str_mod
vd_str_mod = {}
global pShipp
pShipp = {}

#global LastShipType
LastShipType = "nonArmored"

def detectBrokenSubsystemFromList(pShip, pSubsystem, subSystemList, subSystemPoundList, extraDamage=0, removeHeal=0, broken = 0, total = 0):
	if (pSubsystem.GetName() in subSystemList):
		total = total + 1
		broken = broken + (pSubsystem.GetCondition() <= 0.0) + (pSubsystem.GetCondition() - extraDamage <= 0.0 )

	iChildren = pSubsystem.GetNumChildSubsystems()
	if iChildren > 0:
		for iIndex in range(iChildren):
			pChild = pSubsystem.GetChildSubsystem(iIndex)
			if pChild:
				broken, total = detectBrokenSubsystemFromList(pShip, pChild, subSystemList, subSystemPoundList, extraDamage, removeHeal, broken, total)
	return broken, total	

def healSubsystemAndChild(pShip, pSubsystem, subSystemList, subSystemPoundList, extraDamage=0, removeHeal=0, invinState=0, depth = 0, systemsToDestroy=[]):
	if (pSubsystem.GetName() in subSystemList): # the "armor"
		if not pSubsystem.IsTargetable():
			finalDmg = pSubsystem.GetMaxCondition() - extraDamage
			if finalDmg > 0.0:
				pSubsystem.SetCondition(finalDmg)
			elif not (pShip.IsDead() or pShip.IsDying()):
				systemsToDestroy.append(pSubsystem)
	else:
		imTheEnergyBackup = (pSubsystem.GetName() in subSystemPoundList)
		if imTheEnergyBackup: # the "energy" counterparts
			if (not pSubsystem.IsHurtable()):
				pSubsystem.SetHurtable(1)

			if (not pSubsystem.IsTargetable()):
				finalDmg = pSubsystem.GetMaxCondition() - extraDamage
				if finalDmg < 0.0:
					finalDmg = 0.00001
				pSubsystem.SetCondition(finalDmg)

		elif (invinState) or (not pSubsystem.IsHurtable()):
			pSubsystem.SetHurtable(not invinState)

		#pSubsystem.SetCondition(pSubsystem.GetMaxCondition())

	iChildren = pSubsystem.GetNumChildSubsystems()
	if iChildren > 0:
		for iIndex in range(iChildren):
			pChild = pSubsystem.GetChildSubsystem(iIndex)
			if pChild:
				systemsToDestroy = healSubsystemAndChild(pShip, pChild, subSystemList, subSystemPoundList, extraDamage, removeHeal, invinState, depth + 1, systemsToDestroy)

	if (not invinState) or (not pSubsystem.IsInvincible()):
		pSubsystem.SetInvincible(invinState)

	if depth == 0:
		for system in systemsToDestroy:
			pShip.DestroySystem(system)

		return []
	else:
		return systemsToDestroy

def unhurtAllSubsystemsExceptASet(pShip, subSystemList, subSystemPoundList, extraDamage=0, removeHeal=0):

	invinState = 0
	try:
		broken = 0
		total = 0
		if removeHeal == 0:
			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			while pSubsystem:
				broken, total = detectBrokenSubsystemFromList(pShip, pSubsystem, subSystemList, subSystemPoundList, extraDamage, removeHeal, broken, total)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			pShip.EndGetSubsystemMatch(pIterator)

		invinState = ((removeHeal == 0) and ((total == 0) or (broken/total >= 1.0)))

		pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		systemsToDestroy = []
		while pSubsystem:
			systemsToDestroy = healSubsystemAndChild(pShip, pChild, subSystemList, subSystemPoundList, extraDamage, removeHeal, invinState, 1, systemsToDestroy)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

		pShip.EndGetSubsystemMatch(pIterator)

		for system in systemsToDestroy:
			pShip.DestroySystem(system)
	except:
		print (__name__, ".unhurtAllSubsystemsExceptASet ERROR:")
		traceback.print_exc()
		invinState = 0

	return invinState


# This class does control the attach and detach of the Models
class AdvArmorTechEXDef(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated Reality Bomb counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayerRespawned")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayerRespawned")

	def PlayerRespawned(self, pEvent):
		pPlayer = MissionLib.GetPlayer()
		if pPlayer:
			pInstance = findShipInstance(pPlayer)
			if not pInstance or not pInstance.__dict__.has_key(self.name):
				try:
					self.DeleteMenuButton("Tactical", "Adv Plating EX Offline")
				except:
					pass
				try:
					self.DeleteMenuButton("Tactical", "Adv Plating EX Online")
				except:
					pass

	# called by FoundationTech when a ship is created
	def AttachShip(self, pShip, pInstance):
		debug(__name__ + ", AttachShip")
		print ("Ship ", pShip.GetName(), "with ", self.name, " support added")

		self.bAddedWarpListener = {} # this variable will make sure we add our event handlers only once

		ModelList = 0
		try:
			ModelList = pInstance.__dict__[self.name]
		except:
			ModelList = 0
		
		if not ModelList:
			return
		
		try:
			global ArmorButton
			global AdvArmorRecord
			global vd_rad_mod
			global vd_str_mod
			global pShipp
			global LastShipType

			iShipID = pShip.GetObjID()
			if iShipID == None or iShipID == App.NULL_ID:
				return

			pGame = App.Game_GetCurrentGame()
			pEpisode = pGame.GetCurrentEpisode()
			pMission = pEpisode.GetCurrentMission()
			pPlayer = MissionLib.GetPlayer()
			iPlayerID = None
			if pPlayer and hasattr(pPlayer, "GetObjID"):
				iPlayerID = pPlayer.GetObjID()

			pBridge = App.g_kSetManager.GetSet("bridge")
			g_pTactical = App.CharacterClass_GetObject(pBridge,"Tactical")
			pTacticalMenu = Bridge.BridgeUtils.GetBridgeMenu("Tactical")

			AdvArmorRecord[iShipID] = 0
			vd_rad_mod[iShipID] = 0.0
			vd_str_mod[iShipID] = 0.0
			pShipp[iShipID] = pShip

			#print AdvArmorRecord[iShipID]
			#print vd_rad_mod[iShipID]
			#print vd_str_mod[iShipID]
			#print pShipp[iShipID]
			mustGo = 0
			if (iShipID == iPlayerID):
				if not self.bAddedWarpListener.has_key(iShipID):
					if LastShipType == "nonArmored":
						#print ("Ok the previous was not armored")
						ArmorButton = Lib.LibEngineering.CreateMenuButton("Adv Plating EX Offline", "Tactical", __name__ + ".AdvArmorTogglePlayer")
					else:
						#print ("Ok the previous WAS armored, attempting to get the past button")
						try:
							theMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
							ArmorButton = Lib.LibEngineering.GetButton("Adv Plating EX Offline", theMenu)
							#print ("Grabbed online button")
							if not ArmorButton:
								try:
									self.DeleteMenuButton("Tactical", "Adv Plating EX Online")
								except:
									pass
								try:
									self.DeleteMenuButton("Tactical", "Adv Plating EX Offline")
								except:
									pass
								ArmorButton = Lib.LibEngineering.CreateMenuButton("Adv Plating EX Offline", "Tactical", __name__ + ".AdvArmorTogglePlayer")
						except:
							try:
								theMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
								ArmorButton = Lib.LibEngineering.GetButton("Adv Plating EX Online", theMenu)
								#print ("Grabbed offline button")
								if not ArmorButton:
									try:
										self.DeleteMenuButton("Tactical", "Adv Plating EX Online")
									except:
										pass
									try:
										self.DeleteMenuButton("Tactical", "Adv Plating EX Offline")
									except:
										pass
									ArmorButton = Lib.LibEngineering.CreateMenuButton("Adv Plating EX Offline", "Tactical", __name__ + ".AdvArmorTogglePlayer")
							except:
								print("No armor button to grab, huh")
					try:
						LastShipType = "yesArmored"
					except:
						print("It doesn't let me change the LastShipType wth")
						traceback.print_exc()

					pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged") # Because of transporter mods out there
					pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage")
					self.bAddedWarpListener[iShipID] = 1
			else:
				if not self.bAddedWarpListener.has_key(iShipID):
					pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
					pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage")
					self.bAddedWarpListener[iShipID] = 1
				mustGo = 1

			imForced = 0
			try:
				pShipModule=__import__(pShip.GetScript())
				imForced = pShipModule.GetForcedArmor()
				#print ("I am forced, understood")
			except:
				#print ("I am not forced, understood")
				imForced = 0

			armorStatus = ((mustGo == 1) or (imForced == 1))

			if (iShipID == iPlayerID):
				AdvArmorTogglePlayerFirst(armorStatus)
			else:
				AdvArmorToggleAIFirst(pShip, armorStatus)
			
			print("SUCCESS while attaching advarmortechthree")
		except:
			print("ERROR while attaching advarmortechthree")
			traceback.print_exc()  

	# Called by FoundationTech when a Ship is removed from set (eg destruction)
	def DetachShip(self, iShipID, pInstance):
		# get our Ship
		debug(__name__ + ", DetachShip")
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if pShip:
			# remove the listeners
			#print("Have to detach advarmortechthree")
			pPlayer = MissionLib.GetPlayer()
			iPlayerID = None
			if pPlayer and hasattr(pPlayer, "GetObjID"):
				iPlayerID = pPlayer.GetObjID()
			if (iShipID == iPlayerID):
				try:
					self.DeleteMenuButton("Tactical", "Adv Plating EX Offline")
				except:
					pass
				try:
					self.DeleteMenuButton("Tactical", "Adv Plating EX Online")
				except:
					pass
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage")
			else:
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage")
			if self.bAddedWarpListener.has_key(iShipID):
				try:
					if self.bAddedWarpListener.has_key(iShipID):
						del self.bAddedWarpListener[iShipID]
				except:
					pass
				try:
					if AdvArmorRecord.has_key(iShipID):
						del AdvArmorRecord[iShipID]
				except:
					pass
				try:
					if vd_rad_mod.has_key(iShipID):
						del vd_rad_mod[iShipID]
				except:
					pass
				try:
					if vd_str_mod.has_key(iShipID):
						del vd_str_mod[iShipID]
				except:
					pass
				try:
					if pShipp.has_key(iShipID):
						del pShipp[iShipID]
				except:
					pass

	#def Detach(self, pInstance):
	#	debug(__name__ + ", Detach")
	#	self.DetachShip(pInstance.pShipID, pInstance)
	#	pInstance.lTechs.remove(self)

	# Deletes a button. From BCS:TNG's mod
	def DeleteMenuButton(self, sMenuName, sButtonName, sSubMenuName = None):
		debug(__name__ + ", DeleteMenuButton")
		try:
			pMenu   = self.GetBridgeMenu(sMenuName)
		except:
			traceback.print_exc()
			pMenu = None
		if not pMenu:
			pMenu   = Lib.LibEngineering.GetBridgeMenu(sMenuName)
		pButton = pMenu.GetButton(sButtonName)
		if sSubMenuName != None:
			pMenu = pMenu.GetSubmenu(sSubMenuName)
			pButton = pMenu.GetButton(sButtonName)

		pMenu.DeleteChild(pButton)


	# From ATP_GUIUtils:
	def GetBridgeMenu(self, menuName):
		debug(__name__ + ", GetBridgeMenu")
		pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
		pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
		if(pDatabase is None):
			return
		App.g_kLocalizationManager.Unload(pDatabase)
		return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))
		
oAdvArmorTechEX = AdvArmorTechEXDef(TECH_NAME)


# Extra functions
def SubsystemStateChanged(pObject, pEvent):
	debug(__name__ + ", SubsystemStateChanged")
	pShip = App.ShipClass_Cast(pObject)
	if not pShip or not hasattr(pShip, "GetObjID"):
		return
	iShipID = pShip.GetObjID()
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return
	pSubsystem = pEvent.GetSource()
	#debug(__name__ + ", SubsystemStateChanged: Ship ", iShipID, "with AdvArmorTech2 has changed a subsystem")

	# if the subsystem that changes its power is a weapon
	if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM):
		# set wings for this alert state
		#print "Ship %s with AdvArmorTech2 has changed the weapon subsystem" % iShipID
		amIPlayer = 0
		pPlayer = MissionLib.GetPlayer()
		if pPlayer and hasattr(pPlayer, "GetObjID") and not (pPlayer.IsDead() or pPlayer.IsDying()):
			iPlayerID = pPlayer.GetObjID()
			if iPlayerID != None and  iPlayerID != App.NULL_ID and iPlayerID == iShipID:
				amIPlayer = 1
		if not amIPlayer:
			AdvArmorToggleAI(pObject, pEvent, pShip)
		
	pObject.CallNextHandler(pEvent)

# called when subsystem on any ship is damaged
def SubDamage(pObject, pEvent):
	debug(__name__ + ", SubDamage")
	pShip = App.ShipClass_Cast(pObject)
	if not pShip or not hasattr(pShip, "GetObjID"):
		return

	iShipID = pShip.GetObjID()
	if iShipID == None or iShipID == App.NULL_ID:
		return
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return
	if pShip:
		amIPlayer = 0
		pPlayer = MissionLib.GetPlayer()
		if pPlayer and hasattr(pPlayer, "GetObjID") and not (pPlayer.IsDead() or pPlayer.IsDying()):
			iPlayerID = pPlayer.GetObjID()
			if iPlayerID != None and  iPlayerID != App.NULL_ID and iPlayerID == iShipID:
				amIPlayer = 1
		AdvArmorPlayer(pShip, isPlayer=amIPlayer)
	pObject.CallNextHandler(pEvent)

# called when subsystem on the player ship is damaged
def SubDamagePlayer(pObject, pEvent):
	debug(__name__ + ", SubDamagePlayer")
	
	AdvArmorPlayer()
	pObject.CallNextHandler(pEvent)

# Replaces the Model of pShip
def ReplaceModel(pShip, sNewShipScript):
	debug(__name__ + ", ReplaceModel")
	if not pShip or not hasattr(pShip, "GetObjID"):
		return
	iShipID = pShip.GetObjID()
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return

	if App.g_kLODModelManager.AreGlowMapsEnabled() == 1 and App.g_kLODModelManager.GetDropLODLevel() == 0:
		App.g_kLODModelManager.SetGlowMapsEnabled(0)
		App.g_kLODModelManager.SetGlowMapsEnabled(1)

	#print sNewShipScript
	ShipScript = __import__('ships.' + sNewShipScript)
	ShipScript.LoadModel()
	kStats = ShipScript.GetShipStats()
	pShip.SetupModel(kStats['Name'])
	if App.g_kUtopiaModule.IsMultiplayer():
		MPSentReplaceModelMessage(pShip, sNewShipScript)


	# Because hiding and unhiding the ship does not seem to do the job of fixing the weird lack of lights, but something like this dumb thing below does :/
	point = pShip.GetWorldLocation()
	pHitPoint = App.TGPoint3()
	pHitPoint.SetXYZ(point.x, point.y, point.z)

	pVec = pShip.GetVelocityTG()
	pVec.Scale(0.001)
	pHitPoint.Add(pVec)

	mod = "Tactical.Projectiles.AutomaticSystemRepairDummy" 
	try:
		from ftb.Tech.ATPFunctions import *
		pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, iShipID, iShipID, __import__(mod).GetLaunchSpeed())
		pTempTorp.SetLifetime(0.0)
	except:
		print (__name__, ".ReplaceModel: You are most likely missing '", mod, "' torpedo on your install, without that a weird black-texture-until-firing-or-fired bug may happen. Or another error:")
		traceback.print_exc()

def GetAdvArmor(pShip):
	pAdvArmor=0
	if not pShip or not hasattr(pShip, "GetObjID") or pShip.IsDead() or pShip.IsDying():
		return
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return pAdvArmor
	pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	while (pSubsystem != None):
		if(pSubsystem.GetName()=="Armored Hull"):
			pAdvArmor=pSubsystem
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	pShip.EndGetSubsystemMatch(pIterator)
	return(pAdvArmor)

def findShipInstance(pShip):
	debug(__name__ + ", findShipInstance")
	pInstance = None
	try:
		if not pShip or not hasattr(pShip, "GetObjID"):
			return pInstance
		pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
		if not pShip or pShip.IsDead() or pShip.IsDying():
			return pInstance
		if FoundationTech.dShips.has_key(pShip.GetName()):
			pInstance = FoundationTech.dShips[pShip.GetName()]
	except:
		pInstance = None
		pass

	return pInstance

def AdvArmorPlayer(aShip=None, isPlayer=1, techName = TECH_NAME): # For player
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	global pShipp
	armor_ratio=0.0
	pShip=None
	if isPlayer:
		pShip=MissionLib.GetPlayer()
	else:
		pShip = aShip
	if not pShip or not hasattr(pShip, "GetObjID") or pShip.IsDead() or pShip.IsDying():
		return
	iShipID = pShip.GetObjID()
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return

	pInstance = findShipInstance(pShip)
	techDict = None
	if not pInstance or not pInstance.__dict__.has_key(techName):
		return
	else:
		techDict = pInstance.__dict__[techName]

	subSystemList = []
	subSystemPoundList = []

	if type(techDict) == type({}):
		if techDict.has_key("Energy Subsystems"):
			subSystemPoundList = techDict["Energy Subsystems"]
		if techDict.has_key("Armor Subsystems"):
			subSystemList = techDict["Armor Subsystems"]

	pShipModule=__import__(pShip.GetScript())
	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		OldArmor=GetAdvArmor(pShip)
		if (OldArmor==0):
			return
		armor_ratio=.3
	pPower=pShip.GetPowerSubsystem()
	if (pPower==None):
		return
	pHull=pShip.GetHull()
	if (pHull==None):
		return
	if len(subSystemPoundList) <= 0:
		subSystemPoundList.append(pHull.GetName())

	if len(subSystemList) <= 0:
		subSystemList.append(pPower.GetName())

	BtnName=None
	if isPlayer:
		BtnName=App.TGString()
		ArmorButton.GetName(BtnName)
		if (BtnName.Compare(App.TGString("Adv Plating EX Online"),1)):
			return
	else:
		theCondition = not AdvArmorRecord[iShipID]
	
		if (theCondition):
			return

	batt_chg=pPower.GetMainBatteryPower()
	batt_limit=pPower.GetMainBatteryLimit()

	theCondition = (batt_chg<=(batt_limit*.05))

	inde = 0
	energySponge = None
	while ((not energySponge or (energySponge is None)) and inde < len(subSystemPoundList)):
		energySponge = MissionLib.GetSubsystemByName(pShip, subSystemPoundList[inde]) # Potential TO-DO we could totally customize this so it goes through multiple options...
		inde = inde + 1
	if not energySponge:
		energySponge = pHull

	if not theCondition:
		armor_pwr=batt_chg*armor_ratio
		hull_max=energySponge.GetMaxCondition()
		hull_cond=energySponge.GetCondition()
		hull_dmg=hull_max-hull_cond
		theCondition = (armor_pwr<hull_dmg)

	working = unhurtAllSubsystemsExceptASet(pShip, subSystemList, subSystemPoundList, extraDamage=0, removeHeal=(not (theCondition)))

	if (working):
		armor_pwr=armor_pwr-hull_dmg
		energySponge.SetCondition(hull_max)
		pPower.SetMainBatteryPower(armor_pwr/(armor_ratio+0.00001))
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)

	else:
		energySponge.SetCondition(hull_cond+armor_pwr)
		armor_pwr=0
		if isPlayer and ArmorButton != None:
			ArmorButton.SetName(App.TGString("Adv Plating EX Offline"))
		if (AdvArmorRecord[iShipID]):
			AdvArmorRecord[iShipID]=0		
			if (not sOriginalShipScript[iShipID] == None):
				ReplaceModel(pShip, sOriginalShipScript[iShipID])
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[iShipID])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[iShipID])
			pPower.SetMainBatteryPower(armor_pwr/(armor_ratio+0.00001))
	return

def AdvArmor(pShip, techNameAI=TECH_NAME): # for AI
	return AdvArmorPlayer(aShip=pShip, isPlayer=0, techName=techNameAI)


# called when armor button is clicked
def AdvArmorTogglePlayer(pObject, pEvent, aShip=None, isPlayer=1, techNameT=TECH_NAME):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	pShip = None
	if isPlayer:
		pShip=MissionLib.GetPlayer()
	else:
		pShip=aShip
	if not pShip or not hasattr(pShip, "GetObjID") or pShip.IsDead() or pShip.IsDying():
		return
	iShipID = pShip.GetObjID()
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return
	pShipModule=__import__(pShip.GetScript())

	pInstance = findShipInstance(pShip)
	techDict = None
	if not pInstance or not pInstance.__dict__.has_key(techNameT):
		return
	else:
		techDict = pInstance.__dict__[techNameT]

	subSystemList = []
	subSystemPoundList = []

	if type(techDict) == type({}):
		if techDict.has_key("Energy Subsystems"):
			subSystemPoundList = techDict["Energy Subsystems"]
		if techDict.has_key("Armor Subsystems"):
			subSystemList = techDict["Armor Subsystems"]

	if len(subSystemPoundList) <= 0:
		pHull=pShip.GetHull()
		if (pHull==None):
			return
		subSystemPoundList.append(pHull.GetName())

	if len(subSystemList) <= 0:
		pPower=pShip.GetPowerSubsystem()
		if (pPower==None):
			return
		subSystemList.append(pPower.GetName())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

	kStats=None
	try:
		kStats=pShipModule.GetShipStats()
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod[iShipID]=kStats['DamageRadMod']
		else:
			if hasattr(pShipModule, "GetDamageRadMod"):
				vd_rad_mod[iShipID]=pShipModule.GetDamageRadMod()
			else:
				vd_rad_mod[iShipID]=1

		if (kStats.has_key('DamageStrMod')):
			vd_str_mod[iShipID]=kStats['DamageStrMod']
		else:
			if hasattr(pShipModule, "GetDamageStrMod"):
				vd_str_mod[iShipID]=pShipModule.GetDamageStrMod()
			else:
				vd_str_mod[iShipID]=1
	except:
		try:
			if hasattr(pShipModule, "GetDamageRadMod"):
				vd_rad_mod[iShipID]=pShipModule.GetDamageRadMod()
			else:
				vd_rad_mod[iShipID]=1
			if hasattr(pShipModule, "GetDamageStrMod"):
				vd_str_mod[iShipID]=pShipModule.GetDamageStrMod()
			else:
				vd_str_mod[iShipID]=1
		except:
			#print "No visual changes, understood"
			vd_rad_mod[iShipID]=1
			vd_str_mod[iShipID]=1

	try:
		if kStats != None and (kStats.has_key('ArmouredModel')):
			#print "Hey I got it, extra model armour"
			sNewShipScript[iShipID] = kStats['ArmouredModel']
			sOriginalShipScript[iShipID] = kStats["OriginalModel"]
		else:
			if hasattr(pShipModule, "GetArmouredModel"):
				sNewShipScript[iShipID]=pShipModule.GetArmouredModel()
			else:
				sNewShipScript[iShipID] = None

			if hasattr(pShipModule, "GetOriginalShipModel"):
				sOriginalShipScript[iShipID]=pShipModule.GetOriginalShipModel()
			else:
				sOriginalShipScript[iShipID] = None
	except:
		try:
			if hasattr(pShipModule, "GetArmouredModel"):
				sNewShipScript[iShipID]=pShipModule.GetArmouredModel()
			else:
				sNewShipScript[iShipID] = None

			if hasattr(pShipModule, "GetOriginalShipModel"):
				sOriginalShipScript[iShipID]=pShipModule.GetOriginalShipModel()
			else:
				sOriginalShipScript[iShipID] = None
		except:
			#print "No visual armour, understood"
			sNewShipScript[iShipID] = None
			sOriginalShipScript[iShipID] = None

	BtnName=None
	theCondition = None
	if isPlayer:
		BtnName=App.TGString()
		ArmorButton.GetName(BtnName)
		theCondition = (BtnName.Compare(App.TGString("Adv Plating EX Online"),1))
	else:
		theCondition = not AdvArmorRecord[iShipID]	

	working = unhurtAllSubsystemsExceptASet(pShip, subSystemList, subSystemPoundList, extraDamage=0, removeHeal=(not (theCondition)))
	if not theCondition:
		if isPlayer and ArmorButton != None:
			ArmorButton.SetName(App.TGString("Adv Plating EX Offline"))
		conditionA = AdvArmorRecord[iShipID]
		if (conditionA):
			AdvArmorRecord[iShipID]=0
			if not (sOriginalShipScript[iShipID] == None):
				ReplaceModel(pShip, sOriginalShipScript[iShipID])
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[iShipID])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[iShipID])
	else:
		if isPlayer and ArmorButton != None:
			ArmorButton.SetName(App.TGString("Adv Plating EX Online"))
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript[iShipID]:
			ReplaceModel(pShip, sNewShipScript[iShipID])
		AdvArmorPlayer(pShip, isPlayer, techNameT)
	return

# called when armor button is clicked
def AdvArmorToggleAI(pObject, pEvent, pShip, techName=TECH_NAME):
	return AdvArmorTogglePlayer(pObject, pEvent, aShip=pShip, isPlayer=0, techNameT=techName)

# called when armor button is clicked
def AdvArmorTogglePlayerFirst(armourActive, aShip=None, isPlayer=1, techNameTF=TECH_NAME):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript

	if isPlayer:
		pShip=MissionLib.GetPlayer()
	else:
		pShip=aShip
	if not pShip or not hasattr(pShip, "GetObjID") or pShip.IsDead() or pShip.IsDying():
		return
	iShipID = pShip.GetObjID()
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return

	pInstance = findShipInstance(pShip)
	techDict = None
	if not pInstance or not pInstance.__dict__.has_key(techNameTF):
		return
	else:
		techDict = pInstance.__dict__[techNameTF]

	subSystemList = []
	subSystemPoundList = []

	if type(techDict) == type({}):
		if techDict.has_key("Energy Subsystems"):
			subSystemPoundList = techDict["Energy Subsystems"]
		if techDict.has_key("Armor Subsystems"):
			subSystemList = techDict["Armor Subsystems"]
	
	if len(subSystemPoundList) <= 0:
		pHull=pShip.GetHull()
		if (pHull==None):
			return
		subSystemPoundList.append(pHull.GetName())

	if len(subSystemList) <= 0:
		pPower=pShip.GetPowerSubsystem()
		if (pPower==None):
			return
		subSystemList.append(pPower.GetName())


	pShipModule=__import__(pShip.GetScript())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

	kStats=None
	try:
		kStats=pShipModule.GetShipStats()
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod[iShipID]=kStats['DamageRadMod']
		else:
			if hasattr(pShipModule, "GetDamageRadMod"):
				vd_rad_mod[iShipID]=pShipModule.GetDamageRadMod()
			else:
				vd_rad_mod[iShipID]=1

		if (kStats.has_key('DamageStrMod')):
			vd_str_mod[iShipID]=kStats['DamageStrMod']
		else:
			if hasattr(pShipModule, "GetDamageStrMod"):
				vd_str_mod[iShipID]=pShipModule.GetDamageStrMod()
			else:
				vd_str_mod[iShipID]=1
	except:
		try:
			if hasattr(pShipModule, "GetDamageRadMod"):
				vd_rad_mod[iShipID]=pShipModule.GetDamageRadMod()
			else:
				vd_rad_mod[iShipID]=1
			if hasattr(pShipModule, "GetDamageStrMod"):
				vd_str_mod[iShipID]=pShipModule.GetDamageStrMod()
			else:
				vd_str_mod[iShipID]=1
		except:
			#print "No visual changes, understood"
			vd_rad_mod[iShipID]=1
			vd_str_mod[iShipID]=1

	try:
		if kStats != None and (kStats.has_key('ArmouredModel')):
			#print "Hey I got it, extra model armour"
			sNewShipScript[iShipID] = kStats['ArmouredModel']
			sOriginalShipScript[iShipID] = kStats["OriginalModel"]
		else:
			if hasattr(pShipModule, "GetArmouredModel"):
				sNewShipScript[iShipID]=pShipModule.GetArmouredModel()
			else:
				sNewShipScript[iShipID] = None

			if hasattr(pShipModule, "GetOriginalShipModel"):
				sOriginalShipScript[iShipID]=pShipModule.GetOriginalShipModel()
			else:
				sOriginalShipScript[iShipID] = None
	except:
		try:
			if hasattr(pShipModule, "GetArmouredModel"):
				sNewShipScript[iShipID]=pShipModule.GetArmouredModel()
			else:
				sNewShipScript[iShipID] = None

			if hasattr(pShipModule, "GetOriginalShipModel"):
				sOriginalShipScript[iShipID]=pShipModule.GetOriginalShipModel()
			else:
				sOriginalShipScript[iShipID] = None
		except:
			#print "No visual armour, understood"
			sNewShipScript[iShipID] = None
			sOriginalShipScript[iShipID] = None

	BtnName=None
	theCondition = None
	if isPlayer:
		BtnName=App.TGString()
		ArmorButton.GetName(BtnName)
		theCondition = (BtnName.Compare(App.TGString("Adv Plating EX Online"),1))
	else:
		theCondition = not AdvArmorRecord[iShipID]	

	working = unhurtAllSubsystemsExceptASet(pShip, subSystemList, subSystemPoundList, extraDamage=0, removeHeal=(not (armourActive)))
	if not (working):
		if isPlayer and ArmorButton != None:
			ArmorButton.SetName(App.TGString("Adv Plating EX Offline"))

		AdvArmorRecord[iShipID]=0
		if not (sOriginalShipScript[iShipID] == None):
			ReplaceModel(pShip, sOriginalShipScript[iShipID])
		pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[iShipID])
		pShip.SetVisibleDamageStrengthModifier(vd_str_mod[iShipID])
	else:
		if isPlayer:
			ArmorButton.SetName(App.TGString("Adv Plating EX Online"))
		AdvArmorRecord[iShipID]=1
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript[iShipID]:
			ReplaceModel(pShip, sNewShipScript[iShipID])
		AdvArmorPlayer(pShip, isPlayer, techNameTF)
	return

# called when armor button is clicked
def AdvArmorToggleAIFirst(pShip, armourActive, techNameTFAI = TECH_NAME):
	return AdvArmorTogglePlayerFirst(armourActive, aShip=pShip, isPlayer=0, techNameTF = techNameTFAI)

def Restart():
	global ArmorButton
	global pShipp
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer=MissionLib.GetPlayer()
	iPlayerID = None
	if pPlayer and hasattr(pPlayer, "GetObjID"):
		iPlayerID = pPlayer.GetObjID()
	#if (pShipp == repr(pPlayer)):
	#	ArmorButton.SetName(App.TGString("Adv Plating EX Offline"))
	return

def MPSentReplaceModelMessage(pShip, sNewShipScript):
	# Setup the stream.
	# Allocate a local buffer stream.
	kStream = App.TGBufferStream()
	# Open the buffer stream with a 256 byte buffer.
	kStream.OpenBuffer(256)
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(REPLACE_MODEL_MSG))

	try:
		from Multiplayer.Episode.Mission4.Mission4 import dReplaceModel
		dReplaceModel[pShip.GetObjID()] = sNewShipScript
	except ImportError:
		pass

	# send Message
	kStream.WriteInt(pShip.GetObjID())
	iLen = len(sNewShipScript)
	kStream.WriteShort(iLen)
	kStream.Write(sNewShipScript, iLen)

	pMessage = App.TGMessage_Create()
	# Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)
	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	# TODO: Send it to asking client only
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
	# We're done.  Close the buffer.
	kStream.CloseBuffer()


def mp_send_settargetable(iShipID, iMode):
	# Setup the stream.
	# Allocate a local buffer stream.
	kStream = App.TGBufferStream()
	# Open the buffer stream with a 256 byte buffer.
	kStream.OpenBuffer(256)
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(SET_TARGETABLE_MSG))

	# send Message
	kStream.WriteInt(iShipID)
	kStream.WriteInt(iMode)

	pMessage = App.TGMessage_Create()
	# Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)
	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	# TODO: Send it to asking client only
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
	# We're done.  Close the buffer.
	kStream.CloseBuffer()
