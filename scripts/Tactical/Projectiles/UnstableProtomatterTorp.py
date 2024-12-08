########################################################################
#	Filename:	FedHellfire.py				       #
#								       #
#	Description:	Creates a Federation Hellfire torpedo 	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/29/2005				       #
########################################################################

import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(1, 0.254902, 0.075, 1)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.925491, 1, 0.066667, 1)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(1, 0, 0.09, 1)
	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.7,
					2.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					4.0,	 
					4.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					48,		
					2.7,		
					1.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.45)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime ())
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("UnstableProtomatterTorp")

def GetPowerCost():
	return(1000.0)

def GetName():
	return("Unstable Protomatter Torp")

def GetDamage():
	return 140000.0

def GetGuidanceLifetime():
	return 7.5

def GetMaxAngularAccel():
	return 2.5