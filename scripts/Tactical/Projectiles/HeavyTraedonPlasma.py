#modded by grey

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(225.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(50.0 / 255.0, 50.0 / 255.0, 100.0 / 255.0, 1.000000)	


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.45,
					6.0,	 
					"data/Textures/Tactical/Quantum03Glow.tga", 
					kGlowColor,
					3.0,	
					2.0,	 
					2.05,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					35,		
					1.25,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.35)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.RAPIDQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(110.0)

def GetLaunchSound():
	return("HeavyTraedonPlasma")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Traedon Heavy Plasma")

def GetDamage():
	return 55500.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 5.0