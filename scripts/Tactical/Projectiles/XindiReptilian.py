import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.8, 1.0, 0.2, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(1.0, 0.8, 0.2, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 1.0, 0.1)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PULSEDISRUPT)
    return 0

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("XindiReptilian")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Xindi Reptilian Torpedo")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.13
