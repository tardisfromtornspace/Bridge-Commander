
import App
import string
pWeaponLock = {}

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 4.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(85.0 / 255.0, 150.0 / 255.0, 255.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 3.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.3,   #size
					8.0,   #rotation speed, positive is counterclockwise -negative clockwise 
					"data/Textures/Tactical/Quantum03Glow.tga", 
					kGlowColor,
					2.5,	#glow pulsate speed
					0.4,	#glow max radius
					0.3,	#glow min radius
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					150,		#number of flares
					0.125,	#flare size	
					0.03)   #flare speed

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.8)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(220)

def GetLaunchSound():
	return("TransquanticPulse")

def GetPowerCost():
	return(5.0)

def GetName():
	return("TransquanticPulse")

def GetDamage():
	return 2250.0 * 4

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.60

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"