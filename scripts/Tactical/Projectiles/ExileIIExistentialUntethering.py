#modded by grey

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 10.0 / 255.0, 175.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(105.0 / 255.0, 0.0 / 255.0, 175.0 / 255.0, 1.000000)	


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ExistentialUnteatheringCore.tga",
					kCoreColor, 
					0.45,
					6.0,	 
					"data/Textures/Tactical/ExistentialUnteatheringGlow.tga", 
					kGlowColor,
					3.0,	
					2.0,	 
					2.05,	
					"data/Textures/Tactical/ExistentialUnteatheringFlare.tga",
					kGlowColor,										
					35,		
					1.25,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.85)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.RAPIDQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(110.0)

def GetLaunchSound():
	return("ExileIIExistentialUntethering")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Existential Unteathering Device")

def GetDamage():
	return 16500000.0

def GetGuidanceLifetime():
	return 70.0

def GetMaxAngularAccel():
	return 5.0



try:
	import FoundationTech
	import ftb.Tech.CRPProjectile
	oFire = ftb.Tech.CRPProjectile.CRPProjectileDef('CRP Projectile', {
	'MaxHits':			5,
	'InDmgFac':			1,
})
	FoundationTech.dYields[__name__] = oFire
except:
	import sys
	et = sys.exc_info()
	error = str(et[0])+": "+str(et[1])
	print "ERROR at script: " + __name__ +", details -> "+error
