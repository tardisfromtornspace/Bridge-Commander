# Dauntless.py
# April 11, 2002
#
# by Evan Light aka sleight42, all rights reserved
#
# Permission to redistribute this code as part of any other packaging requires
# the explicit permission of the author in advance.
##############################################################################

# A simple example of how to define a custom Carrier with a specified 
# compliment of vessels
Carrier = __import__( "ftb.Carrier")
class Korolev( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Shuttle Bay", pShip)
        group.AddLauncher( "Shuttle Bay", launcher)
        launcher.AddLaunchable( "F3021", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Shuttle Bay 2", pShip)
        group.AddLauncher( "Shuttle Bay 2", launcher)
        
        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        #group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self):
    	return 50
    # Don't use the following Tractors to Dock:
    def IgnoreTractors(self):    	
    	return ["Aft Tractor 2", "Forward Tractor 1", "Forward Tractor 2"]

# "Dauntless" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "Korolev", Korolev)
