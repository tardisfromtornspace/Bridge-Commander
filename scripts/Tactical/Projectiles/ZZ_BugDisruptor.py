import App
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.0 / 255.0, 185.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(186.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.8, 0.05) 	

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
	return(80.0)

def GetLaunchSound():
	return("BugDisruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("BugDisruptor")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 0.7

def GetMaxAngularAccel():
	return 0.17

def GetLifetime():
	return 8.0
