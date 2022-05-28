import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 128.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(125.0 / 255.0, 190.0 / 255.0, 183.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.6,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,										
					12,		
					0.5,		
					0.4)	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.5)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)
	return(0)

def GetLaunchSpeed():
	return(15.0)

def GetLaunchSound():
	return("blackelmbreentorpedo2")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Breen EM Disruptor")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 1.2

#########################
#SpreadType		#
#########################

SpreadType=0

#Spread Options	- all parameters are optional and if not defined take default values	#
#########################################################################################

##for SpreadType 1 & 2
SpreadNumber=0
SpreadPath=""
SpreadDelay=0.0

##for SpreadType 1 
SplitType=0

##for SpreadType 1 with SplitType 1
SpreadDensity=0

##for SpreadType 1 with SplitType 2
SpreadAngle=0

##for SpreadType 3
SpreadRadious=0
SpreadSplash=0


#########################
#ImpactType		#
#########################

ImpactType=0

#Impact Options	#
#################
BounceYield=0
BounceFail=0


#########################
#YieldType		#
#########################

YieldType=1


#Yield Options	- all parameters are optional and if not defined take default values	#
#########################################################################################
DrainerWeapon=1

SensorBlast=0
SensorDisabledTime=120

ShieldDisruptor=0
ShieldDisabledTime=120

EngineJammer=0
EngineDisabledTime=120

IonCannon=0
IonCannonDisabledTime=0
IonCannonMiss=0
IonFrequency=0

# Thirth Party Options #
########################

PhalantiumWave=0

SpatialCharges=0


#########################
#DepleteType		#
#########################

DepleteType = 0
GraphicsTuple=""

#Deplete Options - all parameters are optional and if not defined take default values	#
#########################################################################################
DepletedAtPercentage = 0
DepletionPerSecond = 0
DepleteColour=0
DepleteShrink=0

