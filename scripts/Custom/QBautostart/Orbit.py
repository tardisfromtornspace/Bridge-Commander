# Orbit Planet script by Defiant <mail@defiant.homedns.org>
#
# Simple and Easy :)
#

# Imports
import App
import MissionLib
import Lib.LibEngineering

# Vars
MODINFO = { "Author": "\"Defiant\" mail@defiant.homedns.org",
            "Download": "http://defiant.homedns.org/~erik/STBC/OrbitTarget/",
            "Version": "1.3",
            "License": "GPL",
            "Description": "Orbit your Target",
            "needBridge": 0
            }

sButtonName = "current Target"

# Main part
def  OrbitTarget(pObject, pEvent):
	#print("Orbiting Target...")
	        
	# More Vars
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pTarget = pPlayer.GetTarget()
	pSet = App.g_kSetManager.GetSet("bridge")
	pCharacter = App.CharacterClass_GetObject(pSet, "Helm")
        
        # Test if we have a Target        
        if not pTarget:
                print("No Target")
                return
                        
        if pCharacter:
	        pDatabase = pCharacter.GetDatabase()
                
	        # Play Audio
	        App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SAY_LINE, "StandardOrbit", None, 1, pDatabase).Play()
	
	# ...and Orbit
	MissionLib.SetPlayerAI("Helm", CreateAI(pPlayer,  pTarget))


# 100% from AI.Player.OrbitPlanet
def StartingOrbit(pShip, pPlanet):
	# Send an event saying that the ship is now orbitting the
	# planet it's around.
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(App.ET_AI_ORBITTING)
	pEvent.SetDestination(pPlanet)
	pEvent.SetSource(pShip)
	App.g_kEventManager.AddEvent(pEvent)


# 100% from AI.Player.OrbitPlanet
def CreateAI(pShip, pPlanet):
	#########################################
	# Creating PlainAI StartingOrbitScript at (241, 52)
	pStartingOrbitScript = App.PlainAI_Create(pShip, "StartingOrbitScript")
	pStartingOrbitScript.SetScriptModule("RunScript")
	pStartingOrbitScript.SetInterruptable(1)
	pScript = pStartingOrbitScript.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("StartingOrbit")
	pScript.SetArguments(pShip, pPlanet)
	# Done creating PlainAI StartingOrbitScript
	#########################################
	#########################################
	# Creating PlainAI CirclePlanet at (353, 55)
	pCirclePlanet = App.PlainAI_Create(pShip, "CirclePlanet")
	pCirclePlanet.SetScriptModule("CircleObject")
	pCirclePlanet.SetInterruptable(1)
	pScript = pCirclePlanet.GetScriptInstance()
	pScript.SetFollowObjectName(pPlanet.GetName())
	pScript.SetNearFacingVector(App.TGPoint3_GetModelLeft())
	pScript.SetRoughDistances(pPlanet.GetRadius() + 150, pPlanet.GetRadius() + 190)
	# Done creating PlainAI CirclePlanet
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (201, 111)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (301, 127)
	pSequence.AddAI(pStartingOrbitScript)
	pSequence.AddAI(pCirclePlanet)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating ConditionalAI CloseEnough at (210, 167)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 200.0 + pPlanet.GetRadius(),  pShip.GetName(), pPlanet.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCloseEnough = App.ConditionalAI_Create(pShip, "CloseEnough")
	pCloseEnough.SetInterruptable(1)
	pCloseEnough.SetContainedAI(pSequence)
	pCloseEnough.AddCondition(pInRange)
	pCloseEnough.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CloseEnough
	#########################################
	#########################################
	# Creating PlainAI FlyToPlanet at (328, 183)
	pFlyToPlanet = App.PlainAI_Create(pShip, "FlyToPlanet")
	pFlyToPlanet.SetScriptModule("Intercept")
	pFlyToPlanet.SetInterruptable(1)
	pScript = pFlyToPlanet.GetScriptInstance()
	pScript.SetTargetObjectName(pPlanet.GetName())
	pScript.SetInterceptDistance(0.0)
	pScript.SetAddObjectRadius(1)
	# Done creating PlainAI FlyToPlanet
	#########################################
	#########################################
	# Creating PriorityListAI OrbitPriorityList at (156, 227)
	pOrbitPriorityList = App.PriorityListAI_Create(pShip, "OrbitPriorityList")
	pOrbitPriorityList.SetInterruptable(1)
	# SeqBlock is at (272, 228)
	pOrbitPriorityList.AddAI(pCloseEnough, 1)
	pOrbitPriorityList.AddAI(pFlyToPlanet, 2)
	# Done creating PriorityListAI OrbitPriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI OrbitAvoidObstacles at (128, 289)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pOrbitAvoidObstacles = App.PreprocessingAI_Create(pShip, "OrbitAvoidObstacles")
	pOrbitAvoidObstacles.SetInterruptable(1)
	pOrbitAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pOrbitAvoidObstacles.SetContainedAI(pOrbitPriorityList)
	# Done creating PreprocessingAI OrbitAvoidObstacles
	#########################################
	return pOrbitAvoidObstacles


def CreateOrbitButton():
    # Get the Orbit Planet Button
    pBridgeDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
    ButtonTGLName = pBridgeDatabase.GetString("Orbit Planet")
    App.g_kLocalizationManager.Unload(pBridgeDatabase)
    pHelmMenu = Lib.LibEngineering.GetBridgeMenu("Helm")
    pOrbitMenu = GetButton(ButtonTGLName.GetCString(), pHelmMenu)
    if pOrbitMenu:
    	pOrbitButton = GetButton(sButtonName, pOrbitMenu)

    	if not pOrbitButton:
    		Lib.LibEngineering.CreateMenuButton(sButtonName, "Helm", __name__ + ".OrbitTarget", 0, pOrbitMenu)

	pOrbitMenu.SetOpenable()
	pOrbitMenu.SetEnabled()


def OrbitMenuChanged(pObject, pEvent):  
    CreateOrbitButton()
    pObject.CallNextHandler(pEvent)


def init(arg1 = None, arg2 = None): # evil :P
    CreateOrbitButton()
    pGame = App.Game_GetCurrentGame()
    pPlayer = App.Game_GetCurrentPlayer()
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pGame, __name__ + ".OrbitMenuChanged", pPlayer)


def Restart():
    # evil, really evil!
    MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".init", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
    

def GetButton(ButtonName, pMenu):
    kString = App.TGString()

    # cycle all Buttons
    curButton = pMenu.GetFirstChild()
    while (curButton != None):
        if curButton:
            curButtonattr = App.STButton_Cast(curButton)
            if not curButtonattr:
                curButtonattr = App.STMenu_Cast(curButton)
            if curButtonattr:
                curButtonattr.GetName(kString)
                if (kString.GetCString() == ButtonName):
                    return curButtonattr
        curButton = pMenu.GetNextChild(curButton)
