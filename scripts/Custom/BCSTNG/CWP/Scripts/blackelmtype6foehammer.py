import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.398000, 0.210001, 0.5005000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.940000, 0.940000, 0.940000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.095) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)
	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("blackelmtype6foehammer")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Type 6 Enh Photon")

def GetDamage():
	return 850.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.5
