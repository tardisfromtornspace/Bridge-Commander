# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 26th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file is only added as base configuration, so if we need to change these parameters, we don't have to modify the main file.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes

import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
defaultPassThroughDmgMult = 0.1 # For things that need to actually do bleedtrough... how much?

shieldGoodThreshold = 0.400001 # From this value downwards, SG special bleedthrough block will not work.
shieldPiercedThreshold = 0.25 # Below this value shields are definetely pierced, so full bleedthrough!

SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us when a ship is too small, to prevent a torpedo from just teleporting to the other side

globalRegularShieldReduction = 0.5 # When it's a SG shield vs normal shield during a collision, we take reduced shield damage

oriMultifact = 4.0 # Default "how-many-times-the-shield-regen-facet" are required for Ori ships to use their special shield thingy 