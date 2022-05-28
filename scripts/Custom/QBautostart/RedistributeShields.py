import App 
import MissionLib
import Lib.LibEngineering
import Custom.Autoload.RedistributeShieldsMutator
from Libs.LibQBautostart import chance

SHIELDBUTTON = "No"


#############################################################################################
#                                                                                           #
# Initialization - Here the button is created at the start of each game.					#
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def init():
	global pShieldButton
	
	if not Lib.LibEngineering.CheckActiveMutator("Redistribute Shields"):
		return
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(Custom.Autoload.RedistributeShieldsMutator.ET_KEY_EVENT, MissionLib.GetMission(), __name__ + ".KeyShields")
	pShieldButton = Lib.LibEngineering.CreateMenuButton("Redistribute Shield", "Tactical", __name__ + ".RedistributeShields")


#############################################################################################
#                                                                                           #
# This hapens when you press the "Redistribute Shields" button as							#
# configured in the Main Menu.																#
#                                                                                           #
#                                                                                           #
#############################################################################################

def KeyShields(pObject, pEvent):
	global SHIELDBUTTON
	
	if SHIELDBUTTON == "No":
		SHIELDBUTTON = "Yes"
		RedistributeShields(pObject, pEvent)


#############################################################################################
#                                                                                           #
# This section covers the shield redistribution itself.										#
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def RedistributeShields(pObject, pEvent):
	global pComplete, pDone, SHIELDBUTTON
	
	pShip = MissionLib.GetPlayer()
	pShields = pShip.GetShields()
	
	pShieldsTotal = 0
	pWorstShield = 1
	pBestShield = 0
	pNumShields = pShields.GetNumShields()
	for iSh in range(pNumShields):
		pSingleShieldPercentage = pShields.GetSingleShieldPercentage(iSh)
		pShieldsTotal = pShieldsTotal + pSingleShieldPercentage
		if pSingleShieldPercentage < pWorstShield:
			pWorstShield = pSingleShieldPercentage
		if pSingleShieldPercentage > pBestShield:
			pBestShield = pSingleShieldPercentage
	
	if pShieldsTotal == 0:
		SHIELDBUTTON = "No"
		return
	
	if pNumShields == pShieldsTotal:
		SHIELDBUTTON = "No"
		return
		
	pEvenShields = pShieldsTotal / pNumShields
	pRoundShields = "%.2f"%pEvenShields
	pRoundSingleShield = "%.2f"%pSingleShieldPercentage
	if pRoundShields == pRoundSingleShield:
		SHIELDBUTTON = "No"
		return
	
	pShieldButton.SetDisabled()
	
	# This section covers how Felix responds and what he does (btton pushing)
	pGame = App.Game_GetCurrentGame() 
	pEpisode = pGame.GetCurrentEpisode() 
	pMission = pEpisode.GetCurrentMission()
	pDatabase = pMission.SetDatabase("data/TGL/Bridge Crew General.tgl")
	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
	if chance(25):
		pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "FelixYes1", None, 1, pDatabase))
	elif chance(33):
		pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "FelixYes2", None, 1, pDatabase))
	elif chance(50):
		pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "FelixYes3", None, 1, pDatabase))
	else:
		pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "FelixYes4", None, 1, pDatabase))
		
	if chance(50):
		pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "gt014", None, 1, pDatabase))
	pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_PLAY_ANIMATION, "PushingButtons", None, 0))
	pSequence.Play()
	
	pShields.RedistributeShields()
	
	pShieldDifference = pBestShield / pWorstShield
	if pShieldDifference > 10:
		pShieldDifference = 10
	
	# The maximum time that could be added to the timer is 40 seconds
	pExtraTime = 40
	pAddTime = (float(pShieldDifference) / 10) * pExtraTime
	
	# The minimum time to recalculate is 60 seconds
	pRawTimer = 60
	pTimer = pRawTimer + ((float(pAddTime) - (pExtraTime / 10)) * 1.111)
	
	pComplete = 0
	pDone =  100 / float(pTimer)
	Countdown(pObject, pEvent)


#############################################################################################
#                                                                                           #
# Here we create a neat countdown Timer (in increasing %).									#
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def Countdown(pObject, pEvent):
	global pComplete

	pComplete = pComplete + pDone
	pRoundComplete = float("%.0f"%pComplete)
	pRoundCompleteShow = int(pRoundComplete)
	if (pRoundComplete > 100) or (pRoundComplete == 100):
		AllowButton(pObject, pEvent)
	else:
		pShieldButton.SetName(App.TGString("Recalculating: " + str(pRoundCompleteShow) + "%"))
		MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".Countdown", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)


#############################################################################################
#                                                                                           #
# After 60 seconds we can redistribute again.												#
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def AllowButton(pObject, pEvent):
	global SHIELDBUTTON
	
	pShieldButton.SetName(App.TGString("Redistribute Shield"))
	pShieldButton.SetEnabled()
	SHIELDBUTTON = "No"


#############################################################################################
#                                                                                           #
# The button is enabled each time we start or end a Quick Battle.							#
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

def Restart():
	global pComplete
	
	pComplete = 100
