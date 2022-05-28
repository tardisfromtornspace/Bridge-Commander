import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 200.0 / 255.0, 155.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 200.0 / 255.0, 155.0 / 255.0, 0.500000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 200.0 / 255.0, 155.0 / 255.0, 0.500000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/RomulanPlasma.tga",
					kCoreColor,
					0.07,
					0.8,
					"data/Textures/Tactical/RomulanPlasma.tga",
					kGlowColor,
					2.0,
					0.55,
					0.65,
					"data/Textures/Tactical/Plasma.tga",
					kGlowColor,
					10,
					1.4,
					0.11)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(45)

def GetLaunchSound():
	return("FedTransphasic")

def GetPowerCost():
	return(50.0)

def GetName():
	return("Transphasic Torpedo")

def GetDamage():
	return 8000.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.3

import FoundationTech
import ftb.Tech.FedTransphasic
      
sYieldName = ''
sFireName = ''

oFire = ftb.Tech.FedTransphasic.oTransphasicWeapon
FoundationTech.dOnFires[__name__] = oFire
FoundationTech.dYields[__name__] = oFire
