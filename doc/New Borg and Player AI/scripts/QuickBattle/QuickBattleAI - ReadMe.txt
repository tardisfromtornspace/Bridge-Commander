This file has been modified so that ships will
not try to Avoid Obstacles, and is necessary
to work in conjunction with the BorgAttack AI.
To offset the downside to this, I added the
Avoid Obstacles script into the FedAttack and
NonFedAttack default AI modules so that all
other classes will try not to crash into each
other.

Changes to this file was necessary for the new Player AI to
function properly. If the new Player AI is used with any 
other mods that uses this same file, then the changes listed
below must be included, and by doing so, should not cause 
any conflicts between mods.

import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, App.ObjectGroup_FromModule("QuickBattle.QuickBattle", "pFriendlies"), Difficulty = QuickBattle.GetCurrentAILevel(), MaxFiringRange = 1000.0, AggressivePulseWeapons = 0, ChooseSubsystemTargets = 1, DisableBeforeDestroy = 0, FollowTargetThroughWarp = 1, InaccurateTorps = 1, SmartShields = 0, UseRearTorps = 1)