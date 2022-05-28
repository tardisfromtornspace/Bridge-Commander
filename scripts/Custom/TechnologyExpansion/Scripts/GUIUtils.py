# GUIUtils
#
# by Evan Light aka sleight42
# All Rights Reserved
#
# <rant-mode>
# Man, I can't tell you just how much I hate learning new windowing toolkits!
# Who the fuck wants to learn fifty different ways of painting a window or
# button on-screen.  Just give me one clean API that I could use everywhere
# and I'd be OK with that.  But, no, nearly every damn developer out there
# has to write a new fucking windowing toolkit with a different API from
# every other windowing toolkit out there.  Just how many times do we have
# to reinvent this damn wheel???
# </rant-mode>
# 
# That's why I wrote this stupid module.  I'm going to forget everything that
# I ever learned about this windowing toolkit in short order.  As such, this
# module is going to become an aggregate of every little thing that I need
# to write more than once to muck around in the BC GUI.
#############################################################################

import App

def FindLowestChild( pane):
    index = pane.GetNumChildren() - 1
    iBottom = 0
    lowestChild = None
    current = None
    while index >= 0:
        current = pane.GetNthChild( index)
        currentBottom = current.GetBottom()
        if( currentBottom > iBottom):
            iBottom = currentBottom
            lowestChild = current
        index = index - 1
    return lowestChild

def GetScienceMenu():
    pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
    if(pDatabase is None):
        return 0
    return pTactCtrlWindow.FindMenu(pDatabase.GetString("Science"))

def FindButtonPosInMenu( menu, button):
    retval = 0
    currentButton = menu.GetFirstChild()
    while( currentButton != None):
        castButton = App.STButton_Cast( currentButton)
        if( castButton != None and castButton.this == button.this):
            break
        retval = retval + 1
        currentButton = menu.GetNextChild( currentButton)
    if( currentButton == None):
        retval = -1
    return retval

def GetNumChildrenThatCastTo( pane, cast):
    retval = 0
    current = pane.GetFirstChild()
    while( current != None):
        castVal = cast( current)
        if( castVal != None):
            retval = retval + 1
        current = pane.GetNextChild( current)
    return retval
    
def CreateIntButton( name, eventType, eventDest, intVal, tglDatabase = None):
    button = None
    event = App.TGIntEvent_Create()
    event.SetEventType( eventType)
    event.SetInt( intVal)
    event.SetDestination( eventDest)

    if( tglDatabase == None):
        button = App.STButton_Create( name, event)
    else:
        button = App.STButton_CreateW( tglDatabase.GetString( name), event)

    return button 
