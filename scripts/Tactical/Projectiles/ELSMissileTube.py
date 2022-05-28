###############################################################################
#	Filename:	QuantumTorpedo.py
#		
#	Script for filling in the attributes of Fusion torpedos.
#	
#	 1/19/2005 byMRJOHN 
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Fusion torpedo.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.380392, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.870588, 0.662745, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.02, 0.02) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.08)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(96.0)

def GetLaunchSound():
	return("ValiantMissile")

def GetPowerCost():
	return(16.0)

def GetName():
	return("ELS Missile Tube")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 2.0

def GetLifetime():
	return 9.0
