#script modified by Greystar

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					4.2,		 
					"data/Textures/Tactical/CAKlingonGlow.tga", 
					kGlowColor,
					3.0,	
					0.35,	 
					0.6,	
					"data/Textures/Tactical/WC_photontorpFlares.tga",
					kGlowColor,						
					18,		
					0.1,		
					0.4)

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
	return(70.0)

def GetLaunchSound():
	return("TexasMicroPhoton")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Micro Photon")

def GetDamage():
	return 750.0

def GetGuidanceLifetime():
	return 4.0

def GetMaxAngularAccel():
	return 0.8
