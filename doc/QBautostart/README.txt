README:
==========
Version 0.9.1

This is the QBautostart Extension - formerly known as Engineering Extension, a small
Modification for Bridge Commander to allow easier scripting and loading of other scripts.
I changed the name, cause the option to send Brex to the Engineering has been taken out
in this Version: Most people are using Modded Bridges and why should there be a script only
working on 10% of all Bridges?

The Transporter Function is a copy from Banburys QBR made to work in normal QuickBattle.
You can find his great QBR at http://www.nightsoftware.com/banbury/
If you have "MLeoDaalders Key Foundation" installed, then you will be able to bind the Transporter
to a Key under "Options"->"Key Settings"->"General" in the mainmenu.

If you only get a Black screen, loading QuickBattle then you probably have an old script in your Install
that may require QBR 2.2 or higher.
If you really don't want to install QBR delete all files in scripts/Custom/QBautostart/ and reinstall
this QBautostart Extension.

To get your scripts working in Multiplayer you should use the FBCMP Mission4 module.


Author:
<---------->
Defiant <erik@vontaene.de>
http://StarTrek.webhop.info


Thx to:
<---------->
-Banbury for his Transporter Function and the easy way to create Buttons
-Dasher42 for his LoadExtraPlugins() which everyone is using and is working perfect,
 and the Foundation Triggers (included).


Requirements:
<---------->
None. Please note that some old scripts may still require QBR 2.2.
If your Loading Screen just turns black, install QBR: http://www.nightsoftware.com/banbury/ )


Install:
<---------->
Copy all files from QBautostart/ into your Bridge Commander root folder
and activate the Mutator.


Changes:
<---------->
Version 0.9.1:	- Added missing file UserDict.py, sorry!
Version 0.9:	- Major changes for the Multiplayer support.
Version 0.8:	- Added support for Multiplayer and Key Bindings using MLeoDaalders Key Foundation
		- the scripts/LoadQBautostart.py has been removed - it can be savely deleted on your installation
		- scripts/Lib/LibEngineering.py has been moved to scripts/Custom/Qbautostart/Libs/LibEngineering.py
			but "include Lib.LibEngineering" do still work.
Version 0.7:	- Bugfix: restart() Now does work properly!
Version 0.6:	- Bugfix: Multiple Button problems.
Version 0.5.1:	- The Transporter was broken in 0.5, sorry - fixed
Version 0.5:	- Now using Foundation Triggers (included) to load - no more overwriting of QuickBattle.py required.
		- We now come with our own Library - QBR is no longer required (see Requirements)
		- Added Single Player compatibility
		- Removed Engineering.py (plz delete the files scripts/Custom/QBautostart/Engineering.py(c) from your HD.
Version 0.4: Added ATP3 compatibility, current Transporter Version added.
Version 0.3: Now using Mutators - overwriting files is out!
Version 0.2: Added Compatibility for the QBR (its now working in QBR), AND Custom Bridges should now work in QBR.
Version 0.1: First Release (Engineering Extension)


Bugs:
<---------->
If you have Problems with this Mod:
Please Don't just tell me that "this is not working": Please give me the console output.
I can't help you without the output!


Modders:
<---------->
An init() section in every script is now required!
In the init section we store things like new event handlers and the creation of Buttons.
Please change your scripts todo so. We need that to make SP compatibility sure.

And please also add a MODINFO dict, that looks like this:
MODINFO = { "Author": "\"Defiant\" mail@defiant.homedns.org",
            "Download": "http://defiant.homedns.org/~erik/STBC/Marines/",
            "Version": "0.7",
            "License": "GPL",
            "Description": "This script allows you to beam Troops over to another Ship"
            }


License:
<---------->
GPL (see GPL.txt for details)

Some files included with this Mod are copied from the original Python 1.5 
and are Copyright 1991-1995 by Stichting Mathematisch Centrum, Amsterdam, The Netherlands.

"THIS MATERIAL IS NOT MADE OR SUPPORTED BY ACTIVISION."

LIMITATION ON DAMAGES. IN NO EVENT WILL ACTIVISION BE LIABLE FOR SPECIAL,
INCIDENTAL OR CONSEQUENTIAL DAMAGES RESULTING FROM POSSESSION, USE OR
MALFUNCTION OF THE PROGRAM OR PROGRAM UTILITIES, INCLUDING DAMAGES TO
PROPERTY, LOSS OF GOODWILL, COMPUTER FAILURE OR MALFUNCTION AND, TO THE
EXTENT PERMITTED BY LAW, DAMAGES FOR PERSONAL INJURIES, EVEN IF ACTIVISION
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.


Sorry for...:
<---------->
My Bad English.
