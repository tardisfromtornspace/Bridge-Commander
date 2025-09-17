# BSG1978HadesBasestar.py by CharaToLoki based on Dauntless.py
#
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
class BSG1978HadesBasestar( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Hangar 1", pShip)
        group.AddLauncher( "Hangar 1", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 2", pShip)
        group.AddLauncher( "Hangar 2", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 3", pShip)
        group.AddLauncher( "Hangar 3", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 4", pShip)
        group.AddLauncher( "Hangar 4", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 5", pShip)
        group.AddLauncher( "Hangar 5", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 6", pShip)
        group.AddLauncher( "Hangar 6", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 7", pShip)
        group.AddLauncher( "Hangar 7", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 8", pShip)
        group.AddLauncher( "Hangar 8", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 9", pShip)
        group.AddLauncher( "Hangar 9", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 10", pShip)
        group.AddLauncher( "Hangar 10", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 11", pShip)
        group.AddLauncher( "Hangar 11", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 12", pShip)
        group.AddLauncher( "Hangar 12", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 13", pShip)
        group.AddLauncher( "Hangar 13", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 14", pShip)
        group.AddLauncher( "Hangar 14", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 15", pShip)
        group.AddLauncher( "Hangar 15", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 16", pShip)
        group.AddLauncher( "Hangar 16", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 17", pShip)
        group.AddLauncher( "Hangar 17", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 18", pShip)
        group.AddLauncher( "Hangar 18", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 19", pShip)
        group.AddLauncher( "Hangar 19", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        launcher = LauncherManager.GetLauncher( "Hangar 20", pShip)
        group.AddLauncher( "Hangar 20", launcher)
        launcher.AddLaunchable( "BSG2003MkXRaider", "ftb.friendlyAI", 15)


        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self): 
    	return 360

    # Don't use the following Tractors to Dock:
    def IgnoreTractors(self):    	
    	return []


# "Dauntless" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "BSG1978HadesBasestar", BSG1978HadesBasestar)
