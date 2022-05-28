# Andromeda.py
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
class Andromeda( Carrier.Carrier):
    def __init__( self, pShip):
        Carrier.Carrier.__init__( self, pShip)
        # The script name should be the name of the "ship" script, not the
        # hardpoint (otherwise, you'll crash your BC and this is bad)
        LauncherGroup = __import__( "ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__( "ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher( "Bay 1", pShip)
        group.AddLauncher( "Bay 1", launcher)
        launcher.AddLaunchable( "AndSlipFighter", "QuickBattle.QuickBattleFriendlyAI", 16)

        launcher = LauncherManager.GetLauncher( "Bay 2", pShip)
        group.AddLauncher( "Bay 2", launcher)
        launcher.AddLaunchable( "AndSlipFighterMK1", "QuickBattle.QuickBattleFriendlyAI",12)
 
        launcher = LauncherManager.GetLauncher( "Bay 3", pShip)
        group.AddLauncher( "Bay 3", launcher)
        launcher.AddLaunchable( "AndSlipFighterMK2", "QuickBattle.QuickBattleFriendlyAI", 12)

 	launcher = LauncherManager.GetLauncher( "Bay 4", pShip)
        group.AddLauncher( "Bay 4", launcher)
        launcher.AddLaunchable( "AndSlipFighterMK3", "QuickBattle.QuickBattleFriendlyAI", 13)

 	launcher = LauncherManager.GetLauncher( "Bay 5", pShip)
        group.AddLauncher( "Bay 5", launcher)
        launcher.AddLaunchable( "AndSlipFighterMK3", "QuickBattle.QuickBattleFriendlyAI", 11)

        self.AddLauncher( "Group 1", group)

        # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
        #group.SetLaunchMode( LauncherGroup.ALL)

# "Dauntless" is the "ShipProperty" name of the ship to be registered as
# defined in the Hardpoints PY file for your ship
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "Andromeda", Andromeda)
