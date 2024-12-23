# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\TIEem3.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
IonEngine1 = App.EngineProperty_Create("Ion Engine 1")

IonEngine1.SetMaxCondition(150.000000)
IonEngine1.SetCritical(0)
IonEngine1.SetTargetable(1)
IonEngine1.SetPrimary(1)
IonEngine1.SetPosition(-0.010300, -0.034500, 0.000300)
IonEngine1.SetPosition2D(54, 90)
IonEngine1.SetRepairComplexity(1.000000)
IonEngine1.SetDisabledPercentage(0.500000)
IonEngine1.SetRadius(0.001000)
IonEngine1.SetEngineType(IonEngine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(IonEngine1)
#################################################
IonEngine2 = App.EngineProperty_Create("Ion Engine 2")

IonEngine2.SetMaxCondition(150.000000)
IonEngine2.SetCritical(0)
IonEngine2.SetTargetable(1)
IonEngine2.SetPrimary(1)
IonEngine2.SetPosition(0.010300, -0.034500, 0.000300)
IonEngine2.SetPosition2D(75, 90)
IonEngine2.SetRepairComplexity(1.000000)
IonEngine2.SetDisabledPercentage(0.500000)
IonEngine2.SetRadius(0.001000)
IonEngine2.SetEngineType(IonEngine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(IonEngine2)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(20.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.023000, 0.000000)
Hull.SetPosition2D(66, 83)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.750000)
Hull.SetRadius(0.020000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SolarIonizationReactor = App.PowerProperty_Create("Solar Ionization Reactor")

SolarIonizationReactor.SetMaxCondition(150.000000)
SolarIonizationReactor.SetCritical(1)
SolarIonizationReactor.SetTargetable(1)
SolarIonizationReactor.SetPrimary(1)
SolarIonizationReactor.SetPosition(0.000000, -0.039500, 0.000000)
SolarIonizationReactor.SetPosition2D(65, 94)
SolarIonizationReactor.SetRepairComplexity(1.000000)
SolarIonizationReactor.SetDisabledPercentage(0.500000)
SolarIonizationReactor.SetRadius(0.003000)
SolarIonizationReactor.SetMainBatteryLimit(150000.000000)
SolarIonizationReactor.SetBackupBatteryLimit(100000.000000)
SolarIonizationReactor.SetMainConduitCapacity(500.000000)
SolarIonizationReactor.SetBackupConduitCapacity(120.000000)
SolarIonizationReactor.SetPowerOutput(400.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(SolarIonizationReactor)
#################################################
SlaveCircuit = App.RepairSubsystemProperty_Create("Slave Circuit")

SlaveCircuit.SetMaxCondition(150.000000)
SlaveCircuit.SetCritical(1)
SlaveCircuit.SetTargetable(0)
SlaveCircuit.SetPrimary(1)
SlaveCircuit.SetPosition(0.000000, -0.021000, 0.000000)
SlaveCircuit.SetPosition2D(0.000000, 0.000000)
SlaveCircuit.SetRepairComplexity(1.000000)
SlaveCircuit.SetDisabledPercentage(0.500000)
SlaveCircuit.SetRadius(0.003000)
SlaveCircuit.SetNormalPowerPerSecond(1.000000)
SlaveCircuit.SetMaxRepairPoints(10.000000)
SlaveCircuit.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(SlaveCircuit)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(150.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.030000, 0.000000)
ShieldGenerator.SetPosition2D(0.000000, 0.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.010000)
ShieldGenerator.SetNormalPowerPerSecond(50.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 65.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 50.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 50.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 50.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 50.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 50.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 5.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 5.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 4.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
TIEExperimentalM3 = App.ShipProperty_Create("TIE Experimental M3")

TIEExperimentalM3.SetGenus(0)
TIEExperimentalM3.SetSpecies(401)
TIEExperimentalM3.SetMass(8.150000)
TIEExperimentalM3.SetRotationalInertia(2500.000000)
TIEExperimentalM3.SetShipName("M3")
TIEExperimentalM3.SetModelFilename("data/Models/Ships/tieinterceptor/TIE-EXM3.nif")
TIEExperimentalM3.SetDamageResolution(4.000000)
TIEExperimentalM3.SetAffiliation(0)
TIEExperimentalM3.SetStationary(0)
TIEExperimentalM3.SetAIString("NonFedAttack")
TIEExperimentalM3.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(TIEExperimentalM3)
#################################################
MissileSystem = App.TorpedoSystemProperty_Create("Missile System")

MissileSystem.SetMaxCondition(150.000000)
MissileSystem.SetCritical(0)
MissileSystem.SetTargetable(1)
MissileSystem.SetPrimary(1)
MissileSystem.SetPosition(0.000000, -0.014000, 0.000000)
MissileSystem.SetPosition2D(65, 68)
MissileSystem.SetRepairComplexity(1.000000)
MissileSystem.SetDisabledPercentage(0.500000)
MissileSystem.SetRadius(0.007500)
MissileSystem.SetNormalPowerPerSecond(70.000000)
MissileSystem.SetWeaponSystemType(MissileSystem.WST_TORPEDO)
MissileSystem.SetSingleFire(1)
MissileSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single;1;Burst")
MissileSystem.SetFiringChainString(kFiringChainString)
MissileSystem.SetMaxTorpedoes(0, 16)
MissileSystem.SetTorpedoScript(0, "Tactical.Projectiles.GTcmissile")
MissileSystem.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissileSystem)
#################################################
TIEEngine = App.ImpulseEngineProperty_Create("TIE Engine")

TIEEngine.SetMaxCondition(150.000000)
TIEEngine.SetCritical(0)
TIEEngine.SetTargetable(0)
TIEEngine.SetPrimary(1)
TIEEngine.SetPosition(0.000000, -0.039500, 0.000000)
TIEEngine.SetPosition2D(0.000000, 0.000000)
TIEEngine.SetRepairComplexity(1.000000)
TIEEngine.SetDisabledPercentage(0.500000)
TIEEngine.SetRadius(0.002000)
TIEEngine.SetNormalPowerPerSecond(75.000000)
TIEEngine.SetMaxAccel(5.100000)
TIEEngine.SetMaxAngularAccel(1.200000)
TIEEngine.SetMaxAngularVelocity(1.200000)
TIEEngine.SetMaxSpeed(6.800000)
TIEEngine.SetEngineSound("TIEengine")
App.g_kModelPropertyManager.RegisterLocalTemplate(TIEEngine)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(150.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, -0.021000, -0.012000)
SensorArray.SetPosition2D(65, 71)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.003000)
SensorArray.SetNormalPowerPerSecond(30.000000)
SensorArray.SetBaseSensorRange(675.000000)
SensorArray.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000000, -0.008000, 0.000000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, 0.100000, 0.000000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
MissilePodS = App.TorpedoTubeProperty_Create("Missile Pod S")

MissilePodS.SetMaxCondition(150.000000)
MissilePodS.SetCritical(0)
MissilePodS.SetTargetable(1)
MissilePodS.SetPrimary(1)
MissilePodS.SetPosition(0.041000, -0.007500, 0.000000)
MissilePodS.SetPosition2D(0, 0)
MissilePodS.SetRepairComplexity(1.000000)
MissilePodS.SetDisabledPercentage(0.500000)
MissilePodS.SetRadius(0.001000)
MissilePodS.SetDumbfire(1)
MissilePodS.SetWeaponID(0)
MissilePodS.SetGroups(1)
MissilePodS.SetDamageRadiusFactor(0.600000)
MissilePodS.SetIconNum(365)
MissilePodS.SetIconPositionX(109)
MissilePodS.SetIconPositionY(84)
MissilePodS.SetIconAboveShip(1)
MissilePodS.SetImmediateDelay(0.075000)
MissilePodS.SetReloadDelay(0.300000)
MissilePodS.SetMaxReady(1)
MissilePodSDirection = App.TGPoint3()
MissilePodSDirection.SetXYZ(0.000000, 1.000000, 0.000000)
MissilePodS.SetDirection(MissilePodSDirection)
MissilePodSRight = App.TGPoint3()
MissilePodSRight.SetXYZ(0.000000, 0.000000, -1.000000)
MissilePodS.SetRight(MissilePodSRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissilePodS)
#################################################
MissilePodP = App.TorpedoTubeProperty_Create("Missile Pod P")

MissilePodP.SetMaxCondition(150.000000)
MissilePodP.SetCritical(0)
MissilePodP.SetTargetable(1)
MissilePodP.SetPrimary(1)
MissilePodP.SetPosition(-0.041000, -0.007500, 0.000000)
MissilePodP.SetPosition2D(0, 0)
MissilePodP.SetRepairComplexity(1.000000)
MissilePodP.SetDisabledPercentage(0.500000)
MissilePodP.SetRadius(0.001000)
MissilePodP.SetDumbfire(1)
MissilePodP.SetWeaponID(0)
MissilePodP.SetGroups(1)
MissilePodP.SetDamageRadiusFactor(0.600000)
MissilePodP.SetIconNum(365)
MissilePodP.SetIconPositionX(46)
MissilePodP.SetIconPositionY(84)
MissilePodP.SetIconAboveShip(1)
MissilePodP.SetImmediateDelay(0.075000)
MissilePodP.SetReloadDelay(0.300000)
MissilePodP.SetMaxReady(1)
MissilePodPDirection = App.TGPoint3()
MissilePodPDirection.SetXYZ(0.000000, 1.000000, 0.000000)
MissilePodP.SetDirection(MissilePodPDirection)
MissilePodPRight = App.TGPoint3()
MissilePodPRight.SetXYZ(0.000000, 0.000000, -1.000000)
MissilePodP.SetRight(MissilePodPRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissilePodP)
#################################################
Hyperdrive = App.WarpEngineProperty_Create("Hyperdrive")

Hyperdrive.SetMaxCondition(150.000000)
Hyperdrive.SetCritical(0)
Hyperdrive.SetTargetable(0)
Hyperdrive.SetPrimary(1)
Hyperdrive.SetPosition(0.000000, -0.039500, 0.000000)
Hyperdrive.SetPosition2D(0.000000, 0.000000)
Hyperdrive.SetRepairComplexity(1.000000)
Hyperdrive.SetDisabledPercentage(0.500000)
Hyperdrive.SetRadius(0.005000)
Hyperdrive.SetNormalPowerPerSecond(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Ion Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ion Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Solar Ionization Reactor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Slave Circuit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("TIE Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("TIE Experimental M3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile Pod S", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile Pod P", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperdrive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
