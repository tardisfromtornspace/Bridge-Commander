#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 128.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
							"data/Textures/Tactical/TorpedoCore.tga",
							kCoreColor, 
							0.6,
							0.65,	 
							"data/Models/Effects/PulseP.tga", 
							kGlowColor,
							3.5,	
							0.5,	 
							0.65,	
							"data/Textures/Tactical/TorpedoFlares.tga",
							kFlareColor,							
							25,		
							1.0,		
							0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.60)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("HQuantum2")

def GetPowerCost():
	return(1900.0)

def GetName():
	return("Hyperquantum Mk.2")

def GetDamage():
	return 7631.0

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 0.75
