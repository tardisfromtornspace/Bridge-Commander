Tech Framework 1.1
========================

Short Version:
--------------
After installing you will get a new ship, "Galaxy + Carrier", use this one to launch
Shuttles. If you also want other ships to launch shuttles, read
"How to make a ship capable of launching Shuttles.pdf"


INCLUDES:
--------------
Launching Framework
	originally by Evan Light aka sleight42
	
Secondary Targetting
	originally by Evan Light aka sleight42

New Technology System
	originally by Sim Rex
	
Return Shuttles
	originally by Defiant
	http://dynamic3.gamespy.com/~bridgecommander/phpBB/viewtopic.php?t=10320 for details.


Author is sleight42, sleight42 and only sleight42, but since
sleight42 is not programming for Bridge Commander anymore, we
decided to release our own version.
This package is maintained by {Sim Rex, jwattsjr, Admiral Ames and Defiant}.
We fixed the bugs out of it, added a new options and packed them together.
This is mainly a fork of the original Launching Framework by sleight42 which is no longer
supported. Project leader is Defiant.
Authors email:
	-Admiral Ames: admiral_ames@sfhq.net
	-Sim Rex: simrex@hotmail.com
	-MLeoDaalder: MLeoDaalder@netscape.net
	-jwattsjr: jwattsjr@adelphia.net
	-Defiant: erik@defiant.homedns.org
For details who is responsible for what see Changes.txt


INSTALLATION
------------
Copy the folders data/ scripts/ and sfx/ and maybe Examples/ into your Bridge Commander
install's directory.
You should also copy the files from Examples/ into your main Bridge Commander install,
to get your Galaxy configured for Launching. Please make sure that you always copy both,
scripts/Custom/Carriers/Dauntless.py AND scripts/ships/Hardpoints/Galaxy.py - else the
Game will not load! -If you don't do that, your first ships (the Galaxy) will not be
configured for launching - then the Framework will not show up - DON'T BLAME US IF THAT HAPPEN!
To use the secondary Targetting you should set 'Single Fire' to 0. Only the Phasers can
currently use the Secondary Targetting. Make sure your Targets are in Phaser range before
telling us, that 'this is not working'.
If you upgrade from the old Shuttle Launching Framework please also copy the contents of
Fixes/ into your BC install.


GET SUPPORT
------------
If you have problems or any question, please post here:
	http://dynamic3.gamespy.com/~bridgecommander/phpBB/index.php
We will answer as fast as we can.


FOR MODDERS
-----------
NewTechnologySysten is a system designed to make it easier to add new features to
QuickBattle games, for exciting new additions to the game along the lines of sleight42's
Launching Framework.

The Carrier class may be subclassed to suit any class of ship with a shuttle bay.
Also, a Carrier can carry any type of ship (including of it's own type) in any variety and
quantity.  Loadouts are now accomplished through the Launcher instances which, in turn,
can optionally be grouped within LauncherGroup instances. See "Dauntless.py" for an example.

You can find a very good documentation by Dragon_UK on howto setup ship up for launching shuttles
in the Documentation/ -folder.

You can find a web application that can automaticly create a carrier file for you
here: http://defiant.homedns.org/~erik/STBC/carrier/
Now all you have to do is adding Shuttle Bays to your Hardpoint file. 


KNOWN BUGS
----------
- Switching from a Carrier vessel to a non-Carrier results in the Launch buttons still being displayed
  on the Science Menu
- Shuttle Launching Framework will not load when the Player's ship does not support that.
- If you decide to use the Engineering / QBautostart Extension with this then please upgrade
  to atleast Version 0.6.


CREDITS
----------
Thanks to Banbury for his GetShipList() snippet,
and Dasher for the version in the Foundation.
-Sim Rex for a few functions, many help and his NTS
-BCU community for that nice Idea.
-Sleight42 for his Shuttle Launching Framework: Some parts of this script are based on this Framework.
-Admiral Ames for his Idea to exclude Tractors


LICENSE
----------
All scripts in this package are under the GPL (gpl.txt for details)

"THIS MATERIAL IS NOT MADE OR SUPPORTED BY ACTIVISION."

LIMITATION ON DAMAGES. IN NO EVENT WILL ACTIVISION BE LIABLE FOR SPECIAL,
INCIDENTAL OR CONSEQUENTIAL DAMAGES RESULTING FROM POSSESSION, USE OR
MALFUNCTION OF THE PROGRAM OR PROGRAM UTILITIES, INCLUDING DAMAGES TO
PROPERTY, LOSS OF GOODWILL, COMPUTER FAILURE OR MALFUNCTION AND, TO THE
EXTENT PERMITTED BY LAW, DAMAGES FOR PERSONAL INJURIES, EVEN IF ACTIVISION
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
