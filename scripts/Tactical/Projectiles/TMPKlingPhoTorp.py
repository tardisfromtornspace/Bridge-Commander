###############################################################################
#	Filename:	TMPKlingPhoTorp.py
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	12/2/07 -	Dan Kirk
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Photon Torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 86.0 / 255.0, 69.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 130.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 71.0 / 255.0, 42.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TMPCore.tga",
					kCoreColor, 
					0.09,
					0.2,	 
					"data/Textures/Tactical/TMPGlow.tga", 
					kGlowColor,
					2.3,	
					0.5,	 
					0.8,	
					"data/Textures/Tactical/TMPFlares.tga",
					kGlowColor,										
					10,		
					0.8,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("Kling Photorp")

def GetPowerCost():
	return(15.0)

def GetName():
	return("Photon")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 2.0
