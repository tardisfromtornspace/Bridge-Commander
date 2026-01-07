import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 219.0 / 255.0, 0.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_FCPhotonCore.tga",
					kCoreColor, 
					0.15, 3.5,	 
					"data/Textures/Tactical/ZZ_FCPhotonGlow.tga", 
					kGlowColor,
					5.5, 0.4, 0.8,	
					"data/Textures/Tactical/ZZ_FCPhotonCore.tga",
					kGlowColor, 7, 0.5, 0.5)
					

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.04)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("ZZ_OwlDisr")

def GetPowerCost():
	return(5.0)

def GetName():
	return("RPDisruptor")

def GetDamage():
	return 350.0

def GetGuidanceLifetime():
	return 0.9

def GetMaxAngularAccel():
	return 0.2

def GetLifetime():
	return 15.0

