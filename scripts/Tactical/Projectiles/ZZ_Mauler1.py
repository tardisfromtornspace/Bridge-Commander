import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 176.0 / 255.0, 77.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 242.0 / 255.0, 135.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZMauler1Core.tga",
					kCoreColor, 
					0.2,
					3.0,	 
					"data/textures/tactical/ZZMauler1Glow.tga", 
					kGlowColor,
					3.0,	
					0.5,	 
					0.7,	
					"data/textures/tactical/ZZ_ZZMauler1Core.tga",
					kGlowColor,																		10,		
					0.6,		
					0.6)
					

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("")

def GetPowerCost():
	return(0.0)

def GetName():
	return("")

def GetDamage():
	return 4500.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0

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
		'warheadModule': "Tactical.Projectiles.ZZ_Mauler2",
		'shellLive': 0,
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()
