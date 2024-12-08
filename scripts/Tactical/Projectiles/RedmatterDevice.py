#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 2.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 2.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"data/Textures/Tactical/NemQuantumGlow.tga", 
					kCoreColor,
					4.0,	
					8.3,	 
					8.1,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					300,		
					0.4,		
					0.04)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.50)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("ZRedmatterTorp")

def GetPowerCost():
	return(1.0)

def GetName():
	return("Redmatter Torpedo")

def GetDamage():
	return 65500.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 0.65
