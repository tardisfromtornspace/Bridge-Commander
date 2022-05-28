###############################################################################
# BCS: THE BEGINNING UMM Plugin v0.2
# Last Updated by Wowbagger -- 2/17/2006
#
# We've decided to go with the UMM.  It's kind of an 11th-hour transition
# (no one had a copy until last week), but the UMM promises to be a
# major help in solving some of our customizability issues.
#
# With this release, we only include options for our most contentious
# issues (most notably, the ESR Hull Repair option).  The rest of our
# mods will, at least for now, stay on the mutator list, because it
# is so wonderfully easy to use standard mutators.  As the UMM evolves,
# though, BCS:TNG expects to rely on it heavily.
#
# NOTES TO BCS:TNG:
# Unlike many config systems, when we use in-game variables, this one does NOT
# grab them directly from the config file.  I was having problems getting it to
# write new variables and then reload.  In any case, this system works better,
# because it saves one click for the average user.
#
# So, here's how it goes down: 1) Upon startup of the UMM, we grab all the
# variables that are stored as defaults in the config file.  2) The user changes
# these variables on the main menu as he wishes.  3) Unless he presses the Save
# As Default button, these variables are NOT saved for future games.  However,
# we still have the values he selected stored as global variables within this
# file.  4) When QBautostart boots up, the relevant scripts automatically import
# the relevant variables from THIS file.
#
# Capice?  I *think* I was kind of almost nearly clear with that.
#
# NOTES ON THE ENGINEERING MENU FIX PLUGIN:
# This is something Sovvy and I put together very quickly.  It's actually a fix
# for a BC-wide problem, but TB, because it had so many Engineering menu items,
# made it manifest in about 30% of machines.  Brex's menu, it turns out, can
# only support 4 or 5 menu items before it loses all the text.  The best way
# to fix this, of course, would be to get things out of that menu.  But, since
# most of the "clutter" mods are by other people, this was not an option for
# BCS:TNG.  Sovvy was the one who noticed that placing menu items below the
# damaged systems display prevented the problem from appearing, as long as the
# top part of the menu didn't reach critical mass.  I just implemented a
# truncated version of his code and wrote a UMM plugin for it.
#
# If you're reading this, it means you probably already know what the plugin is
# (it moves certain Engineering menu items to the bottom).  What you want to
# know is how to implement it into your own code, so you can contribute even
# more to the effort.  It's pretty simple, actually.  First, import the variable
# into your plugin, with this code:
#
# pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.BCSTheBeginning")
# pOption = pModule.EngineeringOption
# EngineeringOption = int(pOption)
#
# Then, in the init() function (or wherever you add your menus), (we will assume
# you are representing Brex's Engineering Menu with the variable pMenu, but this
# is by no means required), replace:
#
# pMenu.PrependChild(pChildMenu)
#
# with this edited code:
#
#        # If the code is active, make the special menu.
#        if EngineeringOption == 1:
#                pMenu       = Libs.BCSTNGLib.CreateEngineerMenu("Advanced Core Options", "Engineer")
#
#        # Otherwise, make it in the standard manner.
#        else:
#                pBrexMenu   = Libs.LibEngineering.GetBridgeMenu("Engineering") 
#                pMenu       = App.STMenu_CreateW(App.TGString("Advanced Core Options"))
#                pBrexMenu.PrependChild(pMenu)
#
# Simplicity itself.
#
# This should hold things together until BCS:TNG puts out the permenant fix that
# is currently in a pre-Alpha form.
################################################################################

### Section I: Imports
## Standard Imports: You need 'em.  You want 'em.  You can't do without 'em.
## Do-wah do-wah do-wah do-wah.  Da.
import App
import Foundation
import string
import nt

## Import Default Settings: Get all the variables in BCSTBConfig.
# Grab the module.
pModule = __import__("SavedConfigs.BCSTBConfig")

# Grab the variables.  (That sounds like something that would get you brought up
# on sexual harrassment charges. "He grabbed my variables!" Yes. Moving on...)
ESRHullCustomizationOption  = pModule.ESRHullCustomizationOptionDefault
SRCutscene                  = pModule.SRCutsceneDefault
EngineeringOption           = pModule.EngineeringOptionDefault



### Section II: Global Variables
# Defines the location where we will save our defaults.
ConfigPath  = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\BCSTBConfig.py"



### Section III: Functions
# Name of the mod (req. in UMM).  This defines the name of the options menu.
def GetName():
                return "BCS: The Beginning"


# Builds our menu.  Remember to add the "return App.TGPane_Create(0,0)" command!
def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
                # Make the submenus.
                CreateESRSubmenu(pOptionsPane, pContentPanel)
                CreateSRSubmenu(pOptionsPane, pContentPanel)

                # Add the Engineering Menu Option.
                CreateEngineeringFixButton(pOptionsPane, pContentPanel)

                # Make the Save Config button.
                CreateButton("Save Configuration as Default", pContentPanel, pOptionsPane, pContentPanel, __name__ + ".SaveConfig")

                return App.TGPane_Create(0,0)


## Set of functions for ESR.
def CreateESRSubmenu(pOptionsPane, pContentPanel):
                # Create the ESR Menu.
                pESRMenu = App.STCharacterMenu_Create("Emergency Repair")
                pContentPanel.AddChild(pESRMenu)

                # Create the submenu for hull repair
                pHullMenu = App.STCharacterMenu_Create("Hull Repair (HR) Options")
                pESRMenu.AddChild(pHullMenu)

                # Add buttons.
                CreateButton("1: Disable Hull Repair.", pHullMenu, pOptionsPane, pContentPanel, __name__ + ".HandleESRButtonClicked", EventInt = 0)
                CreateButton("2: Shields to 0% in HR.", pHullMenu, pOptionsPane, pContentPanel, __name__ + ".HandleESRButtonClicked", EventInt = 0)
                CreateButton("3: Shields to 50%/Engines to 0% in HR.", pHullMenu, pOptionsPane, pContentPanel, __name__ + ".HandleESRButtonClicked", EventInt = 0)
                CreateButton("4: Shields to 50% in HR.", pHullMenu, pOptionsPane, pContentPanel, __name__ + ".HandleESRButtonClicked", EventInt = 0)
                CreateButton("5: Engines to 0% in HR plus 20 sec.", pHullMenu, pOptionsPane, pContentPanel, __name__ + ".HandleESRButtonClicked", EventInt = 0)
                CreateButton("6: Engines to 0% in HR.", pHullMenu, pOptionsPane, pContentPanel, __name__ + ".HandleESRButtonClicked", EventInt = 0)
                CreateButton("7: Sensors to 0% in HR.", pHullMenu, pOptionsPane, pContentPanel, __name__ + ".HandleESRButtonClicked", EventInt = 0)

                return pESRMenu

     
def HandleESRButtonClicked(pObject, pEvent):
                global ESRHullCustomizationOption
                sString = pEvent.GetCString()

                # Get the first character of the button; this is the option number we need.
                ESRHullCustomizationOption = sString[0]


## Set of functions for Silent Running.
def CreateSRSubmenu(pOptionsPane, pContentPanel):
                # Create the SR Menu.
                pSRMenu = App.STCharacterMenu_Create("Silent Running")
                pContentPanel.AddChild(pSRMenu)

                # Create the buttons.
                CreateButton("Enable Cutscene", pSRMenu, pOptionsPane, pContentPanel, __name__ + ".HandleSRButtonClicked", EventInt = 0)
                CreateButton("Disable Cutscene", pSRMenu, pOptionsPane, pContentPanel, __name__ + ".HandleSRButtonClicked", EventInt = 0)

                return pSRMenu
            

def HandleSRButtonClicked(pObject, pEvent):
                global SRCutscene
                sString = pEvent.GetCString()

                if sString == "Enable Cutscene":
                        SRCutscene = "ON"  # \" prints as "
                if sString == "Disable Cutscene":
                        SRCutscene = "OFF"  
    

## Set of functions for Engineering Menu Fix
def CreateEngineeringFixButton(pOptionsPane, pContentPanel):
                global EngineeringOption, pEngineeringButton
                pEngineeringButton = CreateChoosableButton("Engineering Menu: Button Text Fix", pContentPanel, pOptionsPane, pContentPanel, EngineeringOption)

                return pEngineeringButton
            

# Saves the current configuration as the default.
def SaveConfig(pObject, pEvent):
                # Write all data to the Config file.
                global ESRHullCustomizationOption
                global SRCutscene, SRCutsceneFile
                # ESR data:
                file = nt.open(ConfigPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
                nt.write(file, "ESRHullCustomizationOptionDefault = " + str(ESRHullCustomizationOption))
                nt.write(file, "\nSRCutsceneDefault = \"" + str(SRCutscene) + "\"")
                nt.write(file, "\nEngineeringOptionDefault = " + str(pEngineeringButton.IsChosen()))
                nt.close(file)
                

# Helper function.  Makes buttons.  Those little pins on the back that let you
# put them on your shirt are sold seperately.
def CreateButton(sButtonName, pMenu, pOptionsPane, pContentPanel, sFunction, EventInt = 0):        
                ET_EVENT = App.UtopiaModule_GetNextEventType()

                pOptionsPane.AddPythonFuncHandlerForInstance(ET_EVENT, sFunction)

                pEvent = App.TGStringEvent_Create()
                pEvent.SetEventType(ET_EVENT)
                pEvent.SetDestination(pOptionsPane)
                pEvent.SetString(sButtonName)

                pButton = App.STButton_Create(sButtonName, pEvent)
                pButton.SetChosen(0)

                pEvent.SetSource(pButton)            
                pMenu.AddChild(pButton)

                return pButton


# Creates a button with one of those nifty little holes on the side that fills in when you press it.
def CreateChoosableButton(sButtonName, pMenu, pOptionsPane, pContentPanel, IsChosen = 0, EventInt = 0):        
                ET_EVENT = App.UtopiaModule_GetNextEventType()

                pEvent = App.TGStringEvent_Create()
                pEvent.SetEventType(ET_EVENT)
                pEvent.SetDestination(pOptionsPane)
                pEvent.SetString(sButtonName)

                pButton = App.STButton_Create(sButtonName, pEvent)
                pButton.SetChoosable(1)
                pButton.SetAutoChoose(1)
                pButton.SetChosen(IsChosen)
                
                pEvent.SetSource(pButton)            
                pMenu.AddChild(pButton)

                return pButton
