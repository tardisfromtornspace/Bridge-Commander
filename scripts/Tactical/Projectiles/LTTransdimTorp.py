#script modified by D&G Productions

import App
import MissionLib

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 240.0 / 255.0, 140.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(135.0 / 255.0, 255.0 / 255.0, 135.0 / 255.0, 1.000000)	


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/QuasarFX.tga",
					kCoreColor, 
					0.35,
					6.0,	 
					"data/Textures/Tactical/TDwave.tga", 
					kGlowColor,
					3.0,	
					0.8,	 
					0.825,	
					"data/Textures/Tactical/MegaPhaserFX.tga",
					kGlowColor,										
					55,		
					0.3375,		
					0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(120.0)

def GetLaunchSound():
	return("LTTransdimTorp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("LT Transdim Strangematter")

def GetDamage():
	return 40000.0

def GetGuidanceLifetime():
	return 8.5

def GetMaxAngularAccel():
	return 0.45
