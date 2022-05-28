README:
==========
0.8 (beta: all functions implemented, but maybe buggy)

This script allows you to beam Troops over to another Ship:
You will get a few new Buttons in the Engineering Menu.
Using the 'capture' button, your troops wil atack your current target.
If you target a subsystem, your crew will try to damage this, else they will to
capture the whole Ship.
Damaging a subsystem will take between 10 and 20 seconds, capturing up to 2 minutes.
And you can still loose your troops...
The Rescue Button can be used to rescue the Crew of a dying, friendly Ship,
and you can swap your Marines between Ships using the two transfer Buttons.

I also tried to make Miguels 'Scan Area' and 'Scan Target' useful in QuickBattle.


German people can get help at the Forum here: http://StarTrek.webhop.info


Requirements:
<---------->
-Engieering Extension 0.5 or higher.

The Shuttle Launching Framework by sleight42 is not required but maybe needed if
you want to create your own configuration files (optional).


Author:
<---------->
Defiant <mail@defiant.homedns.org>
My STBC directory: http://defiant.homedns.org/~erik/STBC/


Install:
<---------->
1. Please put the file into their right place.
   I will not answer any questions regarding "Where to put the file(s) in" - Just watch
   the directory structure.

2. (Optional) You may edit your Carrier files to set your Troops Number to a static Version.
   You are not required to do that, but it is always better, else the script will calculate
   the Number by using the Ship size.
   However you can two functions, GetNumMarines() (Number of attacking human) and 
   GetNumPeople() (Number of Crew flying this Ship, they can not be send to attack, but can
   help defending your vessel).
   See the file Carriers/Defiant.py in the examples/ -directory how to do that.
   And yes, you have to keep the Spaces (tab)!
   If you don't know what I'm talking about here, just leave the files untouched...
   

Thx to:
<---------->
Banbury for writing the first Transporter script,
Book (Lord Apophis ) for coming up with this Idea first,
Sim Rex for writing some code for the ReturnShuttles Mod, which I'm also using here and
the game Klingon Academy, being the model for this.


Todo, Bugs & Changes:
<---------->
see Marines.py for details
If you want to help writing, be welcome: mail@defiant.homedns.org


License:
<---------->
GPL (see GPL.txt for details)

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
