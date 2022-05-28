import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.172549, 1.000000, 0.172549, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.639216, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.8, 0.15) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)
	return(0)

def GetLaunchSpeed():
	return(95.0)

def GetLaunchSound():
	return("blackelmwarbirdpulsedisruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 350.0

def GetGuidanceLifetime():
	return 2.0

def GetMaxAngularAccel():
	return 0.5

def GetLifetime():
	return 8.0
