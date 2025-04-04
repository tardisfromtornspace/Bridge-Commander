from bcdebug import debug
# Carrier file Akira.py autogenerated by http://defiant.homedns.org/~erik/STBC/carrier/

Carrier = __import__("ftb.Carrier")
class Akira(Carrier.Carrier):
    def __init__(self, pShip):
        debug(__name__ + ", __init__")
        Carrier.Carrier.__init__(self, pShip)
        LauncherGroup = __import__("ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__("ftb.LauncherManager")

	launcher1 = LauncherManager.GetLauncher("Shuttle Bay 1", pShip)
	group.AddLauncher("Shuttle Bay 1", launcher1)

	launcher1.AddLaunchable("Shuttle", "ftb.friendlyAI", 6)

	launcher1.AddLaunchable("type9", "ftb.friendlyAI", 4)

	self.AddLauncher("Group 1", group)

ShipManager = __import__("ftb.ShipManager")
ShipManager.RegisterShipClass("Akira", Akira)
