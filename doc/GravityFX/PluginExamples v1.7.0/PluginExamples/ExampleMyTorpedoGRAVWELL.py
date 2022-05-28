# This is a Plugin for GravityFX, made with the GravityFX Plugin Tool
# FOR EXAMPLE  PURPOSES

#-----------------------------------------------------------------------------------------------------------#

# PLUGIN SCRIPT NAME
# the name of the plugin(this script you're reading) specifies the ship OR torpedo (depending of the PLUGIN TYPE you specify
# below) that the gravity effect will be applied to.

#-----------------------------------------------------------------------------------------------------------#

#PLUGIN TYPE
# here you set the type of the plugin that you want for the torpedo you specified, for a torpedo it can be "GravTorpedo" or
# "AntiGravTorpedo", their names explains their purposes. Also remember that a torpedo's gravity effect will start at the
# moment he hits something.

PluginType = "GravTorpedo"

#-----------------------------------------------------------------------------------------------------------#

#LIFETIME
# the time in seconds that the gravity well will last, 0 means that it will last forever.

Lifetime = 120.0

#-----------------------------------------------------------------------------------------------------------#

#MASS
# The Mass property is what establishes the strength of the gravity well. It can be the normal mass number, normally a 
# exponential value (example: 1.2424e+017), or by importing the GravityFXlib module and using the GetMassByMaxDistance(value)
# of it.

GravFXlib = __import__('Custom.GravityFX.GravityFXlib')
Mass = GravFXlib.GetMassByMaxDistance(100)

#the above function GetMassByMaxDistance, returns the mass of a obj that would have the given distance as the max grav force 
#distance. 

#-----------------------------------------------------------------------------------------------------------#

#SOUND DELAY
# This specifies the time in seconds that this gravity effect will emmit a sound, to warn you that it is there in space.
# There are 2 sounds, 1 for gravity torpedoes, and another sound for anti gravity torpedoes.

SoundDelay = 5.0

#-----------------------------------------------------------------------------------------------------------#

#COlOR RED / COLOR GREEN / COLOR BLUE / COLOR ALPHA
# This specifies the color and transparency (RGBA) of the glow that will appear to show where the torpedo gravity effect
# is located. Remember that all values are a float in a range of 0 to 1 (that's why it's 64 divided by 255.0).

ColorRed = 64/255.0
ColorGreen = 128/255.0
ColorBlue = 128/255.0
ColorAlpha = 0.35

#-----------------------------------------------------------------------------------------------------------#

# CONCLUSION
# This example would make the torpedo with the torpedo script "ExampleMyTorpedoGRAVWELL" to make a Gravity Well
# that will last for 120 seconds(2 minutes, or until the ship is destroyed or leave the set), at his start his strength
# woulda make the gravity well reach 100 kilometers, at each 5 seconds it will play a sound, and his glow will have a "75%
# transparent dark bluish green color".

