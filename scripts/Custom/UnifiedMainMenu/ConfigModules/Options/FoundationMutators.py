# FoundationMutators
#
# Adapted from Dashers Mutator Screen
# The main menu version I used to base it from was the one by Defiant to have scrolling mutators
#  Though I'm afraid that the scrolling part is no longer needed...
# Originally it was created by Dasher, but he didn't see the day coming
#  that there wasn't enough room on the mutator screen.
#
# Additional features:
#  Menu's for Mutators!
#  Something on my wishlist for a long time.
#
#  A special thing that you can do is that you can create radio button like mutators with it!
#
#  How to use:
#   To assign a mutator to a group you need to know (atleast) the name of the group.
#   Then you do this:
#   
#   mode = Foundation.MutatorDef("Your mutator")
#   # Here it comes:
#   mode.MutatorGroup = "Name of the 'group' mutator"
#
#   This is only half of the way.
#   The other half is to actually create the group.
#   You can do it like this:
#
#   group = Foundation.MutatorGroup("Name of group")
#
#   The code will automaticly check to see if there is already a group present and use that if needed.
#   Though, if you want to check if there is already a group present, you can use the following function:
#
#   Foundation.GetMutatorGroup("Name of group")
#
#   This function will return None if there isn't a group present with that name,
#   or the group mutator itself if there is.


import App
import Foundation

import MainMenu.mainmenu

def GetName():
    return "Mutators"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
    Foundation.LoadConfig()

    for i in Foundation.mutatorList._arrayList:
        mode = Foundation.mutatorList._keyList[i]
        pMenu = pContentPanel
        if mode.__dict__.has_key("MutatorGroup"):
            if str(mode.MutatorGroup)[0] != "[":
                mode.MutatorGroup = [mode.MutatorGroup]
            pMenu = DoSubMenus(mode.MutatorGroup, pMenu)

        if mode.__dict__.get("IsGroup", 0):
            pPosMenu = pMenu.GetSubmenuW(App.TGString(mode.name))
            if pPosMenu:
                continue
            pPosMenu = App.STCharacterMenu_Create(mode.name)
            pMenu.AddChild(pPosMenu)
        else:
            pMenu.AddChild(CreateMutator(mode, pOptionsWindow))
            pMenu.ResizeToContents()
            pMenu.Layout()
        # Sorry Defiant, this is no longer needed... -MLeo
        # Defiant: pOptionsPane => pContentWindow for Scrolling (change 2/2)
        #pOptionsPane.AddChild(pMenuButton)
        #pContentWindow.AddChild(pMenuButton)
    pContentPanel.Layout()
    Foundation.SaveConfig()
    return App.TGPane_Create()


# Changed for non radio button code
def DoSubMenus(lList, pParent):
    for name in lList:
        pMenu = pParent.GetSubmenuW(App.TGString(name))
        if not pMenu:
            pMenu = App.STCharacterMenu_Create(name)

            pParent.AddChild(pMenu)
            pParent.Layout()

        pParent.SetFocus(pParent.GetFirstChild())
        pParent = pMenu#App.STSubPane_Cast(pMenu.GetFirstChild())
    return pParent

def CreateMutator(mode, pOptionsWindow):
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(MainMenu.mainmenu.ET_CONFIGURE_MUTATOR)
    pEvent.SetDestination(pOptionsWindow)

    pMenuButton = App.STButton_Create(mode.name, pEvent)
    pEvent.SetSource(pMenuButton)
    pEvent.SetString(mode.name)
    pMenuButton.SetChoosable(1)
    pMenuButton.SetAutoChoose(1)
    pMenuButton.SetChosen(mode.IsEnabled())

    return pMenuButton

class MutatorGroup(Foundation.MutatorDef):
	def __init__(self, name, IsRadio = 0):
		mode = GetGroup(name)
		if mode:
			self = mode
		else:
			Foundation.MutatorDef.__init__(self, name)
			self.IsRadio = IsRadio
			self.IsGroup = 1
Foundation.MutatorGroup = MutatorGroup

def GetGroup(sName):
	if sName in Foundation.mutatorList._arrayList:
		mode = Foundation.mutatorList._keyList[sName]
		if mode.__dict__.get("IsGroup", 0):
			return mode
	return None
Foundation.GetMutatorGroup = GetGroup
