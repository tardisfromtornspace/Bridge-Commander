#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class B5Warlock(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay 1', pShip)
               group.AddLauncher('Shuttle Bay 1', launcher1)


               launcher1.AddLaunchable('EAStarfury', 'Custom.Sneaker.Mvam.MvamAI', 12)


               self.AddLauncher('Group 1', group)

               # Play with this feature if you dare... MUHAHAHAHAHAHAHAHAHAHAHAHA!!!!!
               group.SetLaunchMode( LauncherGroup.ALL)


   def GetMaxShuttles(self):
               return 18


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('B5Warlock', B5Warlock)
