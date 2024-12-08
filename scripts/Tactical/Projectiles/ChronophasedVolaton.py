import App
def Create(pTorp):
	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(125.0 / 155.0, 5.0 / 15.0, 235.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(175.0 / 130.0, 150.0 / 150.0, 5.0 / 5.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/apccore.tga",
					kCoreColor, 
					0.5,
					2.0,	 
					"data/textures/tactical/TorpedoGlow.tga", 
					kGlowColor,
					1.25,	
					1.0,	 
					1.35,	
					"data/textures/tactical/qflare.tga",
					kFlareColor,										
					65,		
					0.85,		
					0.50)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.250)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.RAPIDQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("ChronophasedVolaton")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Chronophased Volaton")

def GetDamage():
	return 5250.0

def GetGuidanceLifetime():
	return 15.5

def GetMaxAngularAccel():
	return 1.50
