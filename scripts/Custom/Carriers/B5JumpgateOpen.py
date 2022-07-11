#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class B5JumpgateOpen(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay 1', pShip)
               group.AddLauncher('Shuttle Bay 1', launcher1)


               launcher1.AddLaunchable('EAAsimov', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('EAAchillesFreighter', 'Custom.Sneaker.Mvam.MvamAI', 1)


               launcher1.AddLaunchable('DraziSunHawk', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('EAForceOne', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('EAPsiCorpCrewShuttle', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('EAOmega', 'ftb.friendlyAI', 5)


               launcher1.AddLaunchable('EAKestrel', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('DRA_Shuttle', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('B5TechnomageTransport', 'Custom.Sneaker.Mvam.MvamAI', 2)


               launcher1.AddLaunchable('B5RaiderBattlewagon', 'Custom.Sneaker.Mvam.MvamAI', 2)


               launcher1.AddLaunchable('B5LordShip', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('B5ZephyrRaider', 'ftb.friendlyAI', 7)


               launcher1.AddLaunchable('DRA_Cruiser', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('DeltaWing', 'Custom.Sneaker.Mvam.MvamAI', 4)


               launcher1.AddLaunchable('bluestar', 'ftb.friendlyAI', 6)


               launcher1.AddLaunchable('VOR_DestroyerClosed', 'Custom.Sneaker.Mvam.MvamAI', 2)


               launcher1.AddLaunchable('VOR_Cruiser', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('TorvalusDarkKnife', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('VOR_FighterOpen', 'Custom.Sneaker.Mvam.MvamAI', 4)


               launcher1.AddLaunchable('ZetaWing', 'Custom.Sneaker.Mvam.MvamAI', 4)


               launcher1.AddLaunchable('Warlock', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('VreeXill', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('ThNor', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('GQuan', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('EAWorkerPod', 'Custom.Sneaker.Mvam.MvamAI', 1)


               launcher1.AddLaunchable('EAStarfury', 'Custom.Sneaker.Mvam.MvamAI', 6)


               launcher1.AddLaunchable('MinbariSharlin', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('Shadow_Scout', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('SentriFighter', 'ftb.friendlyAI', 7)


               launcher1.AddLaunchable('NarnFraziFighter', 'ftb.friendlyAI', 7)


               launcher1.AddLaunchable('MindridersThoughtforce', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('EAShadow_Hybrid', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('AlphaWing', 'Custom.Sneaker.Mvam.MvamAI', 6)


               launcher1.AddLaunchable('DRA_Raider', 'ftb.friendlyAI', 8)


               launcher1.AddLaunchable('B5TriadTriumviron', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('Battlecrab', 'Custom.Sneaker.Mvam.MvamAI', 3)


               launcher1.AddLaunchable('EAHyperion', 'ftb.friendlyAI', 4)


               launcher1.AddLaunchable('DraziSkySerpent', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('BrakiriCruiser', 'ftb.friendlyAI', 6)


               launcher1.AddLaunchable('Shadow_Fighter', 'ftb.friendlyAI', 5)


               launcher1.AddLaunchable('B5PsiCorpMothership', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('EchoWing', 'Custom.Sneaker.Mvam.MvamAI', 3)


               launcher1.AddLaunchable('Victory', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('EACrewShuttleBlue', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('Vorchan', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('DRA_Carrier', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('DraziSunHawkWithSerpent', 'Custom.Sneaker.Mvam.MvamAI', 2)


               launcher1.AddLaunchable('EAStealthStarfury', 'Custom.Sneaker.Mvam.MvamAI', 3)


               launcher1.AddLaunchable('VOR_Fighter', 'Custom.Sneaker.Mvam.MvamAI', 2)


               launcher1.AddLaunchable('EAOmegaX', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('EAAchillesFreighterNoModules', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('MinbariNial', 'ftb.friendlyAI', 4)


               launcher1.AddLaunchable('SigmaWalkerScienceLab', 'ftb.friendlyAI', 1)


               launcher1.AddLaunchable('B5SoulHunterVessel', 'ftb.friendlyAI', 5)


               launcher1.AddLaunchable('Primus', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('VreeXorr', 'ftb.friendlyAI', 2)


               launcher1.AddLaunchable('EANova', 'ftb.friendlyAI', 3)


               launcher1.AddLaunchable('Thunderbolt', 'ftb.friendlyAI', 4)


               launcher1.AddLaunchable('VOR_Destroyer', 'Custom.Sneaker.Mvam.MvamAI', 1)


               launcher1.AddLaunchable('whitestar', 'ftb.friendlyAI', 12)


               self.AddLauncher('Group 1', group)


   def GetMaxShuttles(self):
               return 180


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('B5JumpgateOpen', B5JumpgateOpen)
