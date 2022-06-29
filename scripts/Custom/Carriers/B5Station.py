from bcdebug import debug


##############################################################################

Carrier = __import__( "ftb.Carrier")
class B5Station( Carrier.Carrier):
    def __init__( self, pShip):
        debug(__name__ + ", __init__")
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Shuttle Bay 1", pShip)
        group.AddLauncher( "Shuttle Bay 1", launcher)
        launcher.AddLaunchable( "AlphaWing", "Custom.Sneaker.Mvam.MvamAI", 7)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 2", pShip)
        group.AddLauncher( "Shuttle Bay 2", launcher)
        launcher.AddLaunchable( "ZetaWing", "ftb.friendlyAI", 6)
        
        launcher = LauncherManager.GetLauncher( "Shuttle Bay 3", pShip)
        group.AddLauncher( "Shuttle Bay 3", launcher)
        launcher.AddLaunchable( "DeltaWing", "Custom.Sneaker.Mvam.MvamAI", 7)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 4", pShip)
        group.AddLauncher( "Shuttle Bay 4", launcher)
        launcher.AddLaunchable( "EchoWing", "ftb.friendlyAI", 6)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 5", pShip)
        group.AddLauncher( "Shuttle Bay 5", launcher)
        launcher.AddLaunchable( "EAAchillesFreighter", "Custom.Sneaker.Mvam.MvamAI", 2)
        launcher.AddLaunchable( "EACrewShuttleBlue", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 6", pShip)
        group.AddLauncher( "Shuttle Bay 6", launcher)
        launcher.AddLaunchable( "EACrewShuttle", "ftb.friendlyAI", 2)
        launcher.AddLaunchable( "EACrewShuttleRed", "ftb.friendlyAI", 1)
       
        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self):
    	debug(__name__ + ", GetMaxShuttles")
    	return 40

   
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "B5Station", B5Station)
