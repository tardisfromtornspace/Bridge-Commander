# C:\Program Files\Activision\QBR 2.2\Bridge Commander\scripts\ships\Hardpoints\mk10raider.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Mk10Raider = App.ShipProperty_Create("Mk10Raider")

Mk10Raider.SetGenus(1)
Mk10Raider.SetSpecies(107)
Mk10Raider.SetMass(12.000000)
Mk10Raider.SetRotationalInertia(8.000000)
Mk10Raider.SetShipName("Mk10Raider")
Mk10Raider.SetModelFilename("data/models/ships/Mk10Raider/Mk10Raider.nif")
Mk10Raider.SetDamageResolution(5.000000)
Mk10Raider.SetAffiliation(0)
Mk10Raider.SetStationary(0)
Mk10Raider.SetAIString("NonFedAttack")
Mk10Raider.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Mk10Raider)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(700.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.010000)
Hull.SetPosition2D(65.000000, 90.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.500000)
Hull.SetRadius(0.043000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
TyliumEnigizer = App.PowerProperty_Create("Tylium Enigizer")

TyliumEnigizer.SetMaxCondition(700.000000)
TyliumEnigizer.SetCritical(1)
TyliumEnigizer.SetTargetable(1)
TyliumEnigizer.SetPrimary(1)
TyliumEnigizer.SetPosition(0.000000, -0.052201, 0.010000)
TyliumEnigizer.SetPosition2D(65.000000, 70.000000)
TyliumEnigizer.SetRepairComplexity(1.000000)
TyliumEnigizer.SetDisabledPercentage(0.500000)
TyliumEnigizer.SetRadius(0.015000)
TyliumEnigizer.SetMainBatteryLimit(7000.000000)
TyliumEnigizer.SetBackupBatteryLimit(1000.000000)
TyliumEnigizer.SetMainConduitCapacity(42.000000)
TyliumEnigizer.SetBackupConduitCapacity(21.000000)
TyliumEnigizer.SetPowerOutput(55.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(TyliumEnigizer)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(7000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.106435, -0.001497)
SensorArray.SetPosition2D(65.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.005000)
SensorArray.SetNormalPowerPerSecond(5.000000)
SensorArray.SetBaseSensorRange(10000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
MegatronSheilds = App.ShieldProperty_Create("Megatron Sheilds")

MegatronSheilds.SetMaxCondition(700.000000)
MegatronSheilds.SetCritical(0)
MegatronSheilds.SetTargetable(1)
MegatronSheilds.SetPrimary(1)
MegatronSheilds.SetPosition(-0.000650, 0.038663, 0.033000)
MegatronSheilds.SetPosition2D(65.000000, 70.000000)
MegatronSheilds.SetRepairComplexity(1.000000)
MegatronSheilds.SetDisabledPercentage(0.500000)
MegatronSheilds.SetRadius(0.005000)
MegatronSheilds.SetNormalPowerPerSecond(10.000000)
MegatronSheildsShieldGlowColor = App.TGColorA()
MegatronSheildsShieldGlowColor.SetRGBA(0.501961, 0.501961, 0.247059, 0.000000)
MegatronSheilds.SetShieldGlowColor(MegatronSheildsShieldGlowColor)
MegatronSheilds.SetShieldGlowDecay(0.100000)
MegatronSheilds.SetMaxShields(MegatronSheilds.FRONT_SHIELDS, 404.000000)
MegatronSheilds.SetMaxShields(MegatronSheilds.REAR_SHIELDS, 404.000000)
MegatronSheilds.SetMaxShields(MegatronSheilds.TOP_SHIELDS, 404.000000)
MegatronSheilds.SetMaxShields(MegatronSheilds.BOTTOM_SHIELDS, 404.000000)
MegatronSheilds.SetMaxShields(MegatronSheilds.LEFT_SHIELDS, 404.000000)
MegatronSheilds.SetMaxShields(MegatronSheilds.RIGHT_SHIELDS, 404.000000)
MegatronSheilds.SetShieldChargePerSecond(MegatronSheilds.FRONT_SHIELDS, 4.000000)
MegatronSheilds.SetShieldChargePerSecond(MegatronSheilds.REAR_SHIELDS, 4.000000)
MegatronSheilds.SetShieldChargePerSecond(MegatronSheilds.TOP_SHIELDS, 4.000000)
MegatronSheilds.SetShieldChargePerSecond(MegatronSheilds.BOTTOM_SHIELDS, 4.000000)
MegatronSheilds.SetShieldChargePerSecond(MegatronSheilds.LEFT_SHIELDS, 4.000000)
MegatronSheilds.SetShieldChargePerSecond(MegatronSheilds.RIGHT_SHIELDS, 4.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(MegatronSheilds)
#################################################
IonDrive = App.ImpulseEngineProperty_Create("Ion Drive")

IonDrive.SetMaxCondition(700.000000)
IonDrive.SetCritical(0)
IonDrive.SetTargetable(0)
IonDrive.SetPrimary(1)
IonDrive.SetPosition(0.000000, 0.000000, 0.000000)
IonDrive.SetPosition2D(65.000000, 70.000000)
IonDrive.SetRepairComplexity(1.000000)
IonDrive.SetDisabledPercentage(0.500000)
IonDrive.SetRadius(0.002500)
IonDrive.SetNormalPowerPerSecond(9.000000)
IonDrive.SetMaxAccel(10.000000)
IonDrive.SetMaxAngularAccel(0.500000)
IonDrive.SetMaxAngularVelocity(0.500000)
IonDrive.SetMaxSpeed(4.000000)
IonDrive.SetEngineSound("Klingon Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(IonDrive)
#################################################
WarpSys = App.WarpEngineProperty_Create("Warp Sys")

WarpSys.SetMaxCondition(700.000000)
WarpSys.SetCritical(0)
WarpSys.SetTargetable(0)
WarpSys.SetPrimary(1)
WarpSys.SetPosition(0.000000, 0.000000, 0.000000)
WarpSys.SetPosition2D(0.000000, 0.000000)
WarpSys.SetRepairComplexity(1.000000)
WarpSys.SetDisabledPercentage(0.500000)
WarpSys.SetRadius(0.002500)
WarpSys.SetNormalPowerPerSecond(0.700000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpSys)
#################################################
PortIon = App.EngineProperty_Create("Port Ion")

PortIon.SetMaxCondition(700.000000)
PortIon.SetCritical(0)
PortIon.SetTargetable(1)
PortIon.SetPrimary(0)
PortIon.SetPosition(-0.036510, -0.087051, 0.000599)
PortIon.SetPosition2D(45.000000, 95.000000)
PortIon.SetRepairComplexity(1.000000)
PortIon.SetDisabledPercentage(0.500000)
PortIon.SetRadius(0.025000)
PortIon.SetEngineType(PortIon.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortIon)
#################################################
StarIon = App.EngineProperty_Create("Star Ion")

StarIon.SetMaxCondition(700.000000)
StarIon.SetCritical(0)
StarIon.SetTargetable(1)
StarIon.SetPrimary(0)
StarIon.SetPosition(0.036657, -0.087051, 0.000777)
StarIon.SetPosition2D(85.000000, 95.000000)
StarIon.SetRepairComplexity(1.000000)
StarIon.SetDisabledPercentage(0.500000)
StarIon.SetRadius(0.025000)
StarIon.SetEngineType(StarIon.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarIon)
#################################################
LaserTorpSys = App.WeaponSystemProperty_Create("LaserTorp Sys")

LaserTorpSys.SetMaxCondition(400.000000)
LaserTorpSys.SetCritical(0)
LaserTorpSys.SetTargetable(0)
LaserTorpSys.SetPrimary(1)
LaserTorpSys.SetPosition(0.000000, 0.000000, 0.000000)
LaserTorpSys.SetPosition2D(65.000000, 70.000000)
LaserTorpSys.SetRepairComplexity(1.000000)
LaserTorpSys.SetDisabledPercentage(0.500000)
LaserTorpSys.SetRadius(0.002500)
LaserTorpSys.SetNormalPowerPerSecond(7.140000)
LaserTorpSys.SetWeaponSystemType(LaserTorpSys.WST_PULSE)
LaserTorpSys.SetSingleFire(0)
LaserTorpSys.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
LaserTorpSys.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(LaserTorpSys)
#################################################
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")

PortCannon.SetMaxCondition(400.000000)
PortCannon.SetCritical(0)
PortCannon.SetTargetable(1)
PortCannon.SetPrimary(1)
PortCannon.SetPosition(-0.080139, 0.065000, 0.008677)
PortCannon.SetPosition2D(50.000000, 60.000000)
PortCannon.SetRepairComplexity(1.000000)
PortCannon.SetDisabledPercentage(0.500000)
PortCannon.SetRadius(0.025000)
PortCannon.SetDumbfire(1)
PortCannon.SetWeaponID(1)
PortCannon.SetGroups(1)
PortCannon.SetDamageRadiusFactor(0.030000)
PortCannon.SetIconNum(365)
PortCannon.SetIconPositionX(50.000000)
PortCannon.SetIconPositionY(50.000000)
PortCannon.SetIconAboveShip(1)
PortCannon.SetFireSound("(null)")
PortCannon.SetMaxCharge(500.000000)
PortCannon.SetMaxDamage(2.500000)
PortCannon.SetMaxDamageDistance(30.000000)
PortCannon.SetMinFiringCharge(1.000000)
PortCannon.SetNormalDischargeRate(1.000000)
PortCannon.SetRechargeRate(1.000000)
PortCannon.SetIndicatorIconNum(510)
PortCannon.SetIndicatorIconPositionX(35.000000)
PortCannon.SetIndicatorIconPositionY(30.000000)
PortCannonForward = App.TGPoint3()
PortCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannonUp = App.TGPoint3()
PortCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon.SetOrientation(PortCannonForward, PortCannonUp)
PortCannon.SetArcWidthAngles(-0.174533, 0.174533)
PortCannon.SetArcHeightAngles(-0.174533, 0.174533)
PortCannon.SetCooldownTime(0.300000)
PortCannon.SetModuleName("Tactical.Projectiles.Mk10RaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
#################################################
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")

StarCannon.SetMaxCondition(400.000000)
StarCannon.SetCritical(0)
StarCannon.SetTargetable(1)
StarCannon.SetPrimary(0)
StarCannon.SetPosition(0.078693, 0.065000, 0.008804)
StarCannon.SetPosition2D(80.000000, 60.000000)
StarCannon.SetRepairComplexity(1.000000)
StarCannon.SetDisabledPercentage(0.500000)
StarCannon.SetRadius(0.025000)
StarCannon.SetDumbfire(1)
StarCannon.SetWeaponID(2)
StarCannon.SetGroups(1)
StarCannon.SetDamageRadiusFactor(0.030000)
StarCannon.SetIconNum(365)
StarCannon.SetIconPositionX(100.000000)
StarCannon.SetIconPositionY(50.000000)
StarCannon.SetIconAboveShip(1)
StarCannon.SetFireSound("(null)")
StarCannon.SetMaxCharge(500.000000)
StarCannon.SetMaxDamage(2.500000)
StarCannon.SetMaxDamageDistance(30.000000)
StarCannon.SetMinFiringCharge(1.000000)
StarCannon.SetNormalDischargeRate(1.000000)
StarCannon.SetRechargeRate(1.000000)
StarCannon.SetIndicatorIconNum(510)
StarCannon.SetIndicatorIconPositionX(78.000000)
StarCannon.SetIndicatorIconPositionY(30.000000)
StarCannonForward = App.TGPoint3()
StarCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannonUp = App.TGPoint3()
StarCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon.SetOrientation(StarCannonForward, StarCannonUp)
StarCannon.SetArcWidthAngles(-0.174533, 0.174533)
StarCannon.SetArcHeightAngles(-0.174533, 0.174533)
StarCannon.SetCooldownTime(0.300000)
StarCannon.SetModuleName("Tactical.Projectiles.Mk10RaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
#################################################
MissileSys = App.TorpedoSystemProperty_Create("Missile Sys")

MissileSys.SetMaxCondition(700.000000)
MissileSys.SetCritical(0)
MissileSys.SetTargetable(0)
MissileSys.SetPrimary(1)
MissileSys.SetPosition(0.000000, 0.000000, 0.000000)
MissileSys.SetPosition2D(65.000000, 70.000000)
MissileSys.SetRepairComplexity(1.000000)
MissileSys.SetDisabledPercentage(0.500000)
MissileSys.SetRadius(0.002500)
MissileSys.SetNormalPowerPerSecond(0.700000)
MissileSys.SetWeaponSystemType(MissileSys.WST_TORPEDO)
MissileSys.SetSingleFire(0)
MissileSys.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MissileSys.SetFiringChainString(kFiringChainString)
MissileSys.SetMaxTorpedoes(0, 12)
MissileSys.SetTorpedoScript(0, "Tactical.Projectiles.Solonite Missile")
MissileSys.SetMaxTorpedoes(1, 4)
MissileSys.SetTorpedoScript(1, "Tactical.Projectiles.Solonite Bomb")
MissileSys.SetNumAmmoTypes(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissileSys)
#################################################
PortLauncher = App.TorpedoTubeProperty_Create("Port Launcher")

PortLauncher.SetMaxCondition(400.000000)
PortLauncher.SetCritical(0)
PortLauncher.SetTargetable(1)
PortLauncher.SetPrimary(0)
PortLauncher.SetPosition(-0.031025, 0.091839, -0.005137)
PortLauncher.SetPosition2D(35.000000, 35.000000)
PortLauncher.SetRepairComplexity(1.000000)
PortLauncher.SetDisabledPercentage(0.500000)
PortLauncher.SetRadius(0.005000)
PortLauncher.SetDumbfire(1)
PortLauncher.SetWeaponID(3)
PortLauncher.SetGroups(1)
PortLauncher.SetDamageRadiusFactor(0.600000)
PortLauncher.SetIconNum(370)
PortLauncher.SetIconPositionX(70.000000)
PortLauncher.SetIconPositionY(55.000000)
PortLauncher.SetIconAboveShip(1)
PortLauncher.SetImmediateDelay(0.250000)
PortLauncher.SetReloadDelay(5.000000)
PortLauncher.SetMaxReady(3)
PortLauncherDirection = App.TGPoint3()
PortLauncherDirection.SetXYZ(0.000000, 1.000000, 0.000000)
PortLauncher.SetDirection(PortLauncherDirection)
PortLauncherRight = App.TGPoint3()
PortLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
PortLauncher.SetRight(PortLauncherRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortLauncher)
#################################################
StarLauncher = App.TorpedoTubeProperty_Create("Star Launcher")

StarLauncher.SetMaxCondition(400.000000)
StarLauncher.SetCritical(0)
StarLauncher.SetTargetable(1)
StarLauncher.SetPrimary(0)
StarLauncher.SetPosition(0.032864, 0.091877, -0.005247)
StarLauncher.SetPosition2D(95.000000, 35.000000)
StarLauncher.SetRepairComplexity(1.000000)
StarLauncher.SetDisabledPercentage(0.500000)
StarLauncher.SetRadius(0.005000)
StarLauncher.SetDumbfire(1)
StarLauncher.SetWeaponID(4)
StarLauncher.SetGroups(1)
StarLauncher.SetDamageRadiusFactor(0.600000)
StarLauncher.SetIconNum(370)
StarLauncher.SetIconPositionX(80.000000)
StarLauncher.SetIconPositionY(55.000000)
StarLauncher.SetIconAboveShip(1)
StarLauncher.SetImmediateDelay(0.250000)
StarLauncher.SetReloadDelay(5.000000)
StarLauncher.SetMaxReady(3)
StarLauncherDirection = App.TGPoint3()
StarLauncherDirection.SetXYZ(0.000000, 1.000000, 0.000000)
StarLauncher.SetDirection(StarLauncherDirection)
StarLauncherRight = App.TGPoint3()
StarLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
StarLauncher.SetRight(StarLauncherRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarLauncher)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.114039, 0.000000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.099372, 0.001005)
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
ViewscreenLeftPosition.SetXYZ(-0.126518, 0.009109, -0.013058)
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
ViewscreenRightPosition.SetXYZ(0.125398, 0.010335, -0.013482)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.048264, 0.033841)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -0.008076)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
RepairSys = App.RepairSubsystemProperty_Create("Repair Sys")

RepairSys.SetMaxCondition(4000.000000)
RepairSys.SetCritical(0)
RepairSys.SetTargetable(0)
RepairSys.SetPrimary(1)
RepairSys.SetPosition(0.000000, 0.000000, 0.000000)
RepairSys.SetPosition2D(65.000000, 70.000000)
RepairSys.SetRepairComplexity(1.000000)
RepairSys.SetDisabledPercentage(0.500000)
RepairSys.SetRadius(0.002500)
RepairSys.SetNormalPowerPerSecond(0.700000)
RepairSys.SetMaxRepairPoints(3.000000)
RepairSys.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSys)
#################################################
SensorJammer = App.HullProperty_Create("Sensor Jammer")

SensorJammer.SetMaxCondition(600.000000)
SensorJammer.SetCritical(0)
SensorJammer.SetTargetable(1)
SensorJammer.SetPrimary(0)
SensorJammer.SetPosition(0.000000, 0.000000, 0.020000)
SensorJammer.SetPosition2D(0.000000, 0.000000)
SensorJammer.SetRepairComplexity(1.000000)
SensorJammer.SetDisabledPercentage(0.500000)
SensorJammer.SetRadius(0.002500)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorJammer)
#################################################
FirstPersonCamera = App.PositionOrientationProperty_Create("FirstPersonCamera")

FirstPersonCameraForward = App.TGPoint3()
FirstPersonCameraForward.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonCameraUp = App.TGPoint3()
FirstPersonCameraUp.SetXYZ(0.000000, 0.000000, 1.000000)
FirstPersonCameraRight = App.TGPoint3()
FirstPersonCameraRight.SetXYZ(1.000000, 0.000000, 0.000000)
FirstPersonCamera.SetOrientation(FirstPersonCameraForward, FirstPersonCameraUp, FirstPersonCameraRight)
FirstPersonCameraPosition = App.TGPoint3()
FirstPersonCameraPosition.SetXYZ(0.000000, -0.099372, 0.050000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tylium Enigizer", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Megatron Sheilds", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ion Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Ion", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Ion", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("LaserTorp Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("FirstPersonCamera", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Jammer", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Mk10Raider", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
