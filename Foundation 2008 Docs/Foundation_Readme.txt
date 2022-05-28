Foundation plugin system for Bridge Commander

Released March 31, 2002

Written by Daniel B. Houghton (aka Dasher42), 2002.  All rights
reserved.

By default, Bridge Commander allows a great deal of moddability, but
adding new ships requires users to download the SDK and edit the .py
files.  This is a tedious process, and it is unfeasible to distribute,
say, an edited QuickBattle.py for every ship out there if you want
multiple mods on a single installation.

This is a system to allow easy integration of new ships into Bridge
Commander. It replaces the static indexes of Bridge Commander with
dynamic structures, thus providing the means for ship modders to
easily distribute their ships without overwriting any of the end user's
files.

To add a ship with this system, you merely copy in the ship.  That's
it!  It'll appear in the "Other Ships" QuickBattle menu and play with
standard AI.

If you want more, make a plugin .py file and put it in
scripts\Plugins, or put it in scripts\Plugins\Custom folder, and edit
scripts\Plugins\Custom\Custom.py to import the new ship.  That's it!
No more plumbing the depths of QuickBattle.py.

Ship modders:  If you want your ship to appear in another submenu or
incorporate custom AI, you need only include a plugin file, an example
of which is given as Plugins\Custom\Example.py.  See the directions
below.  Even creating this is far easier than what stock BC requires.

Enjoy!

------------------------------------------------------

INSTALLATION

To install this, simply copy the files into the Bridge Commander
installation - or a second copy of it, which I do *strongly* recommend.
This can be done with a simple copy of the Bridge Commander folder.  If
you mess up, just rename your suspect scripts folder and copy the
scripts
folder from your original BC installation in!

This package is beta, and has not been tested for compatibility with
single player and multiplayer game modes.

As a result, you should have:

(Bridge Commander Folder)\Foundation_Readme.txt
(Bridge Commander Folder)\scripts\Foundation.py
(Bridge Commander Folder)\scripts\Registry.py
(Bridge Commander Folder)\scripts\StaticDefs.py
(Bridge Commander Folder)\scripts\LoadTacticalSounds.py
(Bridge Commander Folder)\scripts\loadspacehelper.py
(Bridge Commander Folder)\scripts\Icons\ShipIcons.py
(Bridge Commander Folder)\scripts\Plugins\__init__.py
(Bridge Commander Folder)\scripts\Plugins\Custom\__init__.py
(Bridge Commander Folder)\scripts\Plugins\Custom\Custom.py
(Bridge Commander Folder)\scripts\Plugins\Custom\Example.py
(Bridge Commander Folder)\scripts\Tactical\Interface\ShieldsDisplay.py
(Bridge Commander Folder)\scripts\Tactical\Interface\WeaponsDisplay.py

...where (Bridge Commander Folder) is wherever the new copy of Bridge
Commander is located.

------------------------------------------------------

USAGE

If you're a user that wants to incorporate a new ship, you have three
options:

1)  Just copy the ship in.  It'll appear in "Other Ships" with standard
AI.

2)  If this ship has a file in scripts\Plugins\ or its subfolders,
    either copy that file into scripts\Plugins or
    scripts\Plugins\Custom.
    The scripts\Plugins\Custom folder is for use with Nanobyte's GUI
    tool
    or those willing to edit their scripts\Plugins\Custom\Custom.py
    themselves.  If you edit this file, you need to add a line to the
    end
    it that looks like this:

import ShipName

------------------------------------------------------

ADDING A SHIP

Got a ship you want to make plugin-ready?  Here is a step-by-step guide
to making a ship compliant with Foundation.  When done you will have
something that you can distribute and that the end user can integrate
by adding a single import line to their scripts\Plugins\Plugins.py.

1)  Export the models.  You should have the following:

The model and textures:

data\Models\Ships\NewShip\
data\Models\Ships\NewShip\NewShip.NIF (optionally NewShipMed.NIF and
NewShipLow.NIF too)
data\Models\Ships\NewShip\High\(textures as .TGA's)
data\Models\Ships\NewShip\Medium\(textures as .TGA's)
data\Models\Ships\NewShip\Low\(textures as .TGA's)

The ship definition and hardpoints:

scripts\Ships\NewShip.py
scripts\Ships\Hardpoints\newship.py

2)  Scripts\Ships\NewShip.py must have a properly set up GetShipStats()
    section for the ship to work.  Some of these parameters are case-
    sensitive; be careful!

---

def GetShipStats():
	kShipStats = {
		"FilenameHigh":
		"data/Models/Ships/NewShip/NewShip.nif",
		"FilenameMed":
		"data/Models/Ships/NewShip/NewShipMed.nif",
		"FilenameLow":
		"data/Models/Ships/NewShip/NewShipLow.nif",
		"Name": "NewShip",           #  <-  These are
		"HardpointFile": "newship",  #  <- important!
		"Species": Multiplayer.SpeciesToShip.VORCHA
		# ^^^^^^ The importance of this is still unknown
	}
	return kShipStats

---

3)  You must make a scripts\Plugins\NewShip.py file (replace
    NewShip with your ship's name.  It is important that it refer to
    the name of the Scripts\Ships\NewShip.py file, and it is case-
    sensitive.  Copy scripts\Plugins\Custom\Example.py to
    scripts\Plugins\NewShip.py and edit it according to the
    contained instructions.  Mostly, just search for Example and
    replace it with NewShip.

4)  Got an icon?  A 128x128 .TGA of your ship?  Put it in
    Data\Icons\Ships. If its name is different from that of the ship,
    the Example.py file will show you how to use it.

5)  In order to localize your ship's name and for foreign language
    users, you must use the TGL exporter included with the Bridge
    Commander SDK.  You need to have strings to match "NewShip" and
    "NewShip Description", and in the ship's plugin file, put
    "hasTGLName": 1 and "hasTGLDesc": 1 inside the ShipDef line's
    curley braces, like this:

    ---
    Foundation.ShipDef.Warbird = Foundation.RomulanShipDef('Warbird',
    App.SPECIES_WARBIRD, { 'hasTGLName': 1, 'hasTGLDesc': 1 } )
    ---

That's it!

------------------------------------------------------

ADDING A SOUND

The first plugin type to be supported by the Foundation, sounds can now
be dynamically incorporated.  You may include their statements inside
ship plugin files or indeed any file you load along with the ship.  You
can even use it to make drop-in replacements for sound effects without
replacing the stock sounds.  You need only include a line like the
following:

Foundation.SoundDef("sfx/Weapons/Klingon Torp.wav", "Klingon Plasma
Torpedo", 1.0)

The first argument in double quotes specifies the file, the second
gives you a name to refer to this sound by from inside the ship's
hardpoints, and the third is a volume adjuster, 1.0 being the normal
level.

------------------------------------------------------

WHAT'S NEW?

March 31, 2002 release:

A number of new features have been added:

- A ship may be added to the game without a file in the scripts\Plugins
  folder.  Thanks to a snippet from Banbury which I have adapted and
  incorporated, you only need the conventional file in scripts\Ships
  and its related hardpoint file for the ship to appear in the "Other
  Ships" QuickBattle menus.

- The structure of the scripts\Plugins folder has changed;
  scripts\Plugins\Custom will be used for future versions of Nanobyte's
  GUI tool and use Custom.py as a direct counterpart of the old
  Plugins.py.  Other plugin files can be copied into
  scripts\Plugins where they will be loaded automatically.
  Regular plugins cannot override Custom plugins.

- By default, ships now use ASCII strings for the QuickBattle menu
  buttons.  See the above instructions.  This is meant to provide an
  acceptable minimum level of functionality; TGL support is encouraged!
  It will help the non-English-speaking users.

- Sounds can now be incorporated via plugins!


March 20, 2002 release 2:

First and foremost, the format for the plugins has changed.  I didn't
want to do this, but the change that's been made is the kind that
means that we won't have to do this again.  The new format is much
more flexible and forward-compatible.  It's best to get this over
and done with at this early stage.

Second, this mod's name has changed to better suit its idiom.
"Dynamic Tables" was rather awkward, and hey, a better name always
helps my propaganda efforts. ;)

Finally, a bug has been fixed associated with some ships being set
as the player's ship when their ships\Script\ship.py filename didn't
match their abbreviation.

---

March 20, 2002 release:

This version of the mod corrects cases where ship icons would not
appear in QuickBattle. This fix also resolves an issue with plugins
that include ships that supercede ships already included by Bridge
Commander or previously loaded plugins.  This should make it simple to
include a revised ship without overwriting the original one (unless you
feel it absolutely necessary).

There's still no easy solution to the '???' button issue unless you
install TGL's.  This mod may have a simpler solution, but largely, this
problem is out of scope.  Don't worry! The game will still work!

Multiplayer remains largely untested.  You're likely to see missing
ship icons and more.

I've also included a sample plugin file to load DamoclesX's Mod Pack
1.05 if you have it. If you don't, get it and install it - just DON'T
let it overwrite any existing files, and don't install the outdated
version of this mod that it includes.  I myself have found it best to
rename its DDeridex.py in scripts\ships\hardpoints to dderidex.py -
goes to show you how case-sensitive BC's scripting can be.  I've
even included a line to uncomment in this release's
scripts\Plugins\Plugins.py file.

------------------------------------------------------

TROUBLESHOOTING

Did you install this mod and then see Bridge Commander stop working?
Walk through the following steps:

1)  Is this about the '???' buttons?  They still work.  See the Bridge
    Commander SDK's documentation about TGL files.  If this is your
    only problem, relax.  We're working on it. ;)

2)  Did you unpack this into your copy of the Bridge Commander
    directory?  If so, this file you're reading should appear there,
    above \data, \scripts, \Screen Shots, everything.

3)  Did you have any mods already installed that could be conflicting?
    Try renaming your scripts folder and copying in the scripts folder
    from under the Setup folder on your Bridge Commander CD, and then
    installing a fresh copy of the Foundation over top.

4)  Did you install a plugin and then see the game stop working?  Try
    putting # signs in front of its import statement in
    \scripts\Plugins\Custom\Custom.py, or moving the .py and .pyc files
    out of \scripts\Plugins.

    Did it work?  Maybe an import statement is incorrect.  Double-check
    to be sure; these things are case-sensitive and must match the .py
    file's name.  Also, make sure you have no leading spaces; a line
    that reads " import NewShip.py" is trouble!  See step 8.

    If the plugin still doesn't work, it or Foundation itself could
    have an error, or maybe there's a conflict of some kind.  Getting
    work from separate sources to cooperate nicely on a single install
    isn't as simple as it sounds.

5)  Make sure there are no .PY files in your Bridge Commander folder
    that correspond to the ones included herein.  They could be
    compiled to .PYCs and break this mod. QuickBattles.py,
    loadspacehelper.py, ShipIcons.py, ShieldDisplay.py, and
    WeaponsDisplay.py would be obvious offenders.

6)  Get the latest release version of this mod from:

    www.beldar.com/~dasher/Foundation-current.zip

    You might get the fix you so crave.

7)  Did you install another mod after this one that overwrote
    Foundation? Regrettably, all other existing QuickBattle mods are
    incompatible with this one as of now.  Work will go forward to make
    them into plugins as well.  If you want this mod and them, make
    another fresh copy of Bridge Commander or just get your hands
    dirty.

8)  Failing all this, append " -TestMode" to your Bridge Commander
    icon's target field, hit the back apostrophe in-game when it starts
    to have trouble, and press enter.  Tell us what happened.

------------------------------------------------------

NOTE TO DEVELOPERS

This plugin project is meant to expand beyond ships into an easy "glue
layer" for Bridge Commander mods, providing a simple installation
process and an easy way to activate or deactivate mods.  As such,
please do not distribute modified versions of the existing .PY and .PYC
files in this mod indiscriminately, as you could break compatibility
with other mods that people *will* try to install and future versions
of the Foundation.  The simplest way to get your mod out there is to
put its plugin file in \scripts\Plugins.  You should be able to
do this without requiring any files to be overwritten.


---

CONVERTING FROM DYNAMICTABLES

Developers converting to the new Foundation format should use the new
Example.py.  A minimal conversion can be made by searching-and-
replacing DynamicTables to Foundation and adding a {} as an argument
to the "ShipDef" statement, as in:

DynamicTables.ShipDef.NewVorcha = DynamicTables.ShipDef('NewShip',
App.SPECIES_GALAXY)

to

Foundation.ShipDef.NewVorcha = Foundation.ShipDef('NewShip',
App.SPECIES_GALAXY, {})



------------------------------------------------------

LEGALESE:

This software is provided as-is, and the author (Daniel B. Houghton)
makes no guarantee of the performance of this software, its security,
compatibility, safety, or usefulness, and cannot be held liable for any
consequence of this software's use.

Permission is given to modify or distribute the acommpanying files as a
component of Bridge Commander under the terms of the Activision SDK
license with the following provisions:

1.  This readme file and shall be included in any distribution, and
credit given in any work which incorporates this package's files,

2.  Any changes to the .PY files included in this distribution that do
not incorporate Activision material (Registry.py as of this writing)
shall be included as source code per the terms of the Lesser GNU Public
License (LGPL), where this does not violate the terms of the Activision
SDK
license.  Other files shall be construed as New Game Materials per the
Activision
SDK agreement.

---

In short, use it, hack it, if you distribute changes to it make them
open and give the following people credit.  That's all, have fun!

Daniel Houghton AKA Dasher42 (dasher_42@yahoo.com),

Evan Light AKA Sleight42,

Banbury, who contributed code snippets that were adapted into
this release of the Foundation.

Special thanks also go out to Nanobyte and DigitalFiend whose work is
making the Foundation more accessible for the end users.

