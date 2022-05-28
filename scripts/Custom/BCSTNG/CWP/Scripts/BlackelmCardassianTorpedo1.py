import App
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 45.0 / 255.0, 0.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 200.0 / 255.0, 202.0 / 255.0, 1.000000)
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.2,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.15,	 
					0.3,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.35,		
					0.4)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CARDTORP)
	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("blackelmcardassiantorpedo1")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Cardassian Photon")

def GetDamage():
	return 600.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.3
