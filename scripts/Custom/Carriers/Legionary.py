from bcdebug import debug
##############################################################################

Carrier = __import__( "ftb.Carrier")
class Legionary( Carrier.Carrier):
	def __init__( self, pShip):
		debug(__name__ + ", __init__")
		Carrier.Carrier.__init__( self, pShip)
		# The script name should be the name of the "ship" script, not the
		# hardpoint (otherwise, you'll crash your BC and this is bad)
		LauncherGroup = __import__( "ftb.LauncherGroup")
		group = LauncherGroup.LauncherGroup()

		LauncherManager = __import__( "ftb.LauncherManager")
		launcher = LauncherManager.GetLauncher( "Auto Fighter Bay", pShip)
		group.AddLauncher( "Auto Fighter Bay", launcher)
		launcher.AddLaunchable( "LegionaryAutoFighter", "ftb.friendlyAI", 12)

		LauncherManager = __import__( "ftb.LauncherManager")
		launcher = LauncherManager.GetLauncher( "Manual Fighter Bay", pShip)
		group.AddLauncher( "Manual Fighter Bay", launcher)
		launcher.AddLaunchable( "LegionaryManualFighter", "ftb.friendlyAI", 4)

		self.AddLauncher( "Group 1", group)

		# Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
		group.SetLaunchMode( LauncherGroup.ALL)

	# Define how much Shuttles we can carry maximal (Return Shuttles script)
	def GetMaxShuttles(self):
		debug(__name__ + ", GetMaxShuttles")
		return 16

   
ShipManager = __import__( "ftb.ShipManager")
ShipManager.RegisterShipClass( "Legionary", Legionary)
