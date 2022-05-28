##########################################################################
## Borg AI Final - 10 July 2008                                         ##
## By: jayce AKA Resistance Is Futile                                   ##
##                                                                      ##
## This will be the final version of the Borg AI. It is also the        ##
## The smartest version of the Borg AI with improvements over the       ##
## Previous versions which includes: a smarter target selection         ##
## Process, the ability to focus group attacks on specific targets,     ##
## The ability to now intercept targets, the ability to now follow a    ##
## Target through warp, the ability to now avoid obstacles, and of      ##
## Course, the ability to attack multiple targets simutaniously while   ##
## Moving, not stationary. Online Friendly.                             ##
##                                                                      ##
## Special thanks once again to Defiant for turning me onto some of     ##
## The workings of the AI Distributes Building feature shown below.     ##
##                                                                      ##
## As always, use at your own risk. You are free to distribute but      ##
## **Do Not Modify The Borg AI Final**                                  ##
##########################################################################

*NOTE* This AI can replace the current Borg AI found in use in KM1.0

Credits:

The python files included has been created by jayce and some
assistance from Defiant with the exception of the BasicAttack AI.
The original author or modifier of this file is unknown for me to
give the proper credits. Aparently, it is necessary in order to use
the BorgAttack AI in Quickbattle. It was obtain undoubtedly in one
of the very many downloads of Borg vessels that I have acquired
over the the years, with most new downloads replacing the older
one. The BasicAttack.py AI file was not altered in any way, so if
the author sees their handywork, please contact me and claim it.

About The AI:

This AI comes equipped with both primary and secondary (or multiple)
targetting, previously only accessible by Starbases. The primary 
target within sensor range will be selected based on it's particular
threat assessment as determined by a ship's hull, shields, weapons,
and damage inflicted status. The AI will check the assessment every
few seconds. It will also enable multiple Borg ships to work together
more efficiently in their attack patterns, while attempting to avoid
colliding with each other or any other object as well. This AI will
now intercept the primary target at great distances and will also
pursue the last remaining target through warp between star systems.

Requirements:

	Star Trek Bridge Commander v1.1
	Working Non-Player-Controlled BorgAttackAI Ships

Installation:

To ensure that this AI remains in its stable condition, it is being
distributed in its more secured Compiled Python File (.pyc) form.
There are scripts included in this AI that can not be recreated by
using the AI Editor. This is the main reason why I chose to use the
(.pyc) file. This also means that we have to remove any other AI with
the exact same name not only in (.pyc) form, but also the less secured
Python File (.py) form before installing this AI.

1. Create a Temporary Folder on your Desktop and name it "BC BACKUP".
2. Open your: Activision/Bridge Commander/Scripts/AI/Compound folder.
3. Move any (.py) and/or (.pyc) file named BorgAttack and BasicAttack
	into the "BC BACKUP" folder if you have them.
4. Copy the new BorgAttack.pyc file from the Borg AI Final folder into
	the Activision/Bridge Commander/Scripts/AI/Compound folder.
5. Copy the new BasicAttack.py file from the Borg AI Final folder into
	the Activision/Bridge Commander/Scripts/AI/Compound folder.
6. Open your: Activision/Bridge Commander/Scripts/AI/Compound/Parts
	folder.
7. Move any (.py) and/or (.pyc) file named ICOMove1 if you have them
	into the the "BC BACKUP" folder.
	*NOTE* Step 7 is removing a file(s) that no longer serves a
	purpose.
8. Start game and enjoy.
9. Delete the Temporary Folder on your Desktop if no errors occur on
	installation and after reading and complying with README file.

Reminders About Overrights:

This file can easily be replace by any (.py) file of the exact same
name. Since (.py) and (.pyc) files are technically not the same, you
will get no warning of overright if you add/install a (.py) file with
the exact same name. And once you start the game, you will lose this
file because BC will automatically replace it with another (.pyc) as
soon as the game tries to use this AI. This kind of overright is
usually done when installing new mods that come equipped with their
own AI. Take extra care not to overright BasicAttack.py(c) or the
BorgAttack.pyc as these are the most common to be replaced.

Distributers:

If you distribute this AI with another mod, make every attempt to list
this AI version clearly in your readme file so that people can know
that it's safe to overright if they want to. If you distribute this AI
with another mod, it must contain the entire AI and not just parts of
it. Meaning if you distribute the Borg AI, it needs to contain both
the BorgAttack.pyc and the BasicAttack.py together with the mod. I 
absolutely do not want to see any BorgAttack.py files from this AI 
distributed with any other mods. Period. The last thing I want to hear
is how someone's AI is not working right because of an altered (.py)
file. There is a reason why this AI is being released in (.pyc) form.

Final Note:

If you have any problems with this AI, then simply remove this AI and
restore the files in the "BC BACKUP" folder. Contact me referencing
this version. Only files with the correct Date/Time stamps will
receive assistance.

If you do not comply with any part of this README file, then simply do
not install this AI, or remove this AI and restore the files in the
"BC BACKUP" folder.

This AI will be the last AI that I create as I will no longer be
making smarter AI's. I may still tweak an AI or two here and there.
So do try and enjoy this AI until someone comes along and makes a
better one. If you are curious about this AI or have any questions,
contact me. I occassionally will try and check up on any AI talk on 
the popular forum boards, especially when concerning anything Borg
related.

Changes from BorgAI 1.0 (used in KM1.0):

Added ability to Intercept targets
Added ability to Avoid Obstacles
Added ability to Follow A Target Through Warp
Added ability to Attack in Groups
Minor tweaks to Target Selection and Attack Rate

Bugs:

None

Legal Disclaimer:

Use at your own risk.