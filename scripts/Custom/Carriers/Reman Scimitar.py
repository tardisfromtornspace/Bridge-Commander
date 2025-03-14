Carrier = __import__("ftb.Carrier")
class RemanScimitar(Carrier.Carrier):
    def __init__(self, pShip):
        Carrier.Carrier.__init__(self, pShip)
        LauncherGroup = __import__("ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__("ftb.LauncherManager")

	launcher1 = LauncherManager.GetLauncher("Shuttle Bay", pShip)
	group.AddLauncher("Shuttle Bay", launcher1)

	launcher1.AddLaunchable("scorpion", "ftb.friendlyAI", 10)

	self.AddLauncher("Group 1", group)

ShipManager = __import__("ftb.ShipManager")
ShipManager.RegisterShipClass("scimitar", RemanScimitar)
