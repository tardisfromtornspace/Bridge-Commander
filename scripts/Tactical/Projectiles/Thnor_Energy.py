
import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(128.0 / 255.0, 235.0 / 255.0, 108.0 / 255.0, 0.500000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(100.0 / 255.0, 108.0 / 255.0, 1.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(128.0 / 255.0, 255.0 / 255.0, 118.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.5,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					1,	 
					0.01,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					22,		
					0.7,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)

	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("ThNor HCannon")

def GetPowerCost():
	return(40.0)

def GetName():
	return("ThNor Energy")

def GetDamage():
	return 210.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.7

