# uncompyle6 version 3.7.4
# Python bytecode 1.5 (20121)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: .\Scripts\Tactical\Projectiles\PhotonTorpedosb.py
# Compiled at: 2002-05-16 23:58:28
import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.6, 1.2, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 3.0, 0.3, 0.6, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, 128, 0.8, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.35)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)

    return 0

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("MulticorePhoton")

def GetPowerCost():
	return(5.0)

def GetName():
	return("Seeking Multicore Photon")

def GetDamage():
	return 1150.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 10.0
