#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class EAAsimov(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay 1', pShip)
               group.AddLauncher('Shuttle Bay 1', launcher1)


               launcher1.AddLaunchable("EACrewShuttle", 'ftb.friendlyAI', 1)
               launcher1.AddLaunchable("EACrewShuttleRed", 'ftb.friendlyAI', 1)
               launcher1.AddLaunchable( "EACrewShuttleBlue", "ftb.friendlyAI", 1)


               self.AddLauncher('Group 1', group)


   def GetMaxShuttles(self):
               return 4


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('EAAsimov', EAAsimov)
