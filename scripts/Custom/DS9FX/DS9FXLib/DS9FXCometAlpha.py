# by USS Sovereign, this fixes the transport to Comet Alpha bug

# Imports
import App
import MissionLib

# Swap back to original ship
def IdentityCheck(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSource = App.ShipClass_Cast(pEvent.GetSource())

        if pPlayer is None or pSource is None:
                return 0

        sComet = "Comet Alpha"
        sName = pPlayer.GetName()
        sSourceName = pSource.GetName()

        if not sComet == sName:
                return 0

        pSet = pPlayer.GetContainingSet()

        if not pSet.GetName() == "DeepSpace91":
                return 0

        pOldShip = MissionLib.GetShip(sSourceName, pSet)
        if not pOldShip:
                return 0

        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(pOldShip)

        # Several versions of transporter script, default one adds ships to friendly group
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pFriendly = pMission.GetFriendlyGroup()

        if (pFriendly.IsNameInGroup(sComet)):
                pFriendly.RemoveName(sComet)

        # Probably the AI got fucked up too...
        import Custom.DS9FX.DS9FXAILib.DS9FXCometAI

        pDS9FXComet = MissionLib.GetShip(sComet, pSet)

        DS9FXComet = App.ShipClass_Cast(pDS9FXComet)

        DS9FXComet.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXCometAI.CreateAI(DS9FXComet))

        # Clear the Player's target
        pPlayer = MissionLib.GetPlayer()
        pPlayer.SetTarget(None)


