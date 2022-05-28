Unified Main Menu v1
By MLeo Daalder


Purpose of the mod:
  To provide the one MainMenu modification that will make other MainMenu modifications redundant
  so that there won't be multiple versions of MainMenu. This is done by plugins.


Installation:
  Copy the scripts directory from the zip and put it in your Bridge Commander directory.

  If you have NanoFXv2 Beta (or higher) installed, then I would like to point your attention to
  a separate directory in the zip named NanoFXConfigPanel, this has an another directory in it
  which you must copy to your Bridge Commander directory as well, this will install a NanoFX plugin.

  Be sure that the directory structure is preserved when you unzip it.


This mod includes:
  The UMM (Unified Main Menu)
  A mutators plugin (more on that later)
  Auto Test Mode
  NanoFX Config Panel plugin (in the separate directory)
  KeyFoundation (an older mod of mine, it seemed natural of including it as well)


Features of "plain and pluginless" UMM:
  Allowing modders to create their own menus and options in MainMenu without overwriting mainmenu.py
  And making it an option for their mods, meaning they don't have to include this mod for their menu's (if they do it right)
  A stable method of letting BC run code at start up.
  Filtering non missions from the mission list. And allowing modders to exclude their directories in
  Custom even if their mod does happen to comply with the mission format (more on that later).


How to use:
  Start the game and go to Options, you will see a button called: "Configuration", this is the same button that was
  known as "Mutators".
  Here you will find all the configurations you need under the menu "Configurations". For example, the mutator plugin
  must be made active to see it. You can find the mutators plugin under Configurations->Custom Options->Options->Mutators

  __IMPORTANT__
  Be sure to enable the Master Switch. The Master Switch is there to allow end users who are experiencing problems to see if it's UMM related.
  Also, please note that you need to reload (reclick the Options button at the top) for some changes to take effect.
  Start Up modules require a restart of BC.


Credits:
  Dasher, for his Foundation, FoundationTriggers and FoundationTechnologies
  Defiant, for his scrolling mutators
  Mark, for wanting a configuration menu in the main menu which made me get the project
        off the ground in a matter of days after months (year and a couple of months actually)
        of thinking to do this and for providing the first 3rd (or rather 2nd) party mod to use this.
  Lost_Jedi, for giving it a last minute beta test.
  BCU community who visit the scripting forum for tested this mod


Planned mods by myself (no ETA as of yet, they have their quirks to sort out):
  Foundation Preference Preserver
  Movie Manager (select what movies to show on start up)


Licence:
  Third party scripters are allowed to redistribute the original package in their mods,
  although it is advised that they link to the latest version just to be sure.
  If you, as third party scripter, decide to include this mod, then I would find it very nice
  to see my name in the credits.

  No special permission is needed to redistribute the original, unmodified package (and all files there in).
  However, if you do have made modifications to this mod, or any files in the package, then you _MUST_ run it
  by me as I'd like to test it for problems.


Any Bugs?
  Contact me on MLeoDaalder @ netscape.net or PM me on BCU (MLeo there).
  And tell me what mod you tried to use with it (please include a link to the mod if you can).


About the Mutator plugin:
  I would like to start by giving credit to Dasher for his version of it.
  Defiant for his scrolling mutators (but I'm afraid this modification isn't needed anymore, yet credit must still be given).

  Here is an example on how to use it:
   import Foundation
   TestSubMenusMode = Foundation.MutatorDef("Submenus Test")
   TestSubMenusMode.MutatorGroup = ["Test", "Sub", "Menus"] 


For Modders:
  Creating Main Menu Mods:
  There are several types of mods, though all are the same setup (save for the startup mods)
  These types are (behind the name is the place to put the file):
  StartUp (StartupModules)
  Configurations (ConfigModules)
  Configurations::Options (ConfigModules/Options)
  Configurations::Options::General (ConfigModules/Options/General)
  Configurations::Options::Sound (ConfigModules/Options/Sound)
  Configurations::Options::Graphics (ConfigModules/Options/Graphics)

  All locations are relative to your BC path and the following path:
  scripts/Custom/UnifiedMainMenu/

  As for the basic structure of your plugin, you need atleast 2 functions.
  GetName - this must return the name of your mod
   It has no arguments
  CreateMenu - this must return your configuration screen, if there isn't one then you must return None
   It has the following arguments:
    pOptionsPane - pOptionsPane is the right hand side of the options window, can be entered as None (in the stock scripts it isn't really used, except for the keyboard configuration)
    pContentPanel - this is the direct "parent" your UI will be added to.
    bGameEnded - whether or not the game ended, must default to 0

  There is an exception, namely in the StartUp modules. These mods have an extra function:
   StartUp - this doesn't return anything, and it will have to contain all the code you need for your mod to be "hooked" into BC
    It has no arguments

  If you have any questions, don't hesitate to look through the examples or contact me (my MSN is the same as my e-mail)
