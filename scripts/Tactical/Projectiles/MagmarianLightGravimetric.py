import App

def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(400.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 5.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 5.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(850.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 5.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_BreenCore.tga",
					kCoreColor,
					0.25,
					3.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.25,	 
					0.55,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.25,		
					0.65)

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
	return("MLightGrav")

def GetPowerCost():
	return(25.0)

def GetName():
	return("M Light Gravimetric")

def GetDamage():
	return 3750.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.5
