###############################################################################
#	Create(pTorp)
#	
#	Creates a phased plasma torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero             MRJOHN 5-9-2003
###############################################################################
import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.827000, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.650000, 0.650000, 0.150000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.04) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.09)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return 66.0

def GetLaunchSound():
	return("Thnor Energy")

def GetPowerCost():
	return(35.0)

def GetName():
	return("Drakh Weapon")

def GetDamage():
	return 200.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 4.0

def GetLifetime():
	return 24.0