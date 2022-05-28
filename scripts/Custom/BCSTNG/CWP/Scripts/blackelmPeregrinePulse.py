import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.400000, 0.000001, 0.0005000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 0.700000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.25, 0.07) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)
	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("blackelmpulsephaser2")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Pulse Phaser")

def GetDamage():
	return 400.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 1.0

def GetLifetime():
	return 12.0

