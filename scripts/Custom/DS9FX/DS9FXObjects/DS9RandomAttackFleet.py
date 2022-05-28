# Handles random attack force

# by USS Sovereign

import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def DS9SetEnemyShips():       
        SelectRandomShipNumber = GetRandomRate(4,1)

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.DominionSide == 1:
                if DS9FXSavedConfig.RandomDomStrength == 3:
                        Rand = GetRandomRate(99,1)
                        for i in range(1, Rand):
                                if i <= 33:
                                        CreateLowEnemy(SelectRandomShipNumber)
                                elif i <= 66:
                                        CreateMedEnemy(SelectRandomShipNumber)
                                elif i <= 100:
                                        CreateStrongEnemy(SelectRandomShipNumber)                                        
                elif DS9FXSavedConfig.RandomDomStrength == 2:    
                        for i in range(1, SelectRandomShipNumber):
                                CreateStrongEnemy(i)
                elif DS9FXSavedConfig.RandomDomStrength == 1:
                        for i in range(1, SelectRandomShipNumber):
                                CreateMedEnemy(i)
                else:
                        for i in range(1, SelectRandomShipNumber):
                                CreateLowEnemy(i)              
        else:
                if DS9FXSavedConfig.RandomDomStrength == 3:
                        Rand = GetRandomRate(99,1)
                        for i in range(1, Rand):
                                if i <= 33:
                                        CreateLowFriendly(SelectRandomShipNumber)
                                elif i <= 66:
                                        CreateMedFriendly(SelectRandomShipNumber)
                                elif i <= 100: 
                                        CreateStrongFriendly(SelectRandomShipNumber)                     
                elif DS9FXSavedConfig.RandomDomStrength == 2:
                        for i in range(1, SelectRandomShipNumber):
                                CreateStrongFriendly(i)

                elif DS9FXSavedConfig.RandomDomStrength == 1:
                        for i in range(1, SelectRandomShipNumber):
                                CreateMedFriendly(i)             
                else:
                        for i in range(1, SelectRandomShipNumber):
                                CreateLowFriendly(i)

def CreateStrongEnemy(i):
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        if i == 1:
                Att1 = "Attacker 1"
                pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, DS9Set, Att1, "Random 1 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att1)
                pMission.GetFriendlyGroup().AddName(Att1)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                pAttacker1 = App.ShipClass_Cast(Attacker1)

                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))
        elif i == 2:
                Att2 = "Attacker 2"
                pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att2, "Random 2 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att2)
                pMission.GetFriendlyGroup().AddName(Att2)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                pAttacker2 = App.ShipClass_Cast(Attacker2)

                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))
        elif i == 3:
                Att3 = "Attacker 3"
                pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att3, "Random 3 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att3)
                pMission.GetFriendlyGroup().AddName(Att3)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                pAttacker3 = App.ShipClass_Cast(Attacker3)

                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))
        elif i == 4:
                Att4 = "Attacker 4"
                pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att4, "Random 4 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att4)
                pMission.GetFriendlyGroup().AddName(Att4)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                pAttacker4 = App.ShipClass_Cast(Attacker4)

                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker4))
        elif i == 5:
                Att5 = "Attacker 5"
                pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att5, "Random 5 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att5)
                pMission.GetFriendlyGroup().AddName(Att5)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                pAttacker5 = App.ShipClass_Cast(Attacker5)

                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker5))

def CreateStrongFriendly(i):
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        if i == 1:
                Att1 = "Attacker 1"
                pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, DS9Set, Att1, "Random 1 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att1)
                pMission.GetEnemyGroup().AddName(Att1)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                pAttacker1 = App.ShipClass_Cast(Attacker1)

                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))
        elif i == 2:                
                Att2 = "Attacker 2"
                pAtt2 = loadspacehelper.CreateShip(DS9FXShips.DomBC, DS9Set, Att2, "Random 2 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att2)
                pMission.GetEnemyGroup().AddName(Att2)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                pAttacker2 = App.ShipClass_Cast(Attacker2)

                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))
        elif i == 3:              
                Att3 = "Attacker 3"
                pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att3, "Random 3 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att3)
                pMission.GetEnemyGroup().AddName(Att3)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                pAttacker3 = App.ShipClass_Cast(Attacker3)

                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))
        elif i == 4:              
                Att4 = "Attacker 4"
                pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att4, "Random 4 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att4)
                pMission.GetEnemyGroup().AddName(Att4)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                pAttacker4 = App.ShipClass_Cast(Attacker4)

                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))
        elif i == 5:              
                Att5 = "Attacker 5"
                pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att5, "Random 5 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att5)
                pMission.GetEnemyGroup().AddName(Att5)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                pAttacker5 = App.ShipClass_Cast(Attacker5)

                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

def CreateMedEnemy(i):
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        if i == 1:
                Att1 = "Attacker 1"
                pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, DS9Set, Att1, "Random 1 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att1)
                pMission.GetFriendlyGroup().AddName(Att1)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                pAttacker1 = App.ShipClass_Cast(Attacker1)

                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))
        elif i == 2:              
                Att2 = "Attacker 2"
                pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att2, "Random 2 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att2)
                pMission.GetFriendlyGroup().AddName(Att2)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                pAttacker2 = App.ShipClass_Cast(Attacker2)

                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))
        elif i == 3:              
                Att3 = "Attacker 3"
                pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att3, "Random 3 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att3)
                pMission.GetFriendlyGroup().AddName(Att3)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                pAttacker3 = App.ShipClass_Cast(Attacker3)

                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))
        elif i == 4:              
                Att4 = "Attacker 4"
                pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att4, "Random 4 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att4)
                pMission.GetFriendlyGroup().AddName(Att4)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                pAttacker4 = App.ShipClass_Cast(Attacker4)

                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker4))
        elif i == 5:              
                Att5 = "Attacker 5"
                pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att5, "Random 5 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att5)
                pMission.GetFriendlyGroup().AddName(Att5)

                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                pAttacker5 = App.ShipClass_Cast(Attacker5)

                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker5))

def CreateMedFriendly(i):
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        if i == 1:
                Att1 = "Attacker 1"
                pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, DS9Set, Att1, "Random 1 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att1)
                pMission.GetEnemyGroup().AddName(Att1)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                pAttacker1 = App.ShipClass_Cast(Attacker1)

                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))
        elif i == 2:              
                Att2 = "Attacker 2"
                pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att2, "Random 2 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att2)
                pMission.GetEnemyGroup().AddName(Att2)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                pAttacker2 = App.ShipClass_Cast(Attacker2)

                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))
        elif i == 3:                      
                Att3 = "Attacker 3"
                pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att3, "Random 3 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att3)
                pMission.GetEnemyGroup().AddName(Att3)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                pAttacker3 = App.ShipClass_Cast(Attacker3)

                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))
        elif i == 4:              
                Att4 = "Attacker 4"
                pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att4, "Random 4 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att4)
                pMission.GetEnemyGroup().AddName(Att4)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                pAttacker4 = App.ShipClass_Cast(Attacker4)

                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))
        elif i == 5:              
                Att5 = "Attacker 5"
                pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att5, "Random 5 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att5)
                pMission.GetEnemyGroup().AddName(Att5)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                pAttacker5 = App.ShipClass_Cast(Attacker5)

                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))        

def CreateLowEnemy(i):
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        if i == 1:
                Att1 = "Attacker 1"
                pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att1, "Random 1 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att1)
                pMission.GetFriendlyGroup().AddName(Att1)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                pAttacker1 = App.ShipClass_Cast(Attacker1)

                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))
        elif i == 2:             
                Att2 = "Attacker 2"
                pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att2, "Random 2 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att2)
                pMission.GetFriendlyGroup().AddName(Att2)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                pAttacker2 = App.ShipClass_Cast(Attacker2)

                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))
        elif i == 3:        
                Att3 = "Attacker 3"
                pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att3, "Random 3 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att3)
                pMission.GetFriendlyGroup().AddName(Att3)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                pAttacker3 = App.ShipClass_Cast(Attacker3)

                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))
        elif i == 4:              
                Att4 = "Attacker 4"
                pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att4, "Random 4 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att4)
                pMission.GetFriendlyGroup().AddName(Att4)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                pAttacker4 = App.ShipClass_Cast(Attacker4)

                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))
        elif i == 5:              
                Att5 = "Attacker 5"
                pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att5, "Random 5 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att5)
                pMission.GetFriendlyGroup().AddName(Att5)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                pAttacker5 = App.ShipClass_Cast(Attacker5)

                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

def CreateLowFriendly(i):
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        if i == 1:
                Att1 = "Attacker 1"
                pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att1, "Random 1 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att1)
                pMission.GetEnemyGroup().AddName(Att1)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                pAttacker1 = App.ShipClass_Cast(Attacker1)

                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))
        elif i == 2:              
                Att2 = "Attacker 2"
                pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att2, "Random 2 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att2)
                pMission.GetEnemyGroup().AddName(Att2)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                pAttacker2 = App.ShipClass_Cast(Attacker2)

                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))
        elif i == 3:               
                Att3 = "Attacker 3"
                pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att3, "Random 3 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att3)
                pMission.GetEnemyGroup().AddName(Att3)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                pAttacker3 = App.ShipClass_Cast(Attacker3)

                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))
        elif i == 4:            
                Att4 = "Attacker 4"
                pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att4, "Random 4 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att4)
                pMission.GetEnemyGroup().AddName(Att4)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                pAttacker4 = App.ShipClass_Cast(Attacker4)

                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))
        elif i == 5:            
                Att5 = "Attacker 5"
                pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, DS9Set, Att5, "Random 5 Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Att5)
                pMission.GetEnemyGroup().AddName(Att5)

                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                pAttacker5 = App.ShipClass_Cast(Attacker5)

                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

def GetRandomRate(iRandom, iStatic):
        return App.g_kSystemWrapper.GetRandomNumber(iRandom) + iStatic
