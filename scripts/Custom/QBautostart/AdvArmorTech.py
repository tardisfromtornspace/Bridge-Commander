
import App
import MissionLib
import Bridge.BridgeUtils
import Lib.LibEngineering

MODINFO = { "Author": "ed",
				"Download": "",
				"Version": "2.0",
				"License": "",
				"Description": "Support for armor and advanced armor"
	    		}

# called when subsystem on any ship is damaged
def SubDamage(pObject, pEvent):
	AdvArmor()
	pObject.CallNextHandler(pEvent)

def AdvArmor():
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
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
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
		return
	armor_pwr=batt_chg*armor_ratio
	hull_max=pHull.GetMaxCondition()
	hull_cond=pHull.GetCondition()
	hull_dmg=hull_max-hull_cond
	if (armor_pwr>=hull_dmg):
		armor_pwr=armor_pwr-hull_dmg
		pHull.SetCondition(hull_max)
	else:
		pHull.SetCondition(hull_cond+armor_pwr)
		armor_pwr=0
		ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
	pPower.SetMainBatteryPower(armor_pwr/armor_ratio)
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

# called when armor button is clicked
def AdvArmorToggle(pObject, pEvent):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	pShip=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())
	try:
		kStats=pShipModule.GetShipStats
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod=kStats['DamageRadMod']
		else:
			vd_rad_mod=1
		if (kStats.has_key('DamageStrMod')):
			vd_str_mod=kStats['DamageStrMod']
		else:
			vd_str_mod=1
	except:
		vd_rad_mod=1
		vd_str_mod=1
	BtnName=App.TGString()
	ArmorButton.GetName(BtnName)
	if not (BtnName.Compare(App.TGString("Plating Online"),1)):
		ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
	else:
		ArmorButton.SetName(App.TGString("Plating Online"))
		AdvArmorRecord=MissionLib.HideSubsystems(pShip)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		AdvArmor()
	return

# Initialize
def init():
	global ArmorButton
	global AdvArmorRecord
	global vd_rad_mod
	global vd_str_mod
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer=MissionLib.GetPlayer()
	pBridge = App.g_kSetManager.GetSet("bridge")
	g_pTactical = App.CharacterClass_GetObject(pBridge,"Tactical")
	pTacticalMenu = Bridge.BridgeUtils.GetBridgeMenu("Tactical")
	AdvArmorRecord=0
	vd_rad_mod=0.0
	vd_str_mod=0.0
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_DAMAGED, pMission, __name__ + ".SubDamage")
	ArmorButton=Lib.LibEngineering.CreateMenuButton("Plating Offline", "Tactical", __name__ + ".AdvArmorToggle")
	return

def Restart():
	global ArmorButton
	ArmorButton.SetName(App.TGString("Plating Offline"))
	return