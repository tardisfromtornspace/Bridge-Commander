Carrier = __import__( "ftb.Carrier")

class Aquatic( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Shuttle Bay 1", pShip)
        group.AddLauncher( "Shuttle Bay 1", launcher)
        launcher.AddLaunchable( "WCnx01", "QuickBattle.QuickBattleFriendlyAI", 1)

        self.AddLauncher( "Group 1", group)

        #group.SetLaunchMode( LauncherGroup.ALL)

ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "Aquatic", Aquatic)
