from bcdebug import debug
import loadspacehelper
import MissionLib
import App
import Foundation

Ship_i = 1

def enemy(ShipType, Name = None):
	debug(__name__ + ", enemy")
	global Ship_i
	pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                print "Error: No Player!"
                return
        
	pSet = pPlayer.GetContainingSet()
        pEnemies = MissionLib.GetEnemyGroup()
	pFriendlies = MissionLib.GetFriendlyGroup()
        
        # check Multiplayer
        #try:
        #        import Multiplayer.Episode.Mission4.Mission4
        #        if Multiplayer.Episode.Mission4.Mission4.g_pTeam1:
        #                g_pTeam1 = Multiplayer.Episode.Mission4.Mission4.g_pTeam1
        #                g_pTeam2 = Multiplayer.Episode.Mission4.Mission4.g_pTeam2
        #                if g_pTeam1.IsNameInGroup(pPlayer.GetName()):
        #                        print("Player is Team1")
        #                        #pFriendlies = g_pTeam1
        #                        #pEnemies = g_pTeam2
        #                else:
        #                        print("Player is Team2")
        #                        #pFriendlies = g_pTeam2
        #                        #pEnemies = g_pTeam1
        #except:
        #        #print "Mission4 not installed"
	#	pass
                
	
        if Name:
                pcName = Name
        else:
		pMission = MissionLib.GetMission()
		pMissionDatabase = pMission.SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")
		if pMissionDatabase.GetString(ShipType).GetCString() != "???":
			Name = pMissionDatabase.GetString(ShipType).GetCString()
		else:
			Name = ShipType
                pcName = Name + " " + str(Ship_i)
        while(MissionLib.GetShip(pcName)):
                Ship_i = Ship_i + 1
                pcName = Name + " " + str(Ship_i)
	
	g_pNewShip = loadspacehelper.CreateShip(ShipType, pSet, pcName, "", 1) #The last Number is for the warpflash
	g_pAIShip = App.ShipClass_GetObject(pSet, pcName)
        if not g_pAIShip:
                print "Sorry, was unable to add ship: %s" % ShipType
                # increase on failure
                Ship_i = Ship_i + 1
                return
	CreateAIPosition(g_pNewShip, pSet)
	
	pEnemies.AddName(g_pNewShip.GetName())

	FdtnShips = Foundation.shipList
        if not FdtnShips.has_key(ShipType):
                print("Warning: using old-style AI for %s") % (pcName)
                if g_pAIShip.GetShipProperty().IsStationary(): #test for Station
                        g_pAIShip.SetAI(CreateStarbaseEnemyAI(g_pAIShip, pFriendlies))
                else:
                        g_pAIShip.SetAI(CreateEnemyAI(g_pAIShip, pFriendlies))
        else:
                ship = FdtnShips[ShipType]
                FdtnAI = ship.StrEnemyAI()
                if FdtnAI == "QuickBattleAI":
                        g_pAIShip.SetAI(CreateEnemyAI(g_pAIShip, pFriendlies))
                elif FdtnAI == "StarbaseAI":
                        # Add the starbase itself to the attacker list -- the AI needs to have
                        # *something* on the attacker list so as not to crash, but it won't
                        # try to attack itself
        		#if not pFriendlies.GetNameTuple():
            		#	pFriendlies.AddName("This ship probably wont exist")
                        pFriendlies.AddName(pcName)
                        g_pAIShip.SetAI(CreateStarbaseEnemyAI(g_pAIShip, pFriendlies))
                        pFriendlies.RemoveName(pcName)
                else:
                        pAIModule = __import__("QuickBattle." + FdtnAI)
                        try:
                                g_pAIShip.SetAI(pAIModule.CreateAI(g_pAIShip, pFriendlies))
                        except TypeError:
                                g_pAIShip.SetAI(pAIModule.CreateAI(g_pAIShip))

def friendly(ShipType, Name = None):
	debug(__name__ + ", friendly")
	global Ship_i
	pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                print "Error: No Player!"
                return
	pSet = pPlayer.GetContainingSet()
	
	pFriendlies = MissionLib.GetFriendlyGroup()
	pEnemies = MissionLib.GetEnemyGroup()

        # check Multiplayer
        #try:
        #        import Multiplayer.Episode.Mission4.Mission4
        #        if Multiplayer.Episode.Mission4.Mission4.g_pTeam1:
        #                g_pTeam1 = Multiplayer.Episode.Mission4.Mission4.g_pTeam1
        #                g_pTeam2 = Multiplayer.Episode.Mission4.Mission4.g_pTeam2
        #                if g_pTeam1.IsNameInGroup(pPlayer.GetName()):
        #                        print("Player is Team1")
        #                        #pFriendlies = g_pTeam1
        #                        #pEnemies = g_pTeam2
        #                else:
        #                        print("Player is Team2")
        #                        #pFriendlies = g_pTeam2
        #                        #pEnemies = g_pTeam1
        #except ImportError:
        #        #print "Mission4 not installed"
	#	pass

        if Name:
                pcName = Name
        else:
		pMission = MissionLib.GetMission()
		pMissionDatabase = pMission.SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")
		if pMissionDatabase.GetString(ShipType).GetCString() != "???":
			Name = pMissionDatabase.GetString(ShipType).GetCString()
		else:
			Name = ShipType
                pcName = Name + " " + str(Ship_i)
        while(MissionLib.GetShip(pcName)):
                Ship_i = Ship_i + 1
                pcName = Name + " " + str(Ship_i)
	
	g_pNewShip = loadspacehelper.CreateShip(ShipType, pSet, pcName, "", 1) #The last Number is for the warpflash
	g_pAIShip = App.ShipClass_GetObject(pSet, pcName)
        if not g_pAIShip:
                print "Sorry, was unable to add ship: %s" % ShipType
                # increase on failure
                Ship_i = Ship_i + 1
                return
	CreateAIPosition(g_pNewShip, pSet)
	
	pFriendlies.AddName(g_pNewShip.GetName())

	FdtnShips = Foundation.shipList
        if not FdtnShips.has_key(ShipType):
                print("Warning: using old-style AI for %s") % (pcName)
                if g_pAIShip.GetShipProperty().IsStationary(): #test for Station
                        g_pAIShip.SetAI(CreateStarbaseFriendlyAI(g_pAIShip, pEnemies))
                else:
                        g_pAIShip.SetAI(CreateFriendlyAI(g_pAIShip, pEnemies))
        else:
                ship = FdtnShips[ShipType]
                FdtnAI = ship.StrFriendlyAI()
                if FdtnAI == "QuickBattleFriendlyAI":
                        g_pAIShip.SetAI(CreateFriendlyAI(g_pAIShip, pEnemies))
                elif FdtnAI == "StarbaseFriendlyAI":
                        # Add the starbase itself to the attacker list -- the AI needs to have
                        # *something* on the attacker list so as not to crash, but it won't
                        # try to attack itself
			#if not pEnemies.GetNameTuple():
            		#	pEnemies.AddName("This ship probably wont exist")
                        pEnemies.AddName(pcName)
                        g_pAIShip.SetAI(CreateStarbaseFriendlyAI(g_pAIShip, pEnemies))
                        pEnemies.RemoveName(pcName)
                else:
                        pAIModule = __import__("QuickBattle." + FdtnAI)
                        try:
                                g_pAIShip.SetAI(pAIModule.CreateAI(g_pAIShip, pEnemies))
                        except TypeError:
                                g_pAIShip.SetAI(pAIModule.CreateAI(g_pAIShip))


def neutral(ShipType, Name = None):
	debug(__name__ + ", neutral")
	global Ship_i
	pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                print "Error: No Player!"
                return
        
	pSet = pPlayer.GetContainingSet()
        pNeutralGroup = MissionLib.GetNeutralGroup()
	
        if Name:
                pcName = Name
        else:
		pMission = MissionLib.GetMission()
		pMissionDatabase = pMission.SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")
		if pMissionDatabase.GetString(ShipType).GetCString() != "???":
			Name = pMissionDatabase.GetString(ShipType).GetCString()
		else:
			Name = ShipType
                pcName = Name + " " + str(Ship_i)
        while(MissionLib.GetShip(pcName)):
                Ship_i = Ship_i + 1
                pcName = Name + " " + str(Ship_i)
	
	g_pNewShip = loadspacehelper.CreateShip(ShipType, pSet, pcName, "", 1) #The last Number is for the warpflash
	g_pAIShip = App.ShipClass_GetObject(pSet, pcName)
        if not g_pAIShip:
                print "Sorry, was unable to add ship: %s (%s)" % (ShipType, pcName)
                # increase on failure
                Ship_i = Ship_i + 1
                return
	CreateAIPosition(g_pNewShip, pSet)
	
	pNeutralGroup.AddName(g_pNewShip.GetName())


# returns -RandomMax...+RandomMax
def GetRandom(RandomMax):
        debug(__name__ + ", GetRandom")
        return App.g_kSystemWrapper.GetRandomNumber(RandomMax) * (-1) ** App.g_kSystemWrapper.GetRandomNumber(2)
        
        
def CreateAIPosition(g_pAIShip, pSet):
        debug(__name__ + ", CreateAIPosition")
        RandomMax = 1000
	kLocation = App.TGPoint3()
        X = GetRandom(RandomMax)
        Y = GetRandom(RandomMax)
        Z = GetRandom(RandomMax)
	kLocation.SetXYZ(X, Y, Z)
	
        i = 0
	while ( pSet.IsLocationEmptyTG(kLocation, g_pAIShip.GetRadius()*2, 1) == 0):
		X = GetRandom(RandomMax)
		Y = GetRandom(RandomMax)
                Z = GetRandom(RandomMax)
		kLocation.SetXYZ(X, Y, Z)
                i = i + 1
                if i == 10:
                        i = 0
                        RandomMax = RandomMax + 10000
	
	g_pAIShip.SetTranslate(kLocation)
	g_pAIShip.UpdateNodeOnly()

# Set Friendly AI
def CreateFriendlyAI(pShip, pEnemies):
        debug(__name__ + ", CreateFriendlyAI")
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (194, 57)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pEnemies, Difficulty = 1, FollowTargetThroughWarp=1, UseCloaking=1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 12, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (41, 304)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWait)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles


def CreateEnemyAI(pShip, pFriendlies):
        debug(__name__ + ", CreateEnemyAI")
        if not pFriendlies.GetNameTuple():
            pFriendlies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pFriendlies, Difficulty = 1, FollowTargetThroughWarp = 1, UseCloaking = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PlainAI Turn at (237, 47)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (353, 55)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (429, 103)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (448, 147)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (198, 181)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (309, 185)
	pFlyPointlessly.AddAI(pTurn)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating SequenceAI RepeatForever at (195, 224)
	pRepeatForever = App.SequenceAI_Create(pShip, "RepeatForever")
	pRepeatForever.SetInterruptable(1)
	pRepeatForever.SetLoopCount(-1)
	pRepeatForever.SetResetIfInterrupted(1)
	pRepeatForever.SetDoubleCheckAllDone(1)
	pRepeatForever.SetSkipDormant(0)
	# SeqBlock is at (295, 228)
	pRepeatForever.AddAI(pFlyPointlessly)
	# Done creating SequenceAI RepeatForever
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (30, 228)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 235)
	pPriorityList.AddAI(pAttack, 1)
	pPriorityList.AddAI(pRepeatForever, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (29, 285)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 12, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAvoidObstacles)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def CreateStarbaseFriendlyAI(pShip, pEnemies):
        debug(__name__ + ", CreateStarbaseFriendlyAI")
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def CreateStarbaseEnemyAI(pShip, pFriendlies):
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	debug(__name__ + ", CreateStarbaseEnemyAI")
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pFriendlies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait
