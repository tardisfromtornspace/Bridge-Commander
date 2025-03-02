== Changelog ==
0.13 - Added support for certain possible BCMM dynamic font list creation from a TGFontManager extension, and corrected slight issues with the BCMM FontExtension.py example file from Mario's branch during commit 38eab561eb7c8afca0395a98a24dbda9d1314d68.
0.12 - Made fonts work via import of a new file so people can add or remove fonts without modifying the primary file, also made it nicer regarding menus (i.e. fonts are now ordered alphabetically) and saves while QB was running. Now when saving the Save Config button will properly indicate that you saved your configuration or if there are unsaved changes.
0.1 - First release after a few updates, some ideas still need to be expanded
Pre 0.1 - USS Sovereign and Noat's version (just labeling it as 0.1 because I did not see versioning on the files I was given)
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