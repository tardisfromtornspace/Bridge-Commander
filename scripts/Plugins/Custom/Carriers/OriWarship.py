# OriWarship.py
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
class OriWarship( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Shuttle Bay", pShip)
        group.AddLauncher( "Shuttle Bay", launcher)
        launcher.AddLaunchable( "Fighter", "ftb.friendlyAI", 30)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        #group.SetLaunchMode( LauncherGroup.ALL)
        
    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self): 
    	return 30
    def GetNumMarines(self): 
    	return 60
    def GetNumPeople(self): 
    	return 20

# "OriWarship" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "OriWarship", OriWarship)
