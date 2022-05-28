import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.400000, 0.300000, 1.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.900000, 0.900000, 1.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.5, 0.50) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType(Multiplayer.SpeciesToTorp.DISRUPTOR)
	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("blackelmdominionpulse1")

def GetPowerCost():
	return(100.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.25

def GetLifetime():
	return 8.0
