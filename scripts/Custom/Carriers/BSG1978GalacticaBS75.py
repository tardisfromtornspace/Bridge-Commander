#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__( "ftb.Carrier")
class BSG1978GalacticaBS75( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Launch Tube P1", pShip)
        group.AddLauncher( "Launch Tube P1 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube P2", pShip)
        group.AddLauncher( "Launch Tube P2 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube P3", pShip)
        group.AddLauncher( "Launch Tube P3 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube P4", pShip)
        group.AddLauncher( "Launch Tube P4 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube P5", pShip)
        group.AddLauncher( "Launch Tube P5 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube P6", pShip)
        group.AddLauncher( "Launch Tube P6 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube P7", pShip)
        group.AddLauncher( "Launch Tube P7 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube P8", pShip)
        group.AddLauncher( "Launch Tube P8 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S1", pShip)
        group.AddLauncher( "Launch Tube S1 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S2", pShip)
        group.AddLauncher( "Launch Tube S2 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S3", pShip)
        group.AddLauncher( "Launch Tube S3 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S4", pShip)
        group.AddLauncher( "Launch Tube S4 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S5", pShip)
        group.AddLauncher( "Launch Tube S5 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S6", pShip)
        group.AddLauncher( "Launch Tube S6 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S7", pShip)
        group.AddLauncher( "Launch Tube S7 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Launch Tube S8", pShip)
        group.AddLauncher( "Launch Tube S8 ", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Port Hangar", pShip)
        group.AddLauncher( "Port Hangar", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)


        launcher = LauncherManager.GetLauncher( "Star Hangar", pShip)
        group.AddLauncher( "Star Hangar", launcher)
        launcher.AddLaunchable( "BSG1978Viper", "QuickBattle.QuickBattleFriendlyAI", 6)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        group.SetLaunchMode( LauncherGroup.ALL)

    # Define how much Shuttles we can carry maximal (Return Shuttles script)
    def GetMaxShuttles(self): 
    	return 175

# "BSG1978GalacticaBS75" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "BSG1978GalacticaBS75", BSG1978GalacticaBS75)
