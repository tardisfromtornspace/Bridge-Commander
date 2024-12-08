import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(181.0 / 255.0, 230.0 / 255.0, 253.0 / 255.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(65.0 / 255.0, 82.0 / 255.0, 255.0 / 255.0, 1.000000)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(236.0 / 255.0, 255.0 / 255.0, 17.0 / 255.0, 1.000000)

    pTorp.CreateTorpedoModel(
                                "data/Textures/Tactical/TorpedoCore.tga",
                                kCoreColor,
                                0.4,
                                0.4,
                                "data/Textures/Tactical/FTBpoltorp02.tga", 
                                kGlowColor,
                                1.0,
                                1.8,
                                2.2,
                                "data/Textures/Tactical/Dur_TorpedoFlares.tga",
                                kFlareColor,
                                35,
                                0.25,
                                2.0)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.750)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    
    # Multiplayer specific stuff.  Please, if you create a new torp
    # type. modify the SpeciesToTorp.py file to add the new type.
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    

    return(0)

def GetLaunchSpeed():
	return(45)

def GetLaunchSound():
	return("WaythaeonBioQuadracobalt")

def GetPowerCost():
	return(250.0)

def GetName():
	return("W Bio Quadracobalt")

def GetDamage():
	return 25000.0

def GetGuidanceLifetime():
	return 10.50

def GetMaxAngularAccel():
	return 0.15
