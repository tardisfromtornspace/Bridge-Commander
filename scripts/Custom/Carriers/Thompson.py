#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class Thompson(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay', pShip)
               group.AddLauncher('Shuttle Bay', launcher1)


               launcher1.AddLaunchable('ZZGalileoShuttle', 'ftb.friendlyAI', 4)


               self.AddLauncher('Group 1', group)


   def GetMaxShuttles(self):
               return 6


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('Thompson', Thompson)
