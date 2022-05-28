import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 175.0, 174.0 / 71.0, 66.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(151.0 / 200.0, 15.0 / 100.0, 11.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(151.0 / 200.0, 15.0 / 100.0, 11.0 / 255.0, 1.000000)		
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmorioncore.tga",
					kCoreColor, 
					0.2,
					0.3,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmorionglow.tga", 
					kGlowColor,
					0.1,	
					0.2,	 
					0.2,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmorionflare.tga",
					kFlareColor,										
					200,		
					0.1,		
					0.2)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)
	return(0)

def GetLaunchSpeed():
	return(35.0)

def GetLaunchSound():
	return("blackelmorionplasma")

def GetPowerCost():
	return(75.0)

def GetName():
	return("Plasma")

def GetDamage():
	return 300.0

def GetGuidanceLifetime():
	return 16.0

def GetMaxAngularAccel():
	return 0.15
