import App
import MissionLib

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 110.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 245.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_RMPlasmaCore.tga",
					kCoreColor, 
					0.13,
					4.0,	 
					"data/textures/tactical/ZZ_RMPlasmaGlow.tga", 
					kGlowColor,
					6.0,	
					0.55,	 
					0.25,	
					"data/textures/tactical/ZZ_RMPlasmaCore.tga",
					kGlowColor,										
					55,		
					0.45,		
					0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(100)

def GetLaunchSound():
	return("TrimorphicVolaton")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Trimorphic Volaton")

def GetDamage():
	return 5300.0 * 4

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 0.15
