import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.33, 0.10) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)
	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("blackelmpulsephaser3")

def GetPowerCost():
	return(10.0)

def GetName():
	return("PulsePhsr")

def GetDamage():
	return 150.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.025

def GetLifetime():
	return 10.0

