# This is a Plugin for GravityFX, made with the GravityFX Plugin Tool
# FOR EXAMPLE  PURPOSES

#-----------------------------------------------------------------------------------------------------------#

# PLUGIN SCRIPT NAME
# the name of the plugin(this script you're reading) specifies the ship OR torpedo (depending of the PLUGIN TYPE you specify
# below) that the gravity effect will be applied to.

#-----------------------------------------------------------------------------------------------------------#

#PLUGIN TYPE
# here you set the type of the plugin that you want for the ship you specified, for a ship it can be "GravWell",
# "AntiGravWell" or "NotToBeAffected", their names explains their purposes.

PluginType = "NotToBeAffected"

#------------------------------------------------------------------------------------------------------------#

# CONCLUSION
# This example would make the ship with the ship script "ExampleMyShipNOTTOBEAFFECTED" to NOT BE AFFECT BY GRAVITY!
# Why? because some ships in-game can't be affected by gravity or it woulda ruin the game experience, by ruining 
# some features, for example: probes would behave oddly, being pushed by gravity their courses would be severely affected,
# Firepoints, a ship used by the Blind Fire mod and other mods to act like a target so you can fire in something would also
# behave oddly, because the gravity would take it away of his position, thus taking it away of the spot you wanted to target.
# and some other examples.
# I've by my own already sent together with the mod some plugins of this type to make some popular ships that shouldn't be 
# affected not be affected by gravity, such as: Probes, Mines, Distortion, Firepoint, BigFirepoint, PlasmaStream.