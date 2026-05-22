#script modified by D&G Productions

import App
import MissionLib

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(104.0 / 255.0, 124.0 / 255.0, 197.0 / 255.0, 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(130.0 / 255.0, 3.0 / 255.0, 248.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.5,
					0.8,	 
					"data/Textures/Tactical/S79QuantumGlow.tga", 
					kGlowColor,
					4.0,	
					1.0,	 
					2.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					96,		
					0.40,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.075)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(150.0)

def GetLaunchSound():
	return("MicroT20Quantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Micro T20 Quantum")

def GetDamage():
	return 2520.0 * 4

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 10.0