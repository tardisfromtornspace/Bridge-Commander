#modded by grey

import App
import FoundationTech

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/DimenopointUnphaseDeviceCore.tga",
					kCoreColor, 
					0.45,
					6.0,	 
					"data/Textures/Tactical/AlteredVoidspaceDevice.tga", 
					kCoreColor,
					3.0,	
					1.75,	 
					1.80,	
					"data/Textures/Tactical/DimenopointUnphaseDeviceFlare.tga",
					kCoreColor,										
					55,		
					0.85,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.35)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.RAPIDQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(90.0)

def GetLaunchSound():
	return("AlteredVoidspaceDevice")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Altered Voidspace Device")

def GetDamage():
	return 10500000.0

def GetGuidanceLifetime():
	return 50.0

def GetMaxAngularAccel():
	return 30.0

try:
	import FoundationTech
	import ftb.Tech.CRPProjectile
	oFire = ftb.Tech.CRPProjectile.CRPProjectileDef('CRP Projectile', {
	'MaxHits':			3,
	'InDmgFac':			1.25,
})
	FoundationTech.dYields[__name__] = oFire
except:
	import sys
	et = sys.exc_info()
	error = str(et[0])+": "+str(et[1])
	print "ERROR at script: " + __name__ +", details -> "+error
