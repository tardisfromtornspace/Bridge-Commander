# DS9.py
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
class DS9( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")

	launcher = LauncherManager.GetLauncher( "Shuttle Bay 1", pShip)
        group.AddLauncher( "Shuttle Bay 1", launcher)
        launcher.AddLaunchable( "DanubemkI", "ftb.friendlyAI", 1)

	launcher = LauncherManager.GetLauncher( "Shuttle Bay 2", pShip)
        group.AddLauncher( "Shuttle Bay 2", launcher)
        launcher.AddLaunchable( "DanubemkI", "ftb.friendlyAI", 1)

	launcher = LauncherManager.GetLauncher( "Shuttle Bay 3", pShip)
        group.AddLauncher( "Shuttle Bay 3", launcher)
        launcher.AddLaunchable( "DanubemkII", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Defiant Dock", pShip)
        group.AddLauncher( "Defiant Dock", launcher)
        launcher.AddLaunchable( "Defiant", "ftb.friendlyAI", 1)
        
        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        #group.SetLaunchMode( LauncherGroup.ALL)

# "Deep Space 9" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "Deep Space 9", DS9)
