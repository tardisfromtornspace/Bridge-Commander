import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 2550.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_TNGPhotonCore.tga",
					kCoreColor, 
					0.9,
					4.2,	 
					"data/textures/tactical/ZZ_TNGPhotonGlow.tga", 
					kGlowColor,
					5.0,	
					0.85,	 
					1.9,	
					"data/textures/tactical/ZZST6PhotonFlares.tga",
					kGlowColor,										
					8,		
					0.9,		
					0.7)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(19.0)

def GetLaunchSound():
	return("ZZ_ST6Photon2")

def GetPowerCost():
	return(1.0)

def GetName():
	return("Stage 3")

def GetDamage():
	return 9000.0

def GetGuidanceLifetime():
	return 13.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 20.0


