###############################################################################
#	Filename:	QuantumTorpedo.py
#			
#	Script for filling in the attributes of Fusion torpedoes.
#	
#	Created:	6-3-2003	MRJOHN
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Fusion torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 25.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.0,
					0.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					9,	
					0.8,	 
					3.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					300,		
					1.9,		
					5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.30)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Quantum Torpedo")

def GetPowerCost():
	return(100.0)

def GetName():
	return("UltriumBurst")

def GetDamage():
	return 990.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 6.0
