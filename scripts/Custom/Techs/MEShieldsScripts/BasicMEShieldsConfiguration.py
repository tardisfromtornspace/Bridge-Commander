# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file is only added as base configuration, so if we need to change these parameters, we don't have to modify the main file.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes

import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
defaultPassThroughDmgMult = 1.0 # For things that need to actually do bleedtrough... how much?

shieldGoodThreshold = 0.400001 # From this value downwards, ME special bleedthrough block will not work.
shieldPiercedThreshold = 0.2 #0.25 # Below this value shields are definetely pierced, so full bleedthrough!

SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us when a ship is too small, to prevent a torpedo from just teleporting to the other side

globalRegularShieldReduction = 0.5 # When it's a ME shield vs normal shield during a collision, we take reduced shield damage

RaceShieldTechGlobalConfig = {
	"Name": "Default",
	"CollisionBlock" : 0,
	"BypassMultiplier": 1,
	"FacetFactor": 0,
	"FacetRegeneration": 0,
	"MinimumSpeedTrigger": 5,
	"MaximumSpeedTrigger": 100,
	"AtmosphericNerf": -1,
}