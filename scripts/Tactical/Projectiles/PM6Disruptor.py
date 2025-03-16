###############################################################################
#	Filename:	Disruptor.py
#		
#	Script for filling in the attributes of disruptor blasts.
#	
#	 7/19/2003 byMRJOHN 
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a disruptor blast.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 1.000000, 0.700000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.6, 0.06) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.95)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(76.0)

def GetLaunchSound():
	return("IntrepidCannon")

def GetPowerCost():
	return(15.0)

def GetName():
	return("PM6Disruptor")

def GetDamage():
	return 300.0

def GetGuidanceLifetime():
	return 0.9

def GetMaxAngularAccel():
	return 4.0

def GetLifetime():
	return 8.0
