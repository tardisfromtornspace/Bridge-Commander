import App
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(255.0 / 255.0, 39.0 / 255.0, 9.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(245.0 / 255.0, 65.0 / 255.0, 20.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.35, 0.05) 	
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
	return(28.0)

def GetLaunchSound():
	return("Phase Disrupers")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Phase Disrupers")

def GetDamage():
	return 45.0

def GetGuidanceLifetime():
	return 1.3

def GetMaxAngularAccel():
	return 0.02

def GetLifetime():
	return 15.0
