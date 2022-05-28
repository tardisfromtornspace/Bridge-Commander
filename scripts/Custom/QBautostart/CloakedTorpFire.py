from bcdebug import debug
import App
import MissionLib
import Libs.LibCloakFire

DisableFire = 0

MODINFO = { "Author": "",
            "Download": "",
            "Version": "1.0",
            "License": "GPL",
            "Description": "Allows a ship to fire torpedoes while cloaked",
            "needBridge": 0
            }

def FireCloakTorpedo(pObject, pEvent):
	debug(__name__ + ", FireCloakTorpedo")
	global DisableFire
	if not (pEvent.GetBool()):
		DisableFire=0
		return
	if (DisableFire==1):
		return
	DisableFire=1
	pPlayer=MissionLib.GetPlayer()
	if not pPlayer:
		return
	pTarget=pPlayer.GetTarget()
	if not pTarget:
		return
	pTargetSubsystem=pPlayer.GetTargetSubsystem()
	pTorpSystem=pPlayer.GetTorpedoSystem()
	if (pTorpSystem==None):
		return
        if not pTorpSystem.IsOn():
                return
	pAmmoType=pTorpSystem.GetCurrentAmmoType()
	if (pAmmoType==None):
		return
	TypeNum=pTorpSystem.GetCurrentAmmoTypeNumber()
	pcTorpScriptName=pAmmoType.GetTorpedoScript()
	pLauncher=None
	for Child in range(pTorpSystem.GetNumChildSubsystems()):
		pTube=App.TorpedoTube_Cast(pTorpSystem.GetChildSubsystem(Child))
		if pTube and pTarget and (pTube.GetNumReady()>0 and pTube.IsInArc(pTarget.GetWorldLocation()) and pPlayer.IsCloaked() and pTube.GetConditionPercentage()>pTube.GetDisabledPercentage() and not pTube.IsDumbFire()):
			pLauncher=pTube
	if (pLauncher==None):
		return
	kPoint=pLauncher.GetWorldLocation()
        if App.g_kUtopiaModule.IsMultiplayer():
                Libs.LibCloakFire.MPSendTorpMessage(pPlayer.GetName(), kPoint, pcTorpScriptName, pTarget.GetObjID(), pTargetSubsystem.GetObjID())
	FireTorpFromPoint(kPoint,pcTorpScriptName,pPlayer.GetObjID(),pTarget.GetObjID(),pTargetSubsystem.GetObjID())
	pLauncher.UnloadTorpedo()
	pTorpSystem.LoadAmmoType(TypeNum,-1)
	return

def FireTorpedoEvent(pObject,pEvent):
	debug(__name__ + ", FireTorpedoEvent")
	FireCloakTorpedo(pObject,pEvent)
	pObject.CallNextHandler(pEvent)

def init():
	debug(__name__ + ", init")
	pGame=App.Game_GetCurrentGame()
	pEpisode=pGame.GetCurrentEpisode()
	pMission=pEpisode.GetCurrentMission()
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_INPUT_FIRE_SECONDARY,pMission,__name__+".FireTorpedoEvent")
	return

def Restart():
	debug(__name__ + ", Restart")
	return

###############################################################################
def FireTorpFromPoint(kPoint,pcTorpScriptName,idOwner=App.NULL_ID,idTarget=App.NULL_ID,idTargetSubsystem=App.NULL_ID,fSpeed = 0.0,pcSetName=None):
	debug(__name__ + ", FireTorpFromPoint")
	pTarget = App.ObjectClass_GetObjectByID(App.SetClass_GetNull(), idTarget)

	if (pcSetName != None):
		pSet = App.g_kSetManager.GetSet(pcSetName)
	elif (pTarget != None):
		pSet = pTarget.GetContainingSet()
	else:
		# No idea what set this is supposed to be in.
		return 0

	if (pSet == None):
		# No set.
		return 0

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)

	if (idTargetSubsystem != App.NULL_ID):
		pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(idTargetSubsystem))
		if (pSubsystem != None):
			pTorp.SetTargetOffset(pSubsystem.GetPosition())
		else:
			pTorp.SetTargetOffset(kPoint)
	else:
		pTorp.SetTargetOffset(kPoint)

	# No parent for the torpedo.
	pTorp.SetParent(idOwner)

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)

	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	if (pTarget != None):
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kTargetLocation.Subtract(kTorpLocation)
		kFwd = kTargetLocation
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()

	# Give the torpedo an appropriate speed.
	kVelocity = pTorp.GetWorldForwardTG()
	if (fSpeed == 0.0):
		kVelocity.Scale(pTorp.GetLaunchSpeed())
	else:
		kVelocity.Scale(fSpeed)

	pTorp.SetVelocity(kVelocity)

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

	return 0
###############################################################################