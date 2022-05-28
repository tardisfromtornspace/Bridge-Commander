README:
==========
Version 0.1 (first alpha release)

This will make the Dominion bugships able to Ram their Target if they are outnumbered
or outgunned.


Requirements:
<---------->
-A Dominion bugship of course.


Author:
<---------->
Defiant <mail@defiant.homedns.org>
My STBC directory: http://defiant.homedns.org/~erik/STBC/


Install:
<---------->
1. Put the files into their right place.
2. Open the ftb Ship file of the bugship you use. Usually scripts/Custom/Ships/bug.py
   or scripts/Custom/Ships/bugship.py
3. At the top of the file you will find this:
   import Foundation
   import App
   after, add:
   import F_DomRamAI
4. Then a few line below look for something like:
   Foundation.ShipDef.bugship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
   Now Change Foundation.ShipDef or Foundation.FedShipDef or whatever you have there to
   F_DomRamAI.DomRamAI. So you get:
   Foundation.ShipDef.bugship = F_DomRamAI.DomRamAI(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Thats all. Now start the game.


Thx to:
<---------->
-jwattsjr for the Idea of calling a script.


Changes:
<---------->
Version 0.1: First Release


Bugs:
<---------->
-None known - not yet anyway.


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
