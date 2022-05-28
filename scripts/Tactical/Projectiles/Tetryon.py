#script modified by Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(100.0 / 255.0, 100.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CANitrolitic.tga",
					kCoreColor, 
					0.05,
					3.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					1.0,	
					0.05,	 
					0.1,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					50,		
					1.0,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.001)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.TACHYON)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("Tetryon Burst")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Tetryon Burst")

def GetDamage():
	return 1.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.3

import FoundationTech
import ftb.Tech.TetryonProjectile
      
sYieldName = ''
sFireName = ''

oFire = ftb.Tech.TetryonProjectile.oTetryonWeapon
FoundationTech.dOnFires[__name__] = oFire
FoundationTech.dYields[__name__] = oFire
