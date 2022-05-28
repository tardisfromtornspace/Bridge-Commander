import App
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(238.0 / 255.0, 158.0 / 255.0, 5.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(244.0 / 255.0, 236.0 / 255.0, 155.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.10) 	
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
	return(45.0)

def GetLaunchSound():
	return("WCSonaPhoton2")

def GetPowerCost():
	return(15.0)

def GetName():
	return("Sona Pulse")

def GetDamage():
	return 400.0

def GetGuidanceLifetime():
	return 1.4

def GetMaxAngularAccel():
	return 0.021

def GetLifetime():
	return 16.0
