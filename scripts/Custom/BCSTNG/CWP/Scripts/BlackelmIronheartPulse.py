import App
def Create(pTorp):
	debug(__name__ + ' def Create')
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.400000, 0.000001, 0.0005000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 0.700000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.5, 0.07) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)
	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("blackelmpulsephaser1")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Pulse Phaser")

def GetDamage():
	return 200.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.05

def GetLifetime():
	return 12.0

