from bcdebug import debug
import App
import Custom.QBautostart.Libs.LibEngineering
import MissionLib
import Foundation
import addship
import string
import nt

MODINFO = {     "Author": "\"Defiant\" erik@vontaene.de",
                "Download": "http://defiant.homedns.org/~erik/STBC/addship/",
                "Version": "0.4.1",
                "License": "BSD",
                "Description": "Add extra Ships to BC",
                "needBridge": 0
            }

verbose = 0

SHIPS_WINDOW_X_POS			= 0.0925
SHIPS_WINDOW_Y_POS			= 0.1
SHIPS_WINDOW_WIDTH			= 0.25
SHIPS_WINDOW_HEIGHT			= 1.0
SHIPS_WINDOW_BAR_THICKNESS		= 0.0291667
SHIPS_SUBPANE_WIDTH			= 0.22
ADD_FRIEND_BUTTON_X_POS			= 0.250025
ADD_FRIEND_BUTTON_Y_POS			= 0.52
ADD_FRIEND_BUTTON_WIDTH			= 0.2515625
ADD_FRIEND_BUTTON_HEIGHT		= 0.0354167
ADD_ENEMY_BUTTON_X_POS			= 0.250025
ADD_ENEMY_BUTTON_Y_POS			= 0.56
ADD_ENEMY_BUTTON_WIDTH			= 0.2515625
ADD_ENEMY_BUTTON_HEIGHT			= 0.0354167
ADD_NEUTRAL_BUTTON_X_POS		= 0.250025
ADD_NEUTRAL_BUTTON_Y_POS		= 0.60
ADD_NEUTRAL_BUTTON_WIDTH		= 0.2515625
ADD_NEUTRAL_BUTTON_HEIGHT		= 0.0354167
DEL_BUTTON_X_POS			= 0.250025
DEL_BUTTON_Y_POS			= 0.64
DEL_BUTTON_WIDTH			= 0.2515625
DEL_BUTTON_HEIGHT			= 0.0354167
FRIEND_LIST_X_POS			= 0.5390625
FRIEND_LIST_Y_POS			= 0.0083333
ENEMY_LIST_X_POS			= 0.5390625
ENEMY_LIST_Y_POS			= 0.5020835
NEUTRAL_LIST_X_POS			= 0.5390625
NEUTRAL_LIST_Y_POS			= 1.0
CLOSE_X_POS                             = 0.3
CLOSE_Y_POS                             = 0
START_X_POS                             = 0.3
START_Y_POS                             = 0.05
RACE_NAME_BUTTON_X_POS                  = 0.24
RACE_NAME_BUTTON_Y_POS                  = 0.48
ET_SELECT_SHIP_TYPE                     = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_ADD_AS_FRIEND                        = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_ADD_AS_ENEMY                         = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_ADD_AS_NEUTRAL                       = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_DELETE                               = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_SHIP_IN_FRIENDLY_MENU         = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_SHIP_IN_ENEMY_MENU            = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_SHIP_IN_NEUTRAL_MENU          = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_CLOSE                                = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_START                                = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
ET_USE_NAMES                            = Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType()
SelectedSpecies                         = 0
pAddShipsWindow                         = None
g_pAddFriendButton                      = None
g_pAddEnemyButton                       = None
g_pAddNeutralButton                       = None
ships_list                              = {}
groupEnemy                              = {}
groupFriendly                           = {}
groupNeutral                            = {}
FriendlyButton                          = None
EnemyButton                             = None
NeutralButton                           = None
curShipInMenu                           = None
curMenuInMenu                           = None
useNames                                = 0

NonSerializedObjects = (
"pAddShipsWindow",
)

def Delete(pObject, pEvent):
    debug(__name__ + ", Delete")
    global curMenuInMenu, curShipInMenu, groupFriendly, groupEnemy, groupNeutral
    if (curMenuInMenu == "enemy"):
        i = -1
        check_i = 0
        while check_i < len(groupEnemy.keys()):
            i = i + 1
            if not groupEnemy.has_key(i):
                continue
            check_i = check_i + 1
            if (groupEnemy[i] == curShipInMenu):
                del groupEnemy[i]
                RebuildEnemyMenu()
                break
    elif (curMenuInMenu == "friendly"):
        i = -1
        check_i = 0
        while check_i < len(groupFriendly.keys()):
            i = i + 1
            if not groupFriendly.has_key(i):
                continue
            check_i = check_i + 1
            if (groupFriendly[i] == curShipInMenu):
                del groupFriendly[i]
                RebuildFriendlyMenu()
                break
    elif (curMenuInMenu == "neutral"):
        i = -1
        check_i = 0
        while check_i < len(groupNeutral.keys()):
            i = i + 1
            if not groupNeutral.has_key(i):
                continue
            check_i = check_i + 1
            if (groupNeutral[i] == curShipInMenu):
                del groupNeutral[i]
                RebuildNeutralMenu()
                break


def ShipInEnemyMenuSelect(pObject, pEvent):
    debug(__name__ + ", ShipInEnemyMenuSelect")
    global curMenuInMenu, curShipInMenu
    curMenuInMenu = "enemy"
    curShipInMenu = pEvent.GetInt()
    

def ShipInFriendlyMenuSelect(pObject, pEvent):
    debug(__name__ + ", ShipInFriendlyMenuSelect")
    global curMenuInMenu, curShipInMenu
    curMenuInMenu = "friendly"
    curShipInMenu = pEvent.GetInt()


def ShipInNeutralMenuSelect(pObject, pEvent):
    debug(__name__ + ", ShipInNeutralMenuSelect")
    global curMenuInMenu, curShipInMenu
    curMenuInMenu = "neutral"
    curShipInMenu = pEvent.GetInt()
    

def RebuildEnemyMenu():
    debug(__name__ + ", RebuildEnemyMenu")
    global groupEnemy, pAddShipsWindow, ships_list, EnemyButton

    EnemyButton.KillChildren()
    i = -1
    check_i = 0
    while check_i < len(groupEnemy.keys()):
        i = i + 1
        if not groupEnemy.has_key(i):
            continue
        check_i = check_i + 1
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_SELECT_SHIP_IN_ENEMY_MENU)
        pEvent.SetInt(groupEnemy[i])
        pEvent.SetDestination(pAddShipsWindow)
                
        Ship = ships_list[groupEnemy[i]][1]
        pButton = App.STButton_CreateW(App.TGString(Ship), pEvent)
        EnemyButton.AddChild(pButton)

    # resize Window
    EnemyButton.Open()


def RebuildFriendlyMenu():
    debug(__name__ + ", RebuildFriendlyMenu")
    global groupFriendly, pAddShipsWindow, ships_list, FriendlyButton

    FriendlyButton.KillChildren()
    i = -1
    check_i = 0
    while check_i < len(groupFriendly.keys()):
        i = i + 1
        if not groupFriendly.has_key(i):
            continue
        check_i = check_i + 1
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_SELECT_SHIP_IN_FRIENDLY_MENU)
        pEvent.SetInt(groupFriendly[i])
        pEvent.SetDestination(pAddShipsWindow)
                
        Ship = ships_list[groupFriendly[i]][1]
        pButton = App.STButton_CreateW(App.TGString(Ship), pEvent)
        FriendlyButton.AddChild(pButton)

    # resize Window
    FriendlyButton.Open()
    

def RebuildNeutralMenu():
    debug(__name__ + ", RebuildNeutralMenu")
    global groupNeutral, pAddShipsWindow, ships_list, NeutralButton

    NeutralButton.KillChildren()
    i = -1
    check_i = 0
    while check_i < len(groupNeutral.keys()):
        i = i + 1
        if not groupNeutral.has_key(i):
            continue
        check_i = check_i + 1
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_SELECT_SHIP_IN_NEUTRAL_MENU)
        pEvent.SetInt(groupNeutral[i])
        pEvent.SetDestination(pAddShipsWindow)
                
        Ship = ships_list[groupNeutral[i]][1]
        pButton = App.STButton_CreateW(App.TGString(Ship), pEvent)
        NeutralButton.AddChild(pButton)

    # resize Window
    NeutralButton.Open()
    

def AddShipAsEnemy(pObject, pEvent):
        debug(__name__ + ", AddShipAsEnemy")
        global SelectedSpecies, groupEnemy
        groupNew = {}
        iNew = 0

        # sort
        keylist = groupEnemy.keys()
        keylist.sort()
        for i in keylist:
                groupNew[iNew] = groupEnemy[i]
                iNew = iNew + 1
        
        groupEnemy = groupNew
        groupEnemy[len(groupEnemy.keys())] = SelectedSpecies
        RebuildEnemyMenu()


def AddShipAsFriend(pObject, pEvent):
        debug(__name__ + ", AddShipAsFriend")
        global SelectedSpecies, groupFriendly
        groupNew = {}
        iNew = 0
        
        # sort
        keylist = groupFriendly.keys()
        keylist.sort()
        for i in keylist:
                groupNew[iNew] = groupFriendly[i]
                iNew = iNew + 1
        
        groupFriendly = groupNew
        groupFriendly[len(groupFriendly.keys())] = SelectedSpecies
        RebuildFriendlyMenu()


def AddShipAsNeutral(pObject, pEvent):
        debug(__name__ + ", AddShipAsNeutral")
        global SelectedSpecies, groupNeutral
        groupNew = {}
        iNew = 0
        
        # sort
        keylist = groupNeutral.keys()
        keylist.sort()
        for i in keylist:
                groupNew[iNew] = groupNeutral[i]
                iNew = iNew + 1
        
        groupNeutral = groupNew
        groupNeutral[len(groupNeutral.keys())] = SelectedSpecies
        RebuildNeutralMenu()


def GenerateFriendMenu():
	debug(__name__ + ", GenerateFriendMenu")
	global pAddShipsWindow, FriendlyButton
        
        FriendlyButton = App.STCharacterMenu_Create("Friendly")
	pAddShipsWindow.AddChild(FriendlyButton, FRIEND_LIST_X_POS, FRIEND_LIST_Y_POS)


def GenerateEnemyMenu():
	debug(__name__ + ", GenerateEnemyMenu")
	global pAddShipsWindow, EnemyButton

        EnemyButton = App.STCharacterMenu_Create("Enemy")
        pAddShipsWindow.AddChild(EnemyButton, ENEMY_LIST_X_POS, ENEMY_LIST_Y_POS)


def GenerateNeutralMenu():
	debug(__name__ + ", GenerateNeutralMenu")
	global pAddShipsWindow, NeutralButton
        
        NeutralButton = App.STCharacterMenu_Create("Neutral")
	pAddShipsWindow.AddChild(NeutralButton, NEUTRAL_LIST_X_POS, NEUTRAL_LIST_Y_POS)


def SelectShipType(pObject, pEvent):
        debug(__name__ + ", SelectShipType")
        global g_pAddFriendButton, g_pAddEnemyButton, g_pAddNeutralButton, SelectedSpecies
        
        # Now we have a ship so we can enable these Buttons:
        g_pAddFriendButton.SetEnabled()
        g_pAddEnemyButton.SetEnabled()
        g_pAddNeutralButton.SetEnabled()

	SelectedSpecies = pEvent.GetInt()

	pObject.CallNextHandler(pEvent)


def isMvamChild(mvamships, ShipFile):
        debug(__name__ + ", isMvamChild")
        for key in mvamships.keys():
                for plugin in mvamships[key]:
                        if plugin == ShipFile:
                                return key
        return None
        

def BuildShipSelectWindow():
        debug(__name__ + ", BuildShipSelectWindow")
        global pAddShipsWindow, ships_list

        pSubPane = App.STSubPane_Create(SHIPS_SUBPANE_WIDTH, 500.0, 0)
        
        # Create the buttons
        dict_sides = {}
	mvamships = {}
	mvambuttons = {}
        FdtnShips = Foundation.shipList
        if not FdtnShips:
                return
        
        # try to get all mvam ships
        try:
                list = nt.listdir("scripts/Custom/Autoload/Mvam/")
                list.sort()
                for plugin in list:
                        s = string.split(plugin, '.')
                        extension = s[-1]
                        fileName = string.join(s[:-1], '.')
                        MVAMMaster = ""
                        MVAMchilds = []
                
                        if extension != "pyc" or fileName == "__init__":
                                continue
                        
                        modul = __import__("Custom.Autoload.Mvam." + fileName)
                        MVAMMaster = modul.MvamShips[0]
                        MVAMchilds = modul.MvamShips[1:]
                        mvamships[MVAMMaster] = MVAMchilds
        except:
		print("AddShipGUI Ship Select window problem")
        
        for iIndex in range(len(FdtnShips)):
                SubMenu = None
                Ship = FdtnShips[iIndex]
                ShipLongName = Ship.name
                mvSpecies = Ship.MenuGroup()
                # check for submenu attribute
                if hasattr(Ship, "SubMenu"):
                        # is it a string?
                        if type(Ship.SubMenu) == type(""):
                                # make a list
                                SubMenu = []
                                SubMenu.append(Ship.SubMenu)
                        # or already a list?
                        elif type(Ship.SubMenu) == type([]):
                                SubMenu = Ship.SubMenu
                if not mvSpecies:
			if verbose:
				print "AddShipGUI Warning: No menu group for %s" % str(ShipLongName)
                        continue
                ships_list[iIndex] = Ship.GetShipFile(), ShipLongName
                # Setup the event for when this button is clicked
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_SELECT_SHIP_TYPE)
                pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
                pEvent.SetDestination(pAddShipsWindow)
                
                # if its an mvam ship, add it to the list
                if mvamships.has_key(Ship.GetShipFile()):
                        pButton = App.STCharacterMenu_CreateW(App.TGString(ShipLongName))
                        pButton.SetActivationEvent(pEvent)
                        dict_sides[Ship.GetShipFile()] = pButton
                else:
                        # Create the button.
                        pButton = App.STButton_CreateW(App.TGString(ShipLongName), pEvent)
                        
                pEvent.SetSource(pButton)
                
                if not dict_sides.has_key(mvSpecies):
                        dict_sides[mvSpecies] = App.STCharacterMenu_Create(mvSpecies)
                        pSubPane.AddChild(dict_sides[mvSpecies], 0, 0, 0)
                        
                if not SubMenu:
                        # do not add mvam childs yet
                        mvamMaster = isMvamChild(mvamships, Ship.GetShipFile())
                        if mvamMaster:
                                if not mvambuttons.has_key(mvamMaster):
                                        mvambuttons[mvamMaster] = []
                                mvambuttons[mvamMaster].append(pButton)
                        else:
                                # add to race menu
                                dict_sides[mvSpecies].AddChild(pButton, 0, 0, 0)
                # add to the submenu
                else:
                        LastSubMenu = mvSpecies
                        # cycle as long as the length of the list is > 0 and is still a list
                        while(len(SubMenu) > 0 and type(SubMenu) == type([])):
				sSubmenuKey = mvSpecies + SubMenu[0]
                                if not dict_sides.has_key(sSubmenuKey):
                                        dict_sides[sSubmenuKey] = App.STCharacterMenu_Create(SubMenu[0])
                                        dict_sides[LastSubMenu].AddChild(dict_sides[sSubmenuKey], 0, 0, 0)
                                # the rest list
                                LastSubMenu = sSubmenuKey
                                SubMenu = SubMenu[1:]
                        # finally add the ship to the right submenu
                        dict_sides[LastSubMenu].AddChild(pButton, 0, 0, 0)
                        
        # finally add the mvam submenus
        for key in mvambuttons.keys():
                for pButton in mvambuttons[key]:
			if dict_sides.has_key(key):
				dict_sides[key].AddChild(pButton, 0, 0, 0)
                
        pSubPane.Layout()
        pAddShipsWindow.AddChild(pSubPane)


def CreateWindowInterieur():
        debug(__name__ + ", CreateWindowInterieur")
        global pAddShipsWindow, g_pAddFriendButton, g_pAddEnemyButton, g_pAddNeutralButton
        
        BuildShipSelectWindow()

	pEventAddAsFriendButton = App.TGEvent_Create()
	pEventAddAsFriendButton.SetEventType(ET_ADD_AS_FRIEND)
	pEventAddAsFriendButton.SetDestination(pAddShipsWindow)
	
	pEventAddAsEnemyButton = App.TGEvent_Create()
	pEventAddAsEnemyButton.SetEventType(ET_ADD_AS_ENEMY)
	pEventAddAsEnemyButton.SetDestination(pAddShipsWindow)

	pEventAddAsNeutralButton = App.TGEvent_Create()
	pEventAddAsNeutralButton.SetEventType(ET_ADD_AS_NEUTRAL)
	pEventAddAsNeutralButton.SetDestination(pAddShipsWindow)
	
	pEventDelete = App.TGEvent_Create()
	pEventDelete.SetEventType(ET_DELETE)
	pEventDelete.SetDestination(pAddShipsWindow)
        
        pEventRaceNames = App.TGEvent_Create()
	pEventRaceNames.SetEventType(ET_USE_NAMES)
	pEventRaceNames.SetDestination(pAddShipsWindow)

        # Create a button to add the currently selected ship to the list of friendlies
        g_pAddFriendButton = App.STRoundedButton_CreateW(App.TGString("Add as friend"), pEventAddAsFriendButton, ADD_FRIEND_BUTTON_WIDTH, ADD_FRIEND_BUTTON_HEIGHT, 1)
        g_pAddFriendButton.SetDisabled() # So that you can't add a ship 'til one has been selected
        g_pAddFriendButton.SetNormalColor(App.g_kMainMenuButtonColor)
        g_pAddFriendButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
        g_pAddFriendButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
        g_pAddFriendButton.SetColorBasedOnFlags()
        pAddShipsWindow.AddChild(g_pAddFriendButton, ADD_FRIEND_BUTTON_X_POS, ADD_FRIEND_BUTTON_Y_POS)


	# Create a button to add the currently selected ship to the list of enemies
	g_pAddEnemyButton = App.STRoundedButton_CreateW(App.TGString("Add as enemy"), pEventAddAsEnemyButton, ADD_ENEMY_BUTTON_WIDTH, ADD_ENEMY_BUTTON_HEIGHT, 1)
	g_pAddEnemyButton.SetDisabled() # So that you can't add a ship 'til one has been selected
	g_pAddEnemyButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pAddEnemyButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pAddEnemyButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pAddEnemyButton.SetColorBasedOnFlags()
	pAddShipsWindow.AddChild(g_pAddEnemyButton, ADD_ENEMY_BUTTON_X_POS, ADD_ENEMY_BUTTON_Y_POS)

	g_pAddNeutralButton = App.STRoundedButton_CreateW(App.TGString("Add as neutral"), pEventAddAsNeutralButton, ADD_NEUTRAL_BUTTON_WIDTH, ADD_NEUTRAL_BUTTON_HEIGHT, 1)
	g_pAddNeutralButton.SetDisabled() # So that you can't add a ship 'til one has been selected
	g_pAddNeutralButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pAddNeutralButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pAddNeutralButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pAddNeutralButton.SetColorBasedOnFlags()
	pAddShipsWindow.AddChild(g_pAddNeutralButton, ADD_NEUTRAL_BUTTON_X_POS, ADD_NEUTRAL_BUTTON_Y_POS)

	g_pDeleteButton = App.STRoundedButton_CreateW(App.TGString("Delete"), pEventDelete, DEL_BUTTON_WIDTH, DEL_BUTTON_HEIGHT, 1)
	g_pDeleteButton.SetNormalColor(App.g_kQuickBattleBrightRed)
	pAddShipsWindow.AddChild(g_pDeleteButton, DEL_BUTTON_X_POS, DEL_BUTTON_Y_POS)

        pNamePane = App.TGPane_Create(0.12, 0.3)
        pAddShipsWindow.AddChild(pNamePane, RACE_NAME_BUTTON_X_POS, RACE_NAME_BUTTON_Y_POS)
	pNameButton = App.STButton_CreateW(App.TGString("use names"), pEventRaceNames)
        pEventRaceNames.SetSource(pNameButton)
        pNameButton.SetChoosable(1)
        pNameButton.SetAutoChoose(1)
        pNameButton.SetChosen(0)
        pNamePane.AddChild(pNameButton)

        GenerateFriendMenu()
        GenerateEnemyMenu()
        GenerateNeutralMenu()
        
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetDestination(pAddShipsWindow)
        pEvent.SetInt(0)
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
        pAddShipsWindow.AddChild(pButton, CLOSE_X_POS, CLOSE_Y_POS, 0)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_START)
        pEvent.SetDestination(pAddShipsWindow)
        pEvent.SetInt(0)
        pButton = App.STRoundedButton_CreateW(App.TGString("Start"), pEvent, 0.13125, 0.034583)
        pAddShipsWindow.AddChild(pButton, START_X_POS, START_Y_POS, 0)


def AddShips(pObject, pEvent):
        debug(__name__ + ", AddShips")
        global pAddShipsWindow
        if not pAddShipsWindow:
                # Don't why it hasn't been created. Try to create it
                CreateAddShipsWindow()
                # It does still not exist?
                if not pAddShipsWindow:
                        return
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        if pAddShipsWindow.IsVisible():
                pTacticalControlWindow.MoveToBack(pAddShipsWindow)
                pAddShipsWindow.SetNotVisible()
        else:
                pAddShipsWindow.SetVisible()
                pAddShipsWindow.ScrollToTop()
                pTacticalControlWindow.MoveToFront(pAddShipsWindow)
                # Not so agressiv to the front - only give us problems!
                pTacticalControlWindow.MoveTowardsBack(pAddShipsWindow)
                
        
# handle mouse clicks in empty space
def PassMouse(pWindow, pEvent):
        debug(__name__ + ", PassMouse")
        pWindow.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()


def GetRandomNameFor(sShipType):
        debug(__name__ + ", GetRandomNameFor")
	try:
		from Custom.QBautostart.Libs.Races import Races
		FdtnShip = Foundation.shipList[sShipType]
		if FdtnShip.GetRace() and Races.has_key(FdtnShip.GetRace().name):
			ShipRace = FdtnShip.GetRace().name
			return Races[ShipRace].GetRandomName()
	except:
		pass
	return None


def addshiphelper(pObject, pEvent):
        debug(__name__ + ", addshiphelper")
        global ships_list, groupFriendly, groupEnemy, groupNeutral
        for i in groupFriendly.keys():
                ship = ships_list[groupFriendly[i]][0]
                #print("add friendly: %s") % (ship)
                if useNames:
                        sShipName = GetRandomNameFor(ship)
                        addship.friendly(ship, Name = sShipName)
                else:
                        addship.friendly(ship)
        for i in groupEnemy.keys():
                ship = ships_list[groupEnemy[i]][0]
                #print("add enemy: %s") % (ship)
                if useNames:
                        sShipName = GetRandomNameFor(ship)
                        addship.enemy(ship, Name = sShipName)
                else:
                        addship.enemy(ship)
        for i in groupNeutral.keys():
                ship = ships_list[groupNeutral[i]][0]
                #print("add neutral: %s") % (ship)
                if useNames:
                        sShipName = GetRandomNameFor(ship)
                        addship.neutral(ship, Name = sShipName)
                else:
                        addship.neutral(ship)
        groupFriendly = {}
        groupEnemy = {}
        groupNeutral = {}
        RebuildEnemyMenu()
        RebuildFriendlyMenu()
        RebuildNeutralMenu()
        AddShips(pObject, pEvent)


def SetuseNames(pObject, pEvent):
        debug(__name__ + ", SetuseNames")
        global useNames
        pButton = App.STButton_Cast(pEvent.GetSource ())
        if pButton:
                useNames = pButton.IsChosen()


def CreateAddShipsWindow(pObject=None, pEvent=None):
        debug(__name__ + ", CreateAddShipsWindow")
        global pAddShipsWindow
        
        # test if it doesn't already exist
        if pAddShipsWindow:
                return
        
        # Create the Engineering extra Window:
        pAddShipsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Add ships Window"), 0.0, 0.0, None, 1, 0.8, 0.8, App.g_kMainMenuBorderMainColor)
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pTacticalControlWindow.AddChild(pAddShipsWindow, 0.1, 0.1)

        pAddShipsWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".PassMouse")
        pAddShipsWindow.SetNotVisible()
        
        CreateWindowInterieur()

        pBridge = App.g_kSetManager.GetSet("bridge")
        if pBridge:
                g_pXO = App.CharacterClass_GetObject(pBridge, "XO")
                g_pXO.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".WindowClose")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_TYPE, __name__ + ".SelectShipType")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_ADD_AS_ENEMY, __name__ + ".AddShipAsEnemy")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_ADD_AS_FRIEND, __name__ + ".AddShipAsFriend")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_ADD_AS_NEUTRAL, __name__ + ".AddShipAsNeutral")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_DELETE, __name__ + ".Delete")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_IN_FRIENDLY_MENU, __name__ + ".ShipInFriendlyMenuSelect")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_IN_ENEMY_MENU, __name__ + ".ShipInEnemyMenuSelect")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_IN_NEUTRAL_MENU, __name__ + ".ShipInNeutralMenuSelect")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".AddShips")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_START, __name__ + ".addshiphelper")
        pAddShipsWindow.AddPythonFuncHandlerForInstance(ET_USE_NAMES, __name__ + ".SetuseNames")
        
        
def WindowClose(pObject, pEvent):
        debug(__name__ + ", WindowClose")
        global pAddShipsWindow

        if not pAddShipsWindow:
                return

        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        if pAddShipsWindow.IsVisible():
                pTacticalControlWindow.MoveToBack(pAddShipsWindow)
                pAddShipsWindow.SetNotVisible()

        pObject.CallNextHandler(pEvent)
        

def init():
        debug(__name__ + ", init")
        if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return
	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
        Custom.QBautostart.Libs.LibEngineering.CreateMenuButton("Add ships", "XO", __name__ + ".AddShips")
        MissionLib.CreateTimer(Custom.QBautostart.Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CreateAddShipsWindow", App.g_kUtopiaModule.GetGameTime() + 2.0, 0, 0)


def exit():
        debug(__name__ + ", exit")
        global pAddShipsWindow
        if pAddShipsWindow:
                pAddShipsWindow.KillChildren()
                pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
                pTacticalControlWindow.DeleteChild(pAddShipsWindow)
	pAddShipsWindow = None

