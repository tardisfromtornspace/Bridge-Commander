import App
def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(200.0 / 255.0, 230.0 / 200.0, 199.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(65.0 / 255.0, 250.0 / 65.0, 65.0 / 255.0, 1.000000)	


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.2,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.8,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )



	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(8.0)

def GetLaunchSound():
	return("ThNor Missile")

def GetPowerCost():
	return(20.0)

def GetName():
	return("ThNor Missile")

def GetDamage():
	return 150.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.25