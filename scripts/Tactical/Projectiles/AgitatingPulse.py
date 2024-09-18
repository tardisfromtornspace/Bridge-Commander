import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(255.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 0.5000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(150.0 / 255.0, 75.0 / 255.0, 10.0 / 255.0, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.5, 0.125) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(105.0)

def GetLaunchSound():
	return("AgitatorPulse")

def GetPowerCost():
	return(50)

def GetName():
	return("Agitating Pulse")

def GetDamage():
	return 550.0

def GetGuidanceLifetime():
	return 0.25

def GetMaxAngularAccel():
	return 0.125

