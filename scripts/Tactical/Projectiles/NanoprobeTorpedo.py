import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA((225.0 / 255.0), (255.0 / 255.0), (225.0 / 255.0), 1.0)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA((200.0 / 255.0), (255.0 / 255.0), (200.0 / 255.0), 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA((100.0 / 255.0), (255.0 / 255.0), (100.0 / 255.0), 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.07,
					0.8,
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,
					0.45,
					0.55,
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,
					10,
					0.5,
					0.11)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.05)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(24)

def GetLaunchSound():
	return("FedTransphasic")

def GetPowerCost():
	return(12.0)

def GetName():
	return("Nanoprobe Torpedo")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.3

import FoundationTech
import ftb.Tech.Nanoprobe
      
sYieldName = ''
sFireName = ''

oFire = ftb.Tech.Nanoprobe.oNanoprobeWeapon
FoundationTech.dOnFires[__name__] = oFire
FoundationTech.dYields[__name__] = oFire
