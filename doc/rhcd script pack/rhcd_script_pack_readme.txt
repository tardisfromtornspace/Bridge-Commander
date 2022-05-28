RHCD Script Pack v1.05

Written by Brian Moler (RedHotChiliDog) 
brianmoler.com: http://www.brianmoler.com



OVERVIEW

Version 1.05 is a maintenance release that fixes a few minor issues with the script pack:
1) Corrected issue with menu options launching incorrect missions.
2) Exit the "no-win" scripts automatically if the player should somehow manage to beat them.  Previously, 
the ESC key had to be used to terminate the "no-win" scripts if the player beat them.
3) Fixed problem with mission ending prematurely before all waves of ships entered game.
Thanks to dwyspock for finding these issues and beta testing version 1.05 of the pack.

Version 1.04 adds a new script called "Random Skirmish".  There are now a total of 4 different classes of 
missions in my pack that is comprised of 11 variants.

Version 1.03 brings my script pack up to the latest Foundation standards.  Because I want to maintain 
compatibility with Foundation and the Bridge Commander game, I am no longer providing a modified version 
of the main menu script with this script pack.  I have redesigned the missions to work under the TestMode 
option specially designed for custom scripts.  Since I am no longer modifying the mainmenu script, this 
script pack no longer overwrites any of the original BC files.


This is an eleven script pack that contains the following missions:

KOBAYASHI MARU:
1) A TNG version with the player being a Sovereign class up against 9 Klingon Vorcha attack cruisers.
2) A TNG version with the player being a Sovereign class up against 9 Romulan D'Deridex Warbirds.
3) A TOS (classic) version with the player being P81's NCC1701 up against 9 of P81's Klingon D7s.
4) A TNG version with the player being a Sovereign class up against 9 Cardassian Keldons.

This is based on the Kobayashi Maru test from the ST2 movie.

You start in the Voltair I system, where you are briefed.  After the briefing, you can then warp to the 
Voltair II system, in an attempt to rescue the heavily damaged freighter Kobayashi Maru.  The bordering 
neighbor will not like this intrusion into the neutral zone!  They will arrive in three waves of three
ships each.

These scripts are basically my "Hello World" introduction to the Bridge Commander implementation of the 
Python language.  I was able to use the M4Complex tutorial script as a template, as it contained many of 
the features that I needed for this script.  I really only had to move around a bit of code and remove some 
stuff that was not needed for the mission.  All I had to do after that, was implement a function to restrict 
the player from warping to Voltair II until the mission briefing had completed, add code to automatically 
send the player's ship into red alert, change the ship classes for both friendly and enemy ships, increase the 
distances between the friendly and enemy ships, add logic for multiple waves of ships, and create new TGL files 
for the mission text.


TARGET OF OPPORTUNITY:
5) A version that has the player fighting a Klingon fleet.
6) A version that has the player fighting a Romulan fleet.
7) A version that has the player fighting a Cardassian fleet.

You are on a routine patrol of the enemy border, when you discover a large force amassed on their 
side. Your intelligence finds out that they are staging a surprise invasion. Your orders have you  
cross the border and destroy this force, hoping that it will delay or halt the enemy invasion plans. 
You catch the enemy ships flat-footed, as they are at a green alert status. Each enemy ship is 
scripted to activate at a completely random interval.

You will see an enemy fleet in the Yiles II system.  You have caught them off-guard, so they are not 
prepared for your attack.  Their AI will not be activated until a random time has expired.  Each ship is on 
a different timer, so it is possible for ALL enemy ships to activate at the same time, or they could all take 
different times to activate. In any event, it is obvious that you will want to do as much damage as possible 
before they become active!

You start in the Yiles I system, where you are briefed.  After the briefing, you can then warp to the 
Yiles II system, in an attempt to destroy the enemy fleet.  If the mission is going badly for you, you may 
opt to warp back to Yiles I, but you will lose the mission by doing so.


OVERRUN DEFENSE:
8) A version that has the player fighting waves of Klingon Vorchas.
9) A version that has the player fighting waves of Romulan Warbirds.
10) A version that has the player fighting waves of Cardassian Keldons.

This is a three script pack that has the player defending a friendly base from wave after wave of enemy 
ships.  The player ship will have a wing of friendly ships that he may command in the battle.  The battle 
will consist of 10 waves of three enemy ships.  Each wave will enter 4 minutes apart from each other. 
You are to keep on fighting until you are completely overwhelmed.  This is a test of your ability to 
command a small taskforce in an impossible situation, not unlike the Kobayashi Maru.

Each wave of enemy ships will contain 3 ships and will appear 4 minutes apart, except for the Cardassian 
version, where they will appear 3 minutes apart.  This is because the Cardassian ships are really weak, and my 
attempt to use the Hybrid instead of the Keldon, resulted in the player being killed much too early!  I just 
decided to bump their entry time down one minute instead to compensate.

In each case, you are defending a Federation starbase, and you will have a small fleet that consists of 
a Galaxy, Akira, and Nebula that you can issue orders to.

You start in the Poseidon I system, where you are briefed.  After the briefing, you can then warp to the 
Poseidon II system, in an attempt to defend the friendly starbase.


RANDOM SKIRMISH
11) One version that randomly assigns a single player and single enemy vessel.

Random skirmish is a simple script that randomly determines the player's ship and the enemy ship.  The 
player will warp to Yiles II and attempt to defeat this random opponent.  Right now, I have hard-coded 
the random ship selections in the script using the stock ships that come with the game.  The player may 
configure this script to use mods by simply altering the g_PlayerShipClassList and g_EnemyShipClassList 
globals in M11.py.  Here are the defaults for these lists as I provide them:

g_PlayerShipClassList = ["Akira", "Ambassador", "BirdOfPrey", "CardHybrid", "Galaxy", "Galor", "Keldon", "KessokHeavy", "KessokLight", "Marauder", "Nebula", "Sovereign", "Vorcha", "Warbird"]
g_EnemyShipClassList  = ["Akira", "Ambassador", "BirdOfPrey", "CardHybrid", "Galaxy", "Galor", "Keldon", "KessokHeavy", "KessokLight", "Marauder", "Nebula", "Sovereign", "Vorcha", "Warbird"]

The existing entries may be altered and additional entries may be added to the lists.



REQUIREMENTS

Here is all you need for requirements:

1) Version 1.1 of Bridge Commander.

2) Dasher42's Foundation system.  These were tested against version 20020530b of the Foundation system.  The only 
reason you need the Foundation system, is so that the required ship mods necessary for the TOS version of this script 
can be installed.

3) P81's Enterprise NCC1701 and P81's TOS D7 mods.  These are required for the TOS version of these scripts.



INSTALLATION

None of the files in this mod will overwrite anything from the retail version of the game.  You can simply 
unzip the contents into your Bridge Commander folder.  It also should have no ill effects on Dasher42's 
Foundation Plug-In system for adding ship mods to the game.  I have tested these missions using the 20020530b 
version of the Foundation Plug-In system.  Make sure you are only running version 1.1 of the BC game.

Make sure you enable the "Use Folder Names" option for Winzip when extracting the files for my missions.  You can 
then take the extracted Data and Scripts folders from my zip archive and copy them to the main BC folder.  That's 
all you need to do for installing the new scripts!

To play the scripts, you will have to run Bridge Commander in TestMode.  To do this, you can modify the startmenu 
link to your Bridge Commander game by right-clicking the shortcut and selecting properties from the menu.  On the 
shortcut tab, you will see the target option.  Modify the target to have the -TestMode switch like so:

"C:\Program Files\Activision\Bridge Commander\stbc.exe" -TestMode

You can then run Bridge Commander using this shortcut and the new missions should appear under the 
custom menu as "RHCD Scripts".



SUPPORT

If you have any questions or problems regarding these scripts, please e-mail me at bmoler@brianmoler.com.  
Activision does not support the Python SDK or any of the custom missions made using it.



KNOWN ISSUES

None



LEGAL

Mod created by Brian Keith Moler (RedHotChiliDog).  STARTREK and all related marks are trademarks of Paramount 
Pictures, all rights reserved. Bridge Commander Software copyright 2001 Activision, Inc, All rights reserved. 
Activision and the Activision logo are trademarks of Activision, Inc. Totally Games and the Totally Games logo 
are trademarks of Totally Games, Inc. All other copyrights and trademarks are the property of their respective 
owners.

I have included the source code with these missions.  You are permitted to modify or take portions of the original 
source code to create your own missions, as long as you credit me as the original author. You are also free to 
include these missions as part of a modpack or distribute them in any way you please, as long as it is for free, 
does not violate Activision's EULA (End User Licensing Agreement) and you give me credit for being the author of 
the original scripts.


