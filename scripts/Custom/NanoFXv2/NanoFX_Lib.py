from bcdebug import debug
###############################################################################
##	Filename:	NanoFX_Lib.py
##
##	NanoFX Library Helper Functions version 1.0
##
##	Created:	04/03/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App

g_FlickerControl = 0
g_LightsOff = []
CONST_MAXFLICKERS = 2

###############################################################################
## Control the Number of Light Flickers being displayed at once so BC doesn't get
## bogged down or even CRASH!
###############################################################################	
def ControlFlickers(pAction, iNum):
	
	debug(__name__ + ", ControlFlickers")
	global g_FlickerControl
	g_FlickerControl = g_FlickerControl + iNum
		
	return 0

###############################################################################
## Random Rotation Sequence - Add Angular Velocity and/or Speed Velocity
##
## Args: pShip       - The Ship Object you are passing in
##       [fRotation] - Random Angular Velocity to Model (Passing in None = no Change to Current Rotation)
##       [fSpeed]    - Speed Velocity to give the Model (Passing in None = no Change to Current Speed)
##
##	 Return	     - The Assembled Sequence
###############################################################################
def CreateRotationSeq(pShip, fRotation = None, fSpeed = None):

	### Create Sequence Object ###
	debug(__name__ + ", CreateRotationSeq")
	pSequence = App.TGSequence_Create()
	###
	fRotation = App.g_kSystemWrapper.GetRandomNumber(fRotation) + fRotation
	fRotation = fRotation * 0.01
	###
	pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "SetNanoRotation", pShip, fRotation, fSpeed))
	###
	return pSequence
	###

###############################################################################
## Flicker Lights Sequence - Flicker the Lights on a Ship for a set period of time
##
## Args: pShip           - The Ship Object you are passing in
##       fTotalTime      - The Total time in Seconds to flicker the Lights for
##       [fFlickerSpeed] - How Quickly to Flicker the Lights (Important!!! I do not recommend below 0.1)
##	 [sStatus]       - The Final Status of the ship's Lights ("Off" or "On")
##
##	 Return          - The Assembled Sequence
###############################################################################
def CreateFlickerSeq(pShip, fTotalTime, fFlickerSpeed = 0.2, sStatus = "On"):

	### Create Sequence Object ###
	debug(__name__ + ", CreateFlickerSeq")
	pSequence = App.TGSequence_Create()
	pSet = pShip.GetContainingSet()
	if g_FlickerControl < CONST_MAXFLICKERS:
		###
		fFlickerTime = 0
		###
		while (fFlickerTime < fTotalTime - 0.1):
			pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "TurnOffLights", pShip), App.TGAction_CreateNull(), App.g_kSystemWrapper.GetRandomNumber(100) * 0.001 + fFlickerTime)
			pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "TurnOnLights"), App.TGAction_CreateNull(), App.g_kSystemWrapper.GetRandomNumber(100) * 0.001 + fFlickerTime)
			fFlickerTime = fFlickerTime + fFlickerSpeed
		###
		if sStatus == "Off":
			pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "TurnOffLights", pShip), App.TGAction_CreateNull(), fTotalTime)
			bFound = 0
			for sName in g_LightsOff:
				if pShip.GetName() == sName:
					bFound = 1
			if bFound == 0:
				g_LightsOff.append(pShip.GetName())
		if sStatus == "On":
			pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "TurnOnLights"), App.TGAction_CreateNull(), fTotalTime)
			bFound = 0
			for sName in g_LightsOff:
				if pShip.GetName() == sName:
					bFound = 1
			if bFound == 1:
				g_LightsOff.remove(pShip.GetName())
		###
                if pSet:
		        for kShip in pSet.GetClassObjectList(App.CT_DAMAGEABLE_OBJECT):
			        for sName in g_LightsOff:
				        if kShip.GetName() == sName or kShip.GetName() == None:
					        pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "TurnOffLights", kShip), App.TGAction_CreateNull(), fTotalTime + 0.5)
					
		ControlFlickers(None, 1)
		pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlFlickers", -1), App.TGAction_CreateNull(), fTotalTime)			
		
	return pSequence
	###

###############################################################################
## SpecialFX Sequence - Create one of the SpecialFX Sequences
##
## Args: pShip           - The Ship you are passing in
##       pEvent          - The Event to Pass in
##       sFXType         - The SpecialFX TYPE you wish to create
##	 [bPlay]         - If you want immediate Playing of the FX or to Return the TG Sequence for you to Control
##
##	 Return	         - The Assembled Sequence
###############################################################################
def CreateSpecialFXSeq(pShip, pEvent, sFXType, bPlay = 0):
        debug(__name__ + ", CreateSpecialFXSeq")
        pSpecialFX = None
	if (sFXType == "PhalantiumFX"):
		import Custom.NanoFXv2.SpecialFX.PhalantiumFX
		pSpecialFX = Custom.NanoFXv2.SpecialFX.PhalantiumFX.CreatePhalantiumFX(pShip, pEvent)
	
	if (sFXType == "PlasmaFX"):
		import Custom.NanoFXv2.SpecialFX.PlasmaFX
		pSpecialFX = Custom.NanoFXv2.SpecialFX.PlasmaFX.CreatePlasmaFX(pShip, pEvent)
	
	if (sFXType == "Spatial"):
		import Custom.NanoFXv2.SpecialFX.SpatialFX
		pSpecialFX = Custom.NanoFXv2.SpecialFX.SpatialFX.CreateSpatialFX(pShip, pEvent)

	if (sFXType == "AtmosphereFX"):
		import Custom.NanoFXv2.SpecialFX.AtmosphereFX
		pSpecialFX = Custom.NanoFXv2.SpecialFX.SpatialFX.CreateAtmosphereFX(pSet, sName, sPlacement, fSize)

	if (bPlay == 1):
		pSequence = App.TGSequence_Create()
		pSequence.AddAction(pSpecialFX)
		pSequence.Play()
	else:
		return pSpecialFX

def CreateAtmosphereFX(pPlanet, sNifPath = "data/models/environment/planet.nif", sTexturePath = "Class-M"):

	debug(__name__ + ", CreateAtmosphereFX")
	import Custom.NanoFXv2.NanoFX_Config 
	if Custom.NanoFXv2.NanoFX_Config.sFX_Enabled == 1:
		import Custom.NanoFXv2.SpecialFX.AtmosphereFX
		Custom.NanoFXv2.SpecialFX.AtmosphereFX.CreateAtmosphereFX(pPlanet, sNifPath, sTexturePath)

###############################################################################
## Get Species Name - Will return a species name
##
## Args: pShip		- The Ship Object you are passing in
##       
## Return			- A String Name for the Species, Default: "Default"
###############################################################################
def GetSpeciesName(pShip):

	debug(__name__ + ", GetSpeciesName")
	import Foundation
	import string
	
	try:
		pShipScript = string.split(pShip.GetScript(), ".")
	
		pShipDef = Foundation.shipList[pShipScript[-1]]
		sRaceName = pShipDef.race.name
	except:
		sRaceName = "Default"
	
	return sRaceName
	
###############################################################################
## Get Override Color in Ship Plugin
##
## Args: pShip       - The Ship Object
##		 sEffectType - NanoFX type to Override
##       
##	 Return	     - Returns an RGB Color found in Plugin
###############################################################################
def GetOverrideColor(pShip, sEffectType):

	debug(__name__ + ", GetOverrideColor")
	import string
	import Foundation
	
	try:
		pShipScript = string.split(pShip.GetScript(), ".")
		pShipDef = Foundation.shipList[pShipScript[-1]]
	except:
		return None
	
	if sEffectType == "ExpFX":
		if pShipDef.__dict__.has_key("OverrideExpFXColor"):
			return pShipDef.OverrideExpFXColor(None)
		else:
			return None
			
	if sEffectType == "PlasmaFX":
		if pShipDef.__dict__.has_key("OverridePlasmaFXColor"):
			return pShipDef.OverridePlasmaFXColor(None)
		else:
			return None
			
	if sEffectType == "WarpFX":
		if pShipDef.__dict__.has_key("OverrideWarpFXColor"):
			return pShipDef.OverrideWarpFXColor(None)
		else:
			return None


###############################################################################
## Get Race Texture Color 
##
## Args: sRace       - The String Race Name
##       
##	 Return	     - Returns an RGB Color.... if none found it returns Default Color
###############################################################################
def GetRaceTextureColor(sRace):
	
	debug(__name__ + ", GetRaceTextureColor")
	try:
		dRGB  = { "Federation" : ( 55.0, 120.0, 255.0),
					"Klingon"    : (255.0,  20.0,   0.0),
					"Romulan"    : (  0.0, 248.0, 130.0),
					"Cardassian" : (255.0, 200.0,   0.0),
					"Ferengi"    : (255.0, 180.0,   0.0),
					"Kessok"     : (182.0,   0.0, 201.0),
					"Dominion"   : (182.0,   0.0, 201.0),
                	"Borg"       : (  0.0, 248.0, 150.0)
			}
		return dRGB[sRace]
	except:
		sRace = "Default"
		dRGB  = { "Default"    : (155.0, 120.0, 255.0)
			}
		return dRGB[sRace]

###############################################################################
## End of NanoFX Lib
###############################################################################
