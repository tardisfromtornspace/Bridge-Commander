#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.6, 0.6, 1.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.3, 0.3, 1.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					7.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					25.0,	
					0.2,	 
					0.8,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,		
					0.2,		
					0.2)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.000001)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.ZZ_BREENTORP)

	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("BreenTorpedoXL")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Ion Burst")

def GetDamage():
	return 5.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.1

import FoundationTech
import ftb.Tech.IonProjectile
      
sYieldName = ''
sFireName = ''

oFire = ftb.Tech.IonProjectile.oIonWeapon
FoundationTech.dOnFires[__name__] = oFire
FoundationTech.dYields[__name__] = oFire
