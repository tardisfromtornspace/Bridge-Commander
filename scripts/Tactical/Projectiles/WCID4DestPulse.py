import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(147.0 / 203.0, 251.0 / 255.0, 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					1.0,
					1.2,	 
					"data/textures/tactical/WCID4DestPulse.tga", 
					kGlowColor,
					10.0,	
					5.2,	 
					5.0,	
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
	return(200.0)

def GetLaunchSound():
	return("WCID4destpulse")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Destructive Pulse")

def GetDamage():
	return 60000.0

def GetGuidanceLifetime():
	return 25.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 20.0
