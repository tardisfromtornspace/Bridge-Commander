#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__( "ftb.Carrier")
class BSG2003ColDefender( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")

        launcher = LauncherManager.GetLauncher( "Hangar", pShip)
        group.AddLauncher( "Hangar", launcher)
        launcher.AddLaunchable( "BSG2003Raptor", "QuickBattle.QuickBattleFriendlyAI", 3)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 10)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self): 
    	return 20

# "BSG2003ColDefender" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "BSG2003ColDefender", BSG2003ColDefender)
