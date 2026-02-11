#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__( "ftb.Carrier")
class WZErad( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)

        LauncherGroup = __import__( "ftb.LauncherGroup")

        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 1", pShip)
        group.AddLauncher( "Shuttle Bay 1", launcher)
        launcher.AddLaunchable( "WZInter", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 2", pShip)
        group.AddLauncher( "Shuttle Bay 2", launcher)
        launcher.AddLaunchable( "WZInter", "ftb.friendlyAI", 1)
 
        launcher = LauncherManager.GetLauncher( "Shuttle Bay 3", pShip)
        group.AddLauncher( "Shuttle Bay 3", launcher)
        launcher.AddLaunchable( "WZInter", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 4", pShip)
        group.AddLauncher( "Shuttle Bay 4", launcher)
        launcher.AddLaunchable( "WZInter", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 5", pShip)
        group.AddLauncher( "Shuttle Bay 5", launcher)
        launcher.AddLaunchable( "WZInter", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 6", pShip)
        group.AddLauncher( "Shuttle Bay 6", launcher)
        launcher.AddLaunchable( "WZInter", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 1a", pShip)
        group.AddLauncher( "Shuttle Bay 1a", launcher)
        launcher.AddLaunchable( "WZDetec", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 2a", pShip)
        group.AddLauncher( "Shuttle Bay 2a", launcher)
        launcher.AddLaunchable( "WZDetec", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 3a", pShip)
        group.AddLauncher( "Shuttle Bay 3a", launcher)
        launcher.AddLaunchable( "WZDetec", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 1b", pShip)
        group.AddLauncher( "Shuttle Bay 1b", launcher)
        launcher.AddLaunchable( "WZDestru", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 2b", pShip)
        group.AddLauncher( "Shuttle Bay 2b", launcher)
        launcher.AddLaunchable( "WZDestru", "ftb.friendlyAI", 1)
        
        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)


    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self):
        return 12
    # Don't use the following Tractors to Dock:
    def IgnoreTractors(self):
        return []


# "WZErad" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "WZErad", WZErad)
