import App
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.788235, 0.176471, 0.113725, 0.423529)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.807843, 0.603922, 0.752941)

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
	return(30.0)

def GetLaunchSound():
	return("Phase Disrupers")

def GetPowerCost():
	return(15.0)

def GetName():
	return("Phase Disrupers")

def GetDamage():
	return 70.0

def GetGuidanceLifetime():
	return 1.4

def GetMaxAngularAccel():
	return 0.021

def GetLifetime():
	return 16.0
