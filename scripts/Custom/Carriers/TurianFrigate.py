#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class TurianFrigate(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay', pShip)
               group.AddLauncher('Shuttle Bay', launcher1)


               launcher1.AddLaunchable('TurianFighter', 'ftb.friendlyAI', 5)


               self.AddLauncher('Group 1', group)


   def GetMaxShuttles(self):
               return 5


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('TurianFrigate', TurianFrigate)
