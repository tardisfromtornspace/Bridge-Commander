from bcdebug import debug
################################################################
#######  Gravity FX Functions Library ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# This is the function library for GravityFX (tho i may use some functions that are here in other mods)
# It contains functions about a bunch of stuff, except GUI related stuff, because there is the GravityFXguilib 
###################
# UPDATED - in Galaxy Charts v2
###########################
##### Imports #####
import math
import App
import string
import MissionLib
import Foundation

NonSerializedObjects = (
"ConvertKMtoGU",
"ConvertGUtoKM",
)

############################################################################################################
##class##     RefreshEventHandler
######################################
# This class purpose is to create a refresh event, that will continuate to call the determined function, with the determined
#  delay time between calls.
###############################################################################################
#@@@@@@ initializing/creating the RefreshEventHandler
######
# 	- initialize: RefreshEventHandler(sFunc, nDelay = 0.1, sMode = 'NORMAL') 
#		- sFunc: is your function that will be called, her 2 initial args must be pObject, pEvent
#			   Also, the function must NOT have any return statements, or it will cause the Refresher to stop (i think)
#			 NOTE: it is really a function, not a string.
#		- nDelay: it is the delay between calls, defaults to 0.1
#		- sMode: the priority of the event, it can be: 'UNSTOPPABLE', 'CRITICAL', 'NORMAL' and 'LOW',
#		         defaults to 'NORMAL'
###############################################################################################
#@@@@@@ The IconCreator atributes
######
#	- RefreshEventHandler.CLASS -> a string representing the object class.
#	- RefreshEventHandler -> the IconCreator object, it comes with her own unique ID
###############################################################################################
#@@@@@@ The function to edit a value of the event    and to delete the event
######
#	-EditHandler(sType, nValue)
#		- sType: the type of value to be used, it can be:
#			-"Delay": to change the delay of the event
#			-"Priority": to change the priority of the event
#			-"Function": to change the function that is called.
#		- nValue: the value to be set, according to the type selected.
#			-For Delay, use a float.
#			-For Priority, use one of the above mentioned priority strings.
#			-For Function, use a function  duh...
######################################################################################################################
class RefreshEventHandler:
	def __init__(self, sFunc, nDelay = 0.1, sMode = 'NORMAL', nLifetime = 0, sFinalFunc = None):
		debug(__name__ + ", __init__")
		self.ModeDict = {'UNSTOPPABLE': App.TimeSliceProcess.UNSTOPPABLE, 'CRITICAL': App.TimeSliceProcess.CRITICAL, 'NORMAL': App.TimeSliceProcess.NORMAL, 'LOW': App.TimeSliceProcess.LOW}
		self.ID = GetUniqueID("RefreshEventHandler")
		self.CLASS = 'Refresh Event Handler'
		self.Function = sFunc
          	self.Delay = nDelay
		self.Age = 0
		self.Lifetime = nLifetime
		self.FinalFunction = sFinalFunc
		self.StartRefreshHandler(sMode)
	
	def Refresh(self, pObject = None, pEvent = None):
		debug(__name__ + ", Refresh")
		if self.Lifetime != 0:
			if self.Age < self.Lifetime:
				self.Function(pObject, pEvent)
				self.Age = self.Age + self.Delay
			else:
				if self.FinalFunction != None:
					self.FinalFunction(pObject, pEvent)
					self.StopRefreshHandler()
		else:
			self.Function(pObject, pEvent)			

	def EditHandler(self, sType, nValue):
		debug(__name__ + ", EditHandler")
		if sType == "Delay":
			self.Delay = nValue
			self._Refresher.SetDelay(self.Delay)
		elif sType == "Priority":
			if nValue == 'UNSTOPPABLE' or nValue == 'CRITICAL' or nValue == 'NORMAL' or nValue == 'LOW':
				self._Refresher.SetPriority(self.ModeDict[nValue])
			else:
				print "Value", nValue, " given to RefreshEventHandler", self.ID, " EditHandler(", sType, ") is invalid."
		elif sType == "Function":
			self.Function = nValue
		elif sType == "FinalFunction":
			self.FinalFunction = nValue
		elif sType == "Age":
			self.Age = nValue
		elif sType == "Lifetime":
			self.Lifetime = nValue
		else:
			print "Type", sType, " given to RefreshEventHandler", self.ID, " EditHandler(", sType, ") is invalid."

	def StartRefreshHandler(self, sMode):
		debug(__name__ + ", StartRefreshHandler")
		self._Refresher = App.PythonMethodProcess()
		self._Refresher.SetInstance(self)
		self._Refresher.SetFunction("Refresh")
		self._Refresher.SetDelay(self.Delay)
		self._Refresher.SetPriority(self.ModeDict[sMode])

	def StopRefreshHandler(self):
		debug(__name__ + ", StopRefreshHandler")
		if self._Refresher:
			self._Refresher.__del__()
			self._Refresher = None

	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.ID+">"

################################################################
#  The Gravity Constant
###
# Constant variable used in various gravity force related calculations
# - Real Physics value - don't change.
################################################################
gcons = 6.67e-017

################################################################
###    GetGravForce
#plamass --> em Kg
# distance --> distance to object in GameUnits
##return ==> km/h²  (wihout the /3.6 -> return em m/s²)
################################################################
def GetGravForce(plamass, distance):
	debug(__name__ + ", GetGravForce")
	global gcons
	Factor = GetConfigValue("MultiplyFactor")
	dkm = ConvertGUtoKM(distance)
	#print "G:", gcons, "|Mass:", plamass, "|Fac:", Factor, "|Dist:", dkm
	f = (gcons*plamass*Factor)/math.pow(dkm, 2)
	return f/3.6

################################################################
##    GetMaxGravForceDist
#return in GameUnits  
#the distance of the planet with given mass that the gravity force will be 0.1m/s^2  (0.02km/h^2)
#App.UtopiaModule_ConvertGameUnitsToKilometers()
################################################################
def GetMaxGravForceDist(plamass):
	debug(__name__ + ", GetMaxGravForceDist")
	if plamass > 0:
		global gcons
		Factor = GetConfigValue("MultiplyFactor")
		dkm = math.sqrt(gcons*plamass*Factor*10)
		dgu = ConvertKMtoGU(dkm)
		return dgu
	return 0

################################################################
#Helper function to convert Km/h speed units into BC's impulse speed units and vice-versa
################################################################
def ConvertKMHtoImpulse(speed):
	debug(__name__ + ", ConvertKMHtoImpulse")
	return speed/630.0

def ConvertImpulsetoKMH(speed):
	debug(__name__ + ", ConvertImpulsetoKMH")
	return speed*630.0

################################################################
#Helper function to convert Km distance units into BC's game units and vice-versa
################################################################
ConvertKMtoGU = App.UtopiaModule_ConvertKilometersToGameUnits

ConvertGUtoKM = App.UtopiaModule_ConvertGameUnitsToKilometers

########################################################################
## escvel          (escape velocity)            -I'm not sure if it is working correctly
# NOTE: altho this turned out to not be required to create gravity, it's best to leave it here.
# well - the gravity well
#distance - distance to object?  in game units
#return -> velocity in km/h              (without the /3.6 -> return em m/s)
################################################################
def escvel(well, distance):
	debug(__name__ + ", escvel")
	plamass = well.GetMass()
	global gcons
	dkm = ConvertGUtoKM(distance)
	v = math.sqrt(2*(gcons*plamass)/dkm)
	return v/3.6

######################################################
# GetMassByRadius
#radius --> in Km 
#density --> default 5.515 (Earth's density)
#return ==> mass in Kg
################################################################
densityConversionConst = 1000000000000.0  #math.pow(10, 12)
def GetMassByRadius(radius, density = 5.515):
	debug(__name__ + ", GetMassByRadius")
	global densityConversionConst
	nKesph = 4.0/3.0
	vol = nKesph*math.pi*math.pow(radius, 3)
	mass = (density*densityConversionConst)*vol
	return mass

######################################################
# GetMassByMaxDistance
# - used the get the mass of an object by giving the max distance of his grav well.
#distance --> in Km
#return ==> mass in Kg
################################################################
def GetMassByMaxDistance(distance):
	debug(__name__ + ", GetMassByMaxDistance")
	global gcons
	mass = 0.1*math.pow(distance, 2)/gcons
	return mass/GetConfigValue("MultiplyFactor")

################################################################
#These three newton's 2º law functions aren't needed, GetGravForce already returns the acceleration
################################################################
def GetForce(mass, acceleration):
	debug(__name__ + ", GetForce")
	return mass*acceleration

def GetAcceleration(force, mass):
	debug(__name__ + ", GetAcceleration")
	return force/mass

def GetMassByForceAccel(force, acceleration):
	debug(__name__ + ", GetMassByForceAccel")
	return force/acceleration

################################################################
##  GetVectorFromTo
# return the vector from the ship to the planet
# unitize --> if 1, will return the vector unitized, if != than 1, returns the TGPoint3
################################################################
def GetVectorFromTo(ship, planet, unitize = 1):
	debug(__name__ + ", GetVectorFromTo")
	vec = ship.GetWorldLocation()
	vec.Subtract(planet.GetWorldLocation())
	if unitize == 1:
		vec.Unitize()
	debug(__name__ + ", GetVectorFromTo Done")
	return vec

def GetVectorFromToByPoints(point1, point2, unitize = 1):
	debug(__name__ + ", GetVectorFromToByPoints")
	Vec1 = App.TGPoint3()
	Vec1.SetXYZ(point1.x, point1.y, point1.z)
	Vec2 = App.TGPoint3()
	Vec2.SetXYZ(point2.x, point2.y, point2.z)
	Vec1.Subtract(Vec2)
	if unitize == 1:
		Vec1.Unitize()
	return Vec1

################################################################
## DistanceCheck
#  - returns the length between object 1 and 2
#  - it is the same then getting the vector from GetVectorFromTo
#	without unitizing and then using .Length() in it
#It's best here, leaves the main script cleaner
################################################################
def DistanceCheck(pObject1, pObject2):
	debug(__name__ + ", DistanceCheck")
	if pObject1 == None or pObject2 == None:
		return None
	Vec = pObject1.GetWorldLocation()
	Vec.Subtract(pObject2.GetWorldLocation())

	return Vec.Length()

################################################################
## DistanceOfPoints
#  - returns the length between vectors Point1 and Point2
# * yes, it's the same as DistanceCheck, but with the vector directly, and not with objs
################################################################
def DistanceOfPoints(Point1, Point2):
	debug(__name__ + ", DistanceOfPoints")
	if Point1 == None or Point2 == None:
		return None
	Vec = GetVectorFromToByPoints(Point1, Point2, 0)
	return Vec.Length()

################################################################
## IsShipWithinWell
# pShip --> the ship instance to be checked if it is within the well
# pWell --> gravity well instance to be checked upon
# return - 1 if the ship is within the well, 2 if the ship is within the well damage radius
#	     None if the ship isn't within the well
################################################################
def IsShipWithinWell(pShip, pWell):
	debug(__name__ + ", IsShipWithinWell")
	if pShip == None or pWell == None:
		return None
	nDist = DistanceCheck(pWell.Parent, pShip)
	if nDist <= pWell.Radius:
		if pWell.MaxDamageDistance > 0 and nDist <= pWell.MaxDamageDistance:
			return 2
		else:
			return 1
	else:
		return None

################################################################################################################
##   IsAtmosphereObj
#########
#This function is important to determine if a planet was created by NanoFX AtmosphereFX.
# why? because AtmosphereFX creates 4 planet/sun objects in the same spot as a planet to make the AtmosphereFX effects
# and that to GravityFX would mean 5 gravity wells in the same spot, and that isn't nice. So this was made so that
# GravityFX could determine what planet/sun object were created by AtmosphereFX, and then NOT apply a gravity well to it.
#
#This returns 1 if the planet is one of the planet objects created by AtmosphereFX, this checks it by seeing the last word 
#of the planet's name, because AtmosphereFX creates it's objects with the planet's name + " Air", " Clouds", " Glow" or " Planet"
#if the last word is any one of one of these 4 words it'll return 1, else it will return None.
#BEWARE: if there are any planets in any system mod out there to use that by nature have any of these words as a planet's name last word
# this will return 1 yet.
# This problem can be fixed by making that the planets created by AtmosphereFX have a special variable, that defines that they were
# created by AtmosphereFX, but until i'm able to modify/override NanoFXv2, this function will continue to be like the way it is now.
##
# this is an unbound method of App.Planet Class
################################################################
def IsAtmosphereObj(self):
	debug(__name__ + ", IsAtmosphereObj")
	name = self.GetName()
	nameext = string.split(name)
	if nameext[-1] == "Planet":
		return 1
	elif nameext[-1] == "Air":
		return 1
	elif nameext[-1] == "Clouds":
		return 1
	elif nameext[-1] == "Glow":
		return 1
	else:
		return None

################################################################################################################
## ShowGravityWellGlow
#######
# this function creates that glow on a planet, to resemble the gravity well. Used by GravSensorsOptGUI when the Player
# is using the BC Map (3D map), so that the Player can see on the map where are the gravity wells.
#
# nSize --> the size of the glow/gravitywell. The glow/gravitywell goes from the planet radius until this point.
#           defaults to GetMaxGravForceDist(PlanetMass)
#
# returns ==> the GravityWell glow object. it's a torpedo object, created in a way to be a big glow.
################################################################
def ShowGravityWellGlow(pParent, nSize = None):
	debug(__name__ + ", ShowGravityWellGlow")
	Radius = pParent.GetRadius()
	pSet = pParent.GetContainingSet()
	if nSize == None:
		nSize = GetMaxGravForceDist(pParent.GetMass())
	vec = pParent.GetWorldLocation()
	vec.Unitize()
	pPlayer = MissionLib.GetPlayer()
	vec2 = GetVectorFromTo(pParent, pPlayer)
	GlowColor = App.TGColorA()
	GlowColor.SetRGBA(254.0 / 255.0, 0.0 / 255.0, 86.0 / 255.0, 0.3700000)
	pGravityWellGlow = CreateGlowEmmiter(pParent, vec2, pSet, 4.5, Radius, nSize, GlowColor)
	pParent.AttachObject(pGravityWellGlow)
	return pGravityWellGlow


################################################################################################################
## DeleteObject
#######
# this function deletes the given Obj, note that it probably doesn't work with all object types.
# it is assured however, that it will work with torpedo objects, and give an AtributeError if the object isn't a torpedo obj.
# But note again, it won't work with all torpedo object... only for those that was created with the CreateGlowEmmiter func.
# So in short: Except you really know what you're doing DON'T USE THIS
#
# returns ==> nothing   ( very usefull right?? )
###########################################################################################################
def DeleteObject(pWellGlow):
	debug(__name__ + ", DeleteObject")
	pSet = pWellGlow.GetContainingSet()
	pParentID = pWellGlow.GetParentID()
	pParent = App.ObjectClass_GetObjectByID(App.SetClass_GetNull(), pParentID)
	#pPlanet = App.Planet_Cast(pParent)
	pParent.DetachObject(pWellGlow)
	pWellGlow.SetGuidanceLifetime(0.0001)
	pWellGlow.SetLifetime(0.0001)
	return 

################################################################################################################
## CreateGlowEmmiter
#######
# this function creates a torpedo object that works as a glow emmiter.
# It will just stand stopped emmiting his glow in the point it was created.
# this is used by the function ShowGravityWellGlow above
#
# pParent --> the parent of the glow emmiter, used to give a name to the glow emmite.
# kPoint --> a TGPoint3 object, the point where the GlowEmmiter will be created.
# pSet --> the set object in which the GlowEmmiter will be created.
# GlowRate --> The rate in which the torpedo glow will pulsate
# MinGlowSize/MaxGlowSize --> the min/max values of the size of the torpedo glow.
# GlowColor --> the color of the glow, it must be a TGColorA obj.
# CoreSize --> The size of the torpedo's core
#
# returns ==> the torpedo object.
################################################################
TorpNameDict = {}
def CreateGlowEmmiter(pParent, kPoint, pSet, GlowRate, MinGlowSize, MaxGlowSize, GlowColor = None, Lifetime = 60.0, CoreSize = 4.0):
	debug(__name__ + ", CreateGlowEmmiter")
	global TorpNameDict
	torpscript = __import__('Custom.GravityFX.GlowEmmiter')
	torpscript.SetCustomVar("Glow Rate", GlowRate)
	torpscript.SetCustomVar("Glow Min Size", MinGlowSize)
	torpscript.SetCustomVar("Glow Max Size", MaxGlowSize)
	torpscript.SetCustomVar("Core Size", CoreSize)
	if GlowColor:
		torpscript.SetCustomVar("Glow Color", GlowColor)
	Vec = App.TGPoint3()
	Vec.SetXYZ(kPoint.x, kPoint.y, kPoint.z)
	pTorp = App.Torpedo_Create(torpscript.__name__, Vec)
	pTorp.SetTarget(App.NULL_ID)
	pTorp.SetParent(pParent.GetObjID())
	pTorp.SetCollisionFlags(App.ObjectClass.CFB_NO_COLLISIONS)
	TorpName = str(pParent.GetName())+" Glow Emmiter"
	if TorpNameDict.has_key(TorpName):
		TorpNameDict[TorpName] = TorpNameDict[TorpName] + 1
		TorpName = TorpName +"-"+ str(TorpNameDict[TorpName])
	else:
		TorpNameDict[TorpName] = 1
	pSet.AddObjectToSet(pTorp, TorpName)
	pTorp.SetLifetime(Lifetime)
	pTorp.UpdateNodeOnly()
	return pTorp

################################################################################################################
## IsSystemOnline
######
# this returns 1 if the system(self) is online, else it returns 0 if it is offline/disabled
# --> this is an unbound method of App.PoweredSubsystem 
################################################################
def IsSystemOnline(self):
	debug(__name__ + ", IsSystemOnline")
	return int(self.IsOn() and not self.IsDisabled())

################################################################################################################
### GetPlanetByNameInSet
#######
# this return the planet or sun object with given name in given set
###############################################################################################################
def GetPlanetByNameInSet(name, set):
	debug(__name__ + ", GetPlanetByNameInSet")
	pObj = set.GetObject(name)
	if pObj:
		if pObj.IsTypeOf(App.CT_PLANET):
			if pObj.IsTypeOf(App.CT_SUN):
				pSun = App.Sun_Cast(pObj)
				return pSun
			else:
				pPlanet = App.Planet_Cast(pObj)
				return pPlanet
	else:
		#print there is no obj with given name in given set
		return None

###############################################################################################################
#### GetUniqueID
#########
# very usefull function, it returns name_ID, ID is a 12 character long string, it can contain:
#        - upper case letters ( from A to Z)
#        - lower case letters ( from a to z)
#        - digits (from 0 to 9)
#
# plus, this function has a safety loop, so the chance of creating a ID that was already created before is 0 (zero)
# yes, this function will NEVER return the same value, actually if you use 8916100448255 times with the same name
# there won't be any new value, but i think nobody is stupid enough to do it (or possible to do that), and as besides
# the 12 character string, there's also the name string in the ID, so it has infinite values.
# this function has endless possibilities
#################################################################################################################
CreatedIDsList = []
def GetUniqueID(name, charnum = 12):
	debug(__name__ + ", GetUniqueID")
	prefix = name + "_"
	while 1:
		retval = ""
		for index in range(charnum):
			i = Dice(3)
			################################lower case letter
			if i == 0:
				c = string.lowercase[ Dice(26) ]
			################################digits
			elif i == 1:
				c = str( Dice(10) )
			################################upper case letters
			elif i == 2:
				c = string.uppercase[ Dice(26) ]
			retval = retval+c
		FinalName = prefix + retval
		if FinalName not in CreatedIDsList:
			CreatedIDsList.append(FinalName)
			return FinalName
	return name

################################################################################################################
### Dice
######
# helper function for GetUniqueID, but as it has other uses too, let make it more noticeable shall we?
###
# NOTE: kinda useless lol, just read her and you'll know why... anyway...
###
#it returns an integer between 0 and number-1.
#  Example: use Dice(10), it will return one of these integers randomly: ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 )
#################################################################################################################
#Dice = App.g_kSystemWrapper.GetRandomNumber
def Dice(i):
	if (i == 0): return 0
	return App.g_kSystemWrapper.GetRandomNumber(i)

####################################################################################
### GetConfigValue
#########
# Function to return the values from the config script
###
# value can be:  "MultiplyFactor" , "SetStockPlanetsDensity", "SystemMapScale", "SystemMapScaleLightyear"
#		     "GravDmgFactor", "Log<insert name>", "AffectStations"
#       if incorrect value is given, raise KeyError
####################################################################################
def GetConfigValue(value):
	debug(__name__ + ", GetConfigValue")
	pConfigScript = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.GravityFXConfigValues")
	if value == "MultiplyFactor":
		return pConfigScript.GravForceXvalue
	elif value == "SetStockPlanetsDensity":
		return pConfigScript.SetStockPlanetsDensity
	elif value == "SystemMapScale":
		return pConfigScript.SystemMapScale
	elif value == "SystemMapScaleLightyear":
		return pConfigScript.SetSMScaleLightyear
	elif value == "GravDmgFactor":
		return pConfigScript.GravDmgFac
	elif value == "LogLoadGravityFX":
		return pConfigScript.SetUseLogs.LoadGravityFX
	elif value == "LogGravityManager":
		return pConfigScript.SetUseLogs.GravityManager
	elif value == "LogGravWellPlugins":
		return pConfigScript.SetUseLogs.GravWellPlugins
	elif value == "LogTorpGravEffects":
		return pConfigScript.SetUseLogs.TorpGravEffects
	elif value == "LogSystemMap":
		return pConfigScript.SetUseLogs.SystemMap
	elif value == "LogGravSensors":
		return pConfigScript.SetUseLogs.GravSensors
	elif value == "LogGravWell":
		return pConfigScript.SetUseLogs.GravWells
	elif value == "LogAstro":
		return pConfigScript.SetUseLogs.Astrometrics
	elif value == "LogGravGen":
		return pConfigScript.SetUseLogs.GravGenerator
	elif value == "AffectStations":
		return pConfigScript.StationsAreAffected
	elif value == "ThrusterState":
		return pConfigScript.ThrusterState
	else:
		#incorrect value
		raise KeyError, "Incorrect Value for GetConfigValue. Use: MultiplyFactor, SetStockPlanetsDensity, SystemMapScale, SystemMapScaleLightyear, GravDmgFactor, AffectStations, ThrusterState, Log<insert name>"
		return None

####################################################################################
### AddKeyBind
#########
# Used to create a key bind in game, with KeyFoundation
###
# KeyName --> the name of the key
# pEvent --> your event type
# EventInt --> the integer to be passed with the event when this key's pressed
# eType --> type of event to be passed with. see App.KeyboardBinding class for possible events.
#		default -> App.KeyboardBinding.GET_INT_EVENT
# Group --> the Keyboard configuration menu in which this key will appear. It can be "General", "Ship", "Camera" and "Menu"
#		default: "General"
####################################################################################
def AddKeyBind(KeyName, pEvent, EventInt, eType = App.KeyboardBinding.GET_INT_EVENT, Group = "General", mode = None):
	debug(__name__ + ", AddKeyBind")
	if hasattr(Foundation, "g_kKeyBucket"):
		if mode == None:
			Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig(KeyName, KeyName, pEvent, eType, EventInt, Group))
		else:
			Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig(KeyName, KeyName, pEvent, eType, EventInt, Group, dict = {"modes": [mode]}))

####################################################################################
### PlaySound
#########
# Used to play a sound file in game. to make sound effects
###
# sFile --> the path + filename + extension of the sound file you want to play
# sName --> the sound name. BC uses this to "identify" the sound. Default: "GravFXlib-PlaySound"
# return ==> the TGSound object
####################################################################################
dSounds = {}  # key/value pairs -->  sFile = App.TGSound
def PlaySound(sFile, sName = "GravFXlib-PlaySound"):
	debug(__name__ + ", PlaySound")
	global dSounds
	if not dSounds.has_key(sFile):
		Sound = App.TGSound_Create(sFile, sName, 0)
		Sound.SetSFX(0)
		Sound.SetInterface(1)
		dSounds[sFile] = Sound
	else:
		Sound = dSounds[sFile]
	Sound.Play()
	return Sound

####################################################################################
### CreateNAVPoint
#########
# This creates a NAV point with given name in the given set in the given position
###
# sName --> the name for the NAV Point
# pSet --> the Set obj in which this NAV Point will be created
# pPOS --> a TGPoint3 obj, this is the coordinates in which the NAV Point will be created
# return ==> the NAV Point  (a App.Waypoint obj)
####################################################################################
def CreateNAVPoint(sName, pSet, pPOS):
	debug(__name__ + ", CreateNAVPoint")
	sSetName = pSet.GetName()
	pNAVPoint = App.Waypoint_Create(sName, sSetName, None)
	pNAVPoint.SetStatic(1)
	pNAVPoint.SetNavPoint(1)
	pNAVPoint.SetTranslateXYZ(pPOS.x, pPOS.y, pPOS.z)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	pNAVPoint.AlignToVectors(kForward, kUp)
	pNAVPoint.SetSpeed(25.000000)
	pNAVPoint.Update(0)
	return pNAVPoint

####################################################################################
### DamageShip
#########
# This damages all systems in the given ship with a random damage between the given Minimum and maximun
# damages. Beware, it can destroy a system if he suffers to much damage, running out of 'health'.
#
# It's a modified version of the MissionLib.DamageShip() function
###
# pShip --> the ship to damage
# MinDmg --> the minimum damage, remember it is damage points, and not percentage!	Check the torpedoes
#		 modules and their damages to get an idea.
# MaxDmg --> the maximum damage, remember it is damage points, and not percentage!   
####################################################################################
def DamageShip(pShip, MinDmg, MaxDmg):
	debug(__name__ + ", DamageShip")
	if pShip == None:
		return
	lMain	 = [pShip.GetHull(), pShip.GetShields(), pShip.GetPowerSubsystem(), pShip.GetSensorSubsystem()]
	lWeapons = [pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem(), pShip.GetTractorBeamSystem()]
	lEngines = [pShip.GetImpulseEngineSubsystem(), pShip.GetWarpEngineSubsystem()]
	lSpecial = [pShip.GetRepairSubsystem(), pShip.GetCloakingSubsystem()]	
	dmg1 = 0.0
	dmg2 = 0.0
	dmg3 = 0.0
	dmg4 = 0.0
	for pSystem in lMain:
		if pSystem:
			dmg1 = DamageSystem(pSystem, MinDmg, MaxDmg)
	for pSystem in lWeapons:
		if pSystem:
			dmg2 = DamageSystem(pSystem, MinDmg, MaxDmg)
	for pSystem in lEngines:
		if pSystem:
			dmg3 = DamageSystem(pSystem, MinDmg, MaxDmg)
	for pSystem in lSpecial:
		if pSystem:
			dmg4 = DamageSystem(pSystem, MinDmg, MaxDmg)
	#Play sound
	#Add visible damage
	return [dmg1, dmg2, dmg3, dmg4]

####################################################################################
### DamageSystem
#########
# Helper function for DamageShip
# This damages the given system (and all his child systems) with a random damage between the
# given Minimum and maximun.
# damages. Beware, it can destroy the system if he suffers to much damage, running out of 'health'.
###
# pSystem --> the system to damage
# MinDmg --> the minimum damage, remember it is damage points, and not percentage!	Check the torpedoes
#		 modules and their damages to get an idea.
# MaxDmg --> the maximum damage, remember it is damage points, and not percentage!
# returns --> the damage that was done.
####################################################################################
def DamageSystem(pSystem, MinDmg, MaxDmg):
	debug(__name__ + ", DamageSystem")
	Dmg = GetRandomInRange(MinDmg, MaxDmg)
	pParentShip = pSystem.GetParentShip()
	for i in range(pSystem.GetNumChildSubsystems()):
		pChild = pSystem.GetChildSubsystem(i)
		if (pChild != None):
			pChild.SetCondition(pChild.GetCondition() - Dmg)
			if pParentShip and pChild.GetCondition() <= 0:
				pParentShip.DestroySystem(pChild)
	return Dmg

####################################################################################
### GetRandomFloat
#########
# This function returns a float in the the range of 0.0 to 1.0
# I made it to be like the random() function in the random module in python2.4
# BC python lacks the random module, so i had to make this...
###################################################################################
def GetRandomFloat():
	debug(__name__ + ", GetRandomFloat")
	num = App.g_kSystemWrapper.GetTimeSinceFrameStart()
	index = 1.0
	n = num
	while n < 0.1 and Dice(10) > 2:
		n = n*10
		index = index*10
	ret = num*index
	while ret > 1.0:
		ret = ret / 10.0
	return ret

####################################################################################
### GetRandomInRange
#########
# This function returns a float between the start and stop args, if stop is none, it returns a float from 0 to start
# It is a modified randrange function from the random module in python2.4, as BC python lacks that module, i made this
# and modified it to work on BC python
####################################################################################
def GetRandomInRange(start, stop=None):
	debug(__name__ + ", GetRandomInRange")
	maxwidth=1L<<53
	istart = float(start)
	if stop is None:
		return Dice(start)
	istop = float(stop)
	width = istop - istart
	if width >= maxwidth:
		return float(istart + Dice(width))
	return float(istart + float(GetRandomFloat()*width))

####################################################################################
### GetStrFromFloat
#########
# This converts an numeric value (be it int, float, or whatever. tho it's most used with floats)
# into an string, just like using 'str(value)', but this function leaves the string with the given
# number of decimal plates, thus reducing the size of the returning string.
###
# value --> the numeric value
# decimalplates --> the number of decimal plates you want on the string. Defaults to 4
# returns ==> the string
####################################################################################
def GetStrFromFloat(value, decimalplates = 4):
	debug(__name__ + ", GetStrFromFloat")
	if int(value) != value:
		return ("%." + str(decimalplates) + "f") % (value)
	return str(value)

####################################################################################
### SetRotation
#########
# Rotates the given ship with the given speed in the given axis.
# Bear in mind that this sets the angular velocity of the ship only, so the ship may
# stop rotating (normally this happens if she has a working impulse engine)
###
# pShip --> The ship instance
# fSpeed --> the speed to rotate the ship, in degrees per second
# X, Y, Z --> the XYZ axis, used to create the vector in which the ship will rotate
# returns ==> the new angular velocity vector
####################################################################################
def SetRotation(pShip, fSpeed, X = 1, Y = 0, Z = 0):
	debug(__name__ + ", SetRotation")
	vVelocity = App.TGPoint3()
	vVelocity.SetXYZ(X, Y, Z)
	vVelocity.Unitize()
	vVelocity.Scale( fSpeed * App.HALF_PI / 180.0 )
	pShip.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
	return vVelocity

####################################################################################
### IsStation
#########
# Checks if the given ship is a station...
#
#NOTE: as i made this function just now, way after the coding of pratically everything else, 
#	 you probably won't see her being used much...
###
# pShip --> The ship instance
# returns ==> 1 if the ship is a station, 0 otherwise
####################################################################################
def IsStation(pShip):
	debug(__name__ + ", IsStation")
	if not pShip.IsTypeOf(App.CT_SHIP):
		return 0
	pProp = pShip.GetShipProperty()
	if pProp.GetGenus() == 2 or pProp.IsStationary() == 1:
		return 1
	return 0

####################################################################################
### GetClass
#########
# A method of App.Planet class, returns the class of the planet, using EarthFX
# TO BE USED WITH App.Planet INSTANCES! Example:
# pPlanet = App.Planet_Cast(*something*)
# sClassString = pPlanet.GetClass()
###
# returns ==> the class string
####################################################################################
def GetClass(self):
	debug(__name__ + ", GetClass")
	try:
		EFXplanetClasses = __import__('Custom.EarthFX.scripts.EFX_AtmosphereOverrides')
		if EFXplanetClasses.dPlanetToClass.has_key(self.GetObjID()):
			sClass = EFXplanetClasses.dPlanetToClass[self.GetObjID()]
		else:
			sClass = "DEFAULT"
		return sClass
	except ImportError:
		return "MISSING EARTHFX"

####################################################################################
### GetSubsystemsOfName
#########
# Based on the function GetSubsystemByName on MissionLib, this returns all subsystems on the given ship
# that have in their names the given name
###
# pShip --> The ship to check for subsystems in.
# pcSubsystemName --> The name to check subsystems for.
# returns ==> a list of the subsystems
####################################################################################
def GetSubsystemsOfName(pShip, pcSubsystemName):
	debug(__name__ + ", GetSubsystemsOfName")
	kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
	lSubsystems = []
	bLoop = 1
	while bLoop == 1:
		pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
		if (pSubsystem == None):
			bLoop = 0
			break
		if string.count(pSubsystem.GetName(), pcSubsystemName) == 1:
			lSubsystems.append(pSubsystem)
		for i in range(pSubsystem.GetNumChildSubsystems()):
			pChild = pSubsystem.GetChildSubsystem(i)
			if (pChild != None) and (string.count(pChild.GetName(), pcSubsystemName) == 1):
				lSubsystems.append(pChild)
	pShip.EndGetSubsystemMatch(kIterator)
	return lSubsystems

####################################################################################
### GetScreenCoordsForObj
#########
# This function returns a tuple (X, Y) of the X and Y coordinates of the point in the screen where the given object
# (3D space object, like a ship) is located.
# Thanks to Wowbagger of BCS:TNG for this function!  
# And thanks to myself for fixing the Y-Axis offset that was occurring, and simplifying it a bit lol :P
###
# pObject --> The space object to check for.
# pCamera --> The Camera to check for, this defaults to the current player camera. Not really usefull using this parameter
#		  unless you know what your doing.
# returns ==> (X, Y) tuple (screen 2D point)
####################################################################################
def GetScreenCoordsForObj(pObject, pCamera = None):
	## Now this, my friend, is completely insane. Explanation:
	## I needed to find a way to "push" the OrderPoints away 
	## from the camera. This is a really strange thing to have 
	## to do, and there's not really any sort of mathematical 
	## equation for it. So I was sitting here, despairing,
	## when it occurred to me that I had had to do the same sort
	## of distance-from-the-camera thing to get the original
	## location for the OrderPoint. Unfortunately, since that
	## used mouse coordinates, it wouldn't work.
	## But then, as I kept thinking, I realized that the mouse
	## coordinates, which are just x-y coordinates on the comp
	## screen, were converted to world locs using *equations*...
	## equations which could be solved backwards, to convert
	## an (x,y,z) coordinate in-game to an (x,y) coordinate on
	## the monitor--a format in which I could easily redo the
	## the distance, convert the new figures back, and voila!
	## I'm cooking with replicators!
	## And actually, having written this explanation, I'm not
	## technically done with the *method* yet, in the sense of
	## actually having started it or anything, so let's see how
	## it works out, eh?

	debug(__name__ + ", GetScreenCoordsForObj")
	if pObject == None:	pObject = MissionLib.GetPlayer().GetTarget()
	if pCamera == None:	pCamera = App.Game_GetCurrentGame().GetPlayerCamera()

	# Grab Object Position:
	vObj = pObject.GetWorldLocation()
	# Grab Camera Position and Orientation Data:
	vCam = pCamera.GetWorldLocation()
	kForward = pCamera.GetWorldForwardTG()
	kUp = pCamera.GetWorldUpTG()
	kRight = pCamera.GetWorldRightTG()

	lList = [kForward.x, kForward.y, kForward.z, kRight.x, kRight.y, kRight.z, kUp.x, kUp.y, kUp.z]
	for i in range(len(lList)):
		try:	
			1/lList[i]
		except:
			lList[i] = 0.0001

	K = vObj.x - vCam.x    #K = kX
	L = vObj.y - vCam.y    #L = kY
	M = vObj.z - vCam.z    #M = kZ
	A = lList[0]
	B = lList[1]
	C = lList[2]
	D = lList[3]
	E = lList[4]
	F = lList[5]
	G = lList[6]
	H = lList[7]
	I = lList[8]

	# First, we need to get get all z-coefficents equal to 1, so we have to use some factorizing and distribution.
	Fac1 = (1/A)
	Fac2 = (1/B)
	Fac3 = (1/C)
	K = K * Fac1     # Component X  -   Fac1 = (1/A)
	A = A * Fac1
	D = D * Fac1
	G = G * Fac1

	L = L * Fac2     # Component Y  -   Fac2 = (1/B)
	B = B * Fac2
	E = E * Fac2
	H = H * Fac2

	M = M * Fac3     # Component Z -   Fac3 = (1/C)
	C = C * Fac3 
	F = F * Fac3 
	I = I * Fac3 

	N = K - L
	P = D - E
	R = G - H
	O = L - M
	Q = E - F
	S = H - I

	lList = [P, Q]
	for i in range(len(lList)):
		try:	
			1/lList[i]
		except:
			lList[i] = 0.0001 

	N = N * (1/lList[0])    #N = N * Fac4
	P = P * (1/lList[0])    #P = P * Fac4
	R = R * (1/lList[0])    #R = R * Fac4
	O = O * (1/lList[1])    #O = O * Fac5
	Q = Q * (1/lList[1])    #Q = Q * Fac5
	S = S * (1/lList[1])    #S = S * Fac5

	iY = (N - O)/(R - S)
	iX = (N - (R * iY))/P
	iZ = (K - (D * iX + G * iY))/A

	iMouseX = (iX + (iZ/4))/(iZ/2)
	iMouseY = (iY - (iZ/4))/(-iZ/2)

	# Y-Axis Offset Correction:
	# First, we set the correction factor, which to discover I spent several minutes on BC finding values for example
	# about the coords (the coord on the screen of an obj according to this equation without the offset correction,
	# and the REAL coords on the screen of it, putting the mouse above it to check). I got 8 pairs of values to use as
	# an example, then on python IDLE i spent more several minutes (maybe hours) increasing the factor decimal by decimal
	# to find the factor that whould make the values the closest to reality possible, and I found it.
	# That's because after some observations I came to the conclusion that the offset was "static". The amount of the 
	# offset that happened on that point was always the same on that same point.
	offFactor = 0.1738359214921854
	iMouseY = iMouseY + (iMouseY/(1.0/(2*offFactor)) - offFactor)

	# Behind Camera Coords Bug Correction:
	# The following is to correct the bug which causes the coords of objects that are behind the camera appear on the
	# screen, as if they were appearing on the screen, which in reality they aren't.
	if iZ < 0:
		# this means that the object is behind the camera, so we just set both X and Y values to something off screen.
		iMouseX = -1.0
		iMouseY = -1.0

	return iMouseX, iMouseY

####################################################################################
### Get3DMapWindow
#########
# Returns the BC 3D Map Window object.  (App.MapWindow)
###
# returns ==> the BC 3D Map, App.MapWindow class
####################################################################################
def Get3DMapWindow():	
	debug(__name__ + ", Get3DMapWindow")
	pTopWindow = App.TopWindow_GetTopWindow()
	TopChild = pTopWindow.GetFirstChild()
	while TopChild:
		MapWindow = App.MapWindow_Cast(TopChild)
		if MapWindow:
			return MapWindow
		TopChild = pTopWindow.GetNextChild(TopChild)
