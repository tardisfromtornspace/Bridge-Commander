#script modified by FekLeyrTarg
import App
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.6, 1.0, 0.6, 1.0)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.0, 1.0, 0.0, 1.0)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 5, 0.07) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("TOS-disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 110.0

def GetGuidanceLifetime():
	return 0.5

def GetMaxAngularAccel():
	return 0.15

def GetLifetime():
	return 8.0
