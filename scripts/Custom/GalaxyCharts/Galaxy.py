from bcdebug import debug
########################################################################################################################
###   Galaxy.py
###                 by Fernando Aluani, aka USS Frontier
#######################
# This is the main script of the Galaxy Charts mod.
# Well, not actually the main script, since there are others pretty important too, and this is more like a library...
# But still, this was the first script made for this mod, and the one which contains one of the most important things
# that make this mod be what it is.
# The functions that calculate Warp Speed, Time to warp from place A to B, and other related stuff.
# Also hold the version variable of this mod.
###
# NOTES:
#	- These functions, now with Galaxy Charts v1.1, are made to calculate the travel time, distance, etc, for any kind of travel.
#	  However, for backward compatibility, I won't rename them, changing "Warp" for "Travel" in the name of most of them.
#  	   (like GetWarpValues to GetTravelValues)
#	- Also, all fSpeed arguments that are needed to pass to these functions are speed in the "c" measurement unit.
#	  1 c = speed-of-light (in km/h)
#	  So, in other words, the fSpeed arg to be passed is how many times the speed-of-light the ship is travelling by.
########################################################################################################################
import App
import string
import math
import Custom.GravityFX.Logger
import GalaxyLIB
WarpFX_GUI = __import__('Custom.NanoFXv2.WarpFX.WarpFX_GUI')

#################################################
#  Global Mod Version Variable
#################################################
MOD_VERSION = 1.5

#################################################
#  Global Variables
#################################################
if GalaxyLIB.GetConfigValue("LogGalaxy") == 1:
	Logger = Custom.GravityFX.Logger.LogCreator("Main Galaxy Logger", "scripts\Custom\GalaxyCharts\Logs\GalaxyLOG.txt")
	Logger.LogString("Initialized Main Galaxy logger")
else:
	Logger = Custom.GravityFX.Logger.DummyLogger()

#################################################
#  Global Static Constants
#################################################
TRUE = 1                                     # bool value, true
FALSE = 0                                    # bool value, false
LIGHT_YEAR = 300000.0*60.0*60.0*24.0*365.0   # a light-year. in kilometers. (speed of light(km/s)*secs in 1 min*mins in 1 hour*hours in 1 day*days in 1 year)
LIGHT_SPEED = 1079252848.8                   # speed of light in kilometers per hour. (physics constant "c")

def CalculateTimeToTravel(pWasIn, pGoingTo, fSpeed, bReturnAllVariables):
	debug(__name__ + ", CalculateTimeToTravel")
	try:
		if pWasIn == None or pGoingTo == None:
			Logger.LogString("Can't calculate time to warp: WasIn or GoingTo is none")
			return None
		pWasRegion = pWasIn.GetRegion()
		pGoingRegion = pGoingTo.GetRegion()
		Logger.LogString("Calculating Time To Travel...")
		Logger.LogString(" -Was Set: "+pWasIn.GetName())
		Logger.LogString(" -GoingTo Set: "+pGoingTo.GetName())
		Logger.LogString(" -Was Region: "+str(pWasRegion))
		Logger.LogString(" -Going Region: "+str(pGoingRegion))

		# Get the distance to travel.
		if pWasRegion.Name == pGoingRegion.Name:
			iDist = pWasRegion.GetDistanceBetweenSystems(pWasIn.GetRegionModule(), pGoingTo.GetRegionModule())
			fCatetum = math.sqrt(math.pow(iDist, 2)/2)
			vDist = App.NiPoint2(fCatetum, fCatetum)
		else:
			vWasLoc = pWasRegion.GetLocation()
			vGoLoc = pGoingRegion.GetLocation()
			vDist = App.NiPoint2(vGoLoc.x - vWasLoc.x, vGoLoc.y - vWasLoc.y)
			iDist = vDist.Length()
	
		dWarpValues = GetWarpValues(iDist, fSpeed)
		Logger.LogString(" -Distance: "+str(iDist)+" lightyears")
		Logger.LogString(" -Speed (arg): "+str(fSpeed))
		Logger.LogString(" -Time to reach: "+str(dWarpValues['Time'])+" seconds")
		if bReturnAllVariables == 0:
			return dWarpValues['Time']
		else:
			dWarpValues['DistanceVector'] = vDist
			return dWarpValues
	except:
		LogError("CalculateTimeToTravel")

# This is the master function use to calculate the distance in kilometers, speed in km/h, and time needed to 
# warp that distance in seconds. All using the given distance in lightyears.
# Returns a dict containg the values: 'Time' in seconds, 'DistanceKM' returning the distance in KMs, 
# 'Speed' is the speed in kilometers per hour
def GetWarpValues(iDist, fSpeed):
	# Try to get the selected warp speed.
	debug(__name__ + ", GetWarpValues")
	fMaxTime = GetTimeToWarp(100000.0, App.g_kTravelManager.ConvertTravelTypeSpeedIntoCs("Warp", 9.99))
	dRealValues = GetTimeToWarp(iDist, fSpeed, 1)
	fRealTime = dRealValues['Time']
	TIME_FACTOR =  1.0/ (fMaxTime / GetUserTimeFactor())
	fTime = fRealTime * TIME_FACTOR

	# And finally, return all values, in a dict
	return {'Time': fTime, 'Speed': dRealValues['Speed'], 'DistanceKM': dRealValues['DistanceKM']}

def GetTimeToWarp(iDist, fSpeed, bReturnDict = 0):
	# Convert the distance, which is in lightyears, to kilometers.
	debug(__name__ + ", GetTimeToWarp")
	iDist = iDist * LIGHT_YEAR

	# Okay, we have the variables. Calculate the final one, the speed in which the ship is in. speed in km/h
	speed = LIGHT_SPEED*fSpeed

	# Now calculate the time in hours
	time = iDist / speed    
      
	# Now calculate the time in seconds
	secs = time * 60.0 * 60.0
	if bReturnDict == 0:
		return secs
	else:
		return {'Time': secs, 'Speed': speed, 'DistanceKM': iDist}

def GetWarpFactor(pShip = None):
	debug(__name__ + ", GetWarpFactor")
	try:
		if pShip == None:
			pShip = App.Game_GetCurrentPlayer()
		iWarpSpeed = pShip.GetWarpSpeed()
	except:
		iWarpSpeed = 7.0
	return iWarpSpeed

#####################################################################
# Helpers to return configurable variables
# These variables are set with UMM
#####################################################################
# GetUserTimeFactor()
#	- returns the time factor selected by the user, it is a float value in seconds, representing the amount of time
#	  that the user wants to spend travelling 100000lightyears at warp 9.99
#####################################################################
def GetUserTimeFactor():
	debug(__name__ + ", GetUserTimeFactor")
	pConfigScript = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.GalaxyChartsConfigValues")
	fUTF = pConfigScript.UserTimeFactor
	if fUTF < 1.0:
		fUTF = 1.0
	fMax = GetTimeToWarp(100000.0, 9.99)
	if fUTF > fMax:
		fUTF = fMax
	if App.g_kUtopiaModule.IsMultiplayer():
		fUTF = 60.0 * 3
	return fUTF

#####################################################################
#      Misc Helpers
#####################################################################
# a little helper to log an exception 
def LogError(strFromFunc):
	debug(__name__ + ", LogError")
	import sys
	et = sys.exc_info()
	if strFromFunc == None:
		strFromFunc = "???"
	if Logger:
		Logger.LogException(et, "ERROR at "+strFromFunc)
	else:
		error = str(et[0])+": "+str(et[1])
		print "ERROR at "+strFromFunc+", details -> "+error