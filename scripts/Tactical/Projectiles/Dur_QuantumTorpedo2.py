###############################################################################
#	Filename:	QuantumTorpedo.py
#	
#	Modified:	8/18/02 -	Durandal
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Quantum Torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(25.0 / 255.0, 25.0 / 255.0, 50.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(50.0 / 255.0, 50.0 / 255.0, 100.0 / 255.0, 1.0)

    pTorp.CreateTorpedoModel(
                                "data/Textures/Tactical/TorpedoCore.tga",
                                kCoreColor,
                                0.15,
                                1.2,
                                "data/Textures/Tactical/TorpedoGlow.tga",
                                kGlowColor,
                                2.0,
                                0.5,
                                0.6,
                                "data/Textures/Tactical/TorpedoFlares.tga",
                                kFlareColor,
                                40,
                                0.12,
                                0.27)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.33)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime( GetLifetime() )

    # Multiplayer specific stuff.  Please, if you create a new torp
    # type. modify the SpeciesToTorp.py file to add the new type.
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    
    return (0)


def GetLaunchSpeed():
    return (24.0)

def GetLaunchSound():
    return ("Dur_Quantum")

def GetPowerCost():
    return (30.0)

def GetName():
    return ("Quantum")

def GetDamage():
    return 1100.0

def GetGuidanceLifetime():
    return 15.0

def GetMaxAngularAccel():
    return 0.17

def GetLifetime():
	return 12.0
