#script modified by Lint

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(140.0 / 255.0, 186.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/LintsDomTorp.tga",
					kCoreColor, 
					0.5,
					10.9,	 
					"data/Textures/Tactical/LintsQuantumCore.tga", 
					kGlowColor,
					6.0,	
					0.5,	 
					0.5,	
					"data/Textures/Tactical/LintsQuantumCore.tga",
					kGlowColor,										
					90,		
					0.05,		
					90.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(60.0)

def GetLaunchSound():
	return("RomTorpJLH")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Dominion Torpedo")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 1.5

