import App
from Custom.Techs.PhasedTorpedoV1 import *

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(180.0 / 255.0, 180.0 / 255.0, 255.0 / 255.0, 1.0)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(123.0 / 255.0, 106.0 / 255.0, 221.0 / 255.0, 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(39.0 / 255.0, 77.0 / 255.0, 244.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.2,
					9.0,
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,
					0.3,
					0.4,
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,
					40,
					0.17,
					0.16)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.17)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(27)

def GetLaunchSound():
	return("Quantum Torpedo")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Phase Quantum")

def GetDamage():
	return 0.0001  ## Damage done to shields

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.2
