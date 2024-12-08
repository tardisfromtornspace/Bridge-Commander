########################################################################
#	Filename:	Biomatter.py				       #
#								       #
#	Description:	Creates a Species 8472 Biomatter torpedo       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 10.0 / 255.0, 175.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(105.0 / 255.0, 0.0 / 255.0, 175.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 120.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.45,
					6.0,	 
					"data/Textures/Tactical/TransdimSMGlow.tga", 
					kGlowColor,
					3.0,	
					2.0,	 
					2.05,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					35,		
					1.25,		
					0.1)

	pTorp.SetDamage(GetDamage())
	pTorp.SetDamageRadiusFactor(0.35)
	pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
	pTorp.SetMaxAngularAccel(GetMaxAngularAccel())

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(75.00)

def GetLaunchSound():
	return("HVTransdimImaginaryTorp")

def GetPowerCost():
	return(20.0)

def GetDamage():
	return 165000.0

def GetName():
	return("HV Transdim Imaginary Torp")

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.4
