import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(55.0 / 255.0, 55.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(220.0 / 255.0, 220.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.3,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					1.0,	
					0.5,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,		
					0.0,		
					0.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("TOS Def TorpKM")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon Torpedo TOS")

def GetDamage():
	return 350.0

def GetGuidanceLifetime():
	return 0.1

def GetMaxAngularAccel():
	return 10.0