from bcdebug import debug
# Intrepid.py
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
class Intrepid( Carrier.Carrier):
    def __init__( self, pShip):
        debug(__name__ + ", __init__")
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Shuttle Bay", pShip)
        group.AddLauncher( "Shuttle Bay", launcher)
        launcher.AddLaunchable( "type9", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "deltaflyer", "ftb.friendlyAI", 1)

        self.AddLauncher( "Group 1", group)

    def GetMaxShuttles(self): 
    	debug(__name__ + ", GetMaxShuttles")
    	return 6

# "Intrepid" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "Intrepid", Intrepid)
