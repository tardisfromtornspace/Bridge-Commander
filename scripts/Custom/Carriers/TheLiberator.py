from bcdebug import debug
##############################################################################

Carrier = __import__( "ftb.Carrier")
class TheLiberator( Carrier.Carrier):
	def __init__( self, pShip):
		debug(__name__ + ", __init__")
		Carrier.Carrier.__init__( self, pShip)
		# The script name should be the name of the "ship" script, not the
		# hardpoint (otherwise, you'll crash your BC and this is bad)
		LauncherGroup = __import__( "ftb.LauncherGroup")
		group = LauncherGroup.LauncherGroup()

		LauncherManager = __import__( "ftb.LauncherManager")
		launcher = LauncherManager.GetLauncher( "Fighter Bay", pShip)
		group.AddLauncher( "Fighter Bay", launcher)
		launcher.AddLaunchable( "LiberatorFighter", "ftb.friendlyAI", 10)

		self.AddLauncher( "Group 1", group)

		# Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
		group.SetLaunchMode( LauncherGroup.ALL)

	# Define how much Shuttles we can carry maximal (Return Shuttles script)
	def GetMaxShuttles(self):
		debug(__name__ + ", GetMaxShuttles")
		return 10

   
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "TheLiberator", TheLiberator)
