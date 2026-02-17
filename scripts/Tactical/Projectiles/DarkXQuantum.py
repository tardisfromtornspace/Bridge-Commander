#script modified by Greystar

import App
import MissionLib

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(1.0 / 255.0, 0.0 / 255.0, 1.0 / 255.0, 1.0)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(125.0 / 255.0, 128.0 / 255.0, 204.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(1.0 / 255.0, 0.0 / 255.0, 1.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.65,
					0.750,	 
					"data/Textures/Tactical/S79QuantumGlow.tga", 
					kGlowColor,
					3.0,	
					4.0,	 
					4.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					35,		
					0.395,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.45)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(110.0)

def GetLaunchSound():
	return("DarkXQuantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Dark X Quantum")

def GetDamage():
	return 4500.0 * 4.5

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 1.0
