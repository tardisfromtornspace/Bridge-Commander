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

PluginType = "AntiGravTorpedo"

#-----------------------------------------------------------------------------------------------------------#

#LIFETIME
# the time in seconds that the gravity well will last, 0 means that it will last forever.

Lifetime = 0.0

#-----------------------------------------------------------------------------------------------------------#

#MASS
# The Mass property is what establishes the strength of the gravity well. It can be the normal mass number, normally a 
# exponential value (example: 1.2424e+017), or by importing the GravityFXlib module and using the GetMassByMaxDistance(value)
# of it.

Mass = 9.3703148425787097e+019

# the above exponential value is used directly for the Mass property, i do not recomend using it if you do not know what
# you're doin. As i have the functions/formulas to discover them i know the values, for example, the mass used here would 
# produce a gravity well that reaches about 250 kilometers.
# The functions/formulas can be found at the GravityFXlib script, it is very detailed. 

#-----------------------------------------------------------------------------------------------------------#

#SOUND DELAY
# This specifies the time in seconds that this gravity effect will emmit a sound, to warn you that it is there in space.
# There are 2 sounds, 1 for gravity torpedoes, and another sound for anti gravity torpedoes.

SoundDelay = 4.1

#-----------------------------------------------------------------------------------------------------------#

#COlOR RED / COLOR GREEN / COLOR BLUE / COLOR ALPHA
# This specifies the color and transparency (RGBA) of the glow that will appear to show where the torpedo gravity effect
# is located. Remember that all values are a float in a range of 0 to 1 (that's why it's 192 divided by 255.0).

ColorRed = 192 / 255.0
ColorGreen = 192 / 255.0
ColorBlue = 192 / 255.0
ColorAlpha = 0.2

#-----------------------------------------------------------------------------------------------------------#

# CONCLUSION
# This example would make the torpedo with the torpedo script "ExampleMyTorpedoANTIGRAVWELL" to make a Anti Gravity Well
# that will last forever(until the ship is destroyed or leave the set), at his start his strength woulda make the anti
# gravity well reach 250 kilometers, at each 4.1 seconds it will play a sound, and his glow will have a "80% transparent
# light grey color".
