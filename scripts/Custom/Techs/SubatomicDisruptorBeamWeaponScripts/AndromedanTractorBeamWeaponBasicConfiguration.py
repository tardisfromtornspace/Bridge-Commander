# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 5th February 2026, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SubatomicDisruptorBeam Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SubatomicDisruptorBeamWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file is only added as base configuration, so if we need to change these parameters, we don't have to modify the main file.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes

import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
SubatomicDisruptorBeamsHullDamageMultiplier = 1
SubatomicDisruptorBeamsGenericShieldDamageMultiplier = 1

legacyImmunity = []