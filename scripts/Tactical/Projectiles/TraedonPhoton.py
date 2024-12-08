#script modified by Dkealt and Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 18.0 / 255.0, 2.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(250.0 / 250.0, 205.0 / 250.0, 0.0, 1.0)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga", #core texture file
					kCoreColor, 
					0.175, #Scale of Core in relation to rest of torpedo
					30.0, #Rate at which torpedo rotates - rpm	 
					"data/Textures/Tactical/TorpedoGlow.tga", #Glow Texture File
					kGlowColor,
					0.5,	#Rate at which glow pulsates
					0.6,	#Min size of glow
					0.4,	#Max size of glow
					"data/Textures/Tactical/TorpedoFlares.tga", #Flare Texture File
					kGlowColor,						
					72,		#Max number of flares
					0.15,	#Length of individual flares
					0.25)    #How long flares last - seconds

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("TraedonPhoton")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Traedon Photon")

def GetDamage():
	return 15500.0

def GetGuidanceLifetime():
	return 30.0

def GetMaxAngularAccel():
	return 0.75
