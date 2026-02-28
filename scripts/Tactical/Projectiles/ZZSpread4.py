import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(221.0 / 255.0, 117.0 / 255.0, 56.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZMauler1Core.tga",
					kCoreColor, 
					1.2,
					10.0,	 
					"data/textures/tactical/ZZMauler1Glow.tga", 
					kGlowColor,
					12.0,	
					2.0,	 
					4.0,	
					"data/textures/tactical/ZZMauler1Core.tga",
					kCoreColor,										
					10,		
					0.6,		
					1.0)

	App.g_kSoundManager.PlaySound("ZZ_Mauler4")
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
	return("ZZ_Mauler")

def GetPowerCost():
	return(1.0)

def GetName():
	return("Stage 4")

def GetDamage():
	return 18000.0

def GetGuidanceLifetime():
	return 13.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 20.0

