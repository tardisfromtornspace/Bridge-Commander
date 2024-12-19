# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds the rapid-config-option "Cyclonic" race to ME Shields.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

RaceShieldTechGlobalConfig = {
	"Name": "Reaper",
	"CollisionBlock" : 2,
	"BypassMultiplier": 0.5,
	"FacetFactor": 3,
	"FacetRegeneration": 1,
	"MinimumSpeedTrigger": -1,
	"MaximumSpeedTrigger": -512,
	"AtmosphericNerf": -1,
}