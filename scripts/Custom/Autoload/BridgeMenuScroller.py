import Foundation
import App

mode = Foundation.MutatorDef("Sneaker98's Bridge Menu Scroller")
Foundation.OverrideDef.SneakerBridgeMenuScroller = Foundation.OverrideDef("SneakerBridgeMenuScroller", "QuickBattle.QuickBattle.GeneratePlayerBridgeMenu", "Custom.Sneaker.MenuScrollers.GeneratePlayerBridgeMenu", dict = { "modes": [ mode ] } )


BRIDGE_MENU_HEIGHT = 0.384375
BRIDGE_MENU_Y_POS  = 0.4614582
PLAYER_TEXT_HEIGHT = 0.157291663

mode2 = Foundation.MutatorDef("3E's Bridge Menu Enlarger")
Foundation.OverrideDef.BridgeMenuEnlargerHeight = Foundation.OverrideDef("BridgeMenuEnlargerHeight", "QuickBattle.QuickBattle.BRIDGE_MENU_HEIGHT", __name__ + ".BRIDGE_MENU_HEIGHT", dict = {"modes": [mode2]})
Foundation.OverrideDef.BridgeMenuEnlargerY_POS = Foundation.OverrideDef("BridgeMenuEnlargerY_POS", "QuickBattle.QuickBattle.BRIDGE_MENU_Y_POS", __name__ + ".BRIDGE_MENU_Y_POS", dict = {"modes": [mode2]})
Foundation.OverrideDef.BridgeMenuEnlargerOtherHeight = Foundation.OverrideDef("BridgeMenuEnlargerOtherHeight", "QuickBattle.QuickBattle.PLAYER_TEXT_HEIGHT", __name__ + ".PLAYER_TEXT_HEIGHT", dict = {"modes": [mode2]})
