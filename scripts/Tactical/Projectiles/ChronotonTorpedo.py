###############################################################################
#	Filename:	CronotonTorpedo.py
#	Date:		10-22-2004
#	Descr:		Chronoton shield-penetrating torpedoes
#	By:		ed
#	
#	Requires: Future Technology Addition's script torpedo support
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App

###############################################################################
#	
#	
#	
#	
#	
#	
#	
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(116.0 / 255.0, 22.0 / 255.0, 55.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(231.0 / 255.0, 16.0 / 255.0, 86.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(116.0 / 255.0, 22.0 / 255.0, 55.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PhqCore.tga",
					kCoreColor,
					0.1,
					1.2,	 
					"data/Textures/Tactical/PhqGlow.tga", 
					kGlowColor,
					2.0,	
					0.34,	 
					0.4,	
					"data/Textures/Tactical/PhqFlares.tga",
					kFlareColor,										
					130,		
					0.08,		
					0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(28)

def GetLaunchSound():
	return("ftsChronoton")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Chronoton")

def GetDamage():
	return 0.000001

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.17

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 350

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.1

def TargetHit(pObject, pEvent):
	pTarget=App.ShipClass_Cast(pEvent.GetDestination())
	Percentage=GetPercentage()
	MinYield=GetMinDamage()
	pHull = pTarget.GetHull()
	if (pHull==None):
		return
	Yield=pHull.GetMaxCondition()*Percentage
	if (Yield<MinYield):
		Yield=MinYield
	if (pHull.GetCondition()>Yield):
		pHull.SetCondition(pHull.GetCondition()-Yield)
		return
	pTarget.DestroySystem(pHull)
	return

def WeaponFired(pObject, pEvent):
	return