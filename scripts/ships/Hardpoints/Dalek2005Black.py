# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\EarlyHatak.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(85.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(85.000000, 57.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.250000)
ShieldGenerator.SetRadius(0.000040)
ShieldGenerator.SetNormalPowerPerSecond(9.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(1.000000, 0.900000, 0.492157, 0.366667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(18.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 14.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 14.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 14.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 14.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 14.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 14.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Policarbide Hull")

Hull.SetMaxCondition(85.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(66.000000, 38.000000)
Hull.SetRepairComplexity(15.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.50000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(85.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.000000, 0.000000)
SensorArray.SetPosition2D(45.000000, 55.000000)
SensorArray.SetRepairComplexity(2.000000)
SensorArray.SetDisabledPercentage(0.750000)
SensorArray.SetRadius(0.080040)
SensorArray.SetNormalPowerPerSecond(1.500000)
SensorArray.SetBaseSensorRange(1700000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ReactorModule = App.PowerProperty_Create("Reactor Module")

ReactorModule.SetMaxCondition(85.000000)
ReactorModule.SetCritical(1)
ReactorModule.SetTargetable(1)
ReactorModule.SetPrimary(1)
ReactorModule.SetPosition(0.000000, 0.0000000, 0.000000)
ReactorModule.SetPosition2D(65.000000, 70.000000)
ReactorModule.SetRepairComplexity(5.000000)
ReactorModule.SetDisabledPercentage(0.250000)
ReactorModule.SetRadius(0.080000)
ReactorModule.SetMainBatteryLimit(20000.000000)
ReactorModule.SetBackupBatteryLimit(100.000000)
ReactorModule.SetMainConduitCapacity(45.000000)
ReactorModule.SetBackupConduitCapacity(5.000000)
ReactorModule.SetPowerOutput(80.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ReactorModule)
#################################################
SublightEngines = App.ImpulseEngineProperty_Create("Sublight Engines")

SublightEngines.SetMaxCondition(40000.000000)
SublightEngines.SetCritical(0)
SublightEngines.SetTargetable(0)
SublightEngines.SetPrimary(1)
SublightEngines.SetPosition(0.000000, 0.000000, 0.000000)
SublightEngines.SetPosition2D(64.000000, 104.000000)
SublightEngines.SetRepairComplexity(2.000000)
SublightEngines.SetDisabledPercentage(0.500000)
SublightEngines.SetRadius(0.070000)
SublightEngines.SetNormalPowerPerSecond(0.000001)
SublightEngines.SetMaxAccel(2.400000)
SublightEngines.SetMaxAngularAccel(2.220000)
SublightEngines.SetMaxAngularVelocity(2.350000)
SublightEngines.SetMaxSpeed(2.350000)
SublightEngines.SetEngineSound("")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngines)
#################################################
PrimaryWeapons = App.WeaponSystemProperty_Create("Primary Weapons")

PrimaryWeapons.SetMaxCondition(90.000000)
PrimaryWeapons.SetCritical(0)
PrimaryWeapons.SetTargetable(1)
PrimaryWeapons.SetPrimary(1)
PrimaryWeapons.SetPosition(0.000000, 0.004000, 0.000000)
PrimaryWeapons.SetPosition2D(64.000000, 44.000000)
PrimaryWeapons.SetRepairComplexity(2.000000)
PrimaryWeapons.SetDisabledPercentage(0.250000)
PrimaryWeapons.SetRadius(0.040000)
PrimaryWeapons.SetNormalPowerPerSecond(3.500000)
PrimaryWeapons.SetWeaponSystemType(PrimaryWeapons.WST_PULSE)
PrimaryWeapons.SetSingleFire(1)
PrimaryWeapons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PrimaryWeapons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PrimaryWeapons)
#################################################
PortEngine = App.EngineProperty_Create("Port Engine")

PortEngine.SetMaxCondition(65.000000)
PortEngine.SetCritical(0)
PortEngine.SetTargetable(1)
PortEngine.SetPrimary(0)
PortEngine.SetPosition(0.002000, 0.0000000, 0.000000)
PortEngine.SetPosition2D(53.000000, 85.000000)
PortEngine.SetRepairComplexity(5.000000)
PortEngine.SetDisabledPercentage(0.250000)
PortEngine.SetRadius(0.250000)
PortEngine.SetEngineType(PortEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortEngine)
#################################################
PortEngine2 = App.EngineProperty_Create("Front Engine")

PortEngine2.SetMaxCondition(65.000000)
PortEngine2.SetCritical(0)
PortEngine2.SetTargetable(1)
PortEngine2.SetPrimary(0)
PortEngine2.SetPosition(0.000000, 0.0020000, 0.000000)
PortEngine2.SetPosition2D(53.000000, 85.000000)
PortEngine2.SetRepairComplexity(5.000000)
PortEngine2.SetDisabledPercentage(0.250000)
PortEngine2.SetRadius(0.250000)
PortEngine2.SetEngineType(PortEngine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortEngine2)
#################################################
StarEngine = App.EngineProperty_Create("Star Engine")

StarEngine.SetMaxCondition(65.000000)
StarEngine.SetCritical(0)
StarEngine.SetTargetable(1)
StarEngine.SetPrimary(1)
StarEngine.SetPosition(-0.002000, 0.0000000, 0.000000)
StarEngine.SetPosition2D(75.000000, 85.000000)
StarEngine.SetRepairComplexity(5.000000)
StarEngine.SetDisabledPercentage(0.250000)
StarEngine.SetRadius(0.250000)
StarEngine.SetEngineType(StarEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarEngine)
#################################################
Hyperdrive1 = App.HullProperty_Create("Hyperdrive 1")

Hyperdrive1.SetMaxCondition(700000.000000)
Hyperdrive1.SetCritical(0)
Hyperdrive1.SetTargetable(0)
Hyperdrive1.SetPrimary(0)
Hyperdrive1.SetPosition(0.000000, -0.001700, 0.000000)
Hyperdrive1.SetPosition2D(46, 78)
Hyperdrive1.SetRepairComplexity(1.000000)
Hyperdrive1.SetDisabledPercentage(0.000000)
Hyperdrive1.SetRadius(0.025000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive1)
#################################################
SlipstreamDrive1 = App.HullProperty_Create("Slipstream Drive 1")

SlipstreamDrive1.SetMaxCondition(700000.000000)
SlipstreamDrive1.SetCritical(0)
SlipstreamDrive1.SetTargetable(0)
SlipstreamDrive1.SetPrimary(0)
SlipstreamDrive1.SetPosition(0.000000, -0.001500, 0.000000)
SlipstreamDrive1.SetPosition2D(46, 66)
SlipstreamDrive1.SetRepairComplexity(0.900000)
SlipstreamDrive1.SetDisabledPercentage(0.500000)
SlipstreamDrive1.SetRadius(0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(SlipstreamDrive1)
#################################################
JumpspaceDriveA = App.HullProperty_Create("Jumpspace Drive 1")

JumpspaceDriveA.SetMaxCondition(600000.000000)
JumpspaceDriveA.SetCritical(0)
JumpspaceDriveA.SetTargetable(0)
JumpspaceDriveA.SetPrimary(0)
JumpspaceDriveA.SetPosition(0.000000, -0.600000, 0.000000)
JumpspaceDriveA.SetPosition2D(75.000000, 40.000000)
JumpspaceDriveA.SetRepairComplexity(3.000000)
JumpspaceDriveA.SetDisabledPercentage(0.750000)
JumpspaceDriveA.SetRadius(0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpspaceDriveA)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(135000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, 0.000000)
WarpEngines.SetPosition2D(46.000000, 60.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.100000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
PortWarp = App.EngineProperty_Create("Warp 1")

PortWarp.SetMaxCondition(84.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(0)
PortWarp.SetPosition(-0.002000, 0.001000, 0.000000)
PortWarp.SetPosition2D(39.000000, 88.000000)
PortWarp.SetRepairComplexity(1.000000)
PortWarp.SetDisabledPercentage(0.500000)
PortWarp.SetRadius(0.400000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Warp 2")

StarWarp.SetMaxCondition(84.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(0)
StarWarp.SetPosition(0.002000, 0.001000, 0.000000)
StarWarp.SetPosition2D(90.000000, 92.000000)
StarWarp.SetRepairComplexity(1.000000)
StarWarp.SetDisabledPercentage(0.500000)
StarWarp.SetRadius(0.400000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
StarWarp2 = App.EngineProperty_Create("Warp 3")

StarWarp2.SetMaxCondition(84.000000)
StarWarp2.SetCritical(0)
StarWarp2.SetTargetable(1)
StarWarp2.SetPrimary(0)
StarWarp2.SetPosition(0.000000, -0.002000, 0.000000)
StarWarp2.SetPosition2D(46.000000, 56.000000)
StarWarp2.SetRepairComplexity(1.000000)
StarWarp2.SetDisabledPercentage(0.500000)
StarWarp2.SetRadius(0.400000)
StarWarp2.SetEngineType(StarWarp2.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp2)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(100000.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(64.000000, 80.000000)
Engineering.SetRepairComplexity(1.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(0.100000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(2.000000)
Engineering.SetNumRepairTeams(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
Dalek2005Black = App.ShipProperty_Create("Dalek2005Black")

Dalek2005Black.SetGenus(1)
Dalek2005Black.SetSpecies(301)
Dalek2005Black.SetMass(1.000000)
Dalek2005Black.SetRotationalInertia(12220.000000)
Dalek2005Black.SetShipName("Dalek2005Black")
Dalek2005Black.SetModelFilename("data/Models/Ships/Dalek2005/Dalek2005Black.nif")
Dalek2005Black.SetDamageResolution(0.000100)
Dalek2005Black.SetAffiliation(0)
Dalek2005Black.SetStationary(0)
Dalek2005Black.SetAIString("NonFedAttack")
Dalek2005Black.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Dalek2005Black)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.500000, 1.200000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.300000, 1.200000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 0.500000, 1.200000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 0.500000, 1.200000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.012686, 2.250000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.029979, -1.250000)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.500000, 1.500000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
FwdCannon1 = App.PulseWeaponProperty_Create("Gunstick")

FwdCannon1.SetMaxCondition(20000.000000)
FwdCannon1.SetCritical(0)
FwdCannon1.SetTargetable(0)
FwdCannon1.SetPrimary(0)
FwdCannon1.SetPosition(-0.004000, 0.008000, 0.060000)
FwdCannon1.SetPosition2D(55.000000, 20.000000)
FwdCannon1.SetRepairComplexity(1.000000)
FwdCannon1.SetDisabledPercentage(0.250000)
FwdCannon1.SetRadius(0.010000)
FwdCannon1.SetDumbfire(1)
FwdCannon1.SetWeaponID(3)
FwdCannon1.SetGroups(8)
FwdCannon1.SetDamageRadiusFactor(0.100000)
FwdCannon1.SetIconNum(365)
FwdCannon1.SetIconPositionX(70.000000)
FwdCannon1.SetIconPositionY(48.000000)
FwdCannon1.SetIconAboveShip(1)
FwdCannon1.SetFireSound("DalekGunstickShot1")
FwdCannon1.SetMaxCharge(1.000000)
FwdCannon1.SetMaxDamage(1.000000)
FwdCannon1.SetMaxDamageDistance(100.000000)
FwdCannon1.SetMinFiringCharge(1.000000)
FwdCannon1.SetNormalDischargeRate(1.000000)
FwdCannon1.SetRechargeRate(0.700000)
FwdCannon1.SetIndicatorIconNum(510)
FwdCannon1.SetIndicatorIconPositionX(56.000000)
FwdCannon1.SetIndicatorIconPositionY(21.000000)
FwdCannon1Forward = App.TGPoint3()
FwdCannon1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
FwdCannon1Up = App.TGPoint3()
FwdCannon1Up.SetXYZ(1.000000, 0.000000, 0.000000)
FwdCannon1.SetOrientation(FwdCannon1Forward, FwdCannon1Up)
FwdCannon1.SetArcWidthAngles(-0.953343, 0.953343)
FwdCannon1.SetArcHeightAngles(-0.353343, 0.353343)
FwdCannon1.SetCooldownTime(0.100000)
FwdCannon1.SetModuleName("Tactical.Projectiles.DalekGunstick")
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdCannon1)
#################################################
CommandRoom = App.HullProperty_Create("Mutant")

CommandRoom.SetMaxCondition(85.000000)
CommandRoom.SetCritical(1)
CommandRoom.SetTargetable(1)
CommandRoom.SetPrimary(0)
CommandRoom.SetPosition(0.000000, 0.007000, 0.000000)
CommandRoom.SetPosition2D(65.000000, 38.000000)
CommandRoom.SetRepairComplexity(3.000000)
CommandRoom.SetDisabledPercentage(0.000000)
CommandRoom.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CommandRoom)
#################################################
ShuttleBayOEP = App.ObjectEmitterProperty_Create("Shuttle Bay OEP")

ShuttleBayOEPForward = App.TGPoint3()
ShuttleBayOEPForward.SetXYZ(0.000000, -1.000000, 0.000000)
ShuttleBayOEPUp = App.TGPoint3()
ShuttleBayOEPUp.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBayOEPRight = App.TGPoint3()
ShuttleBayOEPRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ShuttleBayOEP.SetOrientation(ShuttleBayOEPForward, ShuttleBayOEPUp, ShuttleBayOEPRight)
ShuttleBayOEPPosition = App.TGPoint3()
ShuttleBayOEPPosition.SetXYZ(0.000000, -0.950000, -1.050000)
ShuttleBayOEP.SetPosition(ShuttleBayOEPPosition)
ShuttleBayOEP.SetEmittedObjectType(ShuttleBayOEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBayOEP)
#################################################
ShuttleBay = App.HullProperty_Create("Shuttle Bay")

ShuttleBay.SetMaxCondition(80000.000000)
ShuttleBay.SetCritical(0)
ShuttleBay.SetTargetable(1)
ShuttleBay.SetPrimary(0)
ShuttleBay.SetPosition(0.000000, -15.950000, -1.075000)
ShuttleBay.SetPosition2D(0.000000, 0.000000)
ShuttleBay.SetRepairComplexity(7.000000)
ShuttleBay.SetDisabledPercentage(0.750000)
ShuttleBay.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay)
#################################################
ShuttleBay2OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 2 OEP")

ShuttleBay2OEPForward = App.TGPoint3()
ShuttleBay2OEPForward.SetXYZ(0.000000, -1.000000, 0.000000)
ShuttleBay2OEPUp = App.TGPoint3()
ShuttleBay2OEPUp.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBay2OEPRight = App.TGPoint3()
ShuttleBay2OEPRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ShuttleBay2OEP.SetOrientation(ShuttleBay2OEPForward, ShuttleBay2OEPUp, ShuttleBay2OEPRight)
ShuttleBay2OEPPosition = App.TGPoint3()
ShuttleBay2OEPPosition.SetXYZ(0.250000, -0.600000, 0.075000)
ShuttleBay2OEP.SetPosition(ShuttleBay2OEPPosition)
ShuttleBay2OEP.SetEmittedObjectType(ShuttleBay2OEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay2OEP)
#################################################
ShuttleBay2 = App.HullProperty_Create("Shuttle Bay 2")

ShuttleBay2.SetMaxCondition(80000.000000)
ShuttleBay2.SetCritical(0)
ShuttleBay2.SetTargetable(1)
ShuttleBay2.SetPrimary(0)
ShuttleBay2.SetPosition(0.000000, 15.600000, 0.075000)
ShuttleBay2.SetPosition2D(0.000000, 0.000000)
ShuttleBay2.SetRepairComplexity(7.000000)
ShuttleBay2.SetDisabledPercentage(0.750000)
ShuttleBay2.SetRadius(2.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay2)
#################################################
ArmourGenerator = App.HullProperty_Create("Armored Hull")

ArmourGenerator.SetMaxCondition(85.000000)
ArmourGenerator.SetCritical(0)
ArmourGenerator.SetTargetable(0)
ArmourGenerator.SetPrimary(0)
ArmourGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ArmourGenerator.SetPosition2D(0.000000, 0.000000)
ArmourGenerator.SetRepairComplexity(1.000000)
ArmourGenerator.SetDisabledPercentage(0.500000)
ArmourGenerator.SetRadius(0.000250)
App.g_kModelPropertyManager.RegisterLocalTemplate(ArmourGenerator)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(50000.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(1)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, -0.900000, -0.200000)
Torpedoes.SetPosition2D(65.000000, 80.000000)
Torpedoes.SetRepairComplexity(1.000000)
Torpedoes.SetDisabledPercentage(0.500000)
Torpedoes.SetRadius(0.014000)
Torpedoes.SetNormalPowerPerSecond(10.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 2500)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.DalekGunstick")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
PortAftTorp = App.TorpedoTubeProperty_Create("Aft Torp")

PortAftTorp.SetMaxCondition(120000.000000)
PortAftTorp.SetCritical(0)
PortAftTorp.SetTargetable(1)
PortAftTorp.SetPrimary(0)
PortAftTorp.SetPosition(0.000000, -1.230000, -0.100000)
PortAftTorp.SetPosition2D(65.000000, 90.000000)
PortAftTorp.SetRepairComplexity(1.000000)
PortAftTorp.SetDisabledPercentage(0.500000)
PortAftTorp.SetRadius(0.250000)
PortAftTorp.SetDumbfire(1)
PortAftTorp.SetWeaponID(4)
PortAftTorp.SetGroups(2)
PortAftTorp.SetDamageRadiusFactor(2.999999)
PortAftTorp.SetIconNum(370)
PortAftTorp.SetIconPositionX(63.000000)
PortAftTorp.SetIconPositionY(118.000000)
PortAftTorp.SetIconAboveShip(1)
PortAftTorp.SetImmediateDelay(0.250000)
PortAftTorp.SetReloadDelay(15.000000)
PortAftTorp.SetMaxReady(3)
PortAftTorpDirection = App.TGPoint3()
PortAftTorpDirection.SetXYZ(0.000000, -1.000000, 0.000000)
PortAftTorp.SetDirection(PortAftTorpDirection)
PortAftTorpRight = App.TGPoint3()
PortAftTorpRight.SetXYZ(1.000000, 0.000000, 0.000000)
PortAftTorp.SetRight(PortAftTorpRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortAftTorp)
#################################################
PortForwardTorp = App.TorpedoTubeProperty_Create("Forward Torp")

PortForwardTorp.SetMaxCondition(120000.000000)
PortForwardTorp.SetCritical(0)
PortForwardTorp.SetTargetable(1)
PortForwardTorp.SetPrimary(0)
PortForwardTorp.SetPosition(0.000000, 1.235000, -0.100000)
PortForwardTorp.SetPosition2D(65.000000, 60.000000)
PortForwardTorp.SetRepairComplexity(1.000000)
PortForwardTorp.SetDisabledPercentage(0.500000)
PortForwardTorp.SetRadius(0.250000)
PortForwardTorp.SetDumbfire(1)
PortForwardTorp.SetWeaponID(4)
PortForwardTorp.SetGroups(2)
PortForwardTorp.SetDamageRadiusFactor(2.999999)
PortForwardTorp.SetIconNum(370)
PortForwardTorp.SetIconPositionX(63.000000)
PortForwardTorp.SetIconPositionY(38.000000)
PortForwardTorp.SetIconAboveShip(1)
PortForwardTorp.SetImmediateDelay(0.250000)
PortForwardTorp.SetReloadDelay(15.000000)
PortForwardTorp.SetMaxReady(3)
PortForwardTorpDirection = App.TGPoint3()
PortForwardTorpDirection.SetXYZ(0.000000, 1.000000, 0.000000)
PortForwardTorp.SetDirection(PortForwardTorpDirection)
PortForwardTorpRight = App.TGPoint3()
PortForwardTorpRight.SetXYZ(1.000000, 0.000000, 0.000000)
PortForwardTorp.SetRight(PortForwardTorpRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortForwardTorp)
#################################################
StarAftTorp = App.TorpedoTubeProperty_Create("Star Torp")

StarAftTorp.SetMaxCondition(120000.000000)
StarAftTorp.SetCritical(0)
StarAftTorp.SetTargetable(1)
StarAftTorp.SetPrimary(0)
StarAftTorp.SetPosition(1.230000, 0.000000, -0.100000)
StarAftTorp.SetPosition2D(50.000000, 75.000000)
StarAftTorp.SetRepairComplexity(1.000000)
StarAftTorp.SetDisabledPercentage(0.500000)
StarAftTorp.SetRadius(0.250000)
StarAftTorp.SetDumbfire(1)
StarAftTorp.SetWeaponID(4)
StarAftTorp.SetGroups(2)
StarAftTorp.SetDamageRadiusFactor(2.999999)
StarAftTorp.SetIconNum(370)
StarAftTorp.SetIconPositionX(103.000000)
StarAftTorp.SetIconPositionY(78.000000)
StarAftTorp.SetIconAboveShip(1)
StarAftTorp.SetImmediateDelay(0.250000)
StarAftTorp.SetReloadDelay(15.000000)
StarAftTorp.SetMaxReady(3)
StarAftTorpDirection = App.TGPoint3()
StarAftTorpDirection.SetXYZ(1.000000, 0.000000, 0.000000)
StarAftTorp.SetDirection(StarAftTorpDirection)
StarAftTorpRight = App.TGPoint3()
StarAftTorpRight.SetXYZ(0.000000, 0.000000, 1.000000)
StarAftTorp.SetRight(StarAftTorpRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarAftTorp)
#################################################
StarForwardTorp = App.TorpedoTubeProperty_Create("Port Torp")

StarForwardTorp.SetMaxCondition(120000.000000)
StarForwardTorp.SetCritical(0)
StarForwardTorp.SetTargetable(1)
StarForwardTorp.SetPrimary(0)
StarForwardTorp.SetPosition(-1.230000, 0.000000, -0.075000)
StarForwardTorp.SetPosition2D(80.000000, 75.000000)
StarForwardTorp.SetRepairComplexity(1.000000)
StarForwardTorp.SetDisabledPercentage(0.500000)
StarForwardTorp.SetRadius(0.250000)
StarForwardTorp.SetDumbfire(1)
StarForwardTorp.SetWeaponID(4)
StarForwardTorp.SetGroups(2)
StarForwardTorp.SetDamageRadiusFactor(2.999999)
StarForwardTorp.SetIconNum(370)
StarForwardTorp.SetIconPositionX(23.000000)
StarForwardTorp.SetIconPositionY(78.000000)
StarForwardTorp.SetIconAboveShip(1)
StarForwardTorp.SetImmediateDelay(0.250000)
StarForwardTorp.SetReloadDelay(15.000000)
StarForwardTorp.SetMaxReady(3)
StarForwardTorpDirection = App.TGPoint3()
StarForwardTorpDirection.SetXYZ(-1.000000, 0.000000, 0.000000)
StarForwardTorp.SetDirection(StarForwardTorpDirection)
StarForwardTorpRight = App.TGPoint3()
StarForwardTorpRight.SetXYZ(0.000000, 0.000000, 1.000000)
StarForwardTorp.SetRight(StarForwardTorpRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarForwardTorp)
#################################################
BeamControl = App.WeaponSystemProperty_Create("Beam Controls")

BeamControl.SetMaxCondition(120.000000)
BeamControl.SetCritical(0)
BeamControl.SetTargetable(1)
BeamControl.SetPrimary(1)
BeamControl.SetPosition(0.003000, 0.004000, 0.000000)
BeamControl.SetPosition2D(79.000000, 59.000000)
BeamControl.SetRepairComplexity(3.000000)
BeamControl.SetDisabledPercentage(0.250000)
BeamControl.SetRadius(0.032500)
BeamControl.SetNormalPowerPerSecond(0.500000)
BeamControl.SetWeaponSystemType(BeamControl.WST_PHASER)
BeamControl.SetSingleFire(0)
BeamControl.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
BeamControl.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(BeamControl)
#################################################
Phaser = App.PhaserProperty_Create("Main Weapon")

Phaser.SetMaxCondition(60.000000)
Phaser.SetCritical(0)
Phaser.SetTargetable(0)
Phaser.SetPrimary(0)
Phaser.SetPosition(0.003000, 0.004000, 0.011000)
Phaser.SetPosition2D(65.000000, 26.000000)
Phaser.SetRepairComplexity(3.000000)
Phaser.SetDisabledPercentage(0.750000)
Phaser.SetRadius(0.034000)
Phaser.SetDumbfire(0)
Phaser.SetWeaponID(1)
Phaser.SetGroups(1)
Phaser.SetDamageRadiusFactor(10.000000)
Phaser.SetIconNum(364)
Phaser.SetIconPositionX(62.000000)
Phaser.SetIconPositionY(45.000000)
Phaser.SetIconAboveShip(1)
Phaser.SetFireSound("DalekGunstickShot2")
Phaser.SetMaxCharge(5.000000)
Phaser.SetMaxDamage(130.000000)
Phaser.SetMaxDamageDistance(80.000000)
Phaser.SetMinFiringCharge(2.000000)
Phaser.SetNormalDischargeRate(1.000000)
Phaser.SetRechargeRate(0.750000)
Phaser.SetIndicatorIconNum(510)
Phaser.SetIndicatorIconPositionX(56.000000)
Phaser.SetIndicatorIconPositionY(21.000000)
PhaserForward = App.TGPoint3()
PhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
PhaserUp = App.TGPoint3()
PhaserUp.SetXYZ(1.000000, 0.000000, 0.000000)
Phaser.SetOrientation(PhaserForward, PhaserUp)
Phaser.SetWidth(0.002750)
Phaser.SetLength(0.002750)
Phaser.SetArcWidthAngles(-0.953343, 0.953343)
Phaser.SetArcHeightAngles(-0.353530, 0.353530)
Phaser.SetPhaserTextureStart(0)
Phaser.SetPhaserTextureEnd(7)
Phaser.SetPhaserWidth(1.002000)
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.200000, 1.000000, 1.000000)
Phaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 0.500000)
Phaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.80000, 0.900000, 1.000000, 0.80000)
Phaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.900000, 0.990000, 1.000000, 0.100000)
Phaser.SetInnerCoreColor(kColor)
Phaser.SetNumSides(8)
Phaser.SetMainRadius(0.001000)
Phaser.SetTaperRadius(0.000000)
Phaser.SetCoreScale(0.001000)
Phaser.SetTaperRatio(0.000001)
Phaser.SetTaperMinLength(1.000000)
Phaser.SetTaperMaxLength(3.000000)
Phaser.SetLengthTextureTilePerUnit(0.000500)
Phaser.SetPerimeterTile(1.000000)
Phaser.SetTextureSpeed(2.500000)
Phaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Phaser)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(120000.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(1)
Tractors.SetPrimary(1)
Tractors.SetPosition(-0.003000, 0.008000, 0.000000)
Tractors.SetPosition2D(52.000000, 59.000000)
Tractors.SetRepairComplexity(4.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.020000)
Tractors.SetNormalPowerPerSecond(0.000001)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Main Tool")

ForwardTractor.SetMaxCondition(40000.000000)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(0)
ForwardTractor.SetPrimary(0)
ForwardTractor.SetPosition(-0.003000, 0.008000, 0.011000)
ForwardTractor.SetPosition2D(52.000000, 55.000000)
ForwardTractor.SetRepairComplexity(4.000000)
ForwardTractor.SetDisabledPercentage(0.750000)
ForwardTractor.SetRadius(0.040000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(0)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(1.199999)
ForwardTractor.SetIconNum(364)
ForwardTractor.SetIconPositionX(100.000000)
ForwardTractor.SetIconPositionY(20.000000)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Dominion Tractor")
ForwardTractor.SetMaxCharge(999.000000)
ForwardTractor.SetMaxDamage(10000.000000)
ForwardTractor.SetMaxDamageDistance(5.000000)
ForwardTractor.SetMinFiringCharge(3.000000)
ForwardTractor.SetNormalDischargeRate(1.000000)
ForwardTractor.SetRechargeRate(0.300000)
ForwardTractor.SetIndicatorIconNum(510)
ForwardTractor.SetIndicatorIconPositionX(100.000000)
ForwardTractor.SetIndicatorIconPositionY(20.000000)
ForwardTractorForward = App.TGPoint3()
ForwardTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractorUp = App.TGPoint3()
ForwardTractorUp.SetXYZ(1.000000, 0.000000, 0.000000)
ForwardTractor.SetOrientation(ForwardTractorForward, ForwardTractorUp)
ForwardTractor.SetArcWidthAngles(-2.999999, 2.999999)
ForwardTractor.SetArcHeightAngles(-2.999999, 2.999999)
ForwardTractor.SetTractorBeamWidth(0.001001)
ForwardTractor.SetTextureStart(0)
ForwardTractor.SetTextureEnd(0)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
ForwardTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
ForwardTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
ForwardTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
ForwardTractor.SetInnerCoreColor(kColor)
ForwardTractor.SetNumSides(12)
ForwardTractor.SetMainRadius(0.001000)
ForwardTractor.SetTaperRadius(0.000000)
ForwardTractor.SetCoreScale(0.000100)
ForwardTractor.SetTaperRatio(0.100000)
ForwardTractor.SetTaperMinLength(1.000000)
ForwardTractor.SetTaperMaxLength(5.000000)
ForwardTractor.SetLengthTextureTilePerUnit(0.250000)
ForwardTractor.SetPerimeterTile(1.000000)
ForwardTractor.SetTextureSpeed(0.200000)
ForwardTractor.SetTextureName("data/Textures/Tactical/CADominion.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTractor)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Dalek2005Black", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Policarbide Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Armored Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Mutant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Reactor Module", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Front Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperdrive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Slipstream Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam Controls", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Weapon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Primary Weapons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gunstick", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Tool", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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