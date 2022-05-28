import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.7, 0.008) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.04)
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
	return(16.0)

def GetLaunchSound():
	return("cmissile")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Concussion")

def GetDamage():
	return 70.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.3

def GetLifetime():
	return 13.0
