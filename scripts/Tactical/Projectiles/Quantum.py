	###############################################################################
#	Filename:	PatriotQuantum.py
#	
#	
#	Created:	17/10/05 -	RBE
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a quantum torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 2.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(40.0 / 255.0, 100.0 / 255.0, 255.0 / 255.0, 2.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 2.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/QuantumTorpedoCore.tga",
					kCoreColor, 
					0.35,
					6.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					6.0,	
					0.6,	 
					0.7,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,									
					6,		
					0.1,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("QuantumTorp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 2450.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 3.15
