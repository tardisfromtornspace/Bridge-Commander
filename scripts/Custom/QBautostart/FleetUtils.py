from bcdebug import debug
# by Defiant <mail@defiant.homedns.org>
# Yes I know that this one is really badly written, but I'm planning a complete! rewrite with multiple
# fleet support...but until then, this file works, so...

# Imports
import App
import MissionLib
import Lib.LibEngineering
import string

# Vars
g_pMyTargetTarget = None
g_dOverrideAIs = {}

MODINFO = {     "Author": "\"Defiant\" mail@defiant.homedns.org",
                "Download": "http://defiant.homedns.org/~erik/STBC/FleetOrders/",
                "Version": "1.3",
                "License": "GPL",
                "Description": "Send orders to your (friendly) Target or the whole (friendly) Fleet in your Set.",
                "needBridge": 0
            }

def init():
        debug(__name__ + ", init")
        pKiskaMenu = Lib.LibEngineering.GetBridgeMenu("Helm")
	pButtonOrder = App.STMenu_CreateW(App.TGString("Order..."))
	pKiskaMenu.PrependChild(pButtonOrder)
	
	pButtonOrderShip = App.STMenu_CreateW(App.TGString("Ship..."))
	pButtonOrder.PrependChild(pButtonOrderShip)
	
	pButtonOrderFleet = App.STMenu_CreateW(App.TGString("Fleet..."))
	pButtonOrder.PrependChild(pButtonOrderFleet)
        
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                pButtonCloakFleet = App.STMenu_CreateW(App.TGString("Cloak"))
	        pButtonOrderFleet.PrependChild(pButtonCloakFleet)
        
                Lib.LibEngineering.CreateMenuButton("Cloak", "Helm", __name__ + ".CloakOn", 0, pButtonOrderShip)

                Lib.LibEngineering.CreateMenuButton("Dock at next Base", "Helm", __name__ + ".ShipDock", 0, pButtonOrderShip)

                Lib.LibEngineering.CreateMenuButton("On", "Helm", __name__ + ".FleetCloakOn", 0, pButtonCloakFleet)
                Lib.LibEngineering.CreateMenuButton("Off", "Helm", __name__ + ".FleetCloakOff", 0, pButtonCloakFleet)

	Lib.LibEngineering.CreateMenuButton("Stop", "Helm", __name__ + ".Stay", 0, pButtonOrderShip)
	
	Lib.LibEngineering.CreateMenuButton("Attack", "Helm", __name__ + ".Attack", 0, pButtonOrderShip)
	
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                Lib.LibEngineering.CreateMenuButton("Fly Forward", "Helm", __name__ + ".FlyForward", 0, pButtonOrderShip)
	
                Lib.LibEngineering.CreateMenuButton("Follow", "Helm", __name__ + ".FollowThroughWarp", 0, pButtonOrderShip)
	
        pButtonSD = App.STMenu_CreateW(App.TGString("Self Destruct"))
	pButtonOrderShip.PrependChild(pButtonSD)
        Lib.LibEngineering.CreateMenuButton("Yes", "Helm", __name__ + ".SelfDestruct", 0, pButtonSD)
        
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                Lib.LibEngineering.CreateMenuButton("Stop", "Helm", __name__ + ".StayFleet", 0, pButtonOrderFleet)
	
                Lib.LibEngineering.CreateMenuButton("Attack", "Helm", __name__ + ".AttackFleet", 0, pButtonOrderFleet)
	
                Lib.LibEngineering.CreateMenuButton("Follow", "Helm", __name__ + ".FollowThroughWarpFleet", 0, pButtonOrderFleet)

                Lib.LibEngineering.CreateMenuButton("Attack my Target", "Helm", __name__ + ".AttackMyTarget", 0, pButtonOrderFleet)

                pButtonDefendFleet = App.STMenu_CreateW(App.TGString("Defend"))
	        pButtonOrderFleet.PrependChild(pButtonDefendFleet)

                Lib.LibEngineering.CreateMenuButton("me", "Helm", __name__ + ".DefendFleetPlayer", 0, pButtonDefendFleet)
                Lib.LibEngineering.CreateMenuButton("Target", "Helm", __name__ + ".DefendFleetTarget", 0, pButtonDefendFleet)


def MPIsPlayerShip(pShip):
	return App.g_kUtopiaModule.IsMultiplayer() and pShip.GetNetPlayerID() >= 0


def CloakOn(pObject, pEvent):
	debug(__name__ + ", CloakOn")
	pGame           = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	pPlayer         = MissionLib.GetPlayer()
	pTarget         = pPlayer.GetTarget()
	pTargetattr	= App.ShipClass_Cast(pTarget)

	if not pTarget:
		print("No Target")
		return

        if (pFriendlies.IsNameInGroup(pPlayer.GetTarget().GetName()) != 1):
            print("Target is not friendly - failed.")
            return
        
        pCloak = pTargetattr.GetCloakingSubsystem()
        
        if MPIsPlayerShip(pTargetattr):
                return
        
        if pCloak:
            pCloak.StartCloaking()

            pSequence = App.TGSequence_Create()
            pSet = App.g_kSetManager.GetSet("bridge")
            pHelm = App.CharacterClass_GetObject(pSet, "Helm")
            pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
            pSequence.Play()


def Stay(pObject, pEvent):		
	debug(__name__ + ", Stay")
	pGame	= App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	pPlayer	= MissionLib.GetPlayer()
	pTarget	= pPlayer.GetTarget()
	pTargetattr	= App.ShipClass_Cast(pTarget)

	if not pTarget:
		print("No Target")
		return
	
	if (pFriendlies.IsNameInGroup(pPlayer.GetTarget().GetName()) != 1):
		print("Target is not friendly - failed.")
		return

        if MPIsPlayerShip(pTargetattr):
                return


	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		try:
			from Custom.MultiplayerExtra.MultiplayerLib import SetStopAI
			SetStopAI(pTargetattr)
		except ImportError:
			return
		pSequence = App.TGSequence_Create()
		pSet = App.g_kSetManager.GetSet("bridge")
		if pSet:
			pHelm = App.CharacterClass_GetObject(pSet, "Helm")
			if pHelm:
				pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
		pSequence.Play()
		return

        OverrideAI(pTargetattr, "AI.Player.Stay", "CreateAI", pTargetattr)

	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	pSequence.Play()
	

def ShipDock(pObject, pEvent):		
	debug(__name__ + ", ShipDock")
	pGame	        = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	pPlayer         = MissionLib.GetPlayer()
	pTarget         = pPlayer.GetTarget()
	pTargetattr	= App.ShipClass_Cast(pTarget)
	pSet            = pPlayer.GetContainingSet()
	pFriendlyGroup  = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies    = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
        myStation       = None

	if not pTarget:
		print("No Target")
		return
	
	if (pFriendlies.IsNameInGroup(pPlayer.GetTarget().GetName()) != 1):
		print("Target is not friendly - failed.")
		return

        if MPIsPlayerShip(pTargetattr):
                return

        # Find a Station
	for pFriendly in lpFriendlies:
		pFriendly = App.ShipClass_Cast(pFriendly)
                if (pFriendly.GetShipProperty().IsStationary() == 1):
                    myStation = pFriendly
                    break
	
        if myStation:
            import AI.Compound.DockWithStarbaseLong
            pTargetattr.SetAI(AI.Compound.DockWithStarbaseLong.CreateAI(pTargetattr, myStation, None, NoRepair = not 1, FadeEnd = 1))

            pSequence = App.TGSequence_Create()
            pSet = App.g_kSetManager.GetSet("bridge")
            pHelm = App.CharacterClass_GetObject(pSet, "Helm")
            pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
            pSequence.Play()


def FlyForward(pObject, pEvent):		
	debug(__name__ + ", FlyForward")
	pGame	= App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	pPlayer	= MissionLib.GetPlayer()
	pTarget	= pPlayer.GetTarget()
	pTargetattr	= App.ShipClass_Cast(pTarget)

	if not pTarget:
		print("No Target")
		return
	
	if (pFriendlies.IsNameInGroup(pTarget.GetName()) != 1):
		print("Target is not friendly - failed.")
		return

        if MPIsPlayerShip(pTargetattr):
                return

        OverrideAI(pTargetattr, "AI.Player.FlyForward", "CreateWithAvoid", pTargetattr, 1.0)

	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	pSequence.Play()


def SelfDestruct(pObject, pEvent):
	debug(__name__ + ", SelfDestruct")
	pGame           = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	pPlayer         = MissionLib.GetPlayer()
	pTarget         = pPlayer.GetTarget()
        pTargetattr	= App.ShipClass_Cast(pTarget)
        
	if not pTarget:
		print("No Target")
		return
	
        if not pFriendlies.IsNameInGroup(pTarget.GetName()) and string.find(pTarget.GetName(), 'Mine') == "-1":
                print("Target is not friendly, or a mine - failed.")
                return
        
	if MPIsPlayerShip(pTargetattr):
		print "Target is a Player"
		return
        
	pTargetattr.DestroySystem(pTargetattr.GetHull())
	
	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, pHelm.GetCharacterName() + "Yes" + str(App.g_kSystemWrapper.GetRandomNumber(4)+1), "Captain", 1))
	pSequence.Play()


def StayFleet(pObject, pEvent):		
	debug(__name__ + ", StayFleet")
	pGame	= App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pPlayer	= MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
	
	import AI.Player.Stay

	for pFriendly in lpFriendlies:
		pTargetattr	= App.ShipClass_Cast(pFriendly)
		if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer))) and not MPIsPlayerShip(pTargetattr):
                        OverrideAI(pTargetattr, "AI.Player.Stay", "CreateAI", pTargetattr)
	
	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	pSequence.Play()
	

def Attack(pObject, pEvent):		
	debug(__name__ + ", Attack")
	pGame	= App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	pPlayer	= MissionLib.GetPlayer()
	pTarget	= pPlayer.GetTarget()
	pTargetattr	= App.ShipClass_Cast(pTarget)

	if not pTarget:
		print("No Target")
		return
	
	if (pFriendlies.IsNameInGroup(pPlayer.GetTarget().GetName()) != 1):
		print("Target is not friendly - failed.")
		return

        if MPIsPlayerShip(pTargetattr):
                print("Target is player ship - failed.")
                return

	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		try:
			from Custom.MultiplayerExtra.MultiplayerLib import MPSetAutoAI
			MPSetAutoAI(pTargetattr)
		except ImportError:
			return
		pSequence = App.TGSequence_Create()
		pSet = App.g_kSetManager.GetSet("bridge")
		if pSet:
			pHelm = App.CharacterClass_GetObject(pSet, "Helm")
			if pHelm:
				pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
		pSequence.Play()
		return

        if (StopOverridingAI(pTargetattr) == 1):
            return

        if (pTargetattr.GetShipProperty().IsStationary() == 1):
                pTargetattr.SetAI(Lib.LibEngineering.CreateStarbaseFriendlyAI(pTargetattr))
        else:
                pTargetattr.SetAI(Lib.LibEngineering.CreateFriendlyAI(pTargetattr))

	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	pSequence.Play()
	

def AttackFleet(pObject, pEvent):		
	debug(__name__ + ", AttackFleet")
	pGame	= App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pPlayer	= MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
	
	for pFriendly in lpFriendlies:
		pTargetattr	= App.ShipClass_Cast(pFriendly)
		if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer))) and not MPIsPlayerShip(pTargetattr):
                        if (StopOverridingAI(pTargetattr) != 1):
                            print("StopOverridingAI failed for", pTargetattr.GetName())
                            continue
			# set AI
			# We need to know if we are playing normal QB or QBR:
			# QB
                        if (pTargetattr.GetShipProperty().IsStationary() == 1):
                                pTargetattr.SetAI(Lib.LibEngineering.CreateStarbaseFriendlyAI(pTargetattr))
                        else:
                                pTargetattr.SetAI(Lib.LibEngineering.CreateFriendlyAI(pTargetattr))

	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	pSequence.Play()
	
	
def FollowThroughWarp(pObject, pEvent):		
	debug(__name__ + ", FollowThroughWarp")
	pGame	= App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	pPlayer	= MissionLib.GetPlayer()
	pTarget	= pPlayer.GetTarget()
	pTargetattr	= App.ShipClass_Cast(pTarget)

	if not pTarget:
		print("No Target")
		return
	
        if MPIsPlayerShip(pTargetattr):
                return
        
	if (pFriendlies.IsNameInGroup(pTarget.GetName()) != 1):
		print("Target is not friendly - failed.")
		return

	if ( pTargetattr.GetShipProperty().IsStationary() == 1 ):
		print("Target is a Station - can't follow.")
		return

        OverrideAI(pTargetattr, __name__, "CreateAI", pTargetattr)

	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	pSequence.Play()


def FollowThroughWarpFleet(pObject, pEvent):		
	debug(__name__ + ", FollowThroughWarpFleet")
	pGame	= App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pPlayer	= MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)

	for pFriendly in lpFriendlies:
		pTargetattr	= App.ShipClass_Cast(pFriendly)
		if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer)) and pFriendly.GetShipProperty().IsStationary() == 0 and not MPIsPlayerShip(pTargetattr)):
			OverrideAI(pTargetattr, __name__, "CreateAI", pTargetattr)

	pSequence = App.TGSequence_Create()
	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	pSequence.Play()


def DefendFleetPlayer(pObject, pEvent):
	debug(__name__ + ", DefendFleetPlayer")
	pGame           = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
        pPlayer         = MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)

        for pFriendly in lpFriendlies:
            pTargetattr	= App.ShipClass_Cast(pFriendly)
            if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer))) and not MPIsPlayerShip(pTargetattr):
                OverrideAI(pFriendly, "AI.Compound.Defend", "CreateAI", pFriendly, pPlayer.GetName())

        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pSet, "Helm")
        pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
        pSequence.Play()


def DefendFleetTarget(pObject, pEvent):
	debug(__name__ + ", DefendFleetTarget")
	pGame           = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
        pPlayer         = MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
	pTarget         = pPlayer.GetTarget()

	if not pTarget:
		print("No Target")
		return

        if (pFriendlies.IsNameInGroup(pPlayer.GetTarget().GetName()) != 1):
            print("Target is not friendly - failed.")
            return


        for pFriendly in lpFriendlies:
            pTargetattr	= App.ShipClass_Cast(pFriendly)
            if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer)) and pTarget.GetName() != pFriendly.GetName() ) and not MPIsPlayerShip(pTargetattr):
                OverrideAI(pFriendly, "AI.Compound.Defend", "CreateAI", pFriendly, pTarget.GetName())

        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pSet, "Helm")
        pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
        pSequence.Play()


def FleetCloakOn(pObject, pEvent):
	debug(__name__ + ", FleetCloakOn")
	pGame           = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
        pPlayer         = MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)

        for pFriendly in lpFriendlies:
            pTargetattr	= App.ShipClass_Cast(pFriendly)
            if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer))) and not MPIsPlayerShip(pTargetattr):
                pCloak = pTargetattr.GetCloakingSubsystem()
                if pCloak:
                    pCloak.StartCloaking()

        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pSet, "Helm")
        pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
        pSequence.Play()


def FleetCloakOff(pObject, pEvent):
	debug(__name__ + ", FleetCloakOff")
	pGame           = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
        pPlayer         = MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)

        for pFriendly in lpFriendlies:
            pTargetattr	= App.ShipClass_Cast(pFriendly)
            if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer))) and not MPIsPlayerShip(pTargetattr):
                pCloak = pTargetattr.GetCloakingSubsystem()
                if pCloak:
                    pCloak.StopCloaking()

        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pSet, "Helm")
        pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
        pSequence.Play()


def AttackMyTarget(pObject, pEvent):
        debug(__name__ + ", AttackMyTarget")
        pGame           = App.Game_GetCurrentGame()
	pEpisode	= pGame.GetCurrentEpisode()
	pMission	= pEpisode.GetCurrentMission()
	pPlayer         = MissionLib.GetPlayer()
	pSet            = pPlayer.GetContainingSet()
	pFriendlyGroup  = MissionLib.GetFriendlyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	lpFriendlies    = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
        pTarget         = pPlayer.GetTarget()
        pEnemies        = MissionLib.GetEnemyGroup()
	if not pTarget:
		print("No Target")
		return
	
	if (pEnemies.IsNameInGroup(pPlayer.GetTarget().GetName()) != 1):
		print("Target is not enemy - failed.")
		return
        
        import AI.Compound.BasicAttack
        Getg_PlayerTargets(pTarget)
	for pFriendly in lpFriendlies:
		pTargetattr	= App.ShipClass_Cast(pFriendly)
		if (str(pTargetattr) != str(App.ShipClass_Cast(pPlayer))) and not MPIsPlayerShip(pTargetattr):
                        pFriendly.SetAI(AI.Compound.BasicAttack.CreateAI(pFriendly, App.ObjectGroup_FromModule("Custom.QBautostart.FleetUtils", "g_pMyTargetTarget")))
                        OverrideAI(pFriendly, "AI.Compound.BasicAttack", "CreateAI", pFriendly, App.ObjectGroup_FromModule("Custom.QBautostart.FleetUtils", "g_pMyTargetTarget"))
                        


	pSet = App.g_kSetManager.GetSet("bridge")
	if (pSet):
		pHelm = App.CharacterClass_GetObject(pSet, "Helm")
		if (pHelm):
                        pSequence = App.TGSequence_Create()
			pSequence.AppendAction(App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "SendingOrders" + str(App.g_kSystemWrapper.GetRandomNumber(2) + 1), "Captain", 1))
	                pSequence.Play()


def Getg_PlayerTargets(pTarget):
	debug(__name__ + ", Getg_PlayerTargets")
	global g_pMyTargetTarget
	
	g_pMyTargetTarget = None
	g_pMyTargetTarget = App.ObjectGroup()
	g_pMyTargetTarget.AddName(pTarget.GetName())


# From Maelstrom.Episode4.E4M4.FollowPlayerAI, only changed the string "Player" to pPlayer.GetName()
def CreateAI(pShip):
	debug(__name__ + ", CreateAI")
	pPlayer = MissionLib.GetPlayer()

        Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin
        # Range values used in the AI.
        fInRange = 150.0 + Random(-25, 20)

	#########################################
	# Creating PlainAI Intercept at (279, 253)
	pIntercept = App.PlainAI_Create(pShip, "Intercept")
	pIntercept.SetScriptModule("Intercept")
	pIntercept.SetInterruptable(1)
	pScript = pIntercept.GetScriptInstance()
	pScript.SetTargetObjectName(pPlayer.GetName())
	# Done creating PlainAI Intercept
	#########################################
	#########################################
	# Creating ConditionalAI ConditionIntercept at (148, 273)
	## Conditions:
	#### Condition HaveToIntercept
	pHaveToIntercept = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fInRange, pPlayer.GetName(), pShip.GetName())
	## Evaluation function:
	def EvalFunc(bHaveToIntercept):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bHaveToIntercept:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionIntercept = App.ConditionalAI_Create(pShip, "ConditionIntercept")
	pConditionIntercept.SetInterruptable(1)
	pConditionIntercept.SetContainedAI(pIntercept)
	pConditionIntercept.AddCondition(pHaveToIntercept)
	pConditionIntercept.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionIntercept
	#########################################
	#########################################
	# Creating PlainAI Follow at (280, 181)
	pFollow = App.PlainAI_Create(pShip, "Follow")
	pFollow.SetScriptModule("FollowObject")
	pFollow.SetInterruptable(1)
	pScript = pFollow.GetScriptInstance()
	pScript.SetFollowObjectName(pPlayer.GetName())
	pScript.SetRoughDistances(15,25,50)
	# Done creating PlainAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI PlayerInSameSet at (164, 201)
	## Conditions:
	#### Condition InSet
	pInSet = App.ConditionScript_Create("Conditions.ConditionAllInSameSet", "ConditionAllInSameSet", pShip.GetName(), pPlayer.GetName())
	## Evaluation function:
	def EvalFunc(bInSet):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInSet:
			# Player is in the same set as we are.
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pPlayerInSameSet = App.ConditionalAI_Create(pShip, "PlayerInSameSet")
	pPlayerInSameSet.SetInterruptable(1)
	pPlayerInSameSet.SetContainedAI(pFollow)
	pPlayerInSameSet.AddCondition(pInSet)
	pPlayerInSameSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI PlayerInSameSet
	#########################################
	#########################################
	# Creating CompoundAI FollowWarp at (281, 125)
	import AI.Compound.FollowThroughWarp
	pFollowWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName())
	# Done creating CompoundAI FollowWarp
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (47, 125)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (139, 132)
	pPriorityList.AddAI(pConditionIntercept, 1)
	pPriorityList.AddAI(pPlayerInSameSet, 2)
	pPriorityList.AddAI(pFollowWarp, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (6, 188)
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
	return pAvoidObstacles


# from Bridge.HelmMenuHandlers
def OverrideAI(pShip, sAIModule, AICreate, *lAICreateArgs, **dAICreateKeywords):
    # Try to override the AI.
    debug(__name__ + ", OverrideAI")
    pSequence = App.TGSequence_Create()
    pSequence.AppendAction(App.TGScriptAction_Create(__name__, "OverrideAIMid", pShip.GetObjID(), sAIModule, AICreate, lAICreateArgs, dAICreateKeywords))
    pSequence.Play()

def OverrideAIMid(pAction, idShip, sAIModule, AICreate, lAICreateArgs, dAICreateKeywords):
	debug(__name__ + ", OverrideAIMid")
	pShip = App.ShipClass_GetObjectByID(None, idShip)
	if not pShip:
		return 0

	# Check if the ship has building AI's.
	if pShip.HasBuildingAIs():
		# Can't override AI just yet...  Try again in a little while.
		#debug("Can't override AI yet.  Delaying attempt...")
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction( App.TGScriptAction_Create(__name__, "OverrideAIMid", idShip, sAIModule, AICreate, lAICreateArgs, dAICreateKeywords), 0.5 )
		pSeq.Play()
		return 0

	# Ship has no building AI's.  We can safely replace its AI.
	# Create the new AI...
	pAIModule = __import__(sAIModule)
	pNewAI = apply(getattr(pAIModule, AICreate), lAICreateArgs, dAICreateKeywords)
	if pNewAI:
		OverrideAIInternal(pShip, pNewAI)

	# Reenable fleet commands and say the command has been acknowledged.
	#debug("AI overridden.")
	return 0

def OverrideAIInternal(pShip, pNewAI):
	# Check for an old AI.
	debug(__name__ + ", OverrideAIInternal")
	global g_dOverrideAIs
	pOldAI = pShip.GetAI()
	pOverrideAI = None
	if pOldAI:
		if g_dOverrideAIs.has_key(pShip.GetObjID()):
			# Already have an override AI for this ship.  Check if
			# that AI is still in place.
			pOverrideAI = App.ArtificialIntelligence_GetAIByID(g_dOverrideAIs[pShip.GetObjID()])
			if (not pOverrideAI)  or  (pOverrideAI.GetID() != pOldAI.GetID()):
				# It's not in place.  Gotta make a new one.
				pOverrideAI = None
			else:
				# It's still in place.  Remove whatever was in
				# the priority 1 slot (whatever the player told
				# this ship to do before).
				pOverrideAI.RemoveAIByPriority(1)

	if not pOverrideAI:
		# Make a new Override AI.
		pOverrideAI = App.PriorityListAI_Create(pShip, "FleetCommandOverrideAI")
		pOverrideAI.SetInterruptable(1)

		# Second AI in the list is the current AI.
		if pOldAI:
			pOverrideAI.AddAI(pOldAI, 2)

	# First AI in the list is the AI to override the old one.
	pOverrideAI.AddAI(pNewAI, 1)

	# Replace the ship's AI with the override AI.  The 0 here
	# tells the game not to delete the old AI.
	pShip.ClearAI(0, pOldAI)
	pShip.SetAI(pOverrideAI)

	# Save info about this override AI.
	g_dOverrideAIs[pShip.GetObjID()] = pOverrideAI.GetID()

def StopOverridingAI(pShip):
	debug(__name__ + ", StopOverridingAI")
	global g_dOverrideAIs
	pOldAI = pShip.GetAI()
	pOverrideAI = None
	if pOldAI:
		if g_dOverrideAIs.has_key(pShip.GetObjID()):
			# Have an override AI for this ship.  Check if
			# that AI is still in place.
			pOverrideAI = App.ArtificialIntelligence_GetAIByID(g_dOverrideAIs[pShip.GetObjID()])
			if pOverrideAI  and  (pOverrideAI.GetID() == pOldAI.GetID()):
				# It's still in place.  Remove whatever was in
				# the priority 1 slot (whatever the player told
				# this ship to do before).
				pOverrideAI.RemoveAIByPriority(1)
                                return 1
        return 0

