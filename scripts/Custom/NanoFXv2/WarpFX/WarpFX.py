from bcdebug import debug
###############################################################################
##	Filename:	NanoFXv2.py
##
##	Nano's Warp Sequence Version 1.0
##
##	Created:	03/26/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################

###############################################################################
#      Modified by USS Sovereign                                              #
#                                                                             #
#      Consider this something that should have been done in BC from the      #
#      beginning. Again I've removed my idiotic bable from the old version.   #
#      I've modified the way how calculating warp time works, needed for the  #
#      tweak I've made in NanoFX. I also needed to modify this file to return #
#      warp time in order to determine warp degradation.                      #
###############################################################################

import App 
import string
import TacticalInterfaceHandlers
import Foundation
import Custom.NanoFXv2.NanoFX_Lib
import Custom.NanoFXv2.NanoFX_Config
import Custom.NanoFXv2.NanoFX_ScriptActions
import WarpFX_GUI
import Effects
import MissionLib
import Actions.CameraScriptActions
from Custom.QBautostart.Libs.LibWarp import GetCurWarpSpeed, CalcWarpTime, SetInWarpLocationAction, DeWarp, GetWarpDestination, GetWarpDestinationSet, DoMiscPostWarpStuff, lDisAllowJoin, GetEntryDelayTime

# grml - the whole warp thing is broken - Defiant

g_Distance		 = 5.0
g_ShipSpeed		 = 0.0
g_ShipAccel		 = 0.0

TRUE = 1
FALSE = 0

Effects.g_pcWarpTrailTextureName = "scripts/Custom/NanoFXv2/WarpFX/Gfx/StarStreaks_Nano.tga"
Effects.g_fWarpTrailWidth = 0.175
Effects.g_fWarpTrailHeight = 11.00 * (WarpFX_GUI.GetWarpSpeed() / 2)

###############################################################################
##  Create Warp Nacelle Power up Flash Sequence
###############################################################################
def CreateNacelleFlashSeq(pShip, fSize):
	### Create Sequence Object ###
	debug(__name__ + ", CreateNacelleFlashSeq")
	pSequence = App.TGSequence_Create()
	###
	### Setup for Effect
	fFlashColor   = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "WarpFX")
	if (fFlashColor == None):
		sRace         = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
		fFlashColor   = Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)
	sOutterFile   = "scripts/Custom/NanoFXv2/WarpFX/Gfx/NacelleFlash/NacelleFlash_Outter.tga"
	sCoreFile     = "scripts/Custom/NanoFXv2/WarpFX/Gfx/NacelleFlash/NacelleFlash_Core.tga"
	pEmitFrom     = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	pAttachTo     = pShip.GetNode()
	pWarpSystem   = pShip.GetWarpEngineSubsystem()
	iNumWarpDrive = 0
	if pWarpSystem:
		iNumWarpDrive = pWarpSystem.GetNumChildSubsystems()
	###
	### Get Flash Positions on Each Nacelle
	try:
		#from Custom.AdvancedTechnologies.Data import ATP_Lib
		#lNacellePositions = ATP_Lib.GetNacellePositions(pShip)
		from Custom.Techs.SubModels import GetStartWarpNacellePositions
		lNacellePositions = GetStartWarpNacellePositions(pShip)
	except ImportError:
		retList=[]
		if iNumWarpDrive > 0:
			for i in range(iNumWarpDrive):
				pChild = pWarpSystem.GetChildSubsystem(i)
				if pChild:
					vLoc=pChild.GetPosition()
					retList.append(vLoc)

		lNacellePositions = retList[:]
	###
	### Create Flash on Each Nacelle
	for vWarpEngEmitPos in lNacellePositions:

		pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sOutterFile, pEmitFrom, pAttachTo, fSize * 2.0, vWarpEngEmitPos, iTiming = 11, fRed = fFlashColor[0], fGreen = fFlashColor[1], fBlue = fFlashColor[2], fBrightness = 0.6)
		pSequence.AddAction(pFlash)

		pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sCoreFile, pEmitFrom, pAttachTo, fSize * 2.0, vWarpEngEmitPos, iTiming = 11, fBrightness = 0.5)
		pSequence.AddAction(pFlash)		
	###
	return pSequence


def ETA(pAction, sString, fPosY, fTimer, iSize = 16):
	debug(__name__ + ", ETA")
	pSequence = App.TGSequence_Create()
	
	pString = App.TGString()
	pString.SetString(sString)
	
	pAction = App.TGScriptAction_Create("MissionLib", "TextBanner", pString, 0, fPosY, fTimer, iSize)
	pSequence.AddAction(pAction)
	
	pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pSequence))
	pSequence.Play()
	
	return 0


def DestinationCutscene(pWarpSeq, pShip):
	debug(__name__ + ", DestinationCutscene")
	pSequence = App.TGSequence_Create()
		
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "InitWarpSetLightingAction", "warp", pShip))
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeOut", 1))
		
	pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene", 1.0, 0.125, 1, 1, 0)
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "warp")
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", "warp")
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", "warp", pShip.GetName())
	pSequence.AppendAction(pAction)
			
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeIn", 1))
	
	pcDest = None
	pcDestModule = pWarpSeq.GetDestination()
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule
	pAction = App.TGScriptAction_Create(__name__, "ETA", "En Route to... " + pcDest, 0.04, 5.0)
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 1.0)

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", "warp")	
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 8.0)
        if App.g_kSetManager.GetSet("bridge"):
	        pAction	= App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
	        pSequence.AddAction(pAction, App.TGAction_CreateNull(), 8.0)
		
	pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 8.0)
	
	#pAction = App.TGScriptAction_Create(__name__, "FixBlinkers", pShip)
	#pSequence.AppendAction(pAction)
	
	return pSequence


def DoNothingAction(pAction):
	debug(__name__ + ", DoNothingAction")
	return 0


def DoingNothingSequence(pWarpSeq, pShip):
	debug(__name__ + ", DoingNothingSequence")
	pSequence = App.TGSequence_Create()
	
	pAction = App.TGScriptAction_Create(__name__, "DoNothingAction")
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 8.0)
	
	return pSequence


def FixBlinkers(pAction, pShip):
	debug(__name__ + ", FixBlinkers")
	import Custom.NanoFXv2.SpecialFX.BlinkerFX
	Custom.NanoFXv2.SpecialFX.BlinkerFX.CreateBlinkerFX(pShip)
	
	return 0


###############################################################################
## Engage... Assemble Pre-Warp Sequence
###############################################################################
def EngageWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip):
	### Setup Sequences ###
	debug(__name__ + ", EngageWarpSeq")
	pPreWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.PRE_WARP_SEQUENCE))
	pWarpBeginAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.WARP_BEGIN_ACTION)
	pWarpEndAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.WARP_END_ACTION)
	pMoveAction1 = pWarpSeq.GetWarpSequencePiece(pWarpSeq.MOVE_ACTION_1)
	###
	Effects.g_fWarpTrailHeight = 11.00 * (WarpFX_GUI.GetWarpSpeed() / 2)
	#fEntryDelayTime = 6.0 + pShip.GetRadius() / 2.0
	pWarpSoundAction1 = None
	fEntryDelayTime = GetEntryDelayTime(pShip)
	pShip.SetInvincible(1)
	
	###
	### If Player ship, setup for that ###
	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		### Clear the player's target ###
		TacticalInterfaceHandlers.ClearTarget(None, None)
		###
		pSequence = DestinationCutscene(pWarpSeq, pShip)	
		pWarpSeq.AddActionDuringWarp(pSequence, 1.2)
		pWarpSeq.AddAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"), pPreWarp)
	else:
		pSequence = DoingNothingSequence(pWarpSeq, pShip)
		pWarpSeq.AddActionDuringWarp(pSequence, 1.2)
	### If Ship has Moving Nacelles (Voyager) move them
	try:
		from Custom.AdvancedTechnologies.Data import ATP_Lib
		pMoveNacellesAction = App.TGScriptAction_Create("Custom.AdvancedTechnologies.Data.ATP_Lib", "ForceNacelles", pShip, "Up")
		pWarpSeq.AddAction(pMoveNacellesAction, pPreWarp, fEntryDelayTime - 2.8)
	except:
		ERROR = "No ATP3"
	###		
	### Engage Engine Sound
	sRace = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		pWarpSoundAction1 = App.TGSoundAction_Create(sRace + "EnterWarp")
		pWarpSoundAction1.SetNode(pWarpSet.GetEffectRoot())
		### Force Full Impulse ###
		pWarpSeq.AddAction(App.TGScriptAction_Create(__name__, "SetShipImpulse", pShip, 1.000000, TRUE), pPreWarp)
		fCount = 0.0
		while (fCount < fEntryDelayTime):
			pCoastAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetImpulse", pShip.GetObjID(), 1.0)
			pWarpSeq.AddAction(pCoastAction, pPreWarp, fCount)
			fCount = fCount + 0.1
	###
	else:
		if pWarpSeq.GetOrigin():
			pWarpSoundAction1 = App.TGSoundAction_Create(sRace + "EnterWarp", App.TGSAF_DEFAULTS, pWarpSeq.GetOrigin().GetName())
			pWarpSoundAction1.SetNode(pShip.GetNode())

	###
	pWarpSeq.AddAction(pWarpSoundAction1, pPreWarp, fEntryDelayTime - 2.8)
	pWarpSeq.AddAction(CreateNacelleFlashSeq(pShip, pShip.GetRadius()), pPreWarp, fEntryDelayTime - 0.9)
	###	
	### Begin Warping at the Delay Time ###
	#pWarpSeq.AppendAction(App.TGScriptAction_Create(__name__, "CheckShipStillAbleToWarpAction", pShip))
	pWarpSeq.AddAction(pWarpBeginAction, pPreWarp, fEntryDelayTime)
	###
	### Move the ship ###
	pWarpSeq.AddAction(pWarpEndAction, pWarpBeginAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 4.0)
	###
	### Create the warp flash ###
	pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pWarpSeq.AddAction(pFlashAction1, pWarpEndAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 4.0)
	###
	### Hide the ship ###
	pWarpSeq.AppendAction(App.TGScriptAction_Create(__name__, "HideShip", pShip.GetObjID(), TRUE))
	###
	### Place the ship in the warp set, shortly after WarpFlash ###
	pWarpSeq.AddAction(pMoveAction1, pFlashAction1, 0.1)
	###
	if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost():
		pGame = App.Game_GetCurrentGame()
		pMultGame = App.MultiplayerGame_Cast(pGame)
		pMultGame.SetReadyForNewPlayers(0)
		if not pShip.GetName() in lDisAllowJoin:
			lDisAllowJoin.append(pShip.GetName())

###############################################################################
## Travelling at Warp 9 Captain.... Assemble During Warp Sequence
###############################################################################
def DuringWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip, pFromSet=None):
	debug(__name__ + ", DuringWarpSeq")
	#pWarpSeq.AppendAction(App.TGScriptAction_Create(__name__, "CheckShipStillAbleToWarpAction", pShip))
	### Setup Sequences ###
	pWarpEnterAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.WARP_ENTER_ACTION)
	pDuringWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.DURING_WARP_SEQUENCE))
	pPostDuringWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.POST_DURING_WARP_SEQUENCE))
	pMoveAction1 = pWarpSeq.GetWarpSequencePiece(pWarpSeq.MOVE_ACTION_1)
	###
	pPreDuringWarpAction = pMoveAction1
	###
	pAction = App.TGScriptAction_Create(__name__, "HideShip", pShip.GetObjID(), FALSE)
	pWarpSeq.AppendAction(pAction)
	pWarpSeq.AddAction(pWarpEnterAction, pMoveAction1)
	#if (pPlayer != None) and (pShip.GetObjID() != pPlayer.GetObjID()):
	pAction = App.TGScriptAction_Create(__name__, "SetInWarpLocationAction", pShip, pWarpSeq, pFromSet, pWarpSet)
	pWarpSeq.AddAction(pAction, pWarpEnterAction)
	###
	### If this is the player, add the action that will wait until queued sequences are done ###
	pPrevious = pPreDuringWarpAction
	###
	### Trigger during-warp actions ###
	pWarpSeq.AddAction(pDuringWarp, pPrevious, 0.1)
	###
	### Add sequence for post-during warp actions ###
	###
	iTimeToWarp = int(CalcWarpTime(pShip, pWarpSeq))
	global WarpTime
	WarpTime = round(iTimeToWarp)
	iNum = 7
	pcDest = None
	pcDestModule = pWarpSeq.GetDestination()
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule
	if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
		#try:
		#	iWarpSpeed = WarpFX_GUI.GetWarpSpeed()
		#except:
		#	iWarpSpeed = 7
                # if we are in Multiplayer set this to a static number
                #if App.g_kUtopiaModule.IsMultiplayer():
                #        iTimeToWarp = 30
		#else:
                #        iTimeToWarp = App.g_kSystemWrapper.GetRandomNumber(Custom.NanoFXv2.NanoFX_Config.wFX_MaxRandomDistance)
		#        iTimeToWarp = iTimeToWarp * 9 / iWarpSpeed
		iWarpSpeed = GetCurWarpSpeed(pShip.GetName())
		WarpFX_GUI.SetWarpSpeed(int(iWarpSpeed))
		#print "Warp Speed is at Warp " + str(iWarpSpeed) + " ETA is " + str(iTimeToWarp + 5.0) + " seconds"
		### Set Distance so AI ships can Arrive right after you ###
		#global g_Distance
		#g_Distance = iTimeToWarp
		### Set up ETA Counter ###
		#pAction = App.TGScriptAction_Create(__name__, "ETA", "Destination: " + pcDest, 0.02, iTimeToWarp + 4.8, 12)
		#pWarpSeq.AddAction(pAction, pDuringWarp)
		#pAction = App.TGScriptAction_Create(__name__, "ETA", "Warp Speed: Warp " + str(iWarpSpeed), 0.06, iTimeToWarp + 4.8, 12)
		#pWarpSeq.AddAction(pAction, pDuringWarp)
		fCount = iTimeToWarp + 5
		while (iNum > 0):
			pAction = App.TGScriptAction_Create(__name__, "ETA", "ETA: " + str(fCount) + " seconds", 0.10, 0.8, 12)
			pWarpSeq.AddAction(pAction, pDuringWarp, 5 + iTimeToWarp - fCount)
			pAction = App.TGScriptAction_Create(__name__, "ETA", "Destination: " + pcDest, 0.02, 5.0, 12)
			pWarpSeq.AddAction(pAction, pDuringWarp)
			pAction = App.TGScriptAction_Create(__name__, "ETA", "Warp Speed: Warp " + str(iWarpSpeed), 0.06, 5.0, 12)
			pWarpSeq.AddAction(pAction, pDuringWarp)
			#pWarpSeq.AppendAction(App.TGScriptAction_Create(__name__, "CheckShipStillAbleToWarpAction", pShip))
			fCount = fCount - 1
			iNum = iNum - 1
		###			
		#pWarpSeq.AddAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"), pDuringWarp, iTimeToWarp + 4.5)
		###
	else:
		iWarpSpeed = GetCurWarpSpeed(pShip.GetName())
		pAction = pAction = App.TGScriptAction_Create(__name__, "DoNothingAction")
		pWarpSeq.AddAction(pAction, pDuringWarp)
		pAction = pAction = App.TGScriptAction_Create(__name__, "DoNothingAction")
		pWarpSeq.AddAction(pAction, pDuringWarp)
		fCount = iTimeToWarp + 5
		while (iNum > 0):
			pAction = App.TGScriptAction_Create(__name__, "DoNothingAction")
			pWarpSeq.AddAction(pAction, pDuringWarp, 5 + iTimeToWarp - fCount)
			#pWarpSeq.AppendAction(App.TGScriptAction_Create(__name__, "CheckShipStillAbleToWarpAction", pShip))
			fCount = fCount - 1
			iNum = iNum - 1
		### AI Ships use this Time to Arrive right after Player Ship ###
                # if we are in Multiplayer set this to a static number
                #if App.g_kUtopiaModule.IsMultiplayer():
                #        iTimeToWarp = 30
		#else:
                #        iTimeToWarp = g_Distance - 2.0
		#iTimeToWarp = int(CalcWarpTime(pShip, pWarpSeq))
		###
	###
	#pWarpSeq.AddAction(pPostDuringWarp, pDuringWarp, iTimeToWarp)
	
	pInWarpAction = App.TGScriptAction_Create("Custom.QBautostart.Libs.LibWarp", "RunInWarp", pShip, pWarpSeq, iTimeToWarp - iNum - 2, pDuringWarp, pPostDuringWarp, ExitWarpSeq, pcDest, iWarpSpeed)
	pWarpSeq.AddAction(pInWarpAction, pDuringWarp, 5)
	#pWarpSeq.AppendAction(pPostDuringWarp)
	###
	pWarpSeq.AddAction( App.TGScriptAction_Create("WarpSequence", "BridgeCameraForward"), pPostDuringWarp)
	###


###############################################################################
## Dropping out of Warp Captain..... Assemble Exit Warp Sequence
###############################################################################
def ExitWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip):

	### Get the destination set name from the module name, if applicable ###
	debug(__name__ + ", ExitWarpSeq")
	pcDest = None
	pcDestModule = GetWarpDestination(pShip, pWarpSeq)
	pDestSet = GetWarpDestinationSet(pShip, pWarpSeq)
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule
	###
	### Setup Sequences ###
	pPostDuringWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.POST_DURING_WARP_SEQUENCE))
	pPostWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.POST_WARP_SEQUENCE))
	pDewarpBeginAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.DEWARP_BEGIN_ACTION)
	pDewarpEndAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.DEWARP_END_ACTION)
	pDewarpFinishAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.DEWARP_FINISH_ACTION)
	pMoveAction2 = pWarpSeq.GetWarpSequencePiece(pWarpSeq.MOVE_ACTION_2)
	pFinalAction = pMoveAction2
	pFlashAction2 = None
	###
	fExitDelayTime = 7.0
	###
	pShip.SetInvincible(0)

	#if (App.g_kUtopiaModule.IsMultiplayer() == 0):
	# Add the action for setting the destination placement in the warp subsystem. This
	# has to go after the during-warp action, since mission changing may load new systems.
	pSetPlacementAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetWarpPlacement",
														pShip.GetObjID(), pcDest, pWarpSeq.GetPlacementName())
	pPostDuringWarp.AddAction(pSetPlacementAction)
#	else:
#		pSet = pDestSet
#		fRadius = pShip.GetRadius() * 1.25
#
#		while (1):
#			# Set an exit point instead.  Randomly generate an exit point.
#			kExitPoint = App.TGPoint3()
#			kExitPoint.x = App.g_kSystemWrapper.GetRandomNumber(200)
#			kExitPoint.x = kExitPoint.x - 100.0
#			kExitPoint.y = App.g_kSystemWrapper.GetRandomNumber(200)
#			kExitPoint.y = kExitPoint.y - 100.0
#			kExitPoint.z = App.g_kSystemWrapper.GetRandomNumber(200)
#			kExitPoint.z = kExitPoint.z - 100.0
#
#			if (pSet == None):
#				break
#			elif (pSet.IsLocationEmptyTG (kExitPoint, fRadius)):
#				pWarpSeq.SetExitPoint(kExitPoint)
#				break
#
#		pSetExitPointAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetWarpExitPoint",
#														pShip.GetObjID(), pcDest,
#														kExitPoint.x, kExitPoint.y, kExitPoint.z)
#		pPostDuringWarp.AddAction(pSetExitPointAction)

	# Move the ship from the warp set to the destination set
	# after the warp delay.  If the new set is None, this just
	# deletes the object.
	pPostDuringWarp.AddAction(App.TGScriptAction_Create("Custom.QBautostart.Libs.LibWarp", "CheckWarpInPath", pWarpSeq, pShip.GetObjID(), pDestSet), None, pWarpSeq.GetTimeToWarp())
	pPostDuringWarp.AppendAction(pDewarpBeginAction)
	pPostDuringWarp.AppendAction(pMoveAction2)
	pMoveActionCustom = App.TGScriptAction_Create("Custom.QBautostart.Libs.LibWarp", "DoWarpOutPostMoveAction", pShip, pWarpSeq, pDestSet)
	pPostDuringWarp.AppendAction(pMoveActionCustom)

	# Add the actions for exiting warp only if the destination set exists.
	if(pDestSet != None):
		fFlashDelay = pWarpSeq.GetTimeToWarp() - 0.5
		if(fFlashDelay < 0.0):
			fFlashDelay = 0.0
		fSwitchSetsDelay = fFlashDelay - 0.1
		if(fSwitchSetsDelay < 0.0):
			fSwitchSetsDelay = 0.0

		# If the player is the one warping, change the rendered set to the
		# player's new set.  Do this before the warp flash is created, so
		# the warp flash sound plays.  Also do it before the warp exit sound,
		# for the same reason.
		if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
			pCRSA2 = App.ChangeRenderedSetAction_Create(pcDestModule)
			pPostDuringWarp.AddAction(pCRSA2, App.TGAction_CreateNull(), fSwitchSetsDelay)

			# Setup a cutscene camera for the destination set.
			pCutsceneCameraBegin = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin",
															 pDestSet.GetName(), "WarpCutsceneCamera")
			pPostDuringWarp.AddAction(pCutsceneCameraBegin, pCRSA2)

			# Add actions to move the camera in the destination set to watch the placement,
			# so we can watch the ship come in.
			# Initial position is reverse chasing the placement the ship arrives at.
			#if (App.g_kUtopiaModule.IsMultiplayer()):
			#if 0:
			#	# Multiplayer watches the exit point rather than the exit placement
			#	# Create a placement object at the exit point.
			#	pMPPlacement = App.PlacementObject_Create(pShip.GetName() + "MPWarp1" + str(App.g_kUtopiaModule.GetGameTime()), pcDest, None)
			#	pMPPlacement2 = App.PlacementObject_Create(pShip.GetName() + "MPWarp2" + str(App.g_kUtopiaModule.GetGameTime()), pcDest, None)

			#	kPlayerFwd = pPlayer.GetWorldForwardTG()
			#	pMPPlacement.SetTranslateXYZ(kExitPoint.x, kExitPoint.y + (kPlayerFwd.y * 700.0), kExitPoint.z)
			#	pMPPlacement2.SetTranslateXYZ(kExitPoint.x, kExitPoint.y, kExitPoint.z)

			#	# look at where the player will come in
			#	pCameraAction3 = App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pcDest, pMPPlacement.GetName(), pMPPlacement2.GetName())
			#	pPostDuringWarp.AddAction(pCameraAction3, pCutsceneCameraBegin)
			#	# then, look at the player
			#	pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pcDest, pMPPlacement.GetName(), pPlayer.GetName(), 0)
			#	pPostDuringWarp.AddAction(pCameraAction4, pMoveAction2)
			#else:
			if 1:
				if(pWarpSeq.GetPlacementName() != None):
					fSideOffset = (App.g_kSystemWrapper.GetRandomNumber(700) - 350) / 100.0

					pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch",
															   pcDest, pWarpSeq.GetPlacementName())
					pPostDuringWarp.AddAction(pCameraAction4, pCutsceneCameraBegin)
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pDestSet.GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "AwayDistance", -1.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pDestSet.GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "ForwardOffset", 3.5))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pDestSet.GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "SideOffset", fSideOffset))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pDestSet.GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle1", 70.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pDestSet.GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle2", 110.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pDestSet.GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle3", -20.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pDestSet.GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle4", 20.0))


		# Create the second warp flash, slightly before the ship gets there.
		pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlashEnterSet", pcDestModule, pShip.GetObjID())
		pPostDuringWarp.AddAction(pFlashAction2, App.TGAction_CreateNull(), fFlashDelay)

		# Actions for the de-warping effect. The initiate action happens earlier.
		pPostDuringWarp.AddAction(pDewarpEndAction, pDewarpBeginAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 2.0)
		pPostDuringWarp.AddAction(pDewarpFinishAction, pDewarpEndAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 2.0)
		# Start the warp exit sound
		sRace = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
		if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
			pWarpSoundAction2 = App.TGSoundAction_Create(sRace + "ExitWarp")
			pWarpSoundAction2.SetNode(pWarpSet.GetEffectRoot())
			pPostDuringWarp.AddAction(pWarpSoundAction2, App.TGAction_CreateNull(), pWarpSeq.GetTimeToWarp() + 0.70)
		elif pWarpSeq.GetOrigin():
			pWarpSoundAction2	= App.TGSoundAction_Create(sRace + "ExitWarp", App.TGSAF_DEFAULTS, pWarpSeq.GetOrigin().GetName())
			pWarpSoundAction2.SetNode(pShip.GetNode())
			pPostDuringWarp.AddAction(pWarpSoundAction2, App.TGAction_CreateNull(), pWarpSeq.GetTimeToWarp() + 0.70)
		
		### If Ship has Moving Nacelles (Voyager) move them
		try:
			from Custom.AdvancedTechnologies.Data import ATP_Lib
			pMoveNacellesAction = App.TGScriptAction_Create("Custom.AdvancedTechnologies.Data.ATP_Lib", "ForceNacelles", pShip, "Down")
			pPostDuringWarp.AddAction(pMoveNacellesAction, pFlashAction2, 3.0)
		except:
			ERROR = "No ATP3"
		###
	# Drop out of cinematic mode, if we were in cinematic mode.
	if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
		### Force Full Impulse ###
		if pFlashAction2:
			pPostDuringWarp.AddAction(App.TGScriptAction_Create(__name__, "SetShipImpulse", pShip, 10.000000, FALSE), pFlashAction2)
		fCount = 0.0
		while (fCount < fExitDelayTime):
			pCoastAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetImpulse", pShip.GetObjID(), 0.5)
			pPostDuringWarp.AddAction(pCoastAction, pDewarpFinishAction, fCount)
			fCount = fCount + 0.1
		###	
		pCheckAction = App.TGScriptAction_Create("WarpSequence", "CheckForCameraChange")
		pPostDuringWarp.AddAction(pCheckAction, pDewarpFinishAction, fExitDelayTime)
	###
	# Do post-warp actions.
	pWarpSeq.AddAction(pPostWarp, pPostDuringWarp)

	if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
		pWarpSeq.AddAction(App.TGScriptAction_Create("Bridge.HelmMenuHandlers", "PostWarpEnableMenu"), pPostWarp)
		if not pShip.IsDead() and not pShip.IsDying():
			pWarpSeq.AddAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"), pPostWarp)
			pWarpSeq.AddAction(App.TGScriptAction_Create(__name__, "ResetShipImpulse", pShip, pPlayer), pPostWarp)
	pWarpSeq.AppendAction(App.TGScriptAction_Create(__name__, "DoMiscPostWarpStuff", pShip))


###############################################################################
## Assemble the Warp Sequence...
###############################################################################
def NanoWarpSeq(pWarpSeq):

	debug(__name__ + ", NanoWarpSeq")
	import MissionLib
	pMission = MissionLib.GetMission()
	
	if pMission and string.find(pMission.GetScript(), "Maelstrom") != -1:
		import WarpSequence
		return WarpSequence.SetupSequence_orig(pWarpSeq)

	### Setup ###
	pShip    = pWarpSeq.GetShip()
	pPlayer  = App.Game_GetCurrentPlayer()
	pWarpSet = App.WarpSequence_GetWarpSet()
	###
	### If not a Ship... Bail! ###
	if (pShip == None):
		return
	pFromSet = pShip.GetContainingSet()
	###
	### Picard says:  Engage! ###
	EngageWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip)
	###
	### We are Warping!!!!!
	DuringWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip, pFromSet)
	###
	### Dropping Out of Warp ###
	#ExitWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip)
	###
	
	
###############################################################################
#	WarpFlash(pAction, iShipID, fTime)
#	
#	Creates the warp flash. Should be called before the ship leaves its
#	current set.
#	
#	Args:	pAction			- the action, passed in automatically
#			iShipID			- the ID of the ship being affected
#			fTime			- the amount of time the flash should take
#	
#	Return:	zero for end.
###############################################################################
def WarpFlash(pAction, iShipID, fTime = None):
	debug(__name__ + ", WarpFlash")
	"Creates a warp flash."

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))

	if (pShip == None):
		return(0)

	# fixes problem where ships get orphaned if the mission is terminated
	# while they're warping.
	if (pShip.GetContainingSet() == None):
		return(0)

	if (fTime != None):
		pFlash = App.WarpFlash_Create(pShip, fTime)
	else:
		pFlash = App.WarpFlash_Create(pShip)

	return(0)

###############################################################################
#	WarpFlashEnterSet(pAction, pcSetName, iShipID, fTime = None)
#	
#	Creates a warp flash for a ship entering a set. Queries the ship as to
#	where it will be exiting warp, and the rotation, etc. so we know where
#	to place the flash.
#	
#	Args:	pAction			- the action, passed in automatically
#			pcSetName		- the name of the module for the destination set
#			iShipID			- the ID of the ship being affected
#			fTime			- the amount of time the flash should take
#	
#	Return:	zero for end.
###############################################################################
def WarpFlashEnterSet(pAction, pcSetName, iShipID, fTime = None):
	debug(__name__ + ", WarpFlashEnterSet")
	"Creates a warp flash for a ship entering a set."

#	kDebugObj.Print("WarpFlashEnterSet(): " + pcSetName)

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))

	if (pShip == None):
		return(0)
	
	pSetModule = __import__(pcSetName)
	pSet = pSetModule.GetSet()

	if (pSet == None):
#		kDebugObj.Print("WarpFlashEnterSet(): no set")
		return(0)

	pWarp = pShip.GetWarpEngineSubsystem()

	if (pWarp == None):
#		print "In WarpFlashEnterSet(): no warp engine subsystem for use"
		return(0)

	pLocation = pWarp.GetWarpExitLocation()
	pRotation = pWarp.GetWarpExitRotation()
	fRadius = pShip.GetRadius()

	if (fTime == None):
		pFlash = App.WarpFlash_CreateWithoutShip(pSet, pLocation, pRotation, fRadius)
	else:
		pFlash = App.WarpFlash_CreateWithoutShip(pSet, pLocation, pRotation, fRadius, fTime)

	return(0)


###############################################################################
#	HideShip(pAction, iShipID)
#	
#	Hides a ship. Used to mask the ship during the warp flash.
#	
#	Args:	pAction	- the action
#			iShipID	- the ID of the ship
#	
#	Return:	zero for end
###############################################################################
def HideShip(pAction, iShipID, iHide):
	debug(__name__ + ", HideShip")
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip:
		pShip.SetHidden(iHide)
		pShip.SetInvincible(0)

	return 0


def DebugCutscene(pAction):
	debug(__name__ + ", DebugCutscene")
	print "I am here"
	return 0


###############################################################################
## Set a Random Location
###############################################################################
def SetRandomLocation(pAction, pShip):
	
	debug(__name__ + ", SetRandomLocation")
	vPoint = App.TGPoint3()
	vPoint.SetX(App.g_kSystemWrapper.GetRandomNumber(71) - 35)
	vPoint.SetY(App.g_kSystemWrapper.GetRandomNumber(71) - 35)
	vPoint.SetZ(App.g_kSystemWrapper.GetRandomNumber(71) - 35)

	pShip.SetTranslate(vPoint)
	pShip.UpdateNodeOnly()
	
	return 0	


###############################################################################
## Force Impulse Settings for a Good "Show"
###############################################################################
def SetShipImpulse(pAction, pShip, fAccel, bBackupSettings = 1):
        # Don't Overload Impulse in MP!
        debug(__name__ + ", SetShipImpulse")
        if App.g_kUtopiaModule.IsMultiplayer():
                return 0
	
	if (pShip):
		
		pImpulse = pShip.GetImpulseEngineSubsystem().GetProperty()

		if (bBackupSettings == 1):
			global g_ShipSpeed
			global g_ShipAccel		
		
			g_ShipSpeed = pImpulse.GetMaxSpeed()
			g_ShipAccel = pImpulse.GetMaxAccel()
	
		pImpulse.SetMaxSpeed(7.000000)
		pImpulse.SetMaxAccel(fAccel)

	return 0


###############################################################################
## Reset our Impulse Settings
###############################################################################
def ResetShipImpulse(pAction, pShip, pPlayer):                
	debug(__name__ + ", ResetShipImpulse")
	if (pShip):
                # Don't Overload Impulse in MP!
                if not App.g_kUtopiaModule.IsMultiplayer():
		        pImpulse = pShip.GetImpulseEngineSubsystem().GetProperty()
		
		        pImpulse.SetMaxSpeed(g_ShipSpeed)
		        pImpulse.SetMaxAccel(g_ShipAccel)
		
		if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
			pTop = App.TopWindow_GetTopWindow()
                        if App.g_kSetManager.GetSet("bridge"):
			        pTop.ForceBridgeVisible()
                        else:
                                pTop.ForceTacticalVisible()
		
	return 0


def InitWarpSetLightingAction(pAction, sSetName, pShip):
	debug(__name__ + ", InitWarpSetLightingAction")
	InitWarpSetLighting(sSetName, pShip)
	return 0


def CheckShipStillAbleToWarpAction(pAction, pShip):
	debug(__name__ + ", CheckShipStillAbleToWarpAction")
	pWarp = pShip.GetWarpEngineSubsystem()
		
	if pShip.IsDead() or pShip.IsDying():
		print "Dead ship", pShip.GetName(), "breaking warp cutscene"
		DeWarp(pShip)
		return 1
	elif not pWarp or pWarp.IsDisabled() or not pShip.GetPowerSubsystem() or pShip.GetPowerSubsystem().IsDisabled():
		print pShip.GetName(), "lost his warp engines. Beaking warp cutscene"
		DeWarp(pShip)
		return 1
	return 0


def InitWarpSetLighting(sSetName, pShip):
	debug(__name__ + ", InitWarpSetLighting")
	kShipLocation = pShip.GetWorldLocation()
	
   	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(kShipLocation.GetX() -3.816000, kShipLocation.GetY(), kShipLocation.GetZ())
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.100000)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(kShipLocation.GetX(), kShipLocation.GetY(), kShipLocation.GetZ())
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.844013, 0.398183, 0.359295)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.510363, 0.390388, 0.766242)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.900000, 0.900000, 0.600000, 0.200000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"
	
	# Light position "Directional Light 2"
	kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(kShipLocation.GetX() -7.561178, kShipLocation.GetY() -13.532564, kShipLocation.GetZ()-0.087336)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.808193, 0.132823, -0.573744)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.532103, 0.582186, -0.614757)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.800000, 0.700000, 0.700000, 0.600000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light 2"

##### Sov Edit
def ReturnWarpTime():
    debug(__name__ + ", ReturnWarpTime")
    global WarpTime
    return WarpTime

###############################################################################
## End of WarpFX
###############################################################################
