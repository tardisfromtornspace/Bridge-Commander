from bcdebug import debug

Carrier = __import__( "ftb.Carrier")
class Barrier( Carrier.Carrier):
    def __init__( self, pShip):
        debug(__name__ + ", __init__")
        Carrier.Carrier.__init__( self, pShip)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Shuttle Bay 1", pShip)
        group.AddLauncher( "Shuttle Bay", launcher)
        launcher.AddLaunchable( "Shuttle", "ftb.friendlyAI", 6)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 2", pShip)
        group.AddLauncher( "Shuttle Bay 2", launcher)
        launcher.AddLaunchable( "Type11", "ftb.friendlyAI", 2)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 3", pShip)
        group.AddLauncher( "Shuttle Bay 3", launcher)
        launcher.AddLaunchable( "VentureScout", "ftb.friendlyAI", 1)

        self.AddLauncher( "Group 1", group)

        #self.dShuttleToBay = {"Shuttle": "Shuttle Bay 1", "Type11": "Shuttle Bay 2", "VentureScout": "Shuttle Bay 3"}

    def GetMaxShuttles(self): 
        debug(__name__ + ", GetMaxShuttles")
        return 12

ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "Barrier", Barrier)
