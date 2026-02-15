###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Quantum Torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(1.0 / 255.0, 255.0 / 255.0, 1.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(180.0 / 245.0, 40.0 / 255.0, 10.0 / 255., 1.000000)
	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
                    kCoreColor,
					0.2,
					0.1,	 
					"data/Textures/Tactical/KlingonTorpCore.tga", 
					kGlowColor,
					1.0,	
					1.6,	 
					1.5,	
					"data/Textures/Tactical/TorpedoFlare.tga",
					kFlareColor,										
					4,		
					0.5,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.3)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.Quantum)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("GravimetricQuantum")

def GetPowerCost():
	return(50.0)

def GetName():
	return("Gravimetric Quantum")

def GetDamage():
	return 1650.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.7
