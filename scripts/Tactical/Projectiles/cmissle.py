import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.0005, 0.2, 2.0, 1.5)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.0, 1.0, 1.0, 1.0)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.3, 0.01) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(26.0)

def GetLaunchSound():
	return("cmissle")

def GetPowerCost():
	return(30.0)

def GetName():
	return("C.missile")

def GetDamage():
	return 180.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.3
