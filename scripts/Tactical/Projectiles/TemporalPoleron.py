# uncompyle6 version 3.7.4
# Python bytecode 1.5 (20121)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: .\Scripts\Tactical\Projectiles\TemporalPoleron.py
# Compiled at: 2002-08-07 22:35:14
import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(130.0 / 255.0, 3.0 / 255.0, 248.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(63.0 / 255.0, 69.0 / 255.0, 248.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/PoleronCore.tga', kCoreColor, 0.6, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 4.0, 0.75, 1.25, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 150, 1.7, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)

    return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("TemporalPoleron")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Temporal Poleron")

def GetDamage():
	return 4500 * 4

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 1.65