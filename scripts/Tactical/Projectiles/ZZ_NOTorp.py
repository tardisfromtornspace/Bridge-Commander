import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(200.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 200.0 / 255.0, 0.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PhotonCore.tga",
					kCoreColor, 
					0.05,
					1.2,	 
					"data/textures/tactical/PhotonGlow.tga", 
					kGlowColor,
					3.0,	
					0.35,	 
					0.6,	
					"data/textures/tactical/PhotonFlares.tga",
					kGlowColor,										
					8,		
					0.5,		
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
	return(19.0)

def GetLaunchSound():
	return("ZZ_ST6Photon")

def GetPowerCost():
	return(0.0)

def GetName():
	return("Target Control")

def GetDamage():
	return 900.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.15

def GetLifetime():
	return 20.0
