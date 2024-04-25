import App
import FoundationTech
import MissionLib
import loadspacehelper
import Bridge.BridgeUtils
import Lib.LibEngineering
import math
from bcdebug import debug

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "1.7",
            "License": "LGPL",
            "Description": "Read info below for better understanding"
            }

"""

Sample Setup:
# In scripts/Custom/ships/yourShip.py
# NOTE: replace "AMVoyager" with your abbrev
Foundation.ShipDef.AMVoyager.dTechs = {
	'Adv Armor Tech': 1
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

# This class does control the attach and detach of the Models
class AdvArmorTechTwoDef(FoundationTech.TechDef):
	
	# called by FoundationTech when a ship is created
        def AttachShip(self, pShip, pInstance):
                debug(__name__ + ", AttachShip")
                print "Ship %s with AdvArmorTechThree support added" % pShip.GetName()

                sNamePrefix = repr(pShip) + "_"

                self.bAddedWarpListener = {} # this variable will make sure we add our event handlers only once

                ModelList = 0
                try:
			ModelList = pInstance.__dict__["Adv Armor Tech"]
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

			pGame = App.Game_GetCurrentGame()
			pEpisode = pGame.GetCurrentEpisode()
			pMission = pEpisode.GetCurrentMission()
			pPlayer = MissionLib.GetPlayer()
			pBridge = App.g_kSetManager.GetSet("bridge")
			g_pTactical = App.CharacterClass_GetObject(pBridge,"Tactical")
			pTacticalMenu = Bridge.BridgeUtils.GetBridgeMenu("Tactical")
			AdvArmorRecord[repr(pShip)] = 0
			vd_rad_mod[repr(pShip)] = 0.0
			vd_str_mod[repr(pShip)] = 0.0
			pShipp[repr(pShip)] = pShip

			#print AdvArmorRecord[repr(pShip)]
			#print vd_rad_mod[repr(pShip)]
			#print vd_str_mod[repr(pShip)]
			#print pShipp[repr(pShip)]
			mustGo = 0
			if (repr(pShip) == repr(pPlayer)):
				if not self.bAddedWarpListener.has_key(repr(pShip)):
					if LastShipType == "nonArmored":
						#print ("Ok the previous was not armored")
						ArmorButton = Lib.LibEngineering.CreateMenuButton("Plating Offline", "Tactical", __name__ + ".AdvArmorTogglePlayer")
					else:
						#print ("Ok the previous WAS armored, attempting to get the past button")
						try:
							theMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
							ArmorButton = Libs.LibEngineering.GetButton("Plating Offline", theMenu)
						except:
							try:
								theMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
								ArmorButton = Libs.LibEngineering.GetButton("Plating Online", theMenu)
								#DeleteMenuButton("Tactical", "Plating Online")
							except:
								print("No armor button to grab, huh")
					try:
						LastShipType = "yesArmored"
					except:
						print("It doesn't let me change the LastShipType witb")
					App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_DAMAGED, pMission, __name__ + ".SubDamagePlayer")
					self.bAddedWarpListener[repr(pShip)] = 1
			else:
				if not self.bAddedWarpListener.has_key(repr(pShip)):
					pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
					pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage") # to-do aniadi esto y luego pMission to-do prueba pShip
					#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_DAMAGED, pMission, __name__ + ".SubDamage") # TO-DO AÑADI PSHIP BORRAR SI CRASHEA EL SISTEMA
					self.bAddedWarpListener[repr(pShip)] = 1
				mustGo = 1

			imForced = 0
			try:
				pShipModule=__import__(pShip.GetScript())
				imForced = pShipModule.GetForcedArmor()
				#print "I am forced, understood"
			except:
				#print "I am not forced, understood"
				imForced = 0

			armorStatus = ((mustGo == 1) or (imForced == 1))

			if (repr(pShip) == repr(pPlayer)):
				AdvArmorTogglePlayerFirst(armorStatus)
			else:
				AdvArmorToggleAIFirst(pShip, armorStatus)
			
			print("SUCCESS while attaching advarmortechthree")
		except:
			print("ERROR while attaching advarmortechthree")                

	# Called by FoundationTech when a Ship is removed from set (eg destruction)
        def DetachShip(self, iShipID, pInstance):
		# get our Ship
                debug(__name__ + ", DetachShip")
                pShip = App.ShipClass_GetObjectByID(None, iShipID)
                if pShip:
			# remove the listeners
			#print("Have to detach advarmortechtwo")
			pPlayer = MissionLib.GetPlayer()
			if (repr(pShip) == repr(pPlayer)):
				try:
					DeleteMenuButton("Tactical", "Plating Offline")
				except:
					try:
						DeleteMenuButton("Tactical", "Plating Online")
					except:
						print("No armor button to delete, huh")
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamagePlayer")
			else:
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage")
			if self.bAddedWarpListener.has_key(repr(pShip)):
				del self.bAddedWarpListener[repr(pShip)]
				del AdvArmorRecord[repr(pShip)]
				del vd_rad_mod[repr(pShip)]
				del vd_str_mod[repr(pShip)]
				del pShipp[repr(pShip)]

	# Deletes a button. From BCS:TNG's mod
	def DeleteMenuButton(sMenuName, sButtonName, sSubMenuName = None):
		debug(__name__ + ", DeleteMenuButton")
		pMenu   = GetBridgeMenu(sMenuName)
		pButton = pMenu.GetButton(sButtonName)
		if sSubMenuName != None:
			pMenu = pMenu.GetSubmenu(sSubMenuName)
			pButton = pMenu.GetButton(sButtonName)

		pMenu.DeleteChild(pButton)


	# From ATP_GUIUtils:
	def GetBridgeMenu(menuName):
		debug(__name__ + ", GetBridgeMenu")
		pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
		pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
		if(pDatabase is None):
			return
		App.g_kLocalizationManager.Unload(pDatabase)
		return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

        def SubsystemStateChanged(pObject, pEvent):
                debug(__name__ + ", SubsystemStateChanged")
                pShip = App.ShipClass_Cast(pObject)
                pSubsystem = pEvent.GetSource()
                #print "Ship %s with AdvArmorTech2 has changed a subsystem" % repr(pShip)

        	# if the subsystem that changes its power is a weapon
                if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM):
        		# set wings for this alert state
        		#print "Ship %s with AdvArmorTech2 has changed the weapon subsystem" % repr(pShip)
                        AdvArmorToggleAI(pObject, pEvent, pShip)
		
                pObject.CallNextHandler(pEvent)
                
oAdvArmorTechTwo = AdvArmorTechTwoDef("Adv Armor Tech")

def SubsystemStateChanged(pObject, pEvent):
	debug(__name__ + ", SubsystemStateChanged")
	pShip = App.ShipClass_Cast(pObject)
	pSubsystem = pEvent.GetSource()
	#debug(__name__ + ", SubsystemStateChanged: Ship ", repr(pShip), "with AdvArmorTech2 has changed a subsystem")

	# if the subsystem that changes its power is a weapon
	if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM):
		# set wings for this alert state
		#print "Ship %s with AdvArmorTech2 has changed the weapon subsystem" % repr(pShip)
		AdvArmorToggleAI(pObject, pEvent, pShip)
		
	pObject.CallNextHandler(pEvent)

# called when subsystem on any ship is damaged
def SubDamage(pObject, pEvent):
	debug(__name__ + ", SubDamage")
	pShip = App.ShipClass_Cast(pObject)
	if pShip:
		AdvArmor(pShip)
	pObject.CallNextHandler(pEvent)

# called when subsystem on the player ship is damaged
def SubDamagePlayer(pObject, pEvent):
	debug(__name__ + ", SubDamagePlayer")
	AdvArmorPlayer()
	pObject.CallNextHandler(pEvent)

# Replaces the Model of pShip
def ReplaceModel(pShip, sNewShipScript):
	debug(__name__ + ", ReplaceModel")
	#pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	#if not pShip:
	#	return
	#print sNewShipScript
        ShipScript = __import__('ships.' + sNewShipScript)
        ShipScript.LoadModel()
        kStats = ShipScript.GetShipStats()
        pShip.SetupModel(kStats['Name'])
	if App.g_kUtopiaModule.IsMultiplayer():
		MPSentReplaceModelMessage(pShip, sNewShipScript)

	# Because hiding and unhiding the ship does not seem to do the job of fixing the weird lack of lights, but something like this dumb thing below does :/
	from ftb.Tech.ATPFunctions import *

	point = pShip.GetWorldLocation()
	pHitPoint = App.TGPoint3()
	pHitPoint.SetXYZ(point.x, point.y, point.z)

	pVec = pShip.GetVelocityTG()
	pVec.Scale(0.001)
	pHitPoint.Add(pVec)

	mod = "Tactical.Projectiles.AutomaticSystemRepairDummy" 
	try:
		pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pShip.GetObjID(), pShip.GetObjID(), __import__(mod).GetLaunchSpeed())
		pTempTorp.SetLifetime(0.0)
	except:
		print "You are missing 'Tactical.Projectiles.AutomaticSystemRepairDummy' torpedo on your install, without that a weird black-texture-until-firing-or-fired bug may happen"

def AdvArmorPlayer(): # For player
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	global pShipp
	armor_ratio=0.0
	pShip=MissionLib.GetPlayer()
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

	BtnName=App.TGString()
	ArmorButton.GetName(BtnName)
	if (BtnName.Compare(App.TGString("Plating Online"),1)):
		return

	batt_chg=pPower.GetMainBatteryPower()
	batt_limit=pPower.GetMainBatteryLimit()
	if (batt_chg<=(batt_limit*.05)):
		ArmorButton.SetName(App.TGString("Plating Offline"))
		if (not sOriginalShipScript[repr(pShip)] == None):
			ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
		if (AdvArmorRecord[repr(pShip)]):
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
			AdvArmorRecord[repr(pShip)]=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
			pShip.SetInvincible(0)
		return
	armor_pwr=batt_chg*armor_ratio
	hull_max=pHull.GetMaxCondition()
	hull_cond=pHull.GetCondition()
	hull_dmg=hull_max-hull_cond
	
	if (armor_pwr>=hull_dmg):
		armor_pwr=armor_pwr-hull_dmg
		pHull.SetCondition(hull_max)
		pPower.SetMainBatteryPower(armor_pwr/armor_ratio)
	else:
		pHull.SetCondition(hull_cond+armor_pwr)
		armor_pwr=0
		ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord[repr(pShip)]):
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
			AdvArmorRecord[repr(pShip)]=0		
			if (not sOriginalShipScript[repr(pShip)] == None):
				ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
			pPower.SetMainBatteryPower(armor_pwr/armor_ratio)
			pShip.SetInvincible(0)

	return

def AdvArmor(pShip): # for AI
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	global pShipp
	armor_ratio=0.0
	#pShip=pShipp
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
	theCondition = not AdvArmorRecord[repr(pShip)]
	
	if (theCondition):
		return

	batt_chg=pPower.GetMainBatteryPower()
	batt_limit=pPower.GetMainBatteryLimit()
	if (batt_chg<=(batt_limit*.05)):
		if (not sOriginalShipScript[repr(pShip)] == None):
			ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
		if (AdvArmorRecord[repr(pShip)]):
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
			AdvArmorRecord[repr(pShip)]=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
			pShip.SetInvincible(0)
		return
	armor_pwr=batt_chg*armor_ratio
	hull_max=pHull.GetMaxCondition()
	hull_cond=pHull.GetCondition()
	hull_dmg=hull_max-hull_cond
	
	if (armor_pwr>=hull_dmg):
		armor_pwr=armor_pwr-hull_dmg
		pHull.SetCondition(hull_max)
		pPower.SetMainBatteryPower(armor_pwr/armor_ratio)
	else:
		pHull.SetCondition(hull_cond+armor_pwr)
		armor_pwr=0
		if (AdvArmorRecord[repr(pShip)]):
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
			AdvArmorRecord[repr(pShip)]=0		
			if (not sOriginalShipScript[repr(pShip)] == None):
				ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
			pPower.SetMainBatteryPower(armor_pwr/armor_ratio)
			pShip.SetInvincible(0)

	return

def GetAdvArmor(pShip):
	pAdvArmor=0
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
            if not pShip:
                return pInstance
            if FoundationTech.dShips.has_key(pShip.GetName()):
                pInstance = FoundationTech.dShips[pShip.GetName()]
            #if pInstance == None:
            #        print "After looking, no pInstance for ship:", pShip.GetName(), "How odd..."
        except:
            pass

        return pInstance

# called when armor button is clicked
def AdvArmorTogglePlayer(pObject, pEvent):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	pShip=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())

	pInstance = findShipInstance(pShip)
        if not pInstance or not pInstance.__dict__.has_key("Adv Armor Tech"):
		return

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

	try:
		kStats=pShipModule.GetShipStats
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod[repr(pShip)]=kStats['DamageRadMod']
		else:
			vd_rad_mod[repr(pShip)]=1
		if (kStats.has_key('DamageStrMod')):
			vd_str_mod[repr(pShip)]=kStats['DamageStrMod']
		else:
			vd_str_mod[repr(pShip)]=1
	except:
		try:
			vd_rad_mod[repr(pShip)]=pShipModule.GetDamageRadMod()
			vd_str_mod[repr(pShip)]=pShipModule.GetDamageStrMod()
		except:
			#print "No visual changes, understood"
			vd_rad_mod[repr(pShip)]=1
			vd_str_mod[repr(pShip)]=1
	try:
		if (kStats.has_key('ArmouredModel')):
			#print "Hey I got it, extra model armour"
			sNewShipScript[repr(pShip)] = kStats['ArmouredModel']
			sOriginalShipScript[repr(pShip)] = kStats["OriginalModel"]
	except:
		try:
			sNewShipScript[repr(pShip)]=pShipModule.GetArmouredModel()
			sOriginalShipScript[repr(pShip)]=pShipModule.GetOriginalShipModel()
		except:
			#print "No visual armour, understood"
			sNewShipScript[repr(pShip)] = None
			sOriginalShipScript[repr(pShip)] = None

	BtnName=App.TGString()
	ArmorButton.GetName(BtnName)

	if not (BtnName.Compare(App.TGString("Plating Online"),1)):
		ArmorButton.SetName(App.TGString("Plating Offline"))
		conditionA = AdvArmorRecord[repr(pShip)]
		if (conditionA):
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
			AdvArmorRecord[repr(pShip)]=0
			if not (sOriginalShipScript[repr(pShip)] == None):
				ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
			pShip.SetInvincible(0)
	else:
		ArmorButton.SetName(App.TGString("Plating Online"))
		AdvArmorRecord[repr(pShip)]=MissionLib.HideSubsystems(pShip)
		pShip.SetInvincible(1)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript[repr(pShip)]:
			ReplaceModel(pShip, sNewShipScript[repr(pShip)])
		AdvArmorPlayer()
	return

# called when armor button is clicked
def AdvArmorToggleAI(pObject, pEvent, pShip):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	pShipModule=__import__(pShip.GetScript())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

	try:
		kStats=pShipModule.GetShipStats
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod[repr(pShip)]=kStats['DamageRadMod']
		else:
			vd_rad_mod[repr(pShip)]=1
		if (kStats.has_key('DamageStrMod')):
			vd_str_mod[repr(pShip)]=kStats['DamageStrMod']
		else:
			vd_str_mod[repr(pShip)]=1
	except:
		try:
			vd_rad_mod[repr(pShip)]=pShipModule.GetDamageRadMod()
			vd_str_mod[repr(pShip)]=pShipModule.GetDamageStrMod()
		except:
			#print "No visual changes, understood"
			vd_rad_mod[repr(pShip)]=1
			vd_str_mod[repr(pShip)]=1
	try:
		if (kStats.has_key('ArmouredModel')):
			#print "Hey I got it, extra model armour"
			sNewShipScript[repr(pShip)] = kStats['ArmouredModel']
			sOriginalShipScript[repr(pShip)] = kStats["OriginalModel"]
	except:
		try:
			sNewShipScript[repr(pShip)]=pShipModule.GetArmouredModel()
			sOriginalShipScript[repr(pShip)]=pShipModule.GetOriginalShipModel()
		except:
			#print "No visual armour, understood"
			sNewShipScript[repr(pShip)] = None
			sOriginalShipScript[repr(pShip)] = None

	theCondition = not AdvArmorRecord[repr(pShip)]	
		
	if not (theCondition): # simplify? it's the same as below
		if (AdvArmorRecord[repr(pShip)]):
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
			AdvArmorRecord[repr(pShip)]=0
			if not (sOriginalShipScript[repr(pShip)] == None):
				ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
			pShip.SetInvincible(0)
	else:
		AdvArmorRecord[repr(pShip)]=MissionLib.HideSubsystems(pShip)
		pShip.SetInvincible(1)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript[repr(pShip)]:
			ReplaceModel(pShip, sNewShipScript[repr(pShip)])
		AdvArmor(pShip)
	return
# called when armor button is clicked
def AdvArmorTogglePlayerFirst(armourActive):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	pShip=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

	try:
		kStats=pShipModule.GetShipStats
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod[repr(pShip)]=kStats['DamageRadMod']
		else:
			vd_rad_mod[repr(pShip)]=1
		if (kStats.has_key('DamageStrMod')):
			vd_str_mod[repr(pShip)]=kStats['DamageStrMod']
		else:
			vd_str_mod[repr(pShip)]=1
	except:
		try:
			vd_rad_mod[repr(pShip)]=pShipModule.GetDamageRadMod()
			vd_str_mod[repr(pShip)]=pShipModule.GetDamageStrMod()
		except:
			#print "No visual changes, understood"
			vd_rad_mod[repr(pShip)]=1
			vd_str_mod[repr(pShip)]=1
	try:
		if (kStats.has_key('ArmouredModel')):
			#print "Hey I got it, extra model armour"
			sNewShipScript[repr(pShip)] = kStats['ArmouredModel']
			sOriginalShipScript[repr(pShip)] = kStats["OriginalModel"]
	except:
		try:
			sNewShipScript[repr(pShip)]=pShipModule.GetArmouredModel()
			sOriginalShipScript[repr(pShip)]=pShipModule.GetOriginalShipModel()
		except:
			#print "No visual armour, understood"
			sNewShipScript[repr(pShip)] = None
			sOriginalShipScript[repr(pShip)] = None

	BtnName=App.TGString()
	ArmorButton.GetName(BtnName)

	
	if not (armourActive):
		ArmorButton.SetName(App.TGString("Plating Offline"))
		try:
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
		except:
			pass
		AdvArmorRecord[repr(pShip)]=0
		if not (sOriginalShipScript[repr(pShip)] == None):
			ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
		pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
		pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
		pShip.SetInvincible(0)
	else:
		ArmorButton.SetName(App.TGString("Plating Online"))
		AdvArmorRecord[repr(pShip)]=MissionLib.HideSubsystems(pShip)
		pShip.SetInvincible(1)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript[repr(pShip)]:
			ReplaceModel(pShip, sNewShipScript[repr(pShip)])
		AdvArmorPlayer()
	return

# called when armor button is clicked
def AdvArmorToggleAIFirst(pShip, armourActive):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	pShipModule=__import__(pShip.GetScript())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

	try:
		kStats=pShipModule.GetShipStats
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod[repr(pShip)]=kStats['DamageRadMod']
		else:
			vd_rad_mod[repr(pShip)]=1
		if (kStats.has_key('DamageStrMod')):
			vd_str_mod[repr(pShip)]=kStats['DamageStrMod']
		else:
			vd_str_mod[repr(pShip)]=1
	except:
		try:
			vd_rad_mod[repr(pShip)]=pShipModule.GetDamageRadMod()
			vd_str_mod[repr(pShip)]=pShipModule.GetDamageStrMod()
		except:
			#print "No visual changes, understood"
			vd_rad_mod[repr(pShip)]=1
			vd_str_mod[repr(pShip)]=1
	try:
		if (kStats.has_key('ArmouredModel')):
			#print "Hey I got it, extra model armour"
			sNewShipScript[repr(pShip)] = kStats['ArmouredModel']
			sOriginalShipScript[repr(pShip)] = kStats["OriginalModel"]
	except:
		try:
			sNewShipScript[repr(pShip)]=pShipModule.GetArmouredModel()
			sOriginalShipScript[repr(pShip)]=pShipModule.GetOriginalShipModel()
		except:
			#print "No visual armour, understood"
			sNewShipScript[repr(pShip)] = None
			sOriginalShipScript[repr(pShip)] = None

	theCondition = not AdvArmorRecord[repr(pShip)]	
		
	if not (armourActive):
		try:
			MissionLib.ShowSubsystems(AdvArmorRecord[repr(pShip)])
		except:
			pass
		AdvArmorRecord[repr(pShip)]=0
		if not (sOriginalShipScript[repr(pShip)] == None):
			ReplaceModel(pShip, sOriginalShipScript[repr(pShip)])
		pShip.SetVisibleDamageRadiusModifier(vd_rad_mod[repr(pShip)])
		pShip.SetVisibleDamageStrengthModifier(vd_str_mod[repr(pShip)])
		pShip.SetInvincible(0)
	else:
		AdvArmorRecord[repr(pShip)]=MissionLib.HideSubsystems(pShip)
		pShip.SetInvincible(1)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript[repr(pShip)]:
			ReplaceModel(pShip, sNewShipScript[repr(pShip)])
		AdvArmor(pShip)
	return



def Restart():
	global ArmorButton
	global pShipp
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer=MissionLib.GetPlayer()
	if (pShipp == repr(pPlayer)):
		ArmorButton.SetName(App.TGString("Plating Offline"))
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
