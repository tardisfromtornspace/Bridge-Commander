#script modified by Greystar

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(40.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(135.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					4.2,		 
					"data/Textures/Tactical/CAKlingonGlow.tga", 
					kGlowColor,
					3.0,	
					0.35,	 
					0.75,	
					"data/Textures/Tactical/WC_photontorpFlares.tga",
					kFlareColor,						
					18,		
					0.1,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("TexasMIRVQuantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("MIRV Quantum")

def GetDamage():
	return 1350.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.85

import traceback
try:
    import FoundationTech
    import ftb.Tech.TimedTorpedoes
    oFire = ftb.Tech.TimedTorpedoes.MIRVMultiTargetTorpedo(
        'MIRVMultiTargetTorpedo', {
        'spreadNumber': 6,
        'spreadDensity': 5.5,
        'warheadModule': "Tactical.Projectiles.TexasMIRVQuantumSPLIT",
        'shellLive': 0,
    })
    FoundationTech.dOnFires[__name__] = oFire
except:
    print "Something went wrong with TimedTorpedoes"
    traceback.print_exc()
