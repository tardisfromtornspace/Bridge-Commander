# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\Viper.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(200.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.010000, 0.000000)
Hull.SetPosition2D(78.000000, 100.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.500000)
Hull.SetRadius(0.015000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
IonDrive = App.ImpulseEngineProperty_Create("Ion Drive")

IonDrive.SetMaxCondition(600.000000)
IonDrive.SetCritical(0)
IonDrive.SetTargetable(0)
IonDrive.SetPrimary(1)
IonDrive.SetPosition(0.000000, -0.015000, -0.004100)
IonDrive.SetPosition2D(65.000000, 85.000000)
IonDrive.SetRepairComplexity(1.000000)
IonDrive.SetDisabledPercentage(0.500000)
IonDrive.SetRadius(0.007500)
IonDrive.SetNormalPowerPerSecond(100.000000)
IonDrive.SetMaxAccel(10.000000)
IonDrive.SetMaxAngularAccel(0.750000)
IonDrive.SetMaxAngularVelocity(0.750000)
IonDrive.SetMaxSpeed(12.000000)
IonDrive.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(IonDrive)
#################################################
GravimetricDrive = App.WarpEngineProperty_Create("Gravimetric Drive")

GravimetricDrive.SetMaxCondition(600.000000)
GravimetricDrive.SetCritical(0)
GravimetricDrive.SetTargetable(0)
GravimetricDrive.SetPrimary(1)
GravimetricDrive.SetPosition(0.000000, -0.030000, 0.000000)
GravimetricDrive.SetPosition2D(65.000000, 85.000000)
GravimetricDrive.SetRepairComplexity(1.000000)
GravimetricDrive.SetDisabledPercentage(0.500000)
GravimetricDrive.SetRadius(0.006500)
GravimetricDrive.SetNormalPowerPerSecond(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravimetricDrive)
#################################################
TyliumReactor = App.PowerProperty_Create("Tylium Reactor")

TyliumReactor.SetMaxCondition(600.000000)
TyliumReactor.SetCritical(1)
TyliumReactor.SetTargetable(1)
TyliumReactor.SetPrimary(1)
TyliumReactor.SetPosition(0.000000, -0.046492, 0.000000)
TyliumReactor.SetPosition2D(65.000000, 85.000000)
TyliumReactor.SetRepairComplexity(1.000000)
TyliumReactor.SetDisabledPercentage(0.500000)
TyliumReactor.SetRadius(0.005000)
TyliumReactor.SetMainBatteryLimit(70000.000000)
TyliumReactor.SetBackupBatteryLimit(10000.000000)
TyliumReactor.SetMainConduitCapacity(400.000000)
TyliumReactor.SetBackupConduitCapacity(200.000000)
TyliumReactor.SetPowerOutput(1300.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(TyliumReactor)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(2000.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(65.000000, 85.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.002500)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(10.000000)
RepairSystem.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(600.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000167, 0.038899, -0.006707)
SensorArray.SetPosition2D(65.000000, 45.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.006000)
SensorArray.SetNormalPowerPerSecond(100.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
MegatronShield = App.ShieldProperty_Create("Megatron Shield")

MegatronShield.SetMaxCondition(600.000000)
MegatronShield.SetCritical(0)
MegatronShield.SetTargetable(1)
MegatronShield.SetPrimary(1)
MegatronShield.SetPosition(0.000000, 0.000000, 0.000000)
MegatronShield.SetPosition2D(65.000000, 85.000000)
MegatronShield.SetRepairComplexity(1.000000)
MegatronShield.SetDisabledPercentage(0.500000)
MegatronShield.SetRadius(0.007500)
MegatronShield.SetNormalPowerPerSecond(100.000000)
MegatronShieldShieldGlowColor = App.TGColorA()
MegatronShieldShieldGlowColor.SetRGBA(0.749020, 0.749020, 0.749020, 0.000000)
MegatronShield.SetShieldGlowColor(MegatronShieldShieldGlowColor)
MegatronShield.SetShieldGlowDecay(1.000000)
MegatronShield.SetMaxShields(MegatronShield.FRONT_SHIELDS, 200.000000)
MegatronShield.SetMaxShields(MegatronShield.REAR_SHIELDS, 200.000000)
MegatronShield.SetMaxShields(MegatronShield.TOP_SHIELDS, 200.000000)
MegatronShield.SetMaxShields(MegatronShield.BOTTOM_SHIELDS, 200.000000)
MegatronShield.SetMaxShields(MegatronShield.LEFT_SHIELDS, 200.000000)
MegatronShield.SetMaxShields(MegatronShield.RIGHT_SHIELDS, 200.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.FRONT_SHIELDS, 10.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.REAR_SHIELDS, 10.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.TOP_SHIELDS, 10.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.BOTTOM_SHIELDS, 10.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.LEFT_SHIELDS, 10.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.RIGHT_SHIELDS, 10.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(MegatronShield)
#################################################
MissileSys = App.TorpedoSystemProperty_Create("Missile Sys")

MissileSys.SetMaxCondition(600.000000)
MissileSys.SetCritical(0)
MissileSys.SetTargetable(0)
MissileSys.SetPrimary(1)
MissileSys.SetPosition(0.000000, 0.000000, 0.000000)
MissileSys.SetPosition2D(65.000000, 85.000000)
MissileSys.SetRepairComplexity(1.000000)
MissileSys.SetDisabledPercentage(0.500000)
MissileSys.SetRadius(0.005000)
MissileSys.SetNormalPowerPerSecond(1.000000)
MissileSys.SetWeaponSystemType(MissileSys.WST_TORPEDO)
MissileSys.SetSingleFire(1)
MissileSys.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MissileSys.SetFiringChainString(kFiringChainString)
MissileSys.SetFiringChainString(kFiringChainString)
MissileSys.SetMaxTorpedoes(0, 4)
MissileSys.SetTorpedoScript(0, "Tactical.Projectiles.Solonite Missile")
MissileSys.SetMaxTorpedoes(1, 2)
MissileSys.SetTorpedoScript(1, "Tactical.Projectiles.Solonite Bomb")
MissileSys.SetNumAmmoTypes(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissileSys)
#################################################
LaserTorpSys = App.WeaponSystemProperty_Create("LaserTorp Sys")

LaserTorpSys.SetMaxCondition(200.000000)
LaserTorpSys.SetCritical(0)
LaserTorpSys.SetTargetable(0)
LaserTorpSys.SetPrimary(1)
LaserTorpSys.SetPosition(0.000000, 0.000000, 0.000000)
LaserTorpSys.SetPosition2D(65.000000, 85.000000)
LaserTorpSys.SetRepairComplexity(1.000000)
LaserTorpSys.SetDisabledPercentage(0.500000)
LaserTorpSys.SetRadius(0.005000)
LaserTorpSys.SetNormalPowerPerSecond(100.000000)
LaserTorpSys.SetWeaponSystemType(LaserTorpSys.WST_PULSE)
LaserTorpSys.SetSingleFire(0)
LaserTorpSys.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
LaserTorpSys.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(LaserTorpSys)
#################################################
PortLTCannon = App.PulseWeaponProperty_Create("Port LT Cannon")

PortLTCannon.SetMaxCondition(400.000000)
PortLTCannon.SetCritical(0)
PortLTCannon.SetTargetable(1)
PortLTCannon.SetPrimary(0)
PortLTCannon.SetPosition(-0.008731, 0.012182, -0.003038)
PortLTCannon.SetPosition2D(70.000000, 65.000000)
PortLTCannon.SetRepairComplexity(1.000000)
PortLTCannon.SetDisabledPercentage(0.500000)
PortLTCannon.SetRadius(0.002500)
PortLTCannon.SetDumbfire(1)
PortLTCannon.SetWeaponID(1)
PortLTCannon.SetGroups(1)
PortLTCannon.SetDamageRadiusFactor(0.300000)
PortLTCannon.SetIconNum(365)
PortLTCannon.SetIconPositionX(70.000000)
PortLTCannon.SetIconPositionY(65.000000)
PortLTCannon.SetIconAboveShip(1)
PortLTCannon.SetFireSound("(null)")
PortLTCannon.SetMaxCharge(50.000000)
PortLTCannon.SetMaxDamage(250.000000)
PortLTCannon.SetMaxDamageDistance(10.000000)
PortLTCannon.SetMinFiringCharge(3.000000)
PortLTCannon.SetNormalDischargeRate(1.000000)
PortLTCannon.SetRechargeRate(0.900000)
PortLTCannon.SetIndicatorIconNum(510)
PortLTCannon.SetIndicatorIconPositionX(50.000000)
PortLTCannon.SetIndicatorIconPositionY(25.000000)
PortLTCannonForward = App.TGPoint3()
PortLTCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortLTCannonUp = App.TGPoint3()
PortLTCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortLTCannon.SetOrientation(PortLTCannonForward, PortLTCannonUp)
PortLTCannon.SetArcWidthAngles(-0.043633, 0.174533)
PortLTCannon.SetArcHeightAngles(-0.174533, 0.174533)
PortLTCannon.SetCooldownTime(0.300000)
PortLTCannon.SetModuleName("Tactical.Projectiles.LaserTorp")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortLTCannon)
#################################################
StarLTCannon = App.PulseWeaponProperty_Create("Star LT Cannon")

StarLTCannon.SetMaxCondition(400.000000)
StarLTCannon.SetCritical(0)
StarLTCannon.SetTargetable(1)
StarLTCannon.SetPrimary(0)
StarLTCannon.SetPosition(0.009434, 0.011970, -0.002948)
StarLTCannon.SetPosition2D(85.000000, 65.000000)
StarLTCannon.SetRepairComplexity(1.000000)
StarLTCannon.SetDisabledPercentage(0.500000)
StarLTCannon.SetRadius(0.002500)
StarLTCannon.SetDumbfire(1)
StarLTCannon.SetWeaponID(1)
StarLTCannon.SetGroups(1)
StarLTCannon.SetDamageRadiusFactor(0.300000)
StarLTCannon.SetIconNum(365)
StarLTCannon.SetIconPositionX(85.000000)
StarLTCannon.SetIconPositionY(65.000000)
StarLTCannon.SetIconAboveShip(1)
StarLTCannon.SetFireSound("(null)")
StarLTCannon.SetMaxCharge(50.000000)
StarLTCannon.SetMaxDamage(250.000000)
StarLTCannon.SetMaxDamageDistance(10.000000)
StarLTCannon.SetMinFiringCharge(3.000000)
StarLTCannon.SetNormalDischargeRate(1.000000)
StarLTCannon.SetRechargeRate(1.500000)
StarLTCannon.SetIndicatorIconNum(510)
StarLTCannon.SetIndicatorIconPositionX(65.000000)
StarLTCannon.SetIndicatorIconPositionY(25.000000)
StarLTCannonForward = App.TGPoint3()
StarLTCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarLTCannonUp = App.TGPoint3()
StarLTCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarLTCannon.SetOrientation(StarLTCannonForward, StarLTCannonUp)
StarLTCannon.SetArcWidthAngles(-0.174533, 0.043633)
StarLTCannon.SetArcHeightAngles(-0.174533, 0.174533)
StarLTCannon.SetCooldownTime(0.300000)
StarLTCannon.SetModuleName("Tactical.Projectiles.LaserTorp")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarLTCannon)
#################################################
Engine1 = App.EngineProperty_Create("Engine 1")

Engine1.SetMaxCondition(400.000000)
Engine1.SetCritical(0)
Engine1.SetTargetable(1)
Engine1.SetPrimary(0)
Engine1.SetPosition(0.000806, -0.042728, 0.010758)
Engine1.SetPosition2D(65.000000, 90.000000)
Engine1.SetRepairComplexity(1.000000)
Engine1.SetDisabledPercentage(0.500000)
Engine1.SetRadius(0.008500)
Engine1.SetEngineType(Engine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine1)
#################################################
Viper = App.ShipProperty_Create("Viper")

Viper.SetGenus(1)
Viper.SetSpecies(107)
Viper.SetMass(10.000000)
Viper.SetRotationalInertia(2.000000)
Viper.SetShipName("Viper")
Viper.SetModelFilename("data/Models/Ships/Viper/viper.nif")
Viper.SetDamageResolution(15.000000)
Viper.SetAffiliation(0)
Viper.SetStationary(0)
Viper.SetAIString("NonFedAttack")
Viper.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Viper)
#################################################
Engine2 = App.EngineProperty_Create("Engine 2")

Engine2.SetMaxCondition(400.000000)
Engine2.SetCritical(0)
Engine2.SetTargetable(1)
Engine2.SetPrimary(0)
Engine2.SetPosition(-0.012315, -0.042728, -0.003524)
Engine2.SetPosition2D(47.000000, 100.000000)
Engine2.SetRepairComplexity(1.000000)
Engine2.SetDisabledPercentage(0.500000)
Engine2.SetRadius(0.008500)
Engine2.SetEngineType(Engine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine2)
#################################################
Engine3 = App.EngineProperty_Create("Engine 3")

Engine3.SetMaxCondition(400.000000)
Engine3.SetCritical(0)
Engine3.SetTargetable(1)
Engine3.SetPrimary(0)
Engine3.SetPosition(0.012692, -0.042728, -0.003335)
Engine3.SetPosition2D(83.000000, 100.000000)
Engine3.SetRepairComplexity(1.000000)
Engine3.SetDisabledPercentage(0.500000)
Engine3.SetRadius(0.008500)
Engine3.SetEngineType(Engine3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine3)
#################################################
GravimetricInitiator = App.EngineProperty_Create("Gravimetric Initiator")

GravimetricInitiator.SetMaxCondition(400.000000)
GravimetricInitiator.SetCritical(0)
GravimetricInitiator.SetTargetable(1)
GravimetricInitiator.SetPrimary(0)
GravimetricInitiator.SetPosition(0.000000, -0.050000, -0.005500)
GravimetricInitiator.SetPosition2D(80.000000, 100.000000)
GravimetricInitiator.SetRepairComplexity(1.000000)
GravimetricInitiator.SetDisabledPercentage(0.500000)
GravimetricInitiator.SetRadius(0.006500)
GravimetricInitiator.SetEngineType(GravimetricInitiator.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravimetricInitiator)
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
ViewscreenForwardPosition.SetXYZ(0.000000, -0.002398, 0.010296)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(-0.000156, -0.066494, -0.003082)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
ViewscreenLeft = App.PositionOrientationProperty_Create("ViewscreenLeft")

ViewscreenLeftForward = App.TGPoint3()
ViewscreenLeftForward.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeftUp = App.TGPoint3()
ViewscreenLeftUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenLeftRight = App.TGPoint3()
ViewscreenLeftRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenLeft.SetOrientation(ViewscreenLeftForward, ViewscreenLeftUp, ViewscreenLeftRight)
ViewscreenLeftPosition = App.TGPoint3()
ViewscreenLeftPosition.SetXYZ(-0.003423, -0.007662, 0.008607)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.003264, -0.008971, 0.008930)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(-0.000528, -0.008657, 0.012409)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000615, -0.009310, -0.009469)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
Launcher = App.TorpedoTubeProperty_Create("Launcher")

Launcher.SetMaxCondition(400.000000)
Launcher.SetCritical(0)
Launcher.SetTargetable(1)
Launcher.SetPrimary(0)
Launcher.SetPosition(0.000000, -0.039671, -0.009619)
Launcher.SetPosition2D(65.000000, 60.000000)
Launcher.SetRepairComplexity(1.000000)
Launcher.SetDisabledPercentage(0.500000)
Launcher.SetRadius(0.002500)
Launcher.SetDumbfire(1)
Launcher.SetWeaponID(2)
Launcher.SetGroups(1)
Launcher.SetDamageRadiusFactor(0.600000)
Launcher.SetIconNum(370)
Launcher.SetIconPositionX(78.000000)
Launcher.SetIconPositionY(45.000000)
Launcher.SetIconAboveShip(1)
Launcher.SetImmediateDelay(0.150000)
Launcher.SetReloadDelay(2.500000)
Launcher.SetMaxReady(1)
LauncherDirection = App.TGPoint3()
LauncherDirection.SetXYZ(0.000000, 0.997489, -0.070825)
Launcher.SetDirection(LauncherDirection)
LauncherRight = App.TGPoint3()
LauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
Launcher.SetRight(LauncherRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(Launcher)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ion Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravimetric Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tylium Reactor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Megatron Shield", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("LaserTorp Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port LT Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star LT Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Viper", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravimetric Initiator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenLeft", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenRight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenUp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenDown", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
