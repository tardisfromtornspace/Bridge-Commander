import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(200.0 / 255.0, 230.0 / 200.0, 199.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(65.0 / 255.0, 250.0 / 65.0, 65.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.2,	 
					0.6,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.8,		
					0.4)
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
	return("blackelmklingontorpedo2")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Klingon Adv Photon")

def GetDamage():
	return 850.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.35
