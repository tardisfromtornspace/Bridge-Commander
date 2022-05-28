import App
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(190.0 / 255.0, 49.0 / 255.0, 48.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 218.0 / 255.0, 202.0 / 255.0, 1.000000)
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/BlackElmTorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/BlackElmTorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.2,	 
					0.4,	
					"Scripts/Custom/BCSTNG/CWP/Textures/BlackElmTorpedoFlares.tga",
					kGlowColor,										
					8,		
					1.2,		
					0.04)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)
	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("blackelmklingontorpedo1")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Klingon Photon")

def GetDamage():
	return 750.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 0.45
