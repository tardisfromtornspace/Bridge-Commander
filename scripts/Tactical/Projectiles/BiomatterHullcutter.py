import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(236.0 / 255.0, 255.0 / 255.0, 17.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(181.0 / 255.0, 230.0 / 255.0, 253.0 / 255.0, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 3, 0.25) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.5)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(125.0)

def GetLaunchSound():
	return("BiomatterHullcutter")

def GetPowerCost():
	return(100)

def GetName():
	return("Biomatter Hullcutter")

def GetDamage():
	return 27500.0

def GetGuidanceLifetime():
	return 1.5

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 35.0
