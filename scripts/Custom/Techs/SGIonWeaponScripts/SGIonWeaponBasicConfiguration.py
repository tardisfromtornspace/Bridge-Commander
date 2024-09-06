# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 4th September 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.1
# Meant to be used alongside the SGIonWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGIonWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file is only added as base configuration, so if we need to change these parameters, we don't have to modify the main file.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes

import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
IonHullDamageMultiplier = 10
IonGenericShieldDamageMultiplier = 3.25

legacyImmunity = ["TheExile"]