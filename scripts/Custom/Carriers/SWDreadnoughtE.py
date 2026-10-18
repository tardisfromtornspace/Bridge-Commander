Carrier = __import__( "ftb.Carrier")
class SWDreadnoughtE( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)

        LauncherGroup = __import__( "ftb.LauncherGroup")

        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 1", pShip)
        group.AddLauncher( "Shuttle Bay 1", launcher)
        launcher.AddLaunchable( "ZZTIEFighter", "QuickBattle.ZZAndromedanAttackFriendlyAI", 5)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 2", pShip)
        group.AddLauncher( "Shuttle Bay 2", launcher)
        launcher.AddLaunchable( "ZZTIEFighter", "QuickBattle.ZZAndromedanAttackFriendlyAI", 5)
 
        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)


    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self):
        return 10
    # Don't use the following Tractors to Dock:
    def IgnoreTractors(self):
        return []


# "SWDreadnoughtE" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "SWDreadnoughtE", SWDreadnoughtE)
