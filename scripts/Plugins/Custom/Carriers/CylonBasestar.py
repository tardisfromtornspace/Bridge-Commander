# CylonBasestar.py    a Carrier File by MadJohn
#
# Based off.
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
class CylonBasestar( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Launch Tube P1", pShip)
        group.AddLauncher( "Launch Tube P1 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P2", pShip)
        group.AddLauncher( "Launch Tube P2 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P3", pShip)
        group.AddLauncher( "Launch Tube P3 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P4", pShip)
        group.AddLauncher( "Launch Tube P4 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P5", pShip)
        group.AddLauncher( "Launch Tube P5 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P6", pShip)
        group.AddLauncher( "Launch Tube P6 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P7", pShip)
        group.AddLauncher( "Launch Tube P7 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P8", pShip)
        group.AddLauncher( "Launch Tube P8 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube P9", pShip)
        group.AddLauncher( "Launch Tube P9 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S1", pShip)
        group.AddLauncher( "Launch Tube S1 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S2", pShip)
        group.AddLauncher( "Launch Tube S2 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S3", pShip)
        group.AddLauncher( "Launch Tube S3 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S4", pShip)
        group.AddLauncher( "Launch Tube S4 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S5", pShip)
        group.AddLauncher( "Launch Tube S5 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S6", pShip)
        group.AddLauncher( "Launch Tube S6 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S7", pShip)
        group.AddLauncher( "Launch Tube S7 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S8", pShip)
        group.AddLauncher( "Launch Tube S8 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)


        launcher = LauncherManager.GetLauncher( "Launch Tube S9", pShip)
        group.AddLauncher( "Launch Tube S9 ", launcher)
        launcher.AddLaunchable( "CylonRaider", "ftb.friendlyAI", 2)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        #group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self): 
    	return 36
    # Don't use the following Tractors to Dock:
    def IgnoreTractors(self):    	
    	return []


# "Dauntless" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "CylonBasestar", CylonBasestar)
