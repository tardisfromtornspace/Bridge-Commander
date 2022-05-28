from bcdebug import debug
import App
import string

pMvamTimer = 0
g_Number = 1
pMvamShips = []
snkMvamModules = []
intTimerRunning = 0
intShipSepTally = 0

def CreateAI(pShip):
	debug(__name__ + ", CreateAI")
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	#before we do anything... check to see if it'll seperate. need to recheck the ship...
	import Custom.Sneaker.Mvam.Mvam_Lib
	if (Custom.Sneaker.Mvam.Mvam_Lib.DetermineMvamAi(pShip) == 1):
		#grab what module it is in...
		snkMvamModule = Custom.Sneaker.Mvam.Mvam_Lib.ReturnMvamModule(pShip)

		#make sure the user wants the ship to seperate
		if (snkMvamModule.ReturnAiSepAbility() == 1):
			pMvamShips.append(pShip)
			snkMvamModules.append(snkMvamModule)

			global intTimerRunning
			#okay, I only want to do the following ONCE, as after that one time it'll set everything off
			if (intTimerRunning == 0):
				global pMvamTimer
				ET_MVAM_CHECK = App.Mission_GetNextEventType()

				App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_MVAM_CHECK, pMission, __name__ + ".CheckAi")

				pEvent = App.TGEvent_Create ()
				pEvent.SetEventType (ET_MVAM_CHECK)
				pEvent.SetDestination (pMission)
				pMvamTimer = App.TGTimer_Create()
				pMvamTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 5)
				pMvamTimer.SetDelay(20)
				pMvamTimer.SetDuration(-1.0)
				pMvamTimer.SetEvent(pEvent)
				App.g_kTimerManager.AddTimer(pMvamTimer)

				intTimerRunning = 1

	#########################################
	# Creating CompoundAI AttackEnemies
	import AI.Compound.BasicAttack

	#find the group this ship is in...
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies = pMission.GetFriendlyGroup()

	#we need to find what group the ship was in... 0 = enemy, 1 = friend, 2 = neut
	pAttackEnemies = None
	if pEnemies.IsNameInGroup(pShip.GetName()):
		if pMission.GetFriendlyGroup().GetNameTuple():
			pAttackEnemies = AI.Compound.BasicAttack.CreateAI(pShip,  pMission.GetFriendlyGroup(), Difficulty = 0.1, InaccurateTorps = 1)
	elif pMission.GetEnemyGroup().GetNameTuple():
		pAttackEnemies = AI.Compound.BasicAttack.CreateAI(pShip,  pMission.GetEnemyGroup(), Difficulty = 0.1, InaccurateTorps = 1)
	if not pAttackEnemies:
		return None

	# Done creating CompoundAI AttackEnemies
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (42, 24)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pAttackEnemies)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################

	return pAvoidObstacles


def CheckAi(pObject, pEvent):
	debug(__name__ + ", CheckAi")
	global pMvamShips, snkMvamModules, intShipSepTally, intTimerRunning

	#grab the player and the set the player is in. make sure all these items still exist
	try:
		pGame = App.Game_GetCurrentGame()
		pPlayer = pGame.GetPlayer()
		pSet = pPlayer.GetContainingSet()
	except:
		DoNothing = "NoNeed"

	if (pSet != None):
		#iterate through all the ships
		for i in range (len(pMvamShips)):
			#now we test to see if the ship is still in the set
			pMvamShip = App.ShipClass_GetObject (pSet, pMvamShips[i].GetName())

			#alright, if the ship doesnt exist then don't do it
			if (pMvamShip != None):
				#determine if it's time to seperate or not, using the mvam module. make sure it's not dying!!
				if (snkMvamModules[i].CheckSeperate(pMvamShips[i]) == 1):
					import Custom.Sneaker.Mvam.AiSeperation
					global g_Number
					strNumber = " " + repr(g_Number)
					Custom.Sneaker.Mvam.AiSeperation.Seperation(snkMvamModules[i], [pMvamShips[i].GetName(), strNumber])
					g_Number = g_Number + 1

			#the ship doesn't exist. Add up a tally that we'll use in a bit
			else:
				intShipSepTally = intShipSepTally + 1

		#check to see if there are any mvam ships left...
		if (intShipSepTally < len(pMvamShips)):
			#we dont actually need to do anything
			DoNothing = "NothingAtAll"

		#kill the timer because there's no more need for it. reset EVERYTHING
		else:
			pMvamTimer.SetDuration(0)
			intTimerRunning = 0
			pMvamShips = []
			snkMvamModules = []


	#if these arent around, the timer shouldnt run anymore
	else:
		intTimerRunning = 0
		pMvamShips = []
		snkMvamModules = []

	#reset the ship tally count for use in the next run
	intShipSepTally = 0

	pObject.CallNextHandler(pEvent)