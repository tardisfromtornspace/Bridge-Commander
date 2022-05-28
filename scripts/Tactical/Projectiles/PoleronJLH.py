#Made by ZambieZan, modified by Dragon

import App

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 186.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_BreenCore.tga",
					kCoreColor,
					0.2,
					1.2,	 
					"data/Textures/Tactical/ZZ_BreenGlow.tga", 
					kGlowColor,
					2.0,	
					0.25,	 
					0.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					15,		
					0.05,		
					0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.05)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POLERON)

	return(0)

def GetLaunchSpeed():
	return(30)

def GetLaunchSound():
	return("Polaron Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Polaron Torpedo")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.5
