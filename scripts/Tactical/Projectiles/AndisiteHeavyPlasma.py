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
	kGlowColor.SetRGBA(0.000000, 0.780000, 0.720000, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.000000, 1.000000, 0.650000, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					1.0,
					0.5,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					6.0,	
					0.5,	 
					0.85,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					88,		
					0.65,		
					0.35)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(55.00)

def GetLaunchSound():
	return("AndisiteHeavyPlasma")

def GetPowerCost():
	return(20.0)

def GetName():
	return("A Heavy Plasma")

def GetDamage():
	return 10500

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.350