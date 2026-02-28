import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 255.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 0.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZMauler1Core.tga",
					kCoreColor, 
					0.1,
					5.0,	 
					"data/textures/tactical/ZZMauler1Glow.tga", 
					kGlowColor,
					7.0,	
					0.3,	 
					0.5,	
					"data/textures/tactical/ZZMauler1Core.tga",
					kCoreColor,										
					20,		
					0.35,		
					0.3)

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
	return("ZZ_Mauler")

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
	oFire = ftb.Tech.TimedTorpedoesExpansion.MIRVMultiSingleTargetTorpedoFire2(
		'MIRVMultiSingleTargetTorpedoFire2', {
		'multipleTargetSelect': 0,
		'splitProx': 229,
		'chkInterval': 3,
		'spreadNumber': 1,
		'spreadDensity': 360.1,
		'warheadModule': "Tactical.Projectiles.ZZSpread2",
		'shellLive': 0,
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()