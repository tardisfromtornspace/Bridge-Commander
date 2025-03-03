== Changelog ==
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
* Show/Hide main Hull Bar on the player's Ship Display.
* Show/Hide text providing information about main Hull's Integrity:
    - Show Percentages will make it display a 0-100% text.
    - Show Fraction will add a currentHealth/MaxHealth indicator as well to the bar.
* Number of decimals: an entry number which provides the option to allow as many decimals as you want, from none to what you may feasibly want. NOTE: For ships whose max health is below 1.0, 6 decimals will be shown.
* Radix separator: whether to use lower comma (,), lower dot (.), apostrophe (') or a representation of middle dot (·, in game as ||), as the symbol that separates the integer from the fraction/decimal part (i.e. 2,35 ; 2.25, 2'35 or 2||35).
* Font and Size: currently these allow the player to choose between the following fonts and sizes, alongside a customizable size entry:
    - "Crillee": sizes 5, 6, 9, 12 and 15.
    - "LCARSText": 5, 6, 9, 12, 15.
    - "Tahoma": 8, 14.
    - "Arial": 8.
    - "Serpentine": 12.
* Interface colors: allows the user to modify several colors from the UI during QuickBattle. Colors are modified by altering thier red (r), green (g), blue (b) and opacity (a) values (which, as of version 0.2, go on a [0-1] range), or re-set to default by an individual "Reset to default" buttons. New colors can be added as long as they are registered as part of App.py. Currently, the default colors you can modify without any extra scripts are:
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
        - "g_kSubsystemFillColor": - Also covered the FoundationTech version for hulls.
        - "g_kSubsystemEmptyColor": - Also covered the FoundationTech version for hulls.
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

* Save Config button: do not forget to clik on this button to apply your changes, else they will not be applied nor saved!
* More resistance against certain configuration file errors: if the configuration script finds a missing entry on its Saved Config, it will automatically save with the proper parameters.

== Requirements: ==
    - QBAutostart.
    - Foundation.
    - Unified Main Menu (to see configuration options).

== Usage: ==
    1. Install.
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