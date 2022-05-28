import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.000000, 0.000000, 1.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.33, 0.10) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.FUSIONBOLT)
	return(0)

def GetLaunchSpeed():
	return(175.0)

def GetLaunchSound():
	return("blackelmpulsephaser4")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Pulse Phasers")

def GetDamage():
	return 250.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 4
