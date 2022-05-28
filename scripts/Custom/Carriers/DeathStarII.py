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
class DeathStarII( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Hangar 1", pShip)
        group.AddLauncher( "Hangar 1", launcher)
        launcher.AddLaunchable( "tiedrone", "ftb.friendlyAI", 93)

        launcher = LauncherManager.GetLauncher( "Hangar 2", pShip)
        group.AddLauncher( "Hangar 2", launcher)
        launcher.AddLaunchable( "tiefighter", "ftb.friendlyAI", 90)

        launcher = LauncherManager.GetLauncher( "Hangar 3", pShip)
        group.AddLauncher( "Hangar 3", launcher)
        launcher.AddLaunchable( "tieinterceptor", "ftb.friendlyAI", 56)

        launcher = LauncherManager.GetLauncher( "Hangar 4", pShip)
        group.AddLauncher( "Hangar 4", launcher)
        launcher.AddLaunchable( "ISD", "ftb.friendlyAI", 6)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        #group.SetLaunchMode( LauncherGroup.ALL)

# "Dauntless" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "DeathStarII", DeathStarII)
