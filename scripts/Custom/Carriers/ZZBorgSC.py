# File: Z (Python 1.5)

Carrier = __import__('ftb.Carrier')

class ZZBorgSC(Carrier.Carrier):
    
    def __init__(self, pShip):
        Carrier.Carrier.__init__(self, pShip)
        LauncherGroup = __import__('ftb.LauncherGroup')
        group = LauncherGroup.LauncherGroup()
        LauncherManager = __import__('ftb.LauncherManager')
        launcher = LauncherManager.GetLauncher('Hangar Node', pShip)
        group.AddLauncher('Hangar Node', launcher)
        launcher.AddLaunchable('ZZBNihidrone', 'ftb.friendlyAI', 1)
        self.AddLauncher('Group 1', group)

    
    def GetMaxShuttles(self):
        return 1

    
    def IgnoreTractors(self):
        return [
            'Tractor 1',
            'Tractor 2',
            'Tractor 3',
            'Tractor 4']


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('ZZBorgSC', ZZBorgSC)
