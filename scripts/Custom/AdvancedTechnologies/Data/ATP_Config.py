TRUE = 1
FALSE = 0

DEBUG = TRUE

MAX_ITER = 15

#	Constants
#######################################


PLAYER = "__player__"

STATIONARY	= 1
NOT_STATIONARY	= 0


#	Subevents
######################################



#	Modules
#############################################################
ATP_PATH        = "Custom.AdvancedTechnologies.Data"

CONSTANTS_PATH	= __name__
TOOL_PATH	= ATP_PATH + ".ATP_Tools"
FT_DUMMY	= ATP_PATH + ".ATP_Tools.Dummy"
FT_INDIRECT_CALL= ATP_PATH + ".ATP_Tools.IndirectCall"

## GUI
ATP_GUI		= ATP_PATH + ".GUI"
ATP_GUIUTILS	= ATP_GUI  + ".ATP_GUIUtils"
	
## AI
AI_PATH         = ATP_PATH + ".AI"

## Universe
UNIVERSE_PATH     = ATP_PATH + ".Universe"
ATP_OBJECT_PATH	  = UNIVERSE_PATH + ".ATP_Object"
ATP_VESSELS_PATH  = UNIVERSE_PATH + ".ATP_Vessels"
UNIVERSE_GFX_PATH = UNIVERSE_PATH+ ".Gfx"

#	Classnames
################################################################
RACE			= "Race"
TREE_ELEMENT		= "TreeElement"
UNIVERSE_ELEMENT 	= "UniverseElement"
SOLAR			= "SolarSystem"

#	Paths
#############################################################
GFX_PATH_STARS = "scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Backdrops/Stars.tga"
GFX_PATH_PLANETS  = "data/Models/Environment/"
GFX_PATH_PLANETS_2 = "scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Planets/"

#	Parameters
###############################################################

## Universe
NEBULA_MIN_DISTANCE	= 2.0
SHIPYARD_BUILDSPEED 	= 0.75
SHIFTING_THRESHOLD	= 1.25e+5
SENSOR_MULTIPLYER	= 1.0e+20