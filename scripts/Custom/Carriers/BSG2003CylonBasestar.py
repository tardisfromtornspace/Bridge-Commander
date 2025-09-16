# BSG2003CylonBasestar.py by CharaToLoki based on Dauntless.py
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
class BSG2003CylonBasestar( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")


        launcher = LauncherManager.GetLauncher( "Main Hangar", pShip)
        group.AddLauncher( "Main Hangar", launcher)
        launcher.AddLaunchable( "BSG2003HeavyRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP1", pShip)
        group.AddLauncher( "Launch Tube DP1", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP2", pShip)
        group.AddLauncher( "Launch Tube DP2", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP3", pShip)
        group.AddLauncher( "Launch Tube DP3", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP4", pShip)
        group.AddLauncher( "Launch Tube DP4", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP5", pShip)
        group.AddLauncher( "Launch Tube DP5", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP6", pShip)
        group.AddLauncher( "Launch Tube DP6", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP7", pShip)
        group.AddLauncher( "Launch Tube DP7", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP8", pShip)
        group.AddLauncher( "Launch Tube DP8", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DP9", pShip)
        group.AddLauncher( "Launch Tube DP9", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS1", pShip)
        group.AddLauncher( "Launch Tube DS1", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS2", pShip)
        group.AddLauncher( "Launch Tube DS2", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS3", pShip)
        group.AddLauncher( "Launch Tube DS3", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS4", pShip)
        group.AddLauncher( "Launch Tube DS4", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS5", pShip)
        group.AddLauncher( "Launch Tube DS5", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS6", pShip)
        group.AddLauncher( "Launch Tube DS6", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS7", pShip)
        group.AddLauncher( "Launch Tube DS7", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS8", pShip)
        group.AddLauncher( "Launch Tube DS8", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DS9", pShip)
        group.AddLauncher( "Launch Tube DS9", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB1", pShip)
        group.AddLauncher( "Launch Tube DB1", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB2", pShip)
        group.AddLauncher( "Launch Tube DB2", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB3", pShip)
        group.AddLauncher( "Launch Tube DB3", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB4", pShip)
        group.AddLauncher( "Launch Tube DB4", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB5", pShip)
        group.AddLauncher( "Launch Tube DB5", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB6", pShip)
        group.AddLauncher( "Launch Tube DB6", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB7", pShip)
        group.AddLauncher( "Launch Tube DB7", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB8", pShip)
        group.AddLauncher( "Launch Tube DB8", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube DB9", pShip)
        group.AddLauncher( "Launch Tube DB9", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP1", pShip)
        group.AddLauncher( "Launch Tube UP1", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP2", pShip)
        group.AddLauncher( "Launch Tube UP2", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP3", pShip)
        group.AddLauncher( "Launch Tube UP3", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP4", pShip)
        group.AddLauncher( "Launch Tube UP4", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP5", pShip)
        group.AddLauncher( "Launch Tube UP5", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP6", pShip)
        group.AddLauncher( "Launch Tube UP6", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP7", pShip)
        group.AddLauncher( "Launch Tube UP7", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP8", pShip)
        group.AddLauncher( "Launch Tube UP8", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UP9", pShip)
        group.AddLauncher( "Launch Tube UP9", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US1", pShip)
        group.AddLauncher( "Launch Tube US1", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US2", pShip)
        group.AddLauncher( "Launch Tube US2", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US3", pShip)
        group.AddLauncher( "Launch Tube US3", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US4", pShip)
        group.AddLauncher( "Launch Tube US4", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US5", pShip)
        group.AddLauncher( "Launch Tube US5", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US6", pShip)
        group.AddLauncher( "Launch Tube US6", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US7", pShip)
        group.AddLauncher( "Launch Tube US7", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US8", pShip)
        group.AddLauncher( "Launch Tube US8", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube US9", pShip)
        group.AddLauncher( "Launch Tube US9", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF1", pShip)
        group.AddLauncher( "Launch Tube UF1", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF2", pShip)
        group.AddLauncher( "Launch Tube UF2", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF3", pShip)
        group.AddLauncher( "Launch Tube UF3", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF4", pShip)
        group.AddLauncher( "Launch Tube UF4", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF5", pShip)
        group.AddLauncher( "Launch Tube UF5", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF6", pShip)
        group.AddLauncher( "Launch Tube UF6", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF7", pShip)
        group.AddLauncher( "Launch Tube UF7", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF8", pShip)
        group.AddLauncher( "Launch Tube UF8", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube UF9", pShip)
        group.AddLauncher( "Launch Tube UF9", launcher)
        launcher.AddLaunchable( "BSG2003CylonRaider", "ftb.friendlyAI", 6)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self): 
    	return 365
    # Don't use the following Tractors to Dock:
    def IgnoreTractors(self):    	
    	return []


# "Dauntless" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "BSG2003CylonBasestar", BSG2003CylonBasestar)
