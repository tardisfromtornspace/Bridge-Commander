import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 86.0 / 255.0, 69.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 130.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 71.0 / 255.0, 42.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZMauler3Core.tga",
					kCoreColor, 
					0.2,
					9.0,	 
					"data/textures/tactical/ZZMauler3Glow.tga", 
					kGlowColor,
					12.0,	
					0.3,	 
					1.0,	
					"data/textures/tactical/ZZMauler3Core.tga",
					kGlowColor,										
					20,		
					0.6,		
					1.0)

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
	return(50.0)

def GetLaunchSound():
	return("ZZ_Mauler")

def GetPowerCost():
	return(0.0)

def GetName():
	return("Mauler")

def GetDamage():
	return 4500.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0

def GetLifetime():
	return 20.0
