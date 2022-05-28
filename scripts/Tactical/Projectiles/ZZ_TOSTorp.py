import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(122.0 / 255.0, 224.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 190.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_TOSPhotonCORE.tga",
					kCoreColor, 
					0.05,
					7.5,	 
					"data/textures/tactical/ZZ_TOSPhotonGLOW.tga", 
					kGlowColor,
					2.5,	
					0.35,	 
					0.4,	
					"data/textures/tactical/ZZTOSPhotonFlares.tga",
					kGlowColor,										
					50,		
					0.05,		
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
	return(16.0)

def GetLaunchSound():
	return("ZZ_TOSTorp")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon")

def GetDamage():
	return 550.0

def GetGuidanceLifetime():
	return 13.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 20.0
