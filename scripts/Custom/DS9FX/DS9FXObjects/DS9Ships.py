# Over here we'll save the locations of ships which we'll load when we enter DS9 Map

# by USS Sovereign

# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig


# Ship detail def
def DS9SetShips():
        # Grab the system name from the set file
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.FederationSide == 1:

                if DS9FXSavedConfig.ExcaliburSelection == 1:
                        # Create the Excalibur
                        Excal = "USS Excalibur"
                        pExcal = loadspacehelper.CreateShip(DS9FXShips.Excalibur, DS9Set, Excal, "Excal Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Excal)
                        pMission.GetFriendlyGroup().AddName(Excal)

                        import Custom.DS9FX.DS9FXAILib.DS9FXExcalAI

                        Excalibur = MissionLib.GetShip("USS Excalibur", DS9Set) 

                        pExcalibur = App.ShipClass_Cast(Excalibur)

                        pExcalibur.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExcalAI.CreateAI(pExcalibur))

                if DS9FXSavedConfig.DefiantSelection == 1:
                        # Create the Defiant
                        Def = "USS Defiant"
                        pDef = loadspacehelper.CreateShip(DS9FXShips.Defiant, DS9Set, Def, "Defiant Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Def)
                        pMission.GetFriendlyGroup().AddName(Def)

                        import Custom.DS9FX.DS9FXAILib.DS9FXDefiantAI

                        Defiant = MissionLib.GetShip("USS Defiant", DS9Set)

                        pDefiant = App.ShipClass_Cast(Defiant)

                        pDefiant.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXDefiantAI.CreateAI(pDefiant))

                if DS9FXSavedConfig.OregonSelection == 1:
                        # Create the Oregon
                        Oreg = "USS Oregon"
                        pOreg = loadspacehelper.CreateShip(DS9FXShips.Miranda, DS9Set, Oreg, "Oregon Location")
                        
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Oreg)
                        pMission.GetFriendlyGroup().AddName(Oreg)

                        import Custom.DS9FX.DS9FXAILib.DS9FXOregonAI

                        Oregon = MissionLib.GetShip("USS Oregon", DS9Set)

                        pOregon = App.ShipClass_Cast(Oregon)

                        pOregon.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXOregonAI.CreateAI(pOregon))

                if DS9FXSavedConfig.LakotaSelection == 1:
                        # Create the Lakota
                        Lak = "USS_Lakota"
                        pLak = loadspacehelper.CreateShip(DS9FXShips.Lakota, DS9Set, Lak, "Lakota Location")
                        
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Lak)
                        pMission.GetFriendlyGroup().AddName(Lak)

                        import Custom.DS9FX.DS9FXAILib.DS9FXLakotaAI

                        Lakota = MissionLib.GetShip("USS_Lakota", DS9Set)

                        pLakota = App.ShipClass_Cast(Lakota)

                        pLakota.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXLakotaAI.CreateAI(pLakota))

        else:
            
                if DS9FXSavedConfig.ExcaliburSelection == 1:
                        # Create the Excalibur
                        Excal = "USS Excalibur"
                        pExcal = loadspacehelper.CreateShip(DS9FXShips.Excalibur, DS9Set, Excal, "Excal Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Excal)
                        pMission.GetEnemyGroup().AddName(Excal)

                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyExcalAI

                        Excalibur = MissionLib.GetShip("USS Excalibur", DS9Set) 

                        pExcalibur = App.ShipClass_Cast(Excalibur)

                        pExcalibur.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyExcalAI.CreateAI(pExcalibur))

                if DS9FXSavedConfig.DefiantSelection == 1:
                        # Create the Defiant
                        Def = "USS Defiant"
                        pDef = loadspacehelper.CreateShip(DS9FXShips.Defiant, DS9Set, Def, "Defiant Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Def)
                        pMission.GetEnemyGroup().AddName(Def)

                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyDefiantAI

                        Defiant = MissionLib.GetShip("USS Defiant", DS9Set)

                        pDefiant = App.ShipClass_Cast(Defiant)

                        pDefiant.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyDefiantAI.CreateAI(pDefiant))

                if DS9FXSavedConfig.OregonSelection == 1:
                        # Create the Oregon
                        Oreg = "USS Oregon"
                        pOreg = loadspacehelper.CreateShip(DS9FXShips.Miranda, DS9Set, Oreg, "Oregon Location")
                    
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Oreg)
                        pMission.GetEnemyGroup().AddName(Oreg)
            
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyOregonAI

                        Oregon = MissionLib.GetShip("USS Oregon", DS9Set)

                        pOregon = App.ShipClass_Cast(Oregon)

                        pOregon.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyOregonAI.CreateAI(pOregon))

                if DS9FXSavedConfig.LakotaSelection == 1:
                        # Create the Lakota
                        Lak = "USS_Lakota"
                        pLak = loadspacehelper.CreateShip(DS9FXShips.Lakota, DS9Set, Lak, "Lakota Location")
                                                
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Lak)
                        pMission.GetEnemyGroup().AddName(Lak)
                      
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyLakotaAI

                        Lakota = MissionLib.GetShip("USS_Lakota", DS9Set)

                        pLakota = App.ShipClass_Cast(Lakota)

                        pLakota.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyLakotaAI.CreateAI(pLakota))
