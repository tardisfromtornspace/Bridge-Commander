import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.007843, 1.000000, 0.007843, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.639216, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.0, 0.2) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)
	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("blackelmvorchadisruptorpulse")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 2.0

def GetMaxAngularAccel():
	return 0.25

def GetLifetime():
	return 8.0
