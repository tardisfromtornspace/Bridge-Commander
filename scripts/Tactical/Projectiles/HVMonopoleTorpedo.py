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
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(245.0 / 255.0, 40.0 / 255.0, 145.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TransGravCore.tga",
					kCoreColor,
					1.2,
					0.5,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					6.0,	
					2.5,	 
					5.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					65,		
					0.65,		
					0.35)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
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
	return("HeavyMonopoleTorpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Heavy Monopole Torpedo")

def GetDamage():
	return 150000

def GetGuidanceLifetime():
	return 7.5

def GetMaxAngularAccel():
	return 0.50