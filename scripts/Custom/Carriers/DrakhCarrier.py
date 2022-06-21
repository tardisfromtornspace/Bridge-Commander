#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class DrakhCarrier(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay 1', pShip)
               group.AddLauncher('Shuttle Bay 1', launcher1)


               launcher1.AddLaunchable('DRA_Shuttle', 'ftb.friendlyAI', 5)


               launcher1.AddLaunchable('DRA_Raider', 'ftb.friendlyAI', 40)


               self.AddLauncher('Group 1', group)


   def GetMaxShuttles(self):
               return 45


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('DrakhCarrier', DrakhCarrier)
