import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.00782, 1.0, 0.00782, 1.0)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.59, 1.0, 0.59, 1.0)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.08) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.12)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

    return 0


def GetLaunchSpeed():
    return 53.0

def GetLaunchSound():
    return 'Romulan Disruptor'

def GetPowerCost():
    return 60.0

def GetName():
    return 'Phased Disruptor'

def GetDamage():
    return 130

def GetGuidanceLifetime():
    return 0.0

def GetMaxAngularAccel():
    return 0.05

def GetLifetime():
    return 3.0