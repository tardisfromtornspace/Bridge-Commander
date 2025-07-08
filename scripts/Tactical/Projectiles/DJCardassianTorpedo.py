import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(104.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/DJCardassianTorpedoCore.tga",
					kCoreColor, 
					0.3,
					3.5,	 
					"data/textures/tactical/DJCardassianTorpedoGlow.tga", 
					kGlowColor,
					7,	
					4.10,	 
					4.75,	
					"data/textures/tactical/DJCardassianTorpedoBlank.tga",
					kGlowColor,										
					0,		
					0.1,		
					0.14)

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
	return(150.0)

def GetLaunchSound():
	return("DJCardassianTorpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 3500.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 5.0

def GetLifetime():
	return 30.0
