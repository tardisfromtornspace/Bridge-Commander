import Foundation
import App

mode = Foundation.MutatorDef("Sneaker98's MVAM Infinite")
Foundation.OverrideDef.SneakerCoreMenuAdd = Foundation.OverrideDef("SneakerMenuAdd", "Bridge.XOMenuHandlers.CreateMenus", "Custom.Sneaker.Mvam.SneakerMenuAdd.SneakerCreateMenus", dict = { "modes": [ mode ] } )
Foundation.OverrideDef.SneakerMissionLib = Foundation.OverrideDef("SneakerMissionLib", "MissionLib.CreatePlayerShip", "Custom.Sneaker.Mvam.Mvam_Lib.CreatePlayerShip", dict = { "modes": [ mode ] } )
Foundation.OverrideDef.SneakerMissionLib = Foundation.OverrideDef("SneakerQuickbattle", "QuickBattle.QuickBattle.StartSimulation2", "Custom.Sneaker.Mvam.Mvam_Lib.SneakerStartSimulation2", dict = { "modes": [ mode ] } )