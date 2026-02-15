import App
import MissionLib


def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/HeavyDTRomPlasmaCore.tga",
						kCoreColor,
						0.250,
						1.0,
					"data/Textures/Tactical/HeavyDTRomPlasmaGlow.tga",	
						kGlowColor,
						3.5,
						2.0,
						1.75,
					"data/Textures/Tactical/HeavyDTRomPlasmaCore.tga",
						kGlowColor,
						500,
						0.45,
						0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(30)

def GetLaunchSound():
	return("HeavyDTRomPlasma")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Metaplasma Exp. T-H")

def GetDamage():
	return 5900

# this sets the distance in kilometers at which the torpedo will have the yield set in GetDamage()
def GetDamageDistance():
	return 15

# this sets the maximum damage the torpedo will ever do
def GetMaxDamage():
	return 11500

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.2

def GetLifetime():
	return 30

def TargetHit(pObject, pEvent):
	return

# all the following is the code that actually does the variable damage
# this routine is called by fta when this torpedo is fired
def WeaponFired(pObject, pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pTube=App.TorpedoTube_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pTube==None):
		return
	pShip=pTube.GetParentShip()
	if (pShip==None):
		return
	pTarget=pShip.GetTarget()
	if (pTarget==None):
		return
	distance=App.UtopiaModule_ConvertGameUnitsToKilometers(MissionLib.GetDistance(pShip,pTarget))+0.01
	damage=GetDamage()*(GetDamageDistance()/distance)
	if (damage>GetMaxDamage()):
		damage=GetMaxDamage()
	pTorp.SetDamage(damage)
	return
