#####  Created by:
#####  Bridge Commander Universal Tool



import App
import GlobalPropertyTemplates

# Local Templates
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(50.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.150000, 0.000000)
Hull.SetPosition2D(0.000000, 0.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.500000)
Hull.SetRadius(0.025000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
HeavyRaider = App.ShipProperty_Create("HeavyRaider")

HeavyRaider.SetGenus(1)
HeavyRaider.SetSpecies(107)
HeavyRaider.SetMass(11.000000)
HeavyRaider.SetRotationalInertia(1.750000)
HeavyRaider.SetShipName("HeavyRaider")
HeavyRaider.SetModelFilename("data/models/ships/HeavyRaider/HeavyRaider.nif")
HeavyRaider.SetDamageResolution(0.000100)
HeavyRaider.SetAffiliation(0)
HeavyRaider.SetStationary(0)
HeavyRaider.SetAIString("NonFedAttack")
HeavyRaider.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(HeavyRaider)
#################################################
IonDrive = App.ImpulseEngineProperty_Create("Ion Drive")

IonDrive.SetMaxCondition(50.000000)
IonDrive.SetCritical(0)
IonDrive.SetTargetable(0)
IonDrive.SetPrimary(1)
IonDrive.SetPosition(0.000000, -0.015000, -0.004100)
IonDrive.SetPosition2D(65.000000, 85.000000)
IonDrive.SetRepairComplexity(1.000000)
IonDrive.SetDisabledPercentage(0.500000)
IonDrive.SetRadius(0.007500)
IonDrive.SetNormalPowerPerSecond(100.000000)
IonDrive.SetMaxAccel(2.800000)
IonDrive.SetMaxAngularAccel(0.750000)
IonDrive.SetMaxAngularVelocity(0.750000)
IonDrive.SetMaxSpeed(5.700000)
IonDrive.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(IonDrive)
#################################################
TyliumReactor = App.PowerProperty_Create("Tylium Reactor")

TyliumReactor.SetMaxCondition(50.000000)
TyliumReactor.SetCritical(1)
TyliumReactor.SetTargetable(1)
TyliumReactor.SetPrimary(1)
TyliumReactor.SetPosition(0.000000, -0.046492, 0.010000)
TyliumReactor.SetPosition2D(65.000000, 85.000000)
TyliumReactor.SetRepairComplexity(1.000000)
TyliumReactor.SetDisabledPercentage(0.500000)
TyliumReactor.SetRadius(0.005000)
TyliumReactor.SetMainBatteryLimit(8000.000000)
TyliumReactor.SetBackupBatteryLimit(1500.000000)
TyliumReactor.SetMainConduitCapacity(500.000000)
TyliumReactor.SetBackupConduitCapacity(200.000000)
TyliumReactor.SetPowerOutput(500.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(TyliumReactor)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(1300.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(65.000000, 85.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.002500)
RepairSystem.SetNormalPowerPerSecond(10.000000)
RepairSystem.SetMaxRepairPoints(5.000000)
RepairSystem.SetNumRepairTeams(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(50.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.065000, 0.135000, 0.030000)
SensorArray.SetPosition2D(65.000000, 45.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.006000)
SensorArray.SetNormalPowerPerSecond(120.000000)
SensorArray.SetBaseSensorRange(1900.000000)
SensorArray.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
MegatronShield = App.ShieldProperty_Create("Megatron Shield")

MegatronShield.SetMaxCondition(12.000000)
MegatronShield.SetCritical(0)
MegatronShield.SetTargetable(0)
MegatronShield.SetPrimary(1)
MegatronShield.SetPosition(0.000000, 0.000000, 0.000000)
MegatronShield.SetPosition2D(65.000000, 85.000000)
MegatronShield.SetRepairComplexity(1.000000)
MegatronShield.SetDisabledPercentage(0.500000)
MegatronShield.SetRadius(0.007500)
MegatronShield.SetNormalPowerPerSecond(0.000000)
MegatronShieldShieldGlowColor = App.TGColorA()
MegatronShieldShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
MegatronShield.SetShieldGlowColor(MegatronShieldShieldGlowColor)
MegatronShield.SetShieldGlowDecay(1.000000)
MegatronShield.SetMaxShields(MegatronShield.FRONT_SHIELDS, 0.000000)
MegatronShield.SetMaxShields(MegatronShield.REAR_SHIELDS, 0.000000)
MegatronShield.SetMaxShields(MegatronShield.TOP_SHIELDS, 0.000000)
MegatronShield.SetMaxShields(MegatronShield.BOTTOM_SHIELDS, 0.000000)
MegatronShield.SetMaxShields(MegatronShield.LEFT_SHIELDS, 0.000000)
MegatronShield.SetMaxShields(MegatronShield.RIGHT_SHIELDS, 0.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.FRONT_SHIELDS, 0.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.REAR_SHIELDS, 0.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.TOP_SHIELDS, 0.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.BOTTOM_SHIELDS, 0.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.LEFT_SHIELDS, 0.000000)
MegatronShield.SetShieldChargePerSecond(MegatronShield.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(MegatronShield)
#################################################
Cannons = App.WeaponSystemProperty_Create("Cannons")

Cannons.SetMaxCondition(40.000000)
Cannons.SetCritical(0)
Cannons.SetTargetable(0)
Cannons.SetPrimary(1)
Cannons.SetPosition(0.000000, 0.000000, 0.000000)
Cannons.SetPosition2D(65.000000, 85.000000)
Cannons.SetRepairComplexity(1.000000)
Cannons.SetDisabledPercentage(0.500000)
Cannons.SetRadius(0.005000)
Cannons.SetNormalPowerPerSecond(100.000000)
Cannons.SetWeaponSystemType(Cannons.WST_PULSE)
Cannons.SetSingleFire(0)
Cannons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("1234;Dual")
Cannons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cannons)
#################################################
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")

PortCannon.SetMaxCondition(47.000000)
PortCannon.SetCritical(0)
PortCannon.SetTargetable(1)
PortCannon.SetPrimary(0)
PortCannon.SetPosition(-0.022500, 0.210000, 0.015000)
PortCannon.SetPosition2D(70.000000, 65.000000)
PortCannon.SetRepairComplexity(1.000000)
PortCannon.SetDisabledPercentage(0.500000)
PortCannon.SetRadius(0.002500)
PortCannon.SetDumbfire(1)
PortCannon.SetWeaponID(1)
PortCannon.SetGroups(1)
PortCannon.SetDamageRadiusFactor(0.030000)
PortCannon.SetIconNum(365)
PortCannon.SetIconPositionX(70.000000)
PortCannon.SetIconPositionY(65.000000)
PortCannon.SetIconAboveShip(1)
PortCannon.SetFireSound("")
PortCannon.SetMaxCharge(1.000000)
PortCannon.SetMaxDamage(7.500000)
PortCannon.SetMaxDamageDistance(50.000000)
PortCannon.SetMinFiringCharge(1.000000)
PortCannon.SetNormalDischargeRate(1.000000)
PortCannon.SetRechargeRate(2.000000)
PortCannon.SetIndicatorIconNum(510)
PortCannon.SetIndicatorIconPositionX(50.000000)
PortCannon.SetIndicatorIconPositionY(25.000000)
PortCannonForward = App.TGPoint3()
PortCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannonUp = App.TGPoint3()
PortCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon.SetOrientation(PortCannonForward, PortCannonUp)
PortCannon.SetArcWidthAngles(-0.175001, 0.175001)
PortCannon.SetArcHeightAngles(-0.175001, 0.175001)
PortCannon.SetCooldownTime(0.000015)
PortCannon.SetModuleName("Tactical.Projectiles.CRaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
#################################################
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")

StarCannon.SetMaxCondition(47.000000)
StarCannon.SetCritical(0)
StarCannon.SetTargetable(1)
StarCannon.SetPrimary(0)
StarCannon.SetPosition(0.022500, 0.210000, 0.015000)
StarCannon.SetPosition2D(85.000000, 65.000000)
StarCannon.SetRepairComplexity(1.000000)
StarCannon.SetDisabledPercentage(0.500000)
StarCannon.SetRadius(0.002500)
StarCannon.SetDumbfire(1)
StarCannon.SetWeaponID(4)
StarCannon.SetGroups(4)
StarCannon.SetDamageRadiusFactor(0.030000)
StarCannon.SetIconNum(365)
StarCannon.SetIconPositionX(85.000000)
StarCannon.SetIconPositionY(65.000000)
StarCannon.SetIconAboveShip(1)
StarCannon.SetFireSound("(null)")
StarCannon.SetMaxCharge(1.000000)
StarCannon.SetMaxDamage(7.500000)
StarCannon.SetMaxDamageDistance(50.000000)
StarCannon.SetMinFiringCharge(1.000000)
StarCannon.SetNormalDischargeRate(1.000000)
StarCannon.SetRechargeRate(2.000000)
StarCannon.SetIndicatorIconNum(510)
StarCannon.SetIndicatorIconPositionX(65.000000)
StarCannon.SetIndicatorIconPositionY(25.000000)
StarCannonForward = App.TGPoint3()
StarCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannonUp = App.TGPoint3()
StarCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon.SetOrientation(StarCannonForward, StarCannonUp)
StarCannon.SetArcWidthAngles(-0.175001, 0.175001)
StarCannon.SetArcHeightAngles(-0.175001, 0.175001)
StarCannon.SetCooldownTime(0.000015)
StarCannon.SetModuleName("Tactical.Projectiles.CRaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
#################################################
Engine2 = App.EngineProperty_Create("Engine 2")

Engine2.SetMaxCondition(24.000000)
Engine2.SetCritical(0)
Engine2.SetTargetable(1)
Engine2.SetPrimary(0)
Engine2.SetPosition(-0.065500, -0.300000, 0.022500)
Engine2.SetPosition2D(47.000000, 100.000000)
Engine2.SetRepairComplexity(1.000000)
Engine2.SetDisabledPercentage(0.500000)
Engine2.SetRadius(0.008500)
Engine2.SetEngineType(Engine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine2)
#################################################
Engine1 = App.EngineProperty_Create("Engine 1")

Engine1.SetMaxCondition(24.000000)
Engine1.SetCritical(0)
Engine1.SetTargetable(1)
Engine1.SetPrimary(0)
Engine1.SetPosition(0.065500, -0.300000, 0.022500)
Engine1.SetPosition2D(83.000000, 100.000000)
Engine1.SetRepairComplexity(1.000000)
Engine1.SetDisabledPercentage(0.500000)
Engine1.SetRadius(0.008500)
Engine1.SetEngineType(Engine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine1)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.151230, 0.000000)
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
ViewscreenLeftPosition.SetXYZ(-0.066087, 0.000000, 0.000000)
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
ViewscreenRightPosition.SetXYZ(0.064519, 0.000000, 0.000000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 0.019445)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -0.018823)
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
FirstPersonCameraPosition.SetXYZ(0.000000, -0.070000, 0.050000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
PortCannon2 = App.PulseWeaponProperty_Create("Port Cannon 2")

PortCannon2.SetMaxCondition(47.000000)
PortCannon2.SetCritical(0)
PortCannon2.SetTargetable(1)
PortCannon2.SetPrimary(0)
PortCannon2.SetPosition(-0.012500, 0.210000, 0.007000)
PortCannon2.SetPosition2D(0.000000, 0.000000)
PortCannon2.SetRepairComplexity(1.000000)
PortCannon2.SetDisabledPercentage(0.500000)
PortCannon2.SetRadius(0.002500)
PortCannon2.SetDumbfire(1)
PortCannon2.SetWeaponID(1)
PortCannon2.SetGroups(1)
PortCannon2.SetDamageRadiusFactor(0.030000)
PortCannon2.SetIconNum(365)
PortCannon2.SetIconPositionX(74.000000)
PortCannon2.SetIconPositionY(68.000000)
PortCannon2.SetIconAboveShip(1)
PortCannon2.SetFireSound("")
PortCannon2.SetMaxCharge(1.000000)
PortCannon2.SetMaxDamage(7.500000)
PortCannon2.SetMaxDamageDistance(50.000000)
PortCannon2.SetMinFiringCharge(1.000000)
PortCannon2.SetNormalDischargeRate(1.000000)
PortCannon2.SetRechargeRate(2.000000)
PortCannon2.SetIndicatorIconNum(510)
PortCannon2.SetIndicatorIconPositionX(54.000000)
PortCannon2.SetIndicatorIconPositionY(28.000000)
PortCannon2Forward = App.TGPoint3()
PortCannon2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannon2Up = App.TGPoint3()
PortCannon2Up.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon2.SetOrientation(PortCannon2Forward, PortCannon2Up)
PortCannon2.SetArcWidthAngles(-0.175001, 0.175001)
PortCannon2.SetArcHeightAngles(-0.175001, 0.175001)
PortCannon2.SetCooldownTime(0.000015)
PortCannon2.SetModuleName("Tactical.Projectiles.CRaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon2)
#################################################
PortCannon3 = App.PulseWeaponProperty_Create("Port Cannon 3")

PortCannon3.SetMaxCondition(47.000000)
PortCannon3.SetCritical(0)
PortCannon3.SetTargetable(1)
PortCannon3.SetPrimary(0)
PortCannon3.SetPosition(-0.022500, 0.210000, 0.005000)
PortCannon3.SetPosition2D(0.000000, 0.000000)
PortCannon3.SetRepairComplexity(1.000000)
PortCannon3.SetDisabledPercentage(0.500000)
PortCannon3.SetRadius(0.002500)
PortCannon3.SetDumbfire(1)
PortCannon3.SetWeaponID(2)
PortCannon3.SetGroups(2)
PortCannon3.SetDamageRadiusFactor(0.030000)
PortCannon3.SetIconNum(365)
PortCannon3.SetIconPositionX(70.000000)
PortCannon3.SetIconPositionY(71.000000)
PortCannon3.SetIconAboveShip(1)
PortCannon3.SetFireSound("")
PortCannon3.SetMaxCharge(1.000000)
PortCannon3.SetMaxDamage(7.500000)
PortCannon3.SetMaxDamageDistance(50.000000)
PortCannon3.SetMinFiringCharge(1.000000)
PortCannon3.SetNormalDischargeRate(1.000000)
PortCannon3.SetRechargeRate(2.000000)
PortCannon3.SetIndicatorIconNum(510)
PortCannon3.SetIndicatorIconPositionX(50.000000)
PortCannon3.SetIndicatorIconPositionY(31.000000)
PortCannon3Forward = App.TGPoint3()
PortCannon3Forward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannon3Up = App.TGPoint3()
PortCannon3Up.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon3.SetOrientation(PortCannon3Forward, PortCannon3Up)
PortCannon3.SetArcWidthAngles(-0.175001, 0.175001)
PortCannon3.SetArcHeightAngles(-0.175001, 0.175001)
PortCannon3.SetCooldownTime(0.000015)
PortCannon3.SetModuleName("Tactical.Projectiles.CRaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon3)
#################################################
StarCannon2 = App.PulseWeaponProperty_Create("Star Cannon 2")

StarCannon2.SetMaxCondition(47.000000)
StarCannon2.SetCritical(0)
StarCannon2.SetTargetable(1)
StarCannon2.SetPrimary(0)
StarCannon2.SetPosition(0.012500, 0.210000, 0.007000)
StarCannon2.SetPosition2D(0.000000, 0.000000)
StarCannon2.SetRepairComplexity(1.000000)
StarCannon2.SetDisabledPercentage(0.500000)
StarCannon2.SetRadius(0.002500)
StarCannon2.SetDumbfire(1)
StarCannon2.SetWeaponID(2)
StarCannon2.SetGroups(2)
StarCannon2.SetDamageRadiusFactor(0.030000)
StarCannon2.SetIconNum(365)
StarCannon2.SetIconPositionX(81.000000)
StarCannon2.SetIconPositionY(68.000000)
StarCannon2.SetIconAboveShip(1)
StarCannon2.SetFireSound("")
StarCannon2.SetMaxCharge(1.000000)
StarCannon2.SetMaxDamage(7.500000)
StarCannon2.SetMaxDamageDistance(50.000000)
StarCannon2.SetMinFiringCharge(1.000000)
StarCannon2.SetNormalDischargeRate(1.000000)
StarCannon2.SetRechargeRate(2.000000)
StarCannon2.SetIndicatorIconNum(510)
StarCannon2.SetIndicatorIconPositionX(61.000000)
StarCannon2.SetIndicatorIconPositionY(28.000000)
StarCannon2Forward = App.TGPoint3()
StarCannon2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannon2Up = App.TGPoint3()
StarCannon2Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon2.SetOrientation(StarCannon2Forward, StarCannon2Up)
StarCannon2.SetArcWidthAngles(-0.175001, 0.175001)
StarCannon2.SetArcHeightAngles(-0.175001, 0.175001)
StarCannon2.SetCooldownTime(0.000015)
StarCannon2.SetModuleName("Tactical.Projectiles.CRaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon2)
#################################################
StarCannon3 = App.PulseWeaponProperty_Create("Star Cannon 3")

StarCannon3.SetMaxCondition(47.000000)
StarCannon3.SetCritical(0)
StarCannon3.SetTargetable(1)
StarCannon3.SetPrimary(0)
StarCannon3.SetPosition(0.022500, 0.210000, 0.005000)
StarCannon3.SetPosition2D(0.000000, 0.000000)
StarCannon3.SetRepairComplexity(1.000000)
StarCannon3.SetDisabledPercentage(0.500000)
StarCannon3.SetRadius(0.002500)
StarCannon3.SetDumbfire(1)
StarCannon3.SetWeaponID(4)
StarCannon3.SetGroups(4)
StarCannon3.SetDamageRadiusFactor(0.030000)
StarCannon3.SetIconNum(365)
StarCannon3.SetIconPositionX(85.000000)
StarCannon3.SetIconPositionY(71.000000)
StarCannon3.SetIconAboveShip(1)
StarCannon3.SetFireSound("")
StarCannon3.SetMaxCharge(1.000000)
StarCannon3.SetMaxDamage(7.500000)
StarCannon3.SetMaxDamageDistance(50.000000)
StarCannon3.SetMinFiringCharge(1.000000)
StarCannon3.SetNormalDischargeRate(1.000000)
StarCannon3.SetRechargeRate(2.000000)
StarCannon3.SetIndicatorIconNum(510)
StarCannon3.SetIndicatorIconPositionX(65.000000)
StarCannon3.SetIndicatorIconPositionY(31.000000)
StarCannon3Forward = App.TGPoint3()
StarCannon3Forward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannon3Up = App.TGPoint3()
StarCannon3Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon3.SetOrientation(StarCannon3Forward, StarCannon3Up)
StarCannon3.SetArcWidthAngles(-0.175001, 0.175001)
StarCannon3.SetArcHeightAngles(-0.175001, 0.175001)
StarCannon3.SetCooldownTime(0.000015)
StarCannon3.SetModuleName("Tactical.Projectiles.CRaiderCannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon3)
#################################################
Engine3 = App.EngineProperty_Create("Engine 3")

Engine3.SetMaxCondition(24.000000)
Engine3.SetCritical(0)
Engine3.SetTargetable(1)
Engine3.SetPrimary(0)
Engine3.SetPosition(0.012500, -0.120000, 0.058000)
Engine3.SetPosition2D(0.000000, 0.000000)
Engine3.SetRepairComplexity(1.000000)
Engine3.SetDisabledPercentage(0.500000)
Engine3.SetRadius(0.002500)
Engine3.SetEngineType(Engine3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine3)
#################################################
Engine4 = App.EngineProperty_Create("Engine 4")

Engine4.SetMaxCondition(24.000000)
Engine4.SetCritical(0)
Engine4.SetTargetable(1)
Engine4.SetPrimary(0)
Engine4.SetPosition(-0.012500, -0.120000, 0.058000)
Engine4.SetPosition2D(0.000000, 0.000000)
Engine4.SetRepairComplexity(1.000000)
Engine4.SetDisabledPercentage(0.500000)
Engine4.SetRadius(0.002500)
Engine4.SetEngineType(Engine4.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine4)
#################################################
Engine5 = App.EngineProperty_Create("Engine 5")

Engine5.SetMaxCondition(24.000000)
Engine5.SetCritical(0)
Engine5.SetTargetable(1)
Engine5.SetPrimary(0)
Engine5.SetPosition(0.112500, -0.200000, 0.020000)
Engine5.SetPosition2D(0.000000, 0.000000)
Engine5.SetRepairComplexity(1.000000)
Engine5.SetDisabledPercentage(0.500000)
Engine5.SetRadius(0.002500)
Engine5.SetEngineType(Engine5.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine5)
#################################################
Engine6 = App.EngineProperty_Create("Engine 6")

Engine6.SetMaxCondition(24.000000)
Engine6.SetCritical(0)
Engine6.SetTargetable(1)
Engine6.SetPrimary(0)
Engine6.SetPosition(-0.112500, -0.200000, 0.020000)
Engine6.SetPosition2D(0.000000, 0.000000)
Engine6.SetRepairComplexity(1.000000)
Engine6.SetDisabledPercentage(0.500000)
Engine6.SetRadius(0.002500)
Engine6.SetEngineType(Engine6.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine6)
#################################################
Engine7 = App.EngineProperty_Create("Engine 7")

Engine7.SetMaxCondition(24.000000)
Engine7.SetCritical(0)
Engine7.SetTargetable(1)
Engine7.SetPrimary(0)
Engine7.SetPosition(0.105000, -0.200000, 0.040000)
Engine7.SetPosition2D(0.000000, 0.000000)
Engine7.SetRepairComplexity(1.000000)
Engine7.SetDisabledPercentage(0.500000)
Engine7.SetRadius(0.002500)
Engine7.SetEngineType(Engine7.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine7)
#################################################
Engine8 = App.EngineProperty_Create("Engine 8")

Engine8.SetMaxCondition(24.000000)
Engine8.SetCritical(0)
Engine8.SetTargetable(1)
Engine8.SetPrimary(0)
Engine8.SetPosition(-0.105000, -0.200000, 0.040000)
Engine8.SetPosition2D(0.000000, 0.000000)
Engine8.SetRepairComplexity(1.000000)
Engine8.SetDisabledPercentage(0.500000)
Engine8.SetRadius(0.002500)
Engine8.SetEngineType(Engine8.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine8)
#################################################
FTLDrive = App.WarpEngineProperty_Create("FTL Drive")

FTLDrive.SetMaxCondition(20.000000)
FTLDrive.SetCritical(0)
FTLDrive.SetTargetable(0)
FTLDrive.SetPrimary(1)
FTLDrive.SetPosition(0.000000, 0.000000, 0.000000)
FTLDrive.SetPosition2D(0.000000, 0.000000)
FTLDrive.SetRepairComplexity(1.000000)
FTLDrive.SetDisabledPercentage(0.500000)
FTLDrive.SetRadius(0.250000)
FTLDrive.SetNormalPowerPerSecond(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLDrive)
#################################################
FTLDrive1 = App.EngineProperty_Create("FTL Drive 1")

FTLDrive1.SetMaxCondition(45.000000)
FTLDrive1.SetCritical(0)
FTLDrive1.SetTargetable(1)
FTLDrive1.SetPrimary(1)
FTLDrive1.SetPosition(0.000000, 0.000000, 0.000000)
FTLDrive1.SetPosition2D(0.000000, 0.000000)
FTLDrive1.SetRepairComplexity(1.000000)
FTLDrive1.SetDisabledPercentage(0.500000)
FTLDrive1.SetRadius(0.250000)
FTLDrive1.SetEngineType(FTLDrive1.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLDrive1)
#################################################
MissileSys = App.TorpedoSystemProperty_Create("Missile Sys")

MissileSys.SetMaxCondition(15.000000)
MissileSys.SetCritical(0)
MissileSys.SetTargetable(0)
MissileSys.SetPrimary(1)
MissileSys.SetPosition(0.000000, 0.000000, 0.000000)
MissileSys.SetPosition2D(65.000000, 85.000000)
MissileSys.SetRepairComplexity(1.000000)
MissileSys.SetDisabledPercentage(0.500000)
MissileSys.SetRadius(0.005000)
MissileSys.SetNormalPowerPerSecond(0.000000)
MissileSys.SetWeaponSystemType(MissileSys.WST_TORPEDO)
MissileSys.SetSingleFire(0)
MissileSys.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MissileSys.SetFiringChainString(kFiringChainString)
MissileSys.SetMaxTorpedoes(0, 8)
MissileSys.SetTorpedoScript(0, "Tactical.Projectiles.RaiderMissile")
MissileSys.SetMaxTorpedoes(1, 500)
MissileSys.SetTorpedoScript(1, "Tactical.Projectiles.Canons")
MissileSys.SetNumAmmoTypes(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissileSys)
#################################################
PortLauncher = App.TorpedoTubeProperty_Create("Port Launcher")

PortLauncher.SetMaxCondition(10.000000)
PortLauncher.SetCritical(0)
PortLauncher.SetTargetable(1)
PortLauncher.SetPrimary(0)
PortLauncher.SetPosition(-0.080000, 0.200000, -0.025000)
PortLauncher.SetPosition2D(65.000000, 60.000000)
PortLauncher.SetRepairComplexity(1.000000)
PortLauncher.SetDisabledPercentage(0.500000)
PortLauncher.SetRadius(10.002500)
PortLauncher.SetDumbfire(0)
PortLauncher.SetWeaponID(3)
PortLauncher.SetGroups(4)
PortLauncher.SetDamageRadiusFactor(0.060000)
PortLauncher.SetIconNum(370)
PortLauncher.SetIconPositionX(70.000000)
PortLauncher.SetIconPositionY(45.000000)
PortLauncher.SetIconAboveShip(1)
PortLauncher.SetImmediateDelay(0.200000)
PortLauncher.SetReloadDelay(20.000000)
PortLauncher.SetMaxReady(2)
PortLauncherDirection = App.TGPoint3()
PortLauncherDirection.SetXYZ(0.000000, 1.000000, 0.000000)
PortLauncher.SetDirection(PortLauncherDirection)
PortLauncherRight = App.TGPoint3()
PortLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
PortLauncher.SetRight(PortLauncherRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortLauncher)
#################################################
StarLauncher = App.TorpedoTubeProperty_Create("Star Launcher")

StarLauncher.SetMaxCondition(10.000000)
StarLauncher.SetCritical(0)
StarLauncher.SetTargetable(1)
StarLauncher.SetPrimary(0)
StarLauncher.SetPosition(0.080000, 0.200000, -0.025000)
StarLauncher.SetPosition2D(65.000000, 60.000000)
StarLauncher.SetRepairComplexity(1.000000)
StarLauncher.SetDisabledPercentage(0.500000)
StarLauncher.SetRadius(0.002500)
StarLauncher.SetDumbfire(0)
StarLauncher.SetWeaponID(3)
StarLauncher.SetGroups(4)
StarLauncher.SetDamageRadiusFactor(0.060000)
StarLauncher.SetIconNum(370)
StarLauncher.SetIconPositionX(85.000000)
StarLauncher.SetIconPositionY(45.000000)
StarLauncher.SetIconAboveShip(1)
StarLauncher.SetImmediateDelay(0.200000)
StarLauncher.SetReloadDelay(20.000000)
StarLauncher.SetMaxReady(2)
StarLauncherDirection = App.TGPoint3()
StarLauncherDirection.SetXYZ(0.000000, 1.000000, 0.000000)
StarLauncher.SetDirection(StarLauncherDirection)
StarLauncherRight = App.TGPoint3()
StarLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
StarLauncher.SetRight(StarLauncherRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarLauncher)

# Property Set
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("HeavyRaider", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ion Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Port Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 5", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 6", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 7", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 8", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
