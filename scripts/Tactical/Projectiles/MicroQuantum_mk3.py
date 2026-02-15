#script modified by WileyCoyote

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(163.0 / 255.0, 206.0 / 255.0, 241.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(33.0 / 255.0, 141.0 / 255.0, 250.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					6.0,	 
					"data/Textures/Tactical/WC_quantumtorp.tga", 
					kGlowColor,
					1.0,	
					0.8,	 
					0.7,	
					"data/Textures/Tactical/WC_quantumtorpFlares.tga",
					kGlowColor,						
					15,		
					0.2,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEPHASER)

	return(0)

def GetLaunchSpeed():
	return(60.0)

def GetLaunchSound():
	return("MicroQuantum")

def GetPowerCost():
	return(11.0)

def GetName():
	return("Micro Quantum Torpedoe")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.45
