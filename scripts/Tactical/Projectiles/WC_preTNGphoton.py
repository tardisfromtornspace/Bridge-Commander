#script modified by WileyCoyote

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(243.0 / 255.0, 91.0 / 255.0, 53.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.08,
					6.0,	 
					"data/Textures/Tactical/WC_quantumtorp.tga", 
					kGlowColor,
					1.0,	
					0.9,	 
					0.8,	
					"data/Textures/Tactical/WC_photontorpFlares.tga",
					kGlowColor,						
					12,		
					0.2,		
					0.2)

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
	return(30.0)

def GetLaunchSound():
	return("WCpreTNGtorpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Pre TNG Photon")

def GetDamage():
	return 490.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 1.5
