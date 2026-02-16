import App


def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0 , 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0/ 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/OmnimorphicTemporalCatalystCore.tga",
					kCoreColor, 
					0.24,
					1.12,	 
					"data/Textures/Tactical/OmnimorphicTemporalCatalystGlow.tga", 
					kGlowColor,
					0.2,	
					3.6,	
					3.8,	
					"data/Textures/Tactical/OmnimorphicTemporalCatalystCore.tga",
					kGlowColor,										
					400,		
					0.55,		
					4.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.30)
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
	return("OmnimorphicTemporalCatalyst")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Omnimorphic Temporal Catalyst")

def GetDamage():
	return 5000.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 2.85

try:
	modChronitonTorpe = __import__("Custom.Techs.ChronitonTorpe")
	if(modChronitonTorpe):
		modChronitonTorpe.oChronitonTorpe.AddTorpedo(__name__)
except:
	print "Chroniton Torpedo script not installed, or you are missing Foundation Tech"
