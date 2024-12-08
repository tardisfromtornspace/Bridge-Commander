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
	kCoreColor.SetRGBA(0.850000, 1.000000, 0.600000, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.000000, 1.000000, 0.650000, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.55,
					0.9,	 
					"data/Textures/Tactical/TransdimSMGlow.tga", 
					kGlowColor,
					6.0,	
					2.6,	 
					3.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					88,		
					0.85,		
					0.250)

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
	return("HVTransdimTorp")

def GetPowerCost():
	return(20.0)

def GetDamage():
	return 65000.0

def GetName():
	return("HV Transdim Strangematter")

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.4
