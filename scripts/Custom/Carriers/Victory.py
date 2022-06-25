#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class Victory(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay 1', pShip)
               group.AddLauncher('Shuttle Bay 1', launcher1)


               launcher2 = LauncherManager.GetLauncher('Shuttle Bay 2', pShip)
               group.AddLauncher('Shuttle Bay 2', launcher2)


               launcher3 = LauncherManager.GetLauncher('Shuttle Bay 3', pShip)
               group.AddLauncher('Shuttle Bay 3', launcher3)


               launcher1.AddLaunchable('Thunderbolt', 'ftb.friendlyAI', 10)


               launcher1.AddLaunchable('EAStarfury', 'Custom.Sneaker.Mvam.MvamAI', 4)


               launcher1.AddLaunchable('EAKestrel', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('EAWorkerPod', 'Custom.Sneaker.Mvam.MvamAI', 2)


               launcher2.AddLaunchable('Thunderbolt', 'ftb.friendlyAI', 10)


               launcher2.AddLaunchable('EAStarfury', 'Custom.Sneaker.Mvam.MvamAI', 4)


               launcher2.AddLaunchable('EAKestrel', 'ftb.friendlyAI', 2)


               launcher2.AddLaunchable('EAWorkerPod', 'Custom.Sneaker.Mvam.MvamAI', 3)


               launcher3.AddLaunchable('Thunderbolt', 'ftb.friendlyAI', 10)


               launcher3.AddLaunchable('EAStarfury', 'Custom.Sneaker.Mvam.MvamAI', 4)


               launcher3.AddLaunchable('EAKestrel', 'ftb.friendlyAI', 2)


               launcher3.AddLaunchable('EAWorkerPod', 'Custom.Sneaker.Mvam.MvamAI', 2)


               self.AddLauncher('Group 1', group)


   def GetMaxShuttles(self):
               return 55


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('Victory', Victory)
