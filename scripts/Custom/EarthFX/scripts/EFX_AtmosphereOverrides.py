################################################################################
# PROJECT GOAT: Atmosphere Loading Overrides
# by Wowbagger
#
# There are many ways to get planet classifications, other than just
# making them up on the spot with a Rand() function.  Unfortunately,
# because every planet classification system is based off a mod, and
# these mods do their things in very different ways, in order to "leech"
# the data, we have to actually override something in each system and
# insert a line that will write the classification of each planet to
# a dictionary.
#
# Current Compatabilities: NanoFX (stock planets), Custom Systems
# On The Queue: ATP:Dimensions.
# 
# v0.1 by Wowbagger - 11 May 2006
#       --Mostly, just reorganizing the v0.0.0.0.1 Goat framework into
#       a central, easily adapted file, with a single dictionary for all
#       our references.  We'll see how it ends up working.
#
# v0.2 by Wowbagger - 14 May 2006
#       -- Unfortunately, we can not do the overrides right in this file,
#       as I desired, because Foundation won't allow us to import the mode
#       from the autoload file.  Oh, well.
#
# v0.2.1 by Wowbagger - 14 January 2007
#       -- Altered comments and reference variables to prevent revealing the
#       purpose of *********, aka Project Goat, during public release of file
#       for use in GravityFX.
#
# v0.2.1 Approved for Release - 26 January 2007
#       -- This script is hereby authorized by BCS:TNG for use in USS Frontier's
#       GravityFX mod.  All other standard restrictions and permission rules
#       apply.  (Read: Don't use this without our express written permission.)
################################################################################
# QUOTE OF THE DAY:
#   "For all we know, at this very  moment, somewhere, far beyond all those
#           distant stars... Benny Russell is dreaming of us."
#   --Benjamin Sisko, "Far Beyond The Stars" [DS9]
################################################################################


import App
import Foundation


### Variables
# Our dictionary, which links planet instances to classifications.
dPlanetToClass = {}

## Replacement Functions
# The original, unmodified code for this function is found in this location:
# Custom.NanoFXv2.SpecialFX.AtmosphereFX.CreateAtmosphereFX
def OverrideNanoFX(pPlanet, sNifPath, sTexturePath):
        global dPlanetToClass
        
	### Setup for Effect
	pSet          = pPlanet.GetContainingSet()
	fSize         = pPlanet.GetRadius()
	sName         = pPlanet.GetName()
	###
	pPlanet.SetAtmosphereRadius ((fSize * 1.15) - fSize)
	pPlanet.UpdateNodeOnly()
	###
	# lennie notes:  these layers are render-order specific!

	#0.15 1.15 1.15
	pAtmosphere1 = App.Sun_Create(fSize * 0.1, fSize * 1.05, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/" + sTexturePath + "/GlowColor.tga", None)
	pSet.AddObjectToSet(pAtmosphere1, sName + " Air")
	pAtmosphere1.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere1)

	### Create Sphere Model Around Planet for Clouds ###
	pAtmosphere = App.Planet_Create(fSize * 1.01, sNifPath)
	pSet.AddObjectToSet(pAtmosphere, sTexturePath + " Planet")
	pAtmosphere.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere)

	# 0.1 1.11 0.0
	pAtmosphere2 = App.Sun_Create(fSize * 0.1, fSize * 1.0102, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/" + sTexturePath + "/Clouds.tga", None)
	pSet.AddObjectToSet(pAtmosphere2, sName + " Clouds")
	pAtmosphere2.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere2)

	# 0.65 1.15 1.15
	pAtmosphere3 = App.Sun_Create(fSize * 0.2, fSize * 1.1, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/Glow.tga", None)
	pSet.AddObjectToSet(pAtmosphere3, sName + " Glow")
	pAtmosphere3.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere3)

	#### START OF BCSTNG INSERTS ####
	# Let's get our planet's Starfleet Classification:
        # Store to the dictionary.

        dPlanetToClass[pPlanet.GetObjID()] = sTexturePath
        ##### END OF BCSTNG INSERTS #####


## Insert general code here.
# Most custom-made planets won't automatically load classes.  The user will have
# to decide what planets should be what class, and, in the static placement
# script, he'll have to run every targetable planet through here.  REALLY easy.
def AddCustomPlanet(pPlanet, sClass):
        global dPlanetToClass
        dPlanetToClass[pPlanet] = sClass
        return
