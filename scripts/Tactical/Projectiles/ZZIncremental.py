import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(125.0 / 255.0, 130.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(125.0 / 255.0, 255.0 / 255.0, 0.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_TNGPhotonCore.tga",
					kCoreColor, 
					0.3,
					4.2,	 
					"data/textures/tactical/ZZ_TNGPhotonGlow.tga", 
					kGlowColor,
					3.0,	
					0.35,	 
					0.6,	
					"data/textures/tactical/ZZST6PhotonFlares.tga",
					kGlowColor,										
					8,		
					0.1,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(19.0)

def GetLaunchSound():
	return("ZZ_ST6Photon2")

def GetPowerCost():
	return(1.0)

def GetName():
	return("Mauler")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 13.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 20.0

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
		'LOOK_CUSTOM_XTRA_DMG': 0.1,
		'LOOK_CUSTOM_MAX_DMG': GetDamage() * 9, # GetDamage() from the projectile script
		'LOOK_CUSTOM_INI_DMG': GetDamage(),
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()