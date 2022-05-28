import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(170.0 / 255.0, 240.0 / 255.0, 240.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(1.0 / 255.0, 159.0 / 255.0, 250.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor, 
					0.2,
					0.93,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.23,	 
					0.47,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					8,		
					0.54,		
					0.08)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(80.0)

def GetLaunchSound():
	return("FluxTorpedo")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Vulcan Advanced")

def GetDamage():
	return 2000

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 8.25

