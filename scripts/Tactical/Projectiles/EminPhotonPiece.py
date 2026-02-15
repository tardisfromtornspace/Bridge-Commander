
import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 160.0 / 255.0, 0.0 / 255.0, 1.0)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 225.0 / 255.0, 100.0 / 255.0, 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 220.0 / 255.0, 0.0 / 255.0, 1.0)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.065,
					1.5,	 
					"data/Textures/Tactical/BorgAkiraTorpGlow.tga", 
					kGlowColor,
					2.5,	
					0.85,	 
					0.25,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.65,		
					0.15)

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
	return(75.0)

def GetLaunchSound():
	return("")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon XXVI Component")

def GetDamage():
	return 350.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 0.85

def GetLifetime():
	return 30.0

def GetFlashColor():
	return (165.0, 40.0, 0.0)
