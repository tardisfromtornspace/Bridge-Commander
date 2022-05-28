########################################################################
#	Filename:	PlasmaGlobule.py			       #
#								       #
#	Description:	Creates a Borg Plasma Cannon projectile	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.007843, 1.000000, 0.007843, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.639216, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 3.6, 0.6) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Borg Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("BorgDisruptor")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 10.0
