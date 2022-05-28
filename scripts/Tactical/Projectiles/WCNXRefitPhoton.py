import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(147.0 / 203.0, 203.0 / 255.0, 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 240.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					1.2,	 
					"data/textures/tactical/WCJJConnieGlow.tga", 
					kGlowColor,
					3.0,	
					0.7,	 
					0.8,	
					"data/textures/tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,		
					0.0,		
					0.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("NX Refit Photon")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon")

def GetDamage():
	return 400.0

def GetGuidanceLifetime():
	return 13.0

def GetMaxAngularAccel():
	return 2.66

def GetLifetime():
	return 20.0
