#**********************************************************************************************************************
#	SG1EMPulse.py
#**********************************************************************************************************************
#	Author: wowsher aka Anthony Ordner
#	Created: May 28 2006
#	Credits: SuperSmeg for giving me the idea, Dave975 & DKealt for their excellent Stargate models, uss sovereign for his help
#	What am I?  A mod that adds a button to the Engineer menu with a new weapon.  Be careful it does not care friend or foe and is really to 
#			be used when alone and outnumbered.  I may also add code to ensure your systems are shut down or else it will disable 
#			you as well.  A very powerful weapon which must get some strict limits but still fun watching the ships tumble around...
#
#	As an FYI I actually started with the Tribbles code from BCS: TNG forum http://bcscripterstng.forumsplace.com/
#	Permission was obtained for the use of the Tribbles code from USS Sovereign
#	Permission was obtained from USS Sovereign to also use code from SG1TransportTorps.py to lock it to certain ships
#	Permission to use portions of the effect code used in Phalwave??? Not certain will submit this code to USS Sovereign to see if this is ok
#
#	File List:
#	scripts\custom\QBautostart\SG1EMPulse.py
#	scripts\custom\stargate\effects\em_pulse_short.mp3
#	scripts\custom\stargate\effects\systems_shut_down.mp3
#	scripts\custom\stargate\effects\nova_sphere3a.tga
#	scripts\custom\stargate\effects\nova_sphere.txt
#**********************************************************************************************************************
#	version 0.33 04-Jun-2007 Changed to tie to Cargo ship varients. 
#	version 0.32 03-Feb-2007 Lost code on try one, cleanup, added lock to ship thanks to USS Sovereign!
#					    Removed Mutator option and renamed py file to match SG1TransportTorps.py format
#	version 0.31 20-Jan-2007 Some more cleanup and added sound effects, adjusted camera and em wave effect
#	version 0.3	27-Nov-2006 Rewrote to use more direct calls to OEM code.  Works but does NOT actually do anything when buttons are
#					   Pushed.
#	version 0.21 23.Jun.2006  Removed unnecessary 'return's
#	version 0.2	10.Jun.2006  Now need to "charge" then "release", turn out lights on targets
#	version 0.11	04.Jun.2006  Removal of comments, some minor changes suggested by uss sovereign
#	version 0.1	28.May.2006  Finally got it to work damage wise.
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

pEMPButton = None
EMPEffectTimer = None
EMPChargeTimer = None
emcharge = 0

#Event Types
global EM_CHARGING
global EM_OVERLOAD
EM_CHARGING = App.Mission_GetNextEventType()
EM_OVERLOAD = App.Mission_GetNextEventType()

# Also not certain about this since I do not play MP games.  wowsher
MODINFO = {     "Author": "wowsher",
				"Version": "0.33",
				"License": "GPL",
				"Description": "EM Pulse knocks out ships in a ~20km radius around your ship",
				"needBridge": 0
			}

def init():
	#if not Libs.LibEngineering.CheckActiveMutator("EM Pulse"):
	#	return
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    # When you change a player ship then initiate the script
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".ShipCheck")
	## init

def BuildMenu():
	global pMain, pChargeButton, pReleaseButton
	# define buttons on Engineer menu for controlling the EMP
	pEngMenu = Bridge.BridgeUtils.GetBridgeMenu("Engineer")
	if (pEngMenu != None):
		pPulseMenu=App.STMenu_CreateW(App.TGString("EMPulse"))
		if (pPulseMenu != None):
			pEngMenu.PrependChild(pPulseMenu)
			pReleaseButton = Libs.LibEngineering.CreateMenuButton("Release", "Engineer", __name__ + ".ReleaseEMPulse",0,pPulseMenu)
			pChargeButton = Libs.LibEngineering.CreateMenuButton("Enable", "Engineer", __name__ + ".EnableEMWeapon",0,pPulseMenu)
			pReleaseButton.SetDisabled()
	## BuildMenu

def RemoveMenu():
	pEngMenu = Bridge.BridgeUtils.GetBridgeMenu("Engineer")
	if (pEngMenu != None):
		pPulseMenu = pEngMenu.GetSubmenu("EMPulse")
		if (pPulseMenu != None):
			pEngMenu.DeleteChild(pPulseMenu)
	## RemoveMenu

def ShipCheck(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	RemoveMenu() # Just in case...
	if (GetShipType(pPlayer) == "TelTakRefit"):
		BuildMenu()
	## ShipCheck

def EnableEMWeapon(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	pChargeButton.SetDisabled()
	emcharge = 1 # this is just to make the button a required use thing
	pReleaseButton.SetEnabled()
	#print "charged emcharge(1) = ", emcharge
	## ChargeEMWeapon
	
def ReleaseEMPulse(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode() # moved this left
	pMission = pEpisode.GetCurrentMission() # moved this left
	#This is taken from the phalwave scripts with very minor changes.  So the credit for this goes to uss sovereign.
	InitiateWaveSeq(pObject, pEvent)  
	pSet = pPlayer.GetContainingSet()	# suggested by uss sovereign as a more quick & stable way to get the correct player set
	lObjects = pSet.GetClassObjectList(App.CT_OBJECT)  # Get all the objects in this set
	for pObject in lObjects:
		if pObject.IsTypeOf(App.CT_SHIP):					# Only check further if the object is a ship
			if DistanceToTarget(pObject) < EMPMaxRadius:	# now check proximity to target, if within range then shut it down for a certain time
				pShip = App.ShipClass_Cast(pObject)			# ok we need to get the object reference
				if (pShip == None):							# just make certain we actually have one
					return									# return actually throws us out of the function
				sShipName = pShip.GetName()					# We need the display name for the ship
				pShip = MissionLib.GetShip(sShipName, None, 1)  # ok this may be strange but it really seems like we need a different object reference.. either way it works 
				if sShipName == "Player":					# We are "Player"
					continue  								# Go get the next object as we don't want to disable ourselves
				#print sShipName
				lSubs = [pShip.GetShields(), pShip.GetPowerSubsystem(), pShip.GetSensorSubsystem(),pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem(), pShip.GetTractorBeamSystem(),pShip.GetImpulseEngineSubsystem(), pShip.GetWarpEngineSubsystem(),pShip.GetCloakingSubsystem()]
				for pSystem in lSubs:
					if pSystem:		
						DisabledPercentage = pSystem.GetDisabledPercentage()
						pSystem.SetConditionPercentage(DisabledPercentage-0.02) # Will disable but still allow repair systems to work.EMPDamageEffect
				Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pObject, 1.5, sStatus = "Off")
	pChargeButton.SetEnabled()
	## ReleaseEMPulse	

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
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "LockedView", pPlayer.GetContainingSet().GetName(), pPlayer.GetName(), 350, 10, 50)) # size, distance or angle, distance or angle
	pSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pPlayer, 1.5, sStatus = "Off"), App.TGAction_CreateNull(), 1.0)
	pSequence.Play()
	pSound = App.TGSound_Create("scripts/Custom/Stargate/effects/systems_shut_down.mp3", "EMEnabled", 0)
	pSound.Play()
	MissionLib.CreateTimer(ET_EVENT, __name__ + ".InitiateWaveSeq2", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
	## InitiateWaveSeq

def InitiateWaveSeq2(pObject, pEvent):
	ET_EVENT = App.Mission_GetNextEventType()
	SetPlayerImpulse(None, None)
	pSequence = App.TGSequence_Create ()
	pSound = App.TGSound_Create("scripts/Custom/Stargate/effects/em_pulse_short.mp3", "EMPulse", 0)
	pSound.Play()
	# initiate the GFX sequence
	pSequence.AppendAction(StartSeq(), 1.0)
	MissionLib.CreateTimer(ET_EVENT, __name__ + ".EndSeq", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
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
	pSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pPlayer, 1.5, sStatus = "On"), App.TGAction_CreateNull(), 1.0)
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))
	# switch to bridge view
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
	# vEmitPos =  pPlayer.GetWorldForwardTG()
	# vEmitDir = pPlayer.GetWorldUpTG()
	fSize     = 40 #25  appears to be starting size of effect
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
	# pEffect.SetEmitPositionAndDirection(vEmitPos, vEmitDir)
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

