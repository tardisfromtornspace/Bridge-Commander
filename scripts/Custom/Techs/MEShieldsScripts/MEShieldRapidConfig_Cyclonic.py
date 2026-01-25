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
	"Name": "Cyclonic",
	"CollisionBlock" : 1,
	"BypassMultiplier": 1,
	"FacetFactor": 0,
	"FacetRegeneration": 0,
	"MinimumSpeedTrigger": 5,
	"MaximumSpeedTrigger": -260,
	"AtmosphericNerf": -1,
}