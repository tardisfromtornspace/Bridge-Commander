#script modified by D&G Productions

import App
import string
pWeaponLock = {}

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(10.0 / 255.0, 10.0 / 255.0, 10.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)	


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/AlphaQuantumCore.tga",
					kCoreColor, 
					0.75,
					6.0,	 
					"data/Textures/Tactical/AlphaQuantumGlow.tga", 
					kGlowColor,
					3.0,	
					2.0,	 
					2.05,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					35,		
					0.275,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(5.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(200.0)

def GetLaunchSound():
	return("AlphaQuantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Alpha Quantum")

def GetDamage():
	return 7500.0

def GetGuidanceLifetime():
	return 45.0

def GetMaxAngularAccel():
	return 2.5

def GetFlashColor():
	return (55.0, 55.0, 255.0)

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"