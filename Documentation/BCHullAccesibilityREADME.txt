== Changelog ==
1.0.2 
   - Fixed a gooff that made 0-decimal hull percentage to show as "%" - thank you Sovereign for pointing it out! <3
1.0.1 
   - Updated FoundationTech.GaugeTechDef.DetachShip hull gauge fix unrelated to this mod to be more robust.
1.0.0:
    - Official release of the mod on Gamefront.
0.5.5:
    - Added a new DefaultColorsExtras value file to add support to g_kSTButtonMarkerGray, g_kSTButtonColors and g_pConditionColors.
0.5.4:
    - Updated path to correctly say Accessibility and not Accesibility - those who installed previous versions need to delete scripts\Custom\UnifiedMainMenu\ConfigModules\Options\AccesibilityConfigFiles since that info is now at scripts\Custom\UnifiedMainMenu\ConfigModules\Options\AccessibilityConfigFiles.
0.5.3:
    - Updated value files to be more resistant to errors.
    - Added support for GalaxyChart's Galaxy Map GUI.
0.5.2:
    - Updated the FIX-AblativeArmour1dot0 Autoload script to provide full starbase repair functionality and better armour inheritance.
0.5.1:
    - Simplified the align section immensely, allowing for a far less bug-prone alignment between different KM versions.
0.5.0:
    - Added fixes to FoundationTech.GaugeTechDef.DetachShip
    - Updated FIX-AblativeArmour1dot0 to reflect this in a clean way.
    - Updated AccesibilityConfig and related configuration files so each one remains on topic (f.ex. creation of a FoundationTech file that takes care of the colros from FoundationTech, another that takes care of ftb.Tech.AblativeArmour colors, etc.) and giving examples of how to add and modify new variables.
0.4.2:
    - Certain fixes and modifications on AccesibilityConfig and some of its extra files to allow customization to work for whips with AblativeArmour ftb Tech.
    - Temporarily disabled function that allows players to instantly change the player's own hull gauge colors mid-QB, due to conflicts with other techs that depend on FoundationTech's Gauge. Customization of the Gauge itself has not been modified.
0.4.0:
    - Several interface improvements, among them the option to make the % and fraction go on the same line or separate ones.
    - Fixed non-alignment resize bugs that happened when switching to ships or other configs that had noticeably different string lengths.
0.3.0:
    - Made Hull Gauge text work better for huge and tiny numbers.
0.2.6:
    - Removed a "import Foundation" statement that was doing nothing on the AccesibilityConfig.py
0.2.5:
    - Fixes and improvements to text entries so you cannot cause more invalid inputs, and more resistant saves.
    - Added options to reset a color, or return to your last save's color; both individually and for all colors, thanks to two local and two global master buttons.
0.2.2:
    - Small fix to inputs
0.2.1: 
    - Added slightly more support for FontExtension, albeit on my install I will not be adding FontExtension per se since in order to work properly it requires to do changes on FixApp that some players may not desire
    - Removed the FontExtension file from scripts.
0.2.0:
    - Added Interface color support, improved certain functions (thank you, Sovereign)
0.1.3:
    - Added support for certain possible BCMM dynamic font list creation from a TGFontManager extension, and corrected slight issues with the BCMM FontExtension.py example file from Mario's branch during commit 38eab561eb7c8afca0395a98a24dbda9d1314d68.
0.1.2:
    - Made fonts work via import of a new file so people can add or remove fonts without modifying the primary file, also made it nicer regarding menus (i.e. fonts are now ordered alphabetically) and saves while QB was running. Now when saving the Save Config button will properly indicate that you saved your configuration or if there are unsaved changes.
0.1.0:
    - First release after a few updates, some ideas still need to be expanded
Pre 0.1.0:
    - USS Sovereign and Noat's version (just labeling it as 0.1.0 because I did not see versioning on the files I was given)

== What does this mod do ==
The idea of this mod is inspired by the Shield Percentages mod by Defiant. It was originally made pre-2010 with the goal of showing lots of accessibility options, such as for colorblind people.
The new version also provides the following:
* Save Config button: do not forget to clik on this button to apply your changes, else they will not be applied nor saved, even if you used a master button to reset to default!
* More resistance against certain configuration file errors: if the configuration script finds a missing entry or error on its Saved Config, it will automatically save and re-apply with the proper parameters.
* Show/Hide main Hull Bar toggle button on the player's Ship Display.
* Show/Hide text providing information about main Hull's Integrity, a toggle button:
    - Show Percentages toggle button will make it display a 0-100% text.
    - Show Fraction toggle button will add a currentHealth/MaxHealth indicator as well to the bar.
    - Additionally, you can choose if % and fraction go on the same line, or separate lines, with another toggle button.
* Number of decimals text entry button: an entry number which provides the option to allow as many decimals as you want, from none to what you may feasibly want, for both percentages and fractions. NOTE: For ships whose max health is below 1.0, 6 decimals will always be shown for fractions.
* Radix separator button: whether to use lower comma (,), lower dot (.), apostrophe (') or a representation of middle dot (·, in game as || on certain fonts), as the symbol that separates the integer from the fraction/decimal part (i.e. 2,35 ; 2.25, 2'35 or 2||35). Radix separator may be displayed differently according to the font selected.
* Font and Size: currently these allow the player to choose between the following fonts and sizes, alongside a customizable size entry:
    - "Crillee": sizes 5, 6, 9, 12 and 15.
    - "LCARSText": 5, 6, 9, 12, 15.
    - "Tahoma": 8, 14.
    - "Arial": 8.
    - "Serpentine": 12.
* Interface colors menu: allows the user to modify several colors from the UI, mainly during QuickBattle. These colors are grouped on categories, to facilitate customization. Colors are modified by altering thier red (r), green (g), blue (b) and opacity (a) values (which, as of version 0.2.5, go on a [0-1] range), or can be re-set to default by an individual "Reset to default" buttons or restored back to your last save's config by individual "Reset to last save" buttons. All colors can be collectively reset and restored through two master buttons: "Reset all colors to default" and "Restore all colors to last save". New colors can also be added as long as they are registered as part of App.py. Currently, the default colors you can modify without any extra scripts nor files are:
    - "STButton marker colors":
        - "g_kSTButtonMarkerDefault"
        - "g_kSTButtonMarkerHighlighted"
        - "g_kSTButtonMarkerSelected"
        - "g_kSTButtonCheckmarkOn"
        - "g_kSTButtonCheckmarkOff"
    - "Menu colors":
        - "g_kSTMenuArrowColor":
        - "g_kSTMenu1NormalBase":
        - "g_kSTMenu1HighlightedBase":
        - "g_kSTMenu1Disabled":
        - "g_kSTMenu1OpenedHighlightedBase":
        - "g_kSTMenu1Selected":
        - "g_kSTMenu2NormalBase":
        - "g_kSTMenu2HighlightedBase":
        - "g_kSTMenu2Disabled":
        - "g_kSTMenu2OpenedHighlightedBase":
        - "g_kSTMenu2Selected":
        - "g_kSTMenu3NormalBase":
        - "g_kSTMenu3HighlightedBase":
        - "g_kSTMenu3Disabled":
        - "g_kSTMenu3OpenedHighlightedBase":
        - "g_kSTMenu3Selected":
        - "g_kSTMenu4NormalBase":
        - "g_kSTMenu4HighlightedBase":
        - "g_kSTMenu4Disabled":
        - "g_kSTMenu4OpenedHighlightedBase":
        - "g_kSTMenu4Selected":
        - "g_kSTMenuTextColor":
        - "g_kSTMenuTextSelectedColor":
        - "g_kSTMenuTextHighlightColor":
        - "g_kTextEntryColor":
        - "g_kTextHighlightColor":
        - "g_kTextEntryBackgroundColor":
        - "g_kTextEntryBackgroundHighlightColor":

    - "Tactical Interface Colors":
        - "g_kTIPhotonReadyColor":
        - "g_kTIPhotonNotReadyColor":

    - "Radar border highlight color":
        - "g_kSTRadarBorderHighlighted":

    - "General Interface Colors":
        - "g_kTitleColor":
        - "g_kInterfaceBorderColor":
        - "g_kLeftSeparatorColor":

    - "Radar colors":
        - "g_kRadarBorder":
        - "g_kSTRadarIncomingTorpColor":
        - "g_kRadarFriendlyColor":
        - "g_kRadarEnemyColor":
        - "g_kRadarNeutralColor":
        - "g_kRadarUnknownColor":

    - "Subsystem colors":
        - "g_kSubsystemFillColor": - Partially if only this script, fully if the extra script-file that covers the FoundationTech version for hulls ("FoundationTechExtras") is present.
        - "g_kSubsystemEmptyColor": - Partially if only this script, fully if the extra script-file that covers the FoundationTech version for hulls ("FoundationTechExtras") is present.
        - "g_kSubsystemDisabledColor":

    - "Tactical weapons control header text":
        - "g_kTacWeaponsCtrlHeaderTextColor":

    - "Damage display colors":
        - "g_kDamageDisplayDestroyedColor":
        - "g_kDamageDisplayDamagedColor":
        - "g_kDamageDisplayDisabledColor":

    - "Main menu colors":
        - "g_kMainMenuButtonColor":
        - "g_kMainMenuButtonHighlightedColor":
        - "g_kMainMenuButtonSelectedColor":
        - "g_kMainMenuButton1Color":
        - "g_kMainMenuButton1HighlightedColor":
        - "g_kMainMenuButton1SelectedColor":
        - "g_kMainMenuButton2Color":
        - "g_kMainMenuButton2HighlightedColor":
        - "g_kMainMenuButton2SelectedColor":
        - "g_kMainMenuButton3Color":
        - "g_kMainMenuButton3HighlightedColor":
        - "g_kMainMenuButton3SelectedColor":
        - "g_kMainMenuBorderMainColor":
        - "g_kMainMenuBorderOffColor":
        - "g_kMainMenuBorderBlock1Color":
        - "g_kMainMenuBorderTopColor":

    - "Engineering display colors":
        - "g_kEngineeringShieldsColor":
        - "g_kEngineeringEnginesColor":
        - "g_kEngineeringWeaponsColor":
        - "g_kEngineeringSensorsColor":
        - "g_kEngineeringCloakColor":
        - "g_kEngineeringTractorColor":
        - "g_kEngineeringWarpCoreColor":
        - "g_kEngineeringMainPowerColor":
        - "g_kEngineeringBackupPowerColor":
        - "g_kEngineeringCtrlBkgndLineColor":

    - "QuickBattle and Multiplayer Colors":
        - "g_kQuickBattleBrightRed"
        - "g_kMultiplayerBorderBlue"
        - "g_kMultiplayerBorderPurple"
        - "g_kMultiplayerStylizedPurple"
        - "g_kMultiplayerButtonPurple"
        - "g_kMultiplayerButtonOrange"
        - "g_kMultiplayerDividerPurple"

    - There are also more covered colors, using extra value files:
	* File "DefaultColorsExtras":
            - For "STButton marker colors": "g_kSTButtonMarkerGray".
            - For a new "STButton base colors (some)" category: g_kSTButtonColors.
            - For a new "Other interface colors" category: g_pConditionColors.
        * File "FoundationTechExtras":
            - For installs with FoundationTech, covers the cases of health gauge colors for "g_kSubsystemFillColor" and "g_kSubsystemEmptyColor".
        * File "ftbAblativeArmourExtras":
            - For a new category "Foundation Technologies' colors":
                - Covers the "g_kSubsystemFillColor" for empty armor color.
                - "ftbAblativeArmourFill" for customizable fill armor color.
        * Most other ".*ArmorExtras" and ".*ArmourExtras" seen on this mod:
            - Homologues of "ftbAblativeArmourExtras" but for their own armors/armours. Also located at "Foundation Technologies' colors".
        * File "CustomTechsAlternateSubModelFTLExtras":
            - For the category "Foundation Technologies' colors", adds menu customization of its intra-system intercept feature.
        * File "GalaxyChartsGalaxyMapGUIExtras":
            - For a new category "Galaxy Charts' colors", it provides customization for Galaxy Map GUI colors for systems where the player is located, regions, selected regions, hostile regions and allied regions.

* FoundationTech Gauge fixes - taking care of an issue where FoundationTech.GaugeTechDef.DetachShip could not find its ship's pDisplay even it it existed, which lead to bugs with techs based around that GaugeTech not swapping bars properly.
* FoundationTech AblativeArmour fix: with the "FIX-AblativeArmour1dot0" Autoload file and the gauge fix above, now the armor can not only repair itself properly, but can be rebuilt properly by any other script (specially starbase docking for repairs) and its functionality restored after those repairs, including when the armor was destroyed and the starbase rebuilt it from scratch.

== Requirements: ==
    - QBAutostart.
    - Foundation.
    - Unified Main Menu (to see configuration options).

== Usage: ==
    1. If you are using KM or BCMM, install all the folders and files except those of the folder called "extra (do not add to install, BCMM-related)", by copy-pasting onto your STBC main folder.
	1.2 - For BCMM only - go to the folder "extra (do not add to install, BCMM-related)" and inside you will find another scripts folder. Then you install that folder on your install as well.
    2. Configure in UMM. Do not forget to save your configuration!
    3. That's it.


== Credits ==
    * Mario aka USS Sovereign for QBAutostart and initial coding.
    * Noat for adding UMM config options and adding a switch to have both the bar and text percentage visible.
    * tardis#2540 aka Alex SL Gato for expanding the mod with many more configuration options and greatly enhancing the UX of the mod.
        - Some code fragments inspired by MLeoDaalder's config files.

== License ==

    LGPL

Permissions:
Distribute freely, modify freely as long as credits are given, within the scope of the LGPL license, of course.

Known bugs:
    - 

Fulfilling both the SDK and LGPL licenses:
This mod is not made or supported by Activision. You may distribute this mod freely as long as the original archive is distributed and no part of it, including this document, is modified or missing.

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.

Star Trek, Star Trek: The Next Generation, Star Trek: Deep Space Nine, Star Trek: Voyager and related properties are Registered Trademarks of Paramount Pictures registered in the United States Patent and Trademark Office.

We do not take any responsibility for any kind of damage this does to your computer.

Use it at your own risk.