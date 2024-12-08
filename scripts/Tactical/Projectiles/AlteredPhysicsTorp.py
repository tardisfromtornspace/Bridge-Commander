import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, App.g_kSystemWrapper.GetRandomNumber(255) / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.4,
					1.2,	 
					"data/Textures/Tactical/AlPhTorpGlow.tga", 
					kGlowColor,
					5.0,	
					0.9,	 
					1.2,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					150,		
					0.8,		
					0.05)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("AlPhTorp")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Altered Physics Torpedo")

def GetDamage():
	return 350000.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.65
