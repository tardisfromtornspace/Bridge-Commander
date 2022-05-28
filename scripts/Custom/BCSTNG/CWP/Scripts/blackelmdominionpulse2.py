import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.0/255.0, 128.0/255.0, 255.0/255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.0/255.0, 239.0/255.0, 255.0/255.0, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.0, 0.2) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)
	return(0)

def GetLaunchSpeed():
	return(90.0)

def GetLaunchSound():
	return("blackelmdominionpulse2")

def GetPowerCost():
	return(10.0)

def GetName():
	return("DomCannon2")

def GetDamage():
	return 250.0

def GetGuidanceLifetime():
	return 0.5

def GetMaxAngularAccel():
	return 0.5

def GetLifetime():
	return 8.0
