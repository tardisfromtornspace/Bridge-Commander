# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 20th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGPlasmaWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGPlasmaWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file is only added as base configuration, so if we need to change these parameters, we don't have to modify the main file.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes

import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
IonHullDamageMultiplier = 8 # For standard vessels, it deals 8 times the normal damage (8 -1 = 7 from this script)
IonGenericShieldDamageMultiplier = 1 # Fors tandard vessels, it deals no additional damage (1 -1 = 0 from this script)

legacyImmunity = []