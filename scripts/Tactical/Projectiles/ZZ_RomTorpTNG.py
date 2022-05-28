import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 158.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 255.0 / 255.0, 194.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_TNGRomCore.tga",
					kCoreColor, 
					0.1,
					4.2,	 
					"data/Textures/Tactical/ZZ_TNGRomGlow.tga", 
					kGlowColor,
					3.0,	
					0.35,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.1,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.ZZ_ROMTORPTNG)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("RomTorp2TNG")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Plasma Torp")

def GetDamage():
	return 1300.0

def GetGuidanceLifetime():
	return 12.0

def GetLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.5


