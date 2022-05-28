#script modified by WileyCoyote

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(32.0 / 255.0, 105.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					6.0,	 
					"data/Textures/Tactical/WC_photontorp.tga", 
					kGlowColor,
					1.0,	
					0.5,	 
					0.6,	
					"data/Textures/Tactical/WC_photontorpFlares.tga",
					kGlowColor,						
					12,		
					0.3,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("Quantum Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 1700.0

def GetGuidanceLifetime():
	return 30.0

def GetMaxAngularAccel():
	return 1.0
