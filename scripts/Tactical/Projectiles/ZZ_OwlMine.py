import App

def Create(pTorp):

    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 1.0, 255.0 / 1.0, 255.0 / 1.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 1.0, 255.0 / 1.0, 255.0 / 1.0, 1.000000)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 1.0, 255.0 / 1.0, 255.0 / 1.0, 1.000000)

    pTorp.CreateTorpedoModel("data/Textures/Tactical/ZZBlackCore.tga", kCoreColor, 0.15, 6.0,
                             "data/Textures/Tactical/ZZBlackGlow.tga", kGlowColor, 6.0, 0.15, 0.2,
				"data/Textures/Tactical/ZZBlackCore.tga", kFlareColor, 20.0, 0.1, 0.5)


    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return (0)


def GetLaunchSpeed():
    return 15.0


def GetLaunchSound():
    return 'ZZ_OwlMine'


def GetPowerCost():
    return 5.0


def GetName():
    return 'Plasma Mine'


def GetDamage():
    return 1500.0


def GetGuidanceLifetime():
    return 360.0


def GetMaxAngularAccel():
    return 0.7

def GetLifetime():
    return 360.0

import traceback
try:
    import FoundationTech
    import ftb.Tech.SolidProjectiles
    # The line below is a hypothethical example if you want customized AI - uncomment and adjust accordingly if you want
    #import path.to.tailoredAI.tailoredAIfilename
    #myAIfunction = tailoredAIfilename.CreateAI

    from AI.Compound.ZZMineAI import CreateAI

    import MissionLib
    def CreateAITimed(pShip, pEnemies=MissionLib.GetEnemyGroup(), initTime=3, fRangeValue=40):
        return CreateAI(pShip, pEnemies, initTime, fRangeValue)

    myAIfunction = CreateAITimed
    # Remember, if you don't want AI, do not add the "sAI" field.
    random = App.g_kSystemWrapper.GetRandomNumber(100)
    oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "ZZRMine", "sScale" : 1.0, "sShield": 1, "sCollide": 3, "sX": 0, "sY": 0.5, "sZ": 0, "sShipRmOrDeath": 0, "sHideProj": 0, "sTargetable": 1, "LeftoverDetonation": 0.001, "sAI": {"AI": CreateAITimed, "Side": "Friendly", "Team": "Friendly"}})
    #oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "bug", "sScale" : 0.2, "sShield": 1, "sCollide": 2, "sHideProj": 0, "sTargetable": 1}) 
    FoundationTech.dOnFires[__name__] = oFire
    FoundationTech.dYields[__name__] = oFire
except:
    print "Error with firing solid projectile fix"
    traceback.print_exc()