import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.0, 0.5, 1.0, 1.0)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.001, 0.5, 1.0, 1.0)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 10.0, 0.12) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(3.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(80.0)

def GetLaunchSound():
	return("ImpIon2")

def GetPowerCost():
	return(5.0)

def GetName():
	return("IonLow2")

def GetDamage():
	return 20.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 8.0
