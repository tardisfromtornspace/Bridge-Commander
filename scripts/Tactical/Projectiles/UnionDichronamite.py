import App


def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(190.0 / 255.0, 30.0 / 255.0 , 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(210.0 / 255.0, 210.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0/ 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PoleronCore.tga",
					kCoreColor, 
					0.24,
					1.12,	 
					"data/Textures/Tactical/UnionDichronamite.tga", 
					kGlowColor,
					0.01,	
					1.3,	
					1.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					501,		
					0.48,		
					4.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.28)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(95.0)

def GetLaunchSound():
	return("UnionDichronamite")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Union Dichronamite Device")

def GetDamage():
	return 5477.1 * 4

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 2.75

try:
	modChronitonTorpe = __import__("Custom.Techs.ChronitonTorpe")
	if(modChronitonTorpe):
		modChronitonTorpe.oChronitonTorpe.AddTorpedo(__name__)
except:
	print "Chroniton Torpedo script not installed, or you are missing Foundation Tech"
