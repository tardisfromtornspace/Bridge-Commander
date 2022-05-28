#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.0,
					0.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.0,	
					0.0,	 
					0.0,	
					"data/Textures/Tactical/SubspaceFlares.tga",
					kGlowColor,										
					0.0,		
					0.0,		
					0.0)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.000001)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.REMANPULSE)

	return(0)

def GetLaunchSpeed():
	return(1000.0)

def GetLaunchSound():
	return("None")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Energy Dissipator")

def GetDamage():
	return 0.000001

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 1.0

import FoundationTech
import ftb.Tech.EnergyDissipator
      
sYieldName = ''
sFireName = ''

oFire = ftb.Tech.EnergyDissipator.oIonWeapon
FoundationTech.dOnFires[__name__] = oFire
FoundationTech.dYields[__name__] = oFire
