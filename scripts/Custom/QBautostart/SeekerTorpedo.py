from bcdebug import debug
import App
import Libs.LibEngineering
import MissionLib
import loadspacehelper
import Foundation
import string
from CloakCounterMeasures import MultiPlayerEnableCollisionWith

MODINFO = {     "Author": "GMunoz",
                "Version": "1.0",
                "License": "GPL",
                "Description": "Seeker Torpedo",
                "needBridge": 0
            }

TorpPrepareTime = 60
lShipsWhiteList = ["EnterpriseNCC1701"]



def init():
	if App.g_kUtopiaModule.IsMultiplayer():
		return
	pMission = MissionLib.GetMission()
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__+ ".WeaponHit")
	pPrepare = Libs.LibEngineering.CreateMenuButton("Prepare Seeker Torp", "Science" , __name__ + ".PrepareTorp")
	pFireButton = Libs.LibEngineering.CreateMenuButton("Fire Seeker Torp", "Tactical", __name__ + ".FireHomingTorpedo")
	pFireButton.SetNotVisible()
	CheckButtons()


def PrepareTorp(pObject, pEvent):
	print("Preparing Homing Torpedo")

	pPlayer=MissionLib.GetPlayer()
	if (pPlayer==None):
		return

	pTorpSystem=pPlayer.GetTorpedoSystem()
	if (pTorpSystem==None):
		return

	if pTorpSystem.GetConditionPercentage() == 0:
		Sound = App.TGSound_Create("sfx/Bridge/Crew/Engineering/TorpedoesDestroyed.mp3", "Message", 0)
	elif pTorpSystem.IsDisabled():
		Sound = App.TGSound_Create("sfx/Bridge/Crew/Engineering/TorpedoesDisabled.mp3", "Message", 0)
	elif pTorpSystem.GetNumAvailableTorpsToType(pTorpSystem.GetCurrentAmmoTypeNumber()) == 0: 
		Sound = App.TGSound_Create("sfx/Bridge/Crew/Engineering/OutOfTorpedoes.mp3", "Message", 0)
	else:
		Sound = App.TGSound_Create("sfx/Bridge/Crew/Science/gs007.mp3", "Message", 0)
		Sound.SetSFX(0)
		Sound.SetInterface(1)
		App.g_kSoundManager.PlaySound("Message")
		pPrepareTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ShowFireButton", App.g_kUtopiaModule.GetGameTime() + TorpPrepareTime, 0, 0)
	return 0	

def ShowFireButton(pObject, pEvent):
	print("Homing Torpedo Ready")
	pBridgeSet = App.g_kSetManager.GetSet('bridge')
	pMenu = App.CharacterClass_GetObject(pBridgeSet, "Tactical")
	pTactical = pMenu.GetMenu()
	pFireButton=Libs.LibEngineering.GetButton("Fire Seeker Torp", pTactical)
	pFireButton.SetVisible()
	pTactical.ForceUpdate()
	Sound = App.TGSound_Create("sfx/Bridge/Crew/Tactical/ManualFireOn.mp3", "Ready2Fire", 0)
	Sound.SetSFX(0)
	Sound.SetInterface(1)
	App.g_kSoundManager.PlaySound("Ready2Fire")
	return


def FireHomingTorpedo(pObject, pEvent):
	
	pPlayer=MissionLib.GetPlayer()
	if (pPlayer==None):
		return

	pSet = pPlayer.GetContainingSet()
	if (pSet == None):
		print("No Set")
		return 

	pTorpSystem=pPlayer.GetTorpedoSystem()
	if (pTorpSystem==None):
		return

	pAmmoType=pTorpSystem.GetCurrentAmmoType()
	if (pAmmoType==None):
		return

	TypeNum=pTorpSystem.GetCurrentAmmoTypeNumber()
	pcTorpScriptName=pAmmoType.GetTorpedoScript()

	pLauncher=None
	for Child in range(pTorpSystem.GetNumChildSubsystems()):
		pTube=App.TorpedoTube_Cast(pTorpSystem.GetChildSubsystem(Child))
		if (pTube.GetNumReady()>0 and not pPlayer.IsCloaked() and pTube.GetConditionPercentage()>pTube.GetDisabledPercentage()):
			pLauncher=pTube

	if (pLauncher == None):
		print("No Tube available")
		return

	print("Homing torp loaded in %s" % pLauncher.GetName())

	pBridgeSet = App.g_kSetManager.GetSet('bridge')
	pMenu = App.CharacterClass_GetObject(pBridgeSet, "Tactical")
	pTactical = pMenu.GetMenu()
	pFireButton= Libs.LibEngineering.GetButton("Fire Seeker Torp", pTactical)
	pFireButton.SetNotVisible()
	pLauncher.UnloadTorpedo()
	pTorpSystem.LoadAmmoType(TypeNum,-1)
	pTactical.ForceUpdate()

	# Create the torpedo.
	global pTorp
	kPoint=pLauncher.GetWorldLocation()
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)

	# Set Torpedo Parent
	pTorp.SetParent(pPlayer.GetObjID())

	# Boost the Torp's capabilities.
	pTorp.SetMaxAngularAccel(10.0)
	pTorp.SetGuidanceLifetime(60.0)

	# Add the torpedo to the set
	pSet.AddObjectToSet(pTorp, None)
	pTorp.UpdateNodeOnly()

	pProximityManager = pSet.GetProximityManager()
	if (pProximityManager):
		pProximityManager.UpdateObject(pTorp)

	# Play the torpedo firing sound
	pcLaunchSound = pTorp.GetLaunchSound()
	if pcLaunchSound != None:
		pSound = App.g_kSoundManager.GetSound(pcLaunchSound)
		if pSound != None:
			pSound.AttachToNode(pTorp.GetNode())
			# Associate this sound with the sound region for the set we're in.
			pSoundRegion = App.TGSoundRegion_GetRegion(pSet.GetName())
			if pSoundRegion != None:
				pSoundRegion.AddSound(pSound)
			pSound.Play()

	# Get the Torpedo moving
	kTorpSpeed = pPlayer.GetWorldForwardTG()
	kTorpSpeed.Scale(pTorp.GetLaunchSpeed())
	pTorp.SetVelocity(kTorpSpeed)
	pTorp.UpdateNodeOnly()

	# Create delay before torpedo begins seeking for it's target. - for visiual effect
	pSeekTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".SeekTarget", App.g_kUtopiaModule.GetGameTime() + .5, 0, 0)
	return 0
	
def SeekTarget(pObject, pEvent):
	print("Seeking Target...")
	global pTorp
	idTarget=App.NULL_ID
	pTarget=SetTorpTarget(pTorp)
	if (pTarget != None):
		idTarget=pTarget.GetObjID()
		pTorp.SetTarget(idTarget)
		print ("Torpedo Targeting %s" % (pTarget.GetName()))
	else:
		print ("No Target")
	
	return 0

def SetTorpTarget(pTorp):
	pMission = MissionLib.GetMission()
	pPlayer=MissionLib.GetPlayer()
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies=pMission.GetFriendlyGroup()
	pNeutrals=pMission.GetNeutralGroup()
	pTarget=None
	pShip=None
	vPrevDistance = 300

	if pEnemies != None:
		ObjTuple = pEnemies.GetActiveObjectTupleInSet(pTorp.GetContainingSet())
		if len(ObjTuple):
			for i in ObjTuple:
				pShip = App.ShipClass_Cast(i)
				pShipImpulse = pShip.GetImpulseEngineSubsystem()
				if pShip and pShipImpulse:
					vDistance = DistanceCheck(pTorp, pShip)
					if vDistance <= 600 and vDistance < vPrevDistance:
						pTarget=pShip
						vPrevDistance = vDistance
	if pFriendlies != None:
		ObjTuple = pFriendlies.GetActiveObjectTupleInSet(pTorp.GetContainingSet())
		if len(ObjTuple):
			for i in ObjTuple:
				pShip = App.ShipClass_Cast(i)
				#print pShip.GetName()
				pShipImpulse = pShip.GetImpulseEngineSubsystem()
				if pShip and pShipImpulse and (pShip.GetName() != pPlayer.GetName()):
					vDistance = DistanceCheck(pTorp, pShip)
					if vDistance <= 600 and vDistance < vPrevDistance:
						pTarget=pShip
						vPrevDistance = vDistance

	if pNeutrals != None:
		ObjTuple = pNeutrals.GetActiveObjectTupleInSet(pTorp.GetContainingSet())
		if len(ObjTuple):
			for i in ObjTuple:
				pShip = App.ShipClass_Cast(i)
				pShipImpulse = pShip.GetImpulseEngineSubsystem()
				if pShip and pShipImpulse:
					vDistance = DistanceCheck(pTorp, pShip)
					if vDistance <= 600 and vDistance < vPrevDistance:
						pTarget=pShip
						vPrevDistance = vDistance

	if pTarget==None:
		print("Failed to find Target")
		return None

	print ("Closest ship %s" % (pTarget.GetName()))

	if pTarget.IsCloaked():
		print("Ship is Cloaked")
		pFirePoint=TorpFirepoint(pTarget)
		return pFirePoint

	return pTarget


def TorpFirepoint(pShip):
	pFirePoint = None
	if (pShip != None):
		pFirePoint = MissionLib.GetShip("Torpedo Target")
		# if it does not exist we have to create it first
		if not pFirePoint:
			print("Creating Fire Point")
			pFirePoint = loadspacehelper.CreateShip("Firepoint", pShip.GetContainingSet(), "Torpedo Target", None)
			MissionLib.GetNeutralGroup().AddName("Torpedo Target")
			pFirePoint = MissionLib.GetShip("Torpedo Target")
			pFirePoint.EnableCollisionsWith(pShip, 0)
			if App.g_kUtopiaModule.IsMultiplayer():
				MultiPlayerEnableCollisionWith(pFirePoint, pShip, 0)
			pShip.AttachObject(pFirePoint)
			pFirePoint.SetTargetable(0)

	return pFirePoint

def DistanceCheck(pObject1, pObject2):
	vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())
	nLength=vDifference.Length()
	print ("%s is at distance %s" %(pObject2.GetName(), nLength))
	return vDifference.Length()	


def WeaponHit(pObject, pEvent):
	pFirePoint = MissionLib.GetShip("Torpedo Target")
	if (pFirePoint != None):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
#		print('Seeker Torpedo hit %s' %pShip.GetName())
		MissionLib.GetPlayer().GetContainingSet().RemoveObjectFromSet("Torpedo Target")
#		pFirePointattr = App.ShipClass_Cast(pFirePoint)
#		pFirePointattr.DestroySystem(pFirePointattr.GetHull())

	pObject.CallNextHandler(pEvent)


def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        return string.split(pShip.GetScript(), '.')[-1]


def ShipHasStringInName(shipfile, stringfind):
        debug(__name__ + ", ShipHasStringInName")
        if string.find(string.lower(shipfile), string.lower(stringfind)) == -1:
                return 0
        return 1


def CheckButtons():
	if App.g_kUtopiaModule.IsMultiplayer():
		return
	pBridgeSet = App.g_kSetManager.GetSet('bridge')
	pMenu = App.CharacterClass_GetObject(pBridgeSet, "Tactical")
	pTactical = pMenu.GetMenu()
	pFireButton= Libs.LibEngineering.GetButton("Fire Seeker Torp", pTactical)
	if not pFireButton:
		return
	pFireButton.SetNotVisible()
	pTactical.ForceUpdate()

	# disable button
	pMenu = App.CharacterClass_GetObject(pBridgeSet, "Science")
	pScience = pMenu.GetMenu()
	pPrepareButton = Libs.LibEngineering.GetButton("Prepare Seeker Torp", pScience)
	pPrepareButton.SetNotVisible()

	# and enable if player ship is the 1701-A
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
        shipfile = GetShipType(pPlayer)
	for sShip in lShipsWhiteList:
		if ShipHasStringInName(shipfile, sShip):
			pPrepareButton.SetVisible()


def Restart():
	CheckButtons()

def NewPlayerShip():
	CheckButtons()
