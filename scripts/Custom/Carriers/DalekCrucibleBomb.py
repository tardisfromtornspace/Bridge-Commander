from bcdebug import debug
##############################################################################

Carrier = __import__( "ftb.Carrier")
class DalekCrucibleBomb( Carrier.Carrier):
	def __init__( self, pShip):
		debug(__name__ + ", __init__")
		Carrier.Carrier.__init__( self, pShip)
		# The script name should be the name of the "ship" script, not the
		# hardpoint (otherwise, you'll crash your BC and this is bad)
		LauncherGroup = __import__( "ftb.LauncherGroup")
		group = LauncherGroup.LauncherGroup()

		LauncherManager = __import__( "ftb.LauncherManager")
		launcher = LauncherManager.GetLauncher( "Shuttle Bay 1", pShip)
		group.AddLauncher( "Shuttle Bay 1", launcher)
		launcher.AddLaunchable( "DalekSmallSaucer", "Custom.Sneaker.Mvam.MvamAI", 6)
		launcher.AddLaunchable( "DalekSaucer", "Custom.Sneaker.Mvam.MvamAI", 1)

		launcher = LauncherManager.GetLauncher( "Shuttle Bay 2", pShip)
		group.AddLauncher( "Shuttle Bay 2", launcher)
		launcher.AddLaunchable( "DalekSmallSaucer", "Custom.Sneaker.Mvam.MvamAI", 6)
		launcher.AddLaunchable( "DalekSaucer", "Custom.Sneaker.Mvam.MvamAI", 1)
		
		launcher = LauncherManager.GetLauncher( "Shuttle Bay 3", pShip)
		group.AddLauncher( "Shuttle Bay 3", launcher)
		launcher.AddLaunchable( "DalekSmallSaucer", "Custom.Sneaker.Mvam.MvamAI", 6)
		launcher.AddLaunchable( "DalekSaucer", "Custom.Sneaker.Mvam.MvamAI", 1)

		launcher = LauncherManager.GetLauncher( "Shuttle Bay 4", pShip)
		group.AddLauncher( "Shuttle Bay 4", launcher)
		launcher.AddLaunchable( "DalekSmallSaucer", "Custom.Sneaker.Mvam.MvamAI", 6)
		launcher.AddLaunchable( "DalekSaucer", "Custom.Sneaker.Mvam.MvamAI", 1)

		launcher = LauncherManager.GetLauncher( "Shuttle Bay 5", pShip)
		group.AddLauncher( "Shuttle Bay 5", launcher)
		launcher.AddLaunchable( "DalekSmallSaucer", "Custom.Sneaker.Mvam.MvamAI", 6)
		launcher.AddLaunchable( "DalekSaucer", "Custom.Sneaker.Mvam.MvamAI", 1)

		launcher = LauncherManager.GetLauncher( "Shuttle Bay 6", pShip)
		group.AddLauncher( "Shuttle Bay 6", launcher)
		launcher.AddLaunchable( "DalekSmallSaucer", "Custom.Sneaker.Mvam.MvamAI", 6)
		launcher.AddLaunchable( "DalekSaucer", "Custom.Sneaker.Mvam.MvamAI", 1)

		self.AddLauncher( "Group 1", group)

		# Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
		group.SetLaunchMode( LauncherGroup.ALL)

	# Define how much Shuttles we can carry maximal (Return Shuttles script)
	def GetMaxShuttles(self):
		debug(__name__ + ", GetMaxShuttles")
		return 44

   
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "DalekCrucibleBomb", DalekCrucibleBomb)
