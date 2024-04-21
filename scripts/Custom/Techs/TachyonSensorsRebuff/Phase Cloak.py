# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 21st April 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used along with the Tachyon Sensors Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/TachyonSensorsRebuff
# As these are Sub-techs with some leeway, their manuals must be explained here.
# However, ALL of them have a thing in coommon - they must have a "chance" function and/or a "distance" multiplier function
# chance will give chances in the 0.0(impossible)-1.0(certain) range. If you don't want to affect rates, do not add this function, or return the pChance input value
# distance provides a range multiplier - If you don't want to affect distances, do not add this function, or return the pDistance input value
# In both cases, the "pSensorRange" input is the range of the ship which is scanning the others.
##################################
# SPECIFIC SUB-TECH MANUAL:
# This tech adds a modifier to the chances of being spotted by Tachyon Sensors tech while being cloaked. Specifically, it makes it impossible for a ship with
# Tachyon Sensors to spot the scanned ship.
# How-to-use:
# On this case, this is just to add something to a pre-existing tech, no special fields. However, for other technologies, it may be necessary.
####
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative it becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well

def chance(pScannerShip, pScannedShip, pScannerInstanceDict, pScannedInstanceDict, pChance, pSensorRange):
	debug(__name__ + ", chance")
	# For Phase Cloak is simple, unconditionally undetectable by Tachyon Sensors
	return 0.0

def distance(pScannerShip, pScannedShip, pScannerInstanceDict, pScannedInstanceDict, pDistance, pSensorRange):
	debug(__name__ + ", distance")
	return pDistance