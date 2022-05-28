import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(253.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 0.0 / 139.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_FCPhotonCore.tga",
					kCoreColor, 
					0.06,
					4.2,	 
					"data/textures/tactical/ZZ_FCPhotonGlow.tga", 
					kGlowColor,
					3.0,	
					0.5,	 
					0.8,	
					"data/textures/tactical/ZZ_FCPhotonFlares.tga",
					kGlowColor,										
					8,		
					0.17,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("FCPhoton")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 13.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 20.0
