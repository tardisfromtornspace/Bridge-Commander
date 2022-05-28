import App
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(225.0/ 191.0, 255.0 / 49.0, 17.0 / 255.0, 1.000000)
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.1,
					1.2,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.2,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,						
					30,		
					0.1,		
					0.5)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)
	return(0)

def GetLaunchSpeed():
	return(30)

def GetLaunchSound():
	return("blackelmtype6photon")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Type 6 Photon : 2")

def GetDamage():
	return 850.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.35

try:
	import FoundationTech
	import ftb.Tech.TimedTorpedoes

	oFire = ftb.Tech.TimedTorpedoes.MIRVSingleTargetTorpedo(
		'Spread2', {
			'spreadNumber':	2,
			'spreadDensity': 7.5,
			'warheadModule': 'Custom.BCSTNG.CWP.Scripts.blackelmtype6',
			'shellLive': 0,
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	pass
