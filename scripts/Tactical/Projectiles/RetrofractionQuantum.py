
import App
import string
pWeaponLock = {}

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(50.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 4.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(200.0 / 255.0, 175.0 / 255.0, 255.0 / 255.0, 8.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(115.0 / 255.0, 235.0 / 255.0, 255.0 / 255.0, 3.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.6,   #size
					8.0,   #rotation speed, positive is counterclockwise -negative clockwise 
					"data/Textures/Tactical/Quantum03Glow.tga", 
					kGlowColor,
					1.0,	#glow pulsate speed
					1.2,	#glow max radius
					0.9,	#glow min radius
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					100,		#number of flares
					0.25,	#flare size	
					0.02)   #flare speed

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(1.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("RetrofractionQuantum")

def GetPowerCost():
	return(35.0)

def GetName():
	return("Retrofraction Quantum")

def GetDamage():
	return 7600.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 2.70

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"