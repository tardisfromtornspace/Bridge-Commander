import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.172549, 1.000000, 0.172549, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.639216, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.8, 0.07) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)
	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("blackelmbreldisruptorpulse")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 300.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.35

def GetLifetime():
	return 5.0
