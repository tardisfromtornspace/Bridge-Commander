"""In quickbattle there are 2 small bugs: 1st it doesn't register Foundation.ShipDef.MyShip.hasTGLDesc
defs properly and the 2nd one is that actually ships descriptions are sent to the wrong pane so when a user
selects that pane he cannot see the desc of ships which have string descriptions instead of tgl inputs

by USS Sovereign"""

import App
import Foundation
# import SovDebug

# 1 to turn on, 0 to turn off
bEnabled = 1

# Any foundation version will do..., that's the oldest version signature... I think...
if int(Foundation.version[0:8]) >= 20030222:
	print "Repairing ship description outputs..."

        def SelectPlayerShip(pObject, pEvent):

            import QuickBattle.QuickBattle
            # I keep forgeting: import * as doesn't work in BC's python version (too old)
            QB = QuickBattle.QuickBattle

            # Grab values
            g_sPlayerType = QB.g_sPlayerType
            g_pPlayerIcon = QB.g_pPlayerIcon
            g_pPlayerIconPane = QB.g_pPlayerIconPane
            g_pPlayerText = QB.g_pPlayerText
            g_pShipsDatabase = QB.g_pShipsDatabase
            g_pPlayerTextWindow = QB.g_pPlayerTextWindow
            
            # Specify our new ship
            global g_sPlayerType            
            g_sPlayerType = Foundation.shipList[pEvent.GetInt()]
     
            # Change the icon to reflect the selection 
            iIconNumber = Foundation.shipList[pEvent.GetInt()].GetIconNum() 
            QB.UpdateIcon(iIconNumber, g_pPlayerIcon, g_pPlayerIconPane) 
     
            # Go to the small font 
            import MainMenu.mainmenu 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes]) 
     
            # Update the text to reflect this 
            if g_pShipsDatabase.HasString(g_sPlayerType.abbrev + " Description") and hasattr(g_sPlayerType, "hasTGLDesc"):
                if g_sPlayerType.hasTGLDesc == 1:
                    g_pPlayerText.SetStringW(g_pShipsDatabase.GetString(g_sPlayerType.abbrev + " Description"))

                else: 
                    g_pPlayerText.SetString(g_sPlayerType.desc)

            else: 
                    g_pPlayerText.SetString(g_sPlayerType.desc)
     
            g_pPlayerTextWindow.InteriorChangedSize () 
            g_pPlayerTextWindow.ScrollToTop () 
            g_pPlayerTextWindow.Layout () 
     
            # Go back to the large font 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

            # Update taken QB values
            QB.g_sPlayerType = g_sPlayerType
            QB.g_pPlayerIcon = g_pPlayerIcon
            QB.g_pPlayerIconPane = g_pPlayerIconPane
            QB.g_pPlayerText = g_pPlayerText
            QB.g_pShipsDatabase = g_pShipsDatabase
            QB.g_pPlayerTextWindow = g_pPlayerTextWindow
     
            if pObject != None: 
                    pObject.CallNextHandler(pEvent)

        def SelectShipType(pObject, pEvent):

            import QuickBattle.QuickBattle
            QB = QuickBattle.QuickBattle

            # Grab values
            g_iSelectedShipType = QB.g_iSelectedShipType
            g_pShipsIcon = QB.g_pShipsIcon
            g_pShipsIconPane = QB.g_pShipsIconPane
            g_pShipsDatabase = QB.g_pShipsDatabase
            g_pShipsTextWindow = QB.g_pShipsTextWindow
            g_iSelectedAILevel = QB.g_iSelectedAILevel
            g_pAddEnemyButton = QB.g_pAddEnemyButton
            g_pAddFriendButton = QB.g_pAddFriendButton
            g_pAIMenu = QB.g_pAIMenu
            g_pFriendToEnemyButton = QB.g_pFriendToEnemyButton   
            g_pEnemyToFriendButton = QB.g_pEnemyToFriendButton
            g_pDeleteButton = QB.g_pDeleteButton
            g_pPane = QB.g_pPane
            g_pFriendWindow = QB.g_pFriendWindow
            g_pEnemyWindow = QB.g_pEnemyWindow
            g_kFriendList = QB.g_kFriendList
            g_kEnemyList = QB.g_kEnemyList
            g_pShipsText = QB.g_pShipsText
            
            # Update the appropriate global value
            global g_iSelectedShipType 
            g_iSelectedShipType   = pEvent.GetInt() 
     
            # We must update the Ship Icon with the image of the currently selected ship 
            # Get the icon number from dictionary with help from the event's int 
            iIconNumber = Foundation.shipList[pEvent.GetInt()].GetIconNum() 
            QB.UpdateIcon(iIconNumber, g_pShipsIcon, g_pShipsIconPane) 
     
            # Go to the small font 
            import MainMenu.mainmenu 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes]) 
     
            # Update the text to reflect this      
            ship = Foundation.shipList[pEvent.GetInt()]
            if g_pShipsDatabase.HasString(ship.abbrev + " Description") and hasattr(ship, "hasTGLDesc"):
                if ship.hasTGLDesc == 1:
                    g_pShipsText.SetStringW(g_pShipsDatabase.GetString(ship.abbrev + " Description"))

                else: 
                    g_pShipsText.SetString(ship.desc)

            else: 
                    g_pShipsText.SetString(ship.desc)
     
            g_pShipsTextWindow.InteriorChangedSize () 
            g_pShipsTextWindow.ScrollToTop () 
            g_pShipsTextWindow.Layout () 
     
            # Go back to the large font 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes]) 
     
            # Update the AI Menu to reflect what the ship will be when added 
            QB.SetAI(g_iSelectedAILevel) 
     
            # Now that a ship has been selected, we can enable the buttons that will 
            # add it to our list of friends and enemies and disable the buttons that 
            # shouldn't be operable at the moment 
            g_pAddEnemyButton.SetEnabled() 
            g_pAddFriendButton.SetEnabled() 
            g_pAIMenu.SetVisible() 
            g_pFriendToEnemyButton.SetDisabled() 
            g_pEnemyToFriendButton.SetDisabled() 
            g_pDeleteButton.SetDisabled() 
            g_pPane.Layout() 
     
     
            App.g_kFocusManager.RemoveObjectFromTabOrder(g_pFriendWindow) 
            App.g_kFocusManager.RemoveObjectFromTabOrder(g_pEnemyWindow) 
            App.g_kFocusManager.AddObjectToTabOrder(g_pAddFriendButton) 
            App.g_kFocusManager.AddObjectToTabOrder(g_pAddEnemyButton) 
            App.g_kFocusManager.AddObjectToTabOrder(g_pAIMenu) 
     
            if (len (g_kFriendList) > 0): 
                    App.g_kFocusManager.AddObjectToTabOrder(g_pFriendWindow) 
            if (len (g_kEnemyList) > 0): 
                    App.g_kFocusManager.AddObjectToTabOrder(g_pEnemyWindow)

            # Update QB values
            QB.g_iSelectedShipType = g_iSelectedShipType
            QB.g_pShipsIcon = g_pShipsIcon
            QB.g_pShipsIconPane = g_pShipsIconPane
            QB.g_pShipsDatabase = g_pShipsDatabase
            QB.g_pShipsTextWindow = g_pShipsTextWindow
            QB.g_iSelectedAILevel = g_iSelectedAILevel
            QB.g_pAddEnemyButton = g_pAddEnemyButton
            QB.g_pAddFriendButton = g_pAddFriendButton
            QB.g_pAIMenu = g_pAIMenu
            QB.g_pFriendToEnemyButton = g_pFriendToEnemyButton   
            QB.g_pEnemyToFriendButton = g_pEnemyToFriendButton
            QB.g_pDeleteButton = g_pDeleteButton
            QB.g_pPane = g_pPane
            QB.g_pFriendWindow = g_pFriendWindow
            QB.g_pEnemyWindow = g_pEnemyWindow
            QB.g_kFriendList = g_kFriendList
            QB.g_kEnemyList = g_kEnemyList
            QB.g_pShipsText = g_pShipsText
          
            pObject.CallNextHandler(pEvent)

        def SelectFriend(pObject, pEvent):
            import QuickBattle.QuickBattle
            QB = QuickBattle.QuickBattle

            # Grab values
            g_sSelectedShipSide = QB.g_sSelectedShipSide
            g_iSelectedFriendlyShip = QB.g_iSelectedFriendlyShip
            g_kFriendList = QB.g_kFriendList
            g_pShipsIcon = QB.g_pShipsIcon
            g_pShipsIconPane = QB.g_pShipsIconPane
            g_pShipsDatabase = QB.g_pShipsDatabase
            g_pShipsText = QB.g_pShipsText
            g_pShipsTextWindow = QB.g_pShipsTextWindow
            g_pAddEnemyButton = QB.g_pAddEnemyButton
            g_pAddFriendButton = QB.g_pAddFriendButton
            g_pAIMenu = QB.g_pAIMenu
            g_pFriendToEnemyButton = QB.g_pFriendToEnemyButton
            g_pEnemyToFriendButton = QB.g_pEnemyToFriendButton
            g_pDeleteButton = QB.g_pDeleteButton
 
            global g_sSelectedShipSide 
            g_sSelectedShipSide = "Friend" 
     
            # Update the global number that keeps track of this 
            global g_iSelectedFriendlyShip 
            g_iSelectedFriendlyShip = pEvent.GetInt() 
     
            # Update the Ship Icon to reflect this 
            # Get the icon number from dictionary with help from the event's int 
            iIconNumber = g_kFriendList[pEvent.GetInt()][0].GetIconNum() 
            QB.UpdateIcon(iIconNumber, g_pShipsIcon, g_pShipsIconPane) 
     
            # Go to the small font 
            import MainMenu.mainmenu 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes]) 
     
            # Update the text to reflect this 
            ship = g_kFriendList[pEvent.GetInt()][0] 
            if g_pShipsDatabase.HasString(ship.abbrev + " Description") and hasattr(ship, "hasTGLDesc"):
                if ship.hasTGLDesc == 1:
                    g_pShipsText.SetStringW(g_pShipsDatabase.GetString(ship.abbrev + " Description"))

                else: 
                    g_pShipsText.SetString(ship.desc)

            else: 
                    g_pShipsText.SetString(ship.desc)
     
            g_pShipsTextWindow.InteriorChangedSize () 
            g_pShipsText.Layout()      
     
            # Go back to the large font 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes]) 
     
            # Update the AI Menu to reflect the currently selected ship 
            QB.SetAI(g_kFriendList[pEvent.GetInt()][1]) 
     
            # Enable and disable the appropriate buttons 
            g_pAddEnemyButton.SetDisabled() 
            g_pAddFriendButton.SetDisabled() 
            g_pAIMenu.SetNotVisible() 
            g_pFriendToEnemyButton.SetEnabled() 
            g_pEnemyToFriendButton.SetDisabled() 
            g_pDeleteButton.SetEnabled() 
     
            App.g_kFocusManager.AddObjectToTabOrder(g_pFriendToEnemyButton) 
            App.g_kFocusManager.AddObjectToTabOrder(g_pDeleteButton) 
            App.g_kFocusManager.RemoveObjectFromTabOrder(g_pEnemyToFriendButton)

            # Update QB values
            QB.g_sSelectedShipSide = g_sSelectedShipSide
            QB.g_iSelectedFriendlyShip = g_iSelectedFriendlyShip
            QB.g_kFriendList = g_kFriendList
            QB.g_pShipsIcon = g_pShipsIcon
            QB.g_pShipsIconPane = g_pShipsIconPane
            QB.g_pShipsDatabase = g_pShipsDatabase
            QB.g_pShipsText = g_pShipsText
            QB.g_pShipsTextWindow = g_pShipsTextWindow
            QB.g_pAddEnemyButton = g_pAddEnemyButton
            QB.g_pAddFriendButton = g_pAddFriendButton
            QB.g_pAIMenu = g_pAIMenu
            QB.g_pFriendToEnemyButton = g_pFriendToEnemyButton
            QB.g_pEnemyToFriendButton = g_pEnemyToFriendButton
            QB.g_pDeleteButton = g_pDeleteButton
     
            pObject.CallNextHandler(pEvent) 

        def SelectEnemy(pObject, pEvent): 
            import QuickBattle.QuickBattle
            QB = QuickBattle.QuickBattle

            # Grab values
            g_sSelectedShipSide = QB.g_sSelectedShipSide
            g_iSelectedEnemyShip  = QB.g_iSelectedEnemyShip
            g_kEnemyList = QB.g_kEnemyList
            g_pShipsIcon = QB.g_pShipsIcon
            g_pShipsIconPane = QB.g_pShipsIconPane
            g_pShipsDatabase = QB.g_pShipsDatabase
            g_pShipsText = QB.g_pShipsText
            g_pShipsTextWindow = QB.g_pShipsTextWindow
            g_pAddEnemyButton = QB.g_pAddEnemyButton
            g_pAddFriendButton = QB.g_pAddFriendButton
            g_pAIMenu = QB.g_pAIMenu
            g_pFriendToEnemyButton = QB.g_pFriendToEnemyButton
            g_pEnemyToFriendButton = QB.g_pEnemyToFriendButton
            g_pDeleteButton = QB.g_pDeleteButton
     
            global g_sSelectedShipSide 
            g_sSelectedShipSide = "Enemy" 
     
            # Update the global number that keeps track of this 
            global g_iSelectedEnemyShip 
            g_iSelectedEnemyShip = pEvent.GetInt() 
     
            # Update the Ship Icon to reflect this 
            # Get the icon number from dictionary with help from the event's int 
            iIconNumber = g_kEnemyList[pEvent.GetInt()][0].GetIconNum() 
            QB.UpdateIcon(iIconNumber, g_pShipsIcon, g_pShipsIconPane) 
     
            # Go to the small font 
            import MainMenu.mainmenu 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes]) 
     
            # Update the text to reflect this 
     
            ship = g_kEnemyList[pEvent.GetInt()][0] 
            if g_pShipsDatabase.HasString(ship.abbrev + " Description") and hasattr(ship, "hasTGLDesc"):
                if ship.hasTGLDesc == 1:
                    g_pShipsText.SetStringW(g_pShipsDatabase.GetString(ship.abbrev + " Description"))

                else: 
                    g_pShipsText.SetString(ship.desc)

            else: 
                    g_pShipsText.SetString(ship.desc)
     
            g_pShipsTextWindow.InteriorChangedSize () 
            g_pShipsText.Layout() 
     
            # Go back to the large font 
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes]) 
     
            # Update the AI Menu to reflect the currently selected ship 
            QB.SetAI(g_kEnemyList[pEvent.GetInt()][1]) 
     
            # Enable and disable the appropriate buttons 
            g_pAddEnemyButton.SetDisabled() 
            g_pAddFriendButton.SetDisabled() 
            g_pAIMenu.SetNotVisible() 
            g_pFriendToEnemyButton.SetDisabled() 
            g_pEnemyToFriendButton.SetEnabled() 
            g_pDeleteButton.SetEnabled() 
     
            App.g_kFocusManager.RemoveObjectFromTabOrder(g_pFriendToEnemyButton) 
            App.g_kFocusManager.AddObjectToTabOrder(g_pDeleteButton) 
            App.g_kFocusManager.AddObjectToTabOrder(g_pEnemyToFriendButton)

            # Update QB values
            QB.g_sSelectedShipSide = g_sSelectedShipSide
            QB.g_iSelectedEnemyShip = g_iSelectedEnemyShip
            QB.g_kEnemyList = g_kEnemyList
            QB.g_pShipsIcon = g_pShipsIcon
            QB.g_pShipsIconPane = g_pShipsIconPane
            QB.g_pShipsDatabase = g_pShipsDatabase
            QB.g_pShipsText = g_pShipsText
            QB.g_pShipsTextWindow = g_pShipsTextWindow
            QB.g_pAddEnemyButton = g_pAddEnemyButton
            QB.g_pAddFriendButton = g_pAddFriendButton
            QB.g_pAIMenu = g_pAIMenu
            QB.g_pFriendToEnemyButton = g_pFriendToEnemyButton
            QB.g_pEnemyToFriendButton = g_pEnemyToFriendButton
            QB.g_pDeleteButton = g_pDeleteButton
     
            pObject.CallNextHandler(pEvent) 
	
	class FoundationQBFix:
		def __init__(self):
                        self.bOn = bEnabled
			if self.bOn == 1:
                            self.__funcoverride__()

		def __funcoverride__(self):
                        import QuickBattle.QuickBattle
                        QB = QuickBattle.QuickBattle
			QB.SelectPlayerShip = SelectPlayerShip
                        QB.SelectShipType = SelectShipType
                        QB.SelectFriend = SelectFriend
                        QB.SelectEnemy = SelectEnemy
        
        Foundation.FoundationQBFix = FoundationQBFix()
