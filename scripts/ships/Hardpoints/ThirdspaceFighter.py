# C:\Programme\Activision\Babylon 5 Bridge Commander\scripts\ships\Hardpoints\ThirdspaceFighter.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Engine = App.EngineProperty_Create("Engine")

Engine.SetMaxCondition(140.000000)
Engine.SetCritical(0)
Engine.SetTargetable(1)
Engine.SetPrimary(1)
Engine.SetPosition(0.000000, 0.000000, 0.000000)
Engine.SetPosition2D(0.000000, 0.000000)
Engine.SetRepairComplexity(1.000000)
Engine.SetDisabledPercentage(0.500000)
Engine.SetRadius(1.000000)
Engine.SetEngineType(Engine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine)
#################################################
SelfRepairingHull = App.HullProperty_Create("Self Repairing Hull")

SelfRepairingHull.SetMaxCondition(150.000000)
SelfRepairingHull.SetCritical(1)
SelfRepairingHull.SetTargetable(1)
SelfRepairingHull.SetPrimary(1)
SelfRepairingHull.SetPosition(0.000000, 0.000000, 0.000000)
SelfRepairingHull.SetPosition2D(0.000000, 0.000000)
SelfRepairingHull.SetRepairComplexity(26.000000)
SelfRepairingHull.SetDisabledPercentage(0.000000)
SelfRepairingHull.SetRadius(9.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(SelfRepairingHull)
#################################################
QuantumSingularity = App.PowerProperty_Create("Quantum Singularity")

QuantumSingularity.SetMaxCondition(300.000000)
QuantumSingularity.SetCritical(1)
QuantumSingularity.SetTargetable(1)
QuantumSingularity.SetPrimary(1)
QuantumSingularity.SetPosition(0.000000, 0.000000, 0.000000)
QuantumSingularity.SetPosition2D(0.000000, 0.000000)
QuantumSingularity.SetRepairComplexity(1.000000)
QuantumSingularity.SetDisabledPercentage(0.000001)
QuantumSingularity.SetRadius(1.000000)
QuantumSingularity.SetMainBatteryLimit(1500000.000000)
QuantumSingularity.SetBackupBatteryLimit(1000000.000000)
QuantumSingularity.SetMainConduitCapacity(30.000000)
QuantumSingularity.SetBackupConduitCapacity(20.000000)
QuantumSingularity.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(QuantumSingularity)
#################################################
Sensor = App.SensorProperty_Create("Sensor")

Sensor.SetMaxCondition(150.000000)
Sensor.SetCritical(0)
Sensor.SetTargetable(0)
Sensor.SetPrimary(1)
Sensor.SetPosition(0.000000, 0.000000, 0.000000)
Sensor.SetPosition2D(0.000000, 0.000000)
Sensor.SetRepairComplexity(1.000000)
Sensor.SetDisabledPercentage(0.500000)
Sensor.SetRadius(0.060000)
Sensor.SetNormalPowerPerSecond(1.000000)
Sensor.SetBaseSensorRange(2100.000000)
Sensor.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sensor)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(300.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(1)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.000001)
RepairSystem.SetRadius(0.030000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(150.000000)
RepairSystem.SetNumRepairTeams(3)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
EnergyField = App.ShieldProperty_Create("Energy Field Generator")

EnergyField.SetMaxCondition(300.000000)
EnergyField.SetCritical(0)
EnergyField.SetTargetable(1)
EnergyField.SetPrimary(1)
EnergyField.SetPosition(0.000000, 0.000000, 0.000000)
EnergyField.SetPosition2D(0.000000, 0.000000)
EnergyField.SetRepairComplexity(1.000000)
EnergyField.SetDisabledPercentage(0.500000)
EnergyField.SetRadius(0.010000)
EnergyField.SetNormalPowerPerSecond(1.000000)
EnergyFieldShieldGlowColor = App.TGColorA()
EnergyFieldShieldGlowColor.SetRGBA(1.000000, 1.000000, 0.900000, 1.000000)
EnergyField.SetShieldGlowColor(EnergyFieldShieldGlowColor)
EnergyField.SetShieldGlowDecay(2.000000)
EnergyField.SetMaxShields(EnergyField.FRONT_SHIELDS, 500.000000)
EnergyField.SetMaxShields(EnergyField.REAR_SHIELDS, 500.000000)
EnergyField.SetMaxShields(EnergyField.TOP_SHIELDS, 500.000000)
EnergyField.SetMaxShields(EnergyField.BOTTOM_SHIELDS, 500.000000)
EnergyField.SetMaxShields(EnergyField.LEFT_SHIELDS, 500.000000)
EnergyField.SetMaxShields(EnergyField.RIGHT_SHIELDS, 500.000000)
EnergyField.SetShieldChargePerSecond(EnergyField.FRONT_SHIELDS, 1.000000)
EnergyField.SetShieldChargePerSecond(EnergyField.REAR_SHIELDS, 1.000000)
EnergyField.SetShieldChargePerSecond(EnergyField.TOP_SHIELDS, 1.000000)
EnergyField.SetShieldChargePerSecond(EnergyField.BOTTOM_SHIELDS, 1.000000)
EnergyField.SetShieldChargePerSecond(EnergyField.LEFT_SHIELDS, 1.000000)
EnergyField.SetShieldChargePerSecond(EnergyField.RIGHT_SHIELDS, 1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(EnergyField)
#################################################
ThirdspaceFighter = App.ShipProperty_Create("ThirdspaceFighter")

ThirdspaceFighter.SetGenus(0)
ThirdspaceFighter.SetSpecies(401)
ThirdspaceFighter.SetMass(30.000000)
ThirdspaceFighter.SetRotationalInertia(500.000000)
ThirdspaceFighter.SetShipName("ThirdspaceFighter")
ThirdspaceFighter.SetModelFilename("data/Models/Ships/ThirdspaceFighter/ThirdspaceFighter.nif")
ThirdspaceFighter.SetDamageResolution(0.000010)
ThirdspaceFighter.SetAffiliation(0)
ThirdspaceFighter.SetStationary(0)
ThirdspaceFighter.SetAIString("NonFedAttack")
ThirdspaceFighter.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(ThirdspaceFighter)
#################################################
Telepath = App.TorpedoSystemProperty_Create("Telepath")

Telepath.SetMaxCondition(300.000000)
Telepath.SetCritical(1)
Telepath.SetTargetable(1)
Telepath.SetPrimary(1)
Telepath.SetPosition(0.000000, 0.000000, 0.000000)
Telepath.SetPosition2D(0.000000, 0.000000)
Telepath.SetRepairComplexity(1.000000)
Telepath.SetDisabledPercentage(0.500000)
Telepath.SetRadius(0.080000)
Telepath.SetNormalPowerPerSecond(1.000000)
Telepath.SetWeaponSystemType(Telepath.WST_TORPEDO)
Telepath.SetSingleFire(0)
Telepath.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Telepath.SetFiringChainString(kFiringChainString)
Telepath.SetMaxTorpedoes(0, 100)
Telepath.SetTorpedoScript(0, "Tactical.Projectiles.B5ThirdspaceTeleAttack")
Telepath.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Telepath)
#################################################
AftTorpedo = App.TorpedoTubeProperty_Create("Aft Torpedo")

AftTorpedo.SetMaxCondition(150.000000)
AftTorpedo.SetCritical(0)
AftTorpedo.SetTargetable(1)
AftTorpedo.SetPrimary(1)
AftTorpedo.SetPosition(0.000000, -0.100000, 0.000000)
AftTorpedo.SetPosition2D(0.000000, 0.000000)
AftTorpedo.SetRepairComplexity(3.000000)
AftTorpedo.SetDisabledPercentage(0.750000)
AftTorpedo.SetRadius(0.150000)
AftTorpedo.SetDumbfire(0)
AftTorpedo.SetWeaponID(2)
AftTorpedo.SetGroups(2)
AftTorpedo.SetDamageRadiusFactor(0.999999)
AftTorpedo.SetIconNum(370)
AftTorpedo.SetIconPositionX(76.000000)
AftTorpedo.SetIconPositionY(100.000000)
AftTorpedo.SetIconAboveShip(1)
AftTorpedo.SetImmediateDelay(0.500000)
AftTorpedo.SetReloadDelay(600.000000)
AftTorpedo.SetMaxReady(1)
AftTorpedoDirection = App.TGPoint3()
AftTorpedoDirection.SetXYZ(0.000000, -1.000000, 0.000000)
AftTorpedo.SetDirection(AftTorpedoDirection)
AftTorpedoRight = App.TGPoint3()
AftTorpedoRight.SetXYZ(-1.000000, 0.000000, 0.000000)
AftTorpedo.SetRight(AftTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTorpedo)
#################################################
ThirdspaceEngine = App.ImpulseEngineProperty_Create("Thirdspace Engine")

ThirdspaceEngine.SetMaxCondition(145.000000)
ThirdspaceEngine.SetCritical(0)
ThirdspaceEngine.SetTargetable(1)
ThirdspaceEngine.SetPrimary(1)
ThirdspaceEngine.SetPosition(0.000000, -0.500000, 0.000000)
ThirdspaceEngine.SetPosition2D(0.000000, 0.000000)
ThirdspaceEngine.SetRepairComplexity(1.000000)
ThirdspaceEngine.SetDisabledPercentage(0.500000)
ThirdspaceEngine.SetRadius(1.000000)
ThirdspaceEngine.SetNormalPowerPerSecond(2.000000)
ThirdspaceEngine.SetMaxAccel(5.000000)
ThirdspaceEngine.SetMaxAngularAccel(1.000000)
ThirdspaceEngine.SetMaxAngularVelocity(1.000000)
ThirdspaceEngine.SetMaxSpeed(25.000000)
ThirdspaceEngine.SetEngineSound("ThirdspaceEngine")
App.g_kModelPropertyManager.RegisterLocalTemplate(ThirdspaceEngine)
#################################################
UnknownEngine = App.EngineProperty_Create("Unknown Engine")

UnknownEngine.SetMaxCondition(150.000000)
UnknownEngine.SetCritical(0)
UnknownEngine.SetTargetable(1)
UnknownEngine.SetPrimary(1)
UnknownEngine.SetPosition(0.000000, -0.500000, 0.000000)
UnknownEngine.SetPosition2D(0.000000, 0.000000)
UnknownEngine.SetRepairComplexity(1.000000)
UnknownEngine.SetDisabledPercentage(0.500000)
UnknownEngine.SetRadius(1.000000)
UnknownEngine.SetEngineType(UnknownEngine.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(UnknownEngine)
#################################################
UnknownEngineBack = App.WarpEngineProperty_Create("Unknown Engine Back")

UnknownEngineBack.SetMaxCondition(300.000000)
UnknownEngineBack.SetCritical(0)
UnknownEngineBack.SetTargetable(0)
UnknownEngineBack.SetPrimary(1)
UnknownEngineBack.SetPosition(0.000000, 0.000000, 0.000000)
UnknownEngineBack.SetPosition2D(0.000000, 0.000000)
UnknownEngineBack.SetRepairComplexity(1.000000)
UnknownEngineBack.SetDisabledPercentage(0.000001)
UnknownEngineBack.SetRadius(1.000000)
UnknownEngineBack.SetNormalPowerPerSecond(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(UnknownEngineBack)
#################################################
DeathRay = App.PhaserProperty_Create("Death Ray")

DeathRay.SetMaxCondition(300.000000)
DeathRay.SetCritical(0)
DeathRay.SetTargetable(0)
DeathRay.SetPrimary(1)
DeathRay.SetPosition(0.000000, 0.500000, 0.000000)
DeathRay.SetPosition2D(0.000000, 0.000000)
DeathRay.SetRepairComplexity(1.000000)
DeathRay.SetDisabledPercentage(0.500000)
DeathRay.SetRadius(3.050000)
DeathRay.SetDumbfire(1)
DeathRay.SetWeaponID(0)
DeathRay.SetGroups(1)
DeathRay.SetDamageRadiusFactor(9.999999)
DeathRay.SetIconNum(510)
DeathRay.SetIconPositionX(60.000000)
DeathRay.SetIconPositionY(70.000000)
DeathRay.SetIconAboveShip(1)
DeathRay.SetFireSound("shadowbeam")
DeathRay.SetMaxCharge(1.000000)
DeathRay.SetMaxDamage(250.000000)
DeathRay.SetMaxDamageDistance(80.000000)
DeathRay.SetMinFiringCharge(0.500000)
DeathRay.SetNormalDischargeRate(2.000000)
DeathRay.SetRechargeRate(0.500000)
DeathRay.SetIndicatorIconNum(0)
DeathRay.SetIndicatorIconPositionX(0.000000)
DeathRay.SetIndicatorIconPositionY(0.000000)
DeathRayForward = App.TGPoint3()
DeathRayForward.SetXYZ(0.000000, 1.000000, 0.000000)
DeathRayUp = App.TGPoint3()
DeathRayUp.SetXYZ(0.000000, 0.000000, 1.000000)
DeathRay.SetOrientation(DeathRayForward, DeathRayUp)
DeathRay.SetWidth(0.010000)
DeathRay.SetLength(0.010000)
DeathRay.SetArcWidthAngles(-0.401426, 0.401426)
DeathRay.SetArcHeightAngles(-0.453786, 0.453786)
DeathRay.SetPhaserTextureStart(5)
DeathRay.SetPhaserTextureEnd(20)
DeathRay.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.576471, 0.156863, 1.000000, 1.000000)
DeathRay.SetOuterShellColor(kColor)
kColor.SetRGBA(0.576471, 0.156863, 1.000000, 1.000000)
DeathRay.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 0.200000, 0.400000, 1.000000)
DeathRay.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 0.200000, 0.400000, 1.000000)
DeathRay.SetInnerCoreColor(kColor)
DeathRay.SetNumSides(6)
DeathRay.SetMainRadius(0.200000)
DeathRay.SetTaperRadius(0.020000)
DeathRay.SetCoreScale(0.300000)
DeathRay.SetTaperRatio(0.050000)
DeathRay.SetTaperMinLength(5.000000)
DeathRay.SetTaperMaxLength(20.000000)
DeathRay.SetLengthTextureTilePerUnit(0.300000)
DeathRay.SetPerimeterTile(1.000000)
DeathRay.SetTextureSpeed(0.000100)
DeathRay.SetTextureName("data/b5shadow.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(DeathRay)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 4.500000, 0.000000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -3.500000, 0.500000)
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
ViewscreenLeftPosition.SetXYZ(-9.000000, -2.000000, 0.000000)
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
ViewscreenRightPosition.SetXYZ(9.000000, -2.000000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, -2.000000, 2.000000)
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
ViewscreenDownPosition.SetXYZ(0.000000, -2.000000, -2.000000)
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
FirstPersonCameraPosition.SetXYZ(-0.057000, 1.000000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
FireballSystem = App.WeaponSystemProperty_Create("FireballSystem")

FireballSystem.SetMaxCondition(310.000000)
FireballSystem.SetCritical(0)
FireballSystem.SetTargetable(0)
FireballSystem.SetPrimary(1)
FireballSystem.SetPosition(0.000000, 0.000000, 0.000000)
FireballSystem.SetPosition2D(0.000000, 0.000000)
FireballSystem.SetRepairComplexity(1.000000)
FireballSystem.SetDisabledPercentage(0.050000)
FireballSystem.SetRadius(0.250000)
FireballSystem.SetNormalPowerPerSecond(1.000000)
FireballSystem.SetWeaponSystemType(FireballSystem.WST_PULSE)
FireballSystem.SetSingleFire(0)
FireballSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
FireballSystem.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(FireballSystem)
#################################################
FireballThrower = App.PulseWeaponProperty_Create("FireballThrower")

FireballThrower.SetMaxCondition(130.000000)
FireballThrower.SetCritical(0)
FireballThrower.SetTargetable(1)
FireballThrower.SetPrimary(1)
FireballThrower.SetPosition(0.000000, 2.250000, 0.000000)
FireballThrower.SetPosition2D(0.000000, 0.000000)
FireballThrower.SetRepairComplexity(1.000000)
FireballThrower.SetDisabledPercentage(0.080000)
FireballThrower.SetRadius(0.250000)
FireballThrower.SetDumbfire(1)
FireballThrower.SetWeaponID(0)
FireballThrower.SetGroups(0)
FireballThrower.SetDamageRadiusFactor(3.999999)
FireballThrower.SetIconNum(365)
FireballThrower.SetIconPositionX(65.000000)
FireballThrower.SetIconPositionY(65.000000)
FireballThrower.SetIconAboveShip(1)
FireballThrower.SetFireSound("")
FireballThrower.SetMaxCharge(1.000000)
FireballThrower.SetMaxDamage(25.000000)
FireballThrower.SetMaxDamageDistance(170.000000)
FireballThrower.SetMinFiringCharge(1.000000)
FireballThrower.SetNormalDischargeRate(1.000000)
FireballThrower.SetRechargeRate(1.000000)
FireballThrower.SetIndicatorIconNum(510)
FireballThrower.SetIndicatorIconPositionX(57.000000)
FireballThrower.SetIndicatorIconPositionY(65.000000)
FireballThrowerForward = App.TGPoint3()
FireballThrowerForward.SetXYZ(0.000000, 1.000000, 0.000000)
FireballThrowerUp = App.TGPoint3()
FireballThrowerUp.SetXYZ(0.000000, 0.000000, 1.000000)
FireballThrower.SetOrientation(FireballThrowerForward, FireballThrowerUp)
FireballThrower.SetArcWidthAngles(-2.094395, 2.094395)
FireballThrower.SetArcHeightAngles(-2.094395, 2.094395)
FireballThrower.SetCooldownTime(1.000000)
FireballThrower.SetModuleName("Tactical.Projectiles.B5ThirdspaceFireball")
App.g_kModelPropertyManager.RegisterLocalTemplate(FireballThrower)
#################################################
TelepathAttack = App.PulseWeaponProperty_Create("TelepathAttack")

TelepathAttack.SetMaxCondition(310.000000)
TelepathAttack.SetCritical(0)
TelepathAttack.SetTargetable(0)
TelepathAttack.SetPrimary(1)
TelepathAttack.SetPosition(0.000000, 0.000000, 0.000000)
TelepathAttack.SetPosition2D(0.000000, 0.000000)
TelepathAttack.SetRepairComplexity(1.000000)
TelepathAttack.SetDisabledPercentage(0.500000)
TelepathAttack.SetRadius(0.250000)
TelepathAttack.SetDumbfire(1)
TelepathAttack.SetWeaponID(0)
TelepathAttack.SetGroups(0)
TelepathAttack.SetDamageRadiusFactor(9.999999)
TelepathAttack.SetIconNum(0)
TelepathAttack.SetIconPositionX(0.000000)
TelepathAttack.SetIconPositionY(0.000000)
TelepathAttack.SetIconAboveShip(1)
TelepathAttack.SetFireSound("")
TelepathAttack.SetMaxCharge(1.000000)
TelepathAttack.SetMaxDamage(265.000000)
TelepathAttack.SetMaxDamageDistance(170.000000)
TelepathAttack.SetMinFiringCharge(1.000000)
TelepathAttack.SetNormalDischargeRate(1.000000)
TelepathAttack.SetRechargeRate(0.010000)
TelepathAttack.SetIndicatorIconNum(0)
TelepathAttack.SetIndicatorIconPositionX(0.000000)
TelepathAttack.SetIndicatorIconPositionY(0.000000)
TelepathAttackForward = App.TGPoint3()
TelepathAttackForward.SetXYZ(0.000000, -1.000000, 0.000000)
TelepathAttackUp = App.TGPoint3()
TelepathAttackUp.SetXYZ(0.000000, 0.000000, 1.000000)
TelepathAttack.SetOrientation(TelepathAttackForward, TelepathAttackUp)
TelepathAttack.SetArcWidthAngles(-2.094395, 2.094395)
TelepathAttack.SetArcHeightAngles(-2.094395, 2.094395)
TelepathAttack.SetCooldownTime(120.000000)
TelepathAttack.SetModuleName("Tactical.Projectiles.B5ThirdspaceTeleAttack")
App.g_kModelPropertyManager.RegisterLocalTemplate(TelepathAttack)
#################################################
JumpspaceDrive = App.HullProperty_Create("Jumpspace Drive 1")

JumpspaceDrive.SetMaxCondition(310.000000)
JumpspaceDrive.SetCritical(0)
JumpspaceDrive.SetTargetable(0)
JumpspaceDrive.SetPrimary(0)
JumpspaceDrive.SetPosition(0.000000, 0.000000, 0.000000)
JumpspaceDrive.SetPosition2D(0.000000, 0.000000)
JumpspaceDrive.SetRepairComplexity(1.000000)
JumpspaceDrive.SetDisabledPercentage(0.500000)
JumpspaceDrive.SetRadius(7.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpspaceDrive)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Self Repairing Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Quantum Singularity", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ThirdspaceFighter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Thirdspace Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Unknown Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Unknown Engine Back", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Energy Field Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("FireballSystem", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FireballThrower", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("TelepathAttack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)