import App

def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(186.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 185.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 85.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					7.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.5,	
					0.2,	 
					0.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.07,		
					0.3)

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
	return(35.0)

def GetLaunchSound():
	return("EPhotonic")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Insectorp")

def GetDamage():
	return 200.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.16
