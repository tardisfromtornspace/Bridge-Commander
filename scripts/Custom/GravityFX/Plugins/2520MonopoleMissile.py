# This is a Plugin for GravityFX, made with the GravityFX Plugin Tool

PluginType = "GravTorpedo"

Lifetime = 0.2

GravFXlib = __import__('Custom.GravityFX.GravityFXlib')
Mass = GravFXlib.GetMassByMaxDistance(1)

#the above function GetMassByMaxDistance, returns the mass of a obj that would have the given distance as the max grav force 
#distance. 

SoundDelay = 99999999.0

ColorRed = 255/255.0
ColorGreen = 85/255.0
ColorBlue = 175/255.0
ColorAlpha = 1.00000000
