#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(100.0 / 255.0, 20.0 / 255.0, 220.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(210.0 / 255.0, 120.0 / 255.0, 180.0 / 255.0, 2.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(216.0 / 255.0, 84.0 / 255.0, 0.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/RepulsionWaveTorpCore.tga",
					kCoreColor, 
					0.25,
					0.25,	 
					"data/textures/tactical/QuantumXCore.tga", 
					kGlowColor,
					2.0,	
					1.5,	 
					1.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					550,		
					0.15,		
					0.015)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CAPHASEQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("IsolyticQuantum")

def GetPowerCost():
	return(50.0)

def GetName():
	return("Isolytic Quantum")

def GetDamage():
	return 3500.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 0.3
