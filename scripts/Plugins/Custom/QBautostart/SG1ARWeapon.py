#**********************************************************************************************************************
#	SG1ARWeapon.py
#**********************************************************************************************************************
#	Author: wowsher aka Anthony Ordner
#	Created: June 16 2007
#	Credits: Dave975 & DKealt for their excellent Stargate models and Dave's idea, uss sovereign (This code uses most of the EMPulse)
#	What am I?  A mod that adds a button to the Engineer menu with a new weapon.  This is based on the idea that the Asgard created a weapon 
#	based on the ancient design that disrupts replicators disintegrating them.  It will kill pure replicator ships and disable replicator infected
#	ships while leaving all others alone.
#	This mod can ONLY by distributed with Dave975s permission.  It is tied to the 3rd ship pack release.  Since I am using code from 
# 	EMPulse I am assuming the permission to extend to this derivitive work as well.
#
#	Permission was obtained from USS Sovereign to also use code from SG1TransportTorps.py to lock it to certain ships for EMPulse which
#	with this is based on.
#	Permission to use portions of the effect code used in Phalwave was obtained from USS Sovereign for EMPulse which with this is based on.
#
#	File List:
#	scripts\custom\QBautostart\SG1ARWeapon.py
#	scripts\custom\stargate\effects\ARW.mp3
#	scripts\custom\stargate\effects\nova_sphere.txt
#	scripts\custom\stargate\effects\nova_sphere3a.tga
#**********************************************************************************************************************
#	version 0.32 15.August.2007 Tweaked camera, effect timing, etc.
#	version 0.31 11.August.2007 Changed to custom sound effect ARW.mp3
#	version 0.3 10.August.2007 Added visual and sound back using temp effects.  changed calling order to better syncronize effect, sound
#					      and ship damage but still a little out of sync... maybe with less ships... or no command ship.
#	version 0.2 04.August.2007 Removed all sound and visual effects maybe in the next major release I will try to readd them.
#	version 0.1	16.June.2007  Based completely on the EMPulse weapon code.
#**********************************************************************************************************************
EMPMaxRadius = 120 		# Have to figure out the distance divide by 6 to get km displayed on screen 90 ~ 15km, 120 ~ 20km
#**********************************************************************************************************************

# globals, imports and stuff
import App
import Bridge.BridgeUtils
import Libs.LibEngineering
import MissionLib
import Foundation
import string
import Custom.NanoFXv2.NanoFX_Lib

# Also not certain about this since I do not play MP games.  wowsher
MODINFO = {     "Author": "wowsher",
				"Version": "0.32",
				"License": "Only to Dave975 for his use in the Stargate ship pack 3",
				"Description": "Anti Replicator Weapon",
				"needBridge": 0
			}

def init():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    # When you change a player ship then initiate the script
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".ShipCheck")
	## init

def BuildMenu():
	global pMain, pChargeButton, pReleaseButton
	pEngMenu = Bridge.BridgeUtils.GetBridgeMenu("Engineer")
	if (pEngMenu != None):
		pPulseMenu=App.STMenu_CreateW(App.TGString("ARWeapon"))
		if (pPulseMenu != None):
			pEngMenu.PrependChild(pPulseMenu)
			pReleaseButton = Libs.LibEngineering.CreateMenuButton("Release", "Engineer", __name__ + ".InitiateWaveSeq",0,pPulseMenu)
			pReleaseButton.SetEnabled()
	## BuildMenu

def RemoveMenu():
	pEngMenu = Bridge.BridgeUtils.GetBridgeMenu("Engineer")
	if (pEngMenu != None):
		pPulseMenu = pEngMenu.GetSubmenu("ARWeapon")
		if (pPulseMenu != None):
			pEngMenu.DeleteChild(pPulseMenu)
	## RemoveMenu

def ShipCheck(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	RemoveMenu() # Just in case...
	if (GetShipType(pPlayer) == "DanielJackson"):
		BuildMenu()
	## ShipCheck

def ReleaseARWeapon(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode() # moved this left
	pMission = pEpisode.GetCurrentMission() # moved this left
	pSet = pPlayer.GetContainingSet()	# suggested by uss sovereign as a more quick & stable way to get the correct player set
	lObjects = pSet.GetClassObjectList(App.CT_OBJECT)  # Get all the objects in this set
	for pObject in lObjects:
		if pObject.IsTypeOf(App.CT_SHIP):					# Only check further if the object is a ship
			if DistanceToTarget(pObject) < EMPMaxRadius:	# now check proximity to target, if within range then shut it down for a certain time
				pShip = App.ShipClass_Cast(pObject)			# ok we need to get the object reference
				if (pShip == None):							# just make certain we actually have one
					return									# return actually throws us out of the function
				sShipName = pShip.GetName()					# We need the display name for the ship
				rPure = ['Spider Vessel','Command Cruiser']
				rInfested = ['Stolen Cruiser','Asgard Mothership','Goa`uld Ha`tak']
				# Returns long name in 
				if sShipName[:len(sShipName)-2] in rPure:
					killPure(sShipName,pObject)
				if sShipName[:len(sShipName)-2] in rInfested:
					disableInfested(sShipName,pObject)
	# ReleaseEMPulse	
	
def killPure(sShipName, pObject):
	pShip = MissionLib.GetShip(sShipName, None, 1)  # ok this may be strange but it really seems like we need a different object reference.. either way it works 
	pShip.DestroySystem (pShip.GetHull ())
	#killPure

def disableInfested(sShipName, pObject):
	pShip = MissionLib.GetShip(sShipName, None, 1)  # ok this may be strange but it really seems like we need a different object reference.. either way it works 
	lSubs = [pShip.GetShields(), pShip.GetPowerSubsystem(), pShip.GetSensorSubsystem(),pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem(), pShip.GetTractorBeamSystem(),pShip.GetImpulseEngineSubsystem(), pShip.GetWarpEngineSubsystem(),pShip.GetCloakingSubsystem(), pShip.GetRepairSubsystem()]
	for pSystem in lSubs:
		if pSystem:		
			DisabledPercentage = pSystem.GetDisabledPercentage()
			pSystem.SetConditionPercentage(0)
	#disableInfested

# It returns currently used Ship HP
def GetShipType(pShip):
	if pShip.GetScript():
		return string.split(pShip.GetScript(), '.')[-1]
	## GetShipType
	
# This one gets the distance to target
def DistanceToTarget(pObject):
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vTarget	= pObject.GetWorldLocation() 			# get world location of pObject
	vTarget.Subtract(pPlayer.GetWorldLocation()) 	# subtracts target location from player location ... This must be xyz format
	return vTarget.Length() 						# This must convert xyz difference to an actual straightline distance? Divide by 6 to get approx km
	## DistanceToTarget	
	
#************************************************************************************************************
# For Now we will just use this mostly verbatum from phalwave.py until I figure out the effect texture trick... 
# later I will change this to be how I want it.  wowsher
# Now removed 'return's 23.Jun.2006 wowsher
#************************************************************************************************************
# Path to the GFX folder
GFX = 'scripts/Custom/Stargate/effects/'

def InitiateWaveSeq(pObject, pEvent):
	ET_EVENT = App.Mission_GetNextEventType()
	pPlayer = MissionLib.GetPlayer()
	pSequence = App.TGSequence_Create ()
	pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "LockedView", pPlayer.GetContainingSet().GetName(), pPlayer.GetName(), 290, 25, 200)) # deg around, deg up/down, distance
	pSequence.Play()
	#pSound = App.TGSound_Create("scripts/Custom/Stargate/effects/systems_shut_down.mp3", "EMEnabled", 0)
	#pSound.Play()
	MissionLib.CreateTimer(ET_EVENT, __name__ + ".InitiateWaveSeq2", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
	## InitiateWaveSeq

def InitiateWaveSeq2(pObject, pEvent):
	ET_EVENT = App.Mission_GetNextEventType()
	SetPlayerImpulse(None, None)
	pSequence = App.TGSequence_Create ()
	pSound = App.TGSound_Create("scripts/Custom/Stargate/effects/ARW.mp3", "Firing", 0)
	pSound.Play()
	# initiate the GFX sequence
	pSequence.AppendAction(StartSeq(), 1.0)
	ReleaseARWeapon(pObject, pEvent)
	MissionLib.CreateTimer(ET_EVENT, __name__ + ".EndSeq", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)
	## InitiateWaveSeq2

def SetPlayerImpulse(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	pPlayer.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
	## SetPlayerImpluse

def StartSeq():
	Initiate()
	#InitiateWave(None, None)
	## StartSeq

def EndSeq(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	pSequence = App.TGSequence_Create ()
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))
	if App.g_kSetManager.GetSet("bridge"):
		pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
		pSequence.AppendAction(pAction)
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	pSequence.Play()
	## EndSeq

# Load the GFX
def StartGFX():
	LoadGfx(8,4,GFX) #8x4=32 frames of animation
	## StartGFX

# Create these textures on the ship
def CreateGFX():
	# first basic stuff we define where where from we'll emmit those textures etc.
	pPlayer = MissionLib.GetPlayer()
	pAttachTo = pPlayer.GetNode()
	#vEmitPos = pPlayer.GetWorldForwardTG()
	#vEmitDir = pPlayer.GetWorldUpTG()
	fSize     = 150 #40 #25  appears to be starting size of effect
	pSequence = App.TGSequence_Create()   
	pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pPlayer.GetNode())
	# setup some needed values, overall lifetime of the sequence is 6.5 seconds      
	#sFile = ChooseRandomTexture()
	sFile = GFX + "Nova_Sphere3a.tga"
	iTiming = 15.0
	fLifeTime = 1
	fRed = 255.0
	fGreen = 255.0
	fBlue = 255.0
	fBrightness = 0.8
	fSpeed = iTiming / 15.0
	# we start creating the effect, also very similar to the code from effects.py
	pEffect = App.AnimTSParticleController_Create()
	pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
	pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
	pEffect.AddAlphaKey(0.0, 1.0)
	pEffect.AddAlphaKey(1.0, 1.0)
	pEffect.AddSizeKey(0.0, fSize)
	pEffect.AddSizeKey(1.0, fSize)
	pEffect.SetEmitLife(fSpeed)
	pEffect.SetEmitFrequency(1)
	pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
	pEffect.SetInheritsVelocity(0)
	pEffect.SetDetachEmitObject(0)
	pEffect.CreateTarget(sFile)
	pEffect.SetTargetAlphaBlendModes(0, 7)
	pEffect.SetEmitFromObject(pEmitFrom)
	#pEffect.SetEmitPositionAndDirection(vEmitPos, vEmitDir)
	pEffect.AttachEffect(pAttachTo)               
	Effect = App.EffectAction_Create(pEffect)
	pSequence.AddAction(Effect)
	pSequence.Play ()
	## createGFX

# Support for multiple textures, thanks LJ ;)
def ChooseRandomTexture():
	iRandom = App.g_kSystemWrapper.GetRandomNumber(len(Foundation.GetFileNames(GFX, 'tga')))
	#strFile = GFX + "TT" + str(iRandom) + ".tga"
	strFile = GFX + "Nova_Sphere3a.tga"
	return strFile
	## ChooseRandomTexture

# Load textures
def LoadGfx(iNumXFrames, iNumYFrames, Folder):
	FileNames = Foundation.GetFileNames(Folder, 'tga')       
	for loadIndex in FileNames:
		strFile = Folder + str(loadIndex)
		fX = 0.0
		fY = 0.0
		pContainer = App.g_kTextureAnimManager.AddContainer(strFile)   
		pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
		for index in range(iNumXFrames * iNumYFrames):
			pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
			fX = fX + (1.0 / iNumXFrames)
			if (fX == 1.0):
				fX = 0.0
				fY = fY + (1.0 / iNumYFrames)
	## LoadGFX

# We call this upper in the script and it calls all relevant data to create a texture
def Initiate():
	StartGFX()
	for i in range(1):
		CreateGFX()	
	## Initialize