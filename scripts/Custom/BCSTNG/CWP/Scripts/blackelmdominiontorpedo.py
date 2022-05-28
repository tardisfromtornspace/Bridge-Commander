import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(100.0 / 255.0, 200.0 / 255.0, 250.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(50.0 / 255.0, 125.0 / 255.0, 175.0 / 255.0, 1.000000)
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.2,	 
					0.25,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,										
					30,		
					0.2,		
					0.4)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)
	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("blackelmdominiontorpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Polaron Torp")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.75
