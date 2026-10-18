# File: Z (Python 1.5)

import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.007843, 1.0, 0.007843, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(0.639216, 1.0, 0.639216, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 1.5, 0.08)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.DISRUPTOR)
    return 0


def GetLaunchSpeed():
    return 80.0


def GetLaunchSound():
    return 'ZZTurboLaser2'


def GetPowerCost():
    return 0.0


def GetName():
    return 'Laser'


def GetDamage():
    return 40.0


def GetGuidanceLifetime():
    return 1.0


def GetMaxAngularAccel():
    return 0.125


def GetLifetime():
    return 10.0


import traceback
try:
	import FoundationTech
	import ftb.Tech.TimedTorpedoesExpansion

	# You would need to add another import for each different file you are importing a function from.
	# import ftb.Tech.TimedTorpedoesExpansion
	repeatClass = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassDLoop
	newFuncRepeat = ftb.Tech.TimedTorpedoesExpansion.newCustomFunctionFor1           # <--- and you would change that, too

	ActClass = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassLoop
	newFuncAct = ftb.Tech.TimedTorpedoesExpansion.newCustomFunctionFor2              # <--- and you would change that, too

	oFire = ftb.Tech.TimedTorpedoesExpansion.MIRVMultiSingleTargetTorpedoFire2(
		'MIRVMultiSingleTargetTorpedoFire2', {
		'alternateClassCall1': repeatClass,
		'alternateClassCall2': ActClass,
		'alternateClassCall1Extras': 1,
		'multipleTargetSelect': 1,
		'spreadNumber': 3,
		'spreadDensity': 4.5,
		'warheadModule': "Tactical.Projectiles.ZZSpread2",
		'shellLive': 0,
		'CustomFunction': newFuncRepeat,
		'CustomFunction2': newFuncAct,
		'LOOK_CUSTOM_XTRA_DMG': -0.01,
		'LOOK_CUSTOM_MAX_DMG': GetDamage() * 9, # GetDamage() from the projectile script
		'LOOK_CUSTOM_INI_DMG': GetDamage(),
		'LOOK_CUSTOM_MIN_DMG': GetDamage() * 0.01,
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()

