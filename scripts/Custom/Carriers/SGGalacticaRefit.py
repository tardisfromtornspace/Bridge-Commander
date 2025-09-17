# SGGalacticaRefit.py by CharaToLoki based on Dauntless.py
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
class SGGalacticaRefit( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Launch Tube P1", pShip)
        group.AddLauncher( "Launch Tube P1", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P2", pShip)
        group.AddLauncher( "Launch Tube P2", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P3", pShip)
        group.AddLauncher( "Launch Tube P3", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P4", pShip)
        group.AddLauncher( "Launch Tube P4", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)
        launcher.AddLaunchable( "BSG2003Blackbird", "ftb.friendlyAI", 1)

        launcher = LauncherManager.GetLauncher( "Launch Tube P5", pShip)
        group.AddLauncher( "Launch Tube P5", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P6", pShip)
        group.AddLauncher( "Launch Tube P6", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P7", pShip)
        group.AddLauncher( "Launch Tube P7", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P8", pShip)
        group.AddLauncher( "Launch Tube P8", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P9", pShip)
        group.AddLauncher( "Launch Tube P9", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Launch Tube P10", pShip)
        group.AddLauncher( "Launch Tube P10", launcher)
        launcher.AddLaunchable( "BSG2003ViperMk2", "ftb.friendlyAI", 4)
        launcher.AddLaunchable( "BSG2003ViperMk7", "ftb.friendlyAI", 3)

        launcher = LauncherManager.GetLauncher( "Port Hangar", pShip)
        group.AddLauncher( "Port Hangar", launcher)
        launcher.AddLaunchable( "BSG2003Raptor2", "ftb.friendlyAI", 4)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self): 
    	return 90
    # Don't use the following Tractors to Dock:
    def IgnoreTractors(self):    	
    	return []


# "Dauntless" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "SGGalacticaRefit", SGGalacticaRefit)
