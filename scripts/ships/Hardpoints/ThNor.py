# C:\WINDOWS\Desktop\trek stuff\thnor\B5_ThNor_ship\scripts\ships\hardpoints\ThNor.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(5000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(-0.028201, 2.464150, 0.802552)
ShieldGenerator.SetPosition2D(66.000000, 38.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.120000)
ShieldGenerator.SetNormalPowerPerSecond(0.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.501961, 0.247059, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 20.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 3.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 3.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 3.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(1500.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(-0.002209, 0.007622, 0.015820)
Hull.SetPosition2D(66.000000, 38.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(6.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1400.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.306308, 5.223030, 0.883585)
SensorArray.SetPosition2D(66.000000, 7.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.800000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(1600.000000)
SensorArray.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(1300.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.095439, -3.456930, 0.645812)
ImpulseEngines.SetPosition2D(64.000000, 104.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.100000)
ImpulseEngines.SetNormalPowerPerSecond(50.000000)
ImpulseEngines.SetMaxAccel(3.500000)
ImpulseEngines.SetMaxAngularAccel(0.750000)
ImpulseEngines.SetMaxAngularVelocity(0.500000)
ImpulseEngines.SetMaxSpeed(9.700000)
ImpulseEngines.SetEngineSound("ThNor Engine")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")

PortCannon.SetMaxCondition(1000.000000)
PortCannon.SetCritical(0)
PortCannon.SetTargetable(1)
PortCannon.SetPrimary(1)
PortCannon.SetPosition(-0.529964, 8.389760, 0.115412)
PortCannon.SetPosition2D(15.000000, 45.000000)
PortCannon.SetRepairComplexity(9.000000)
PortCannon.SetDisabledPercentage(0.750000)
PortCannon.SetRadius(1.000000)
PortCannon.SetDumbfire(1)
PortCannon.SetWeaponID(1)
PortCannon.SetGroups(1)
PortCannon.SetDamageRadiusFactor(1.000000)
PortCannon.SetIconNum(365)
PortCannon.SetIconPositionX(74.000000)
PortCannon.SetIconPositionY(28.000000)
PortCannon.SetIconAboveShip(1)
PortCannon.SetFireSound("ThNor HCannon")
PortCannon.SetMaxCharge(7.000000)
PortCannon.SetMaxDamage(100.000000)
PortCannon.SetMaxDamageDistance(75.000000)
PortCannon.SetMinFiringCharge(7.000000)
PortCannon.SetNormalDischargeRate(1.000000)
PortCannon.SetRechargeRate(3.000000)
PortCannon.SetIndicatorIconNum(512)
PortCannon.SetIndicatorIconPositionX(54.000000)
PortCannon.SetIndicatorIconPositionY(20.000000)
PortCannonForward = App.TGPoint3()
PortCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannonUp = App.TGPoint3()
PortCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon.SetOrientation(PortCannonForward, PortCannonUp)
PortCannon.SetArcWidthAngles(-0.436332, 0.436332)
PortCannon.SetArcHeightAngles(-0.436332, 0.436332)
PortCannon.SetCooldownTime(1.000000)
PortCannon.SetModuleName("Tactical.Projectiles.Thnor_Energy")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
#################################################
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")

StarCannon.SetMaxCondition(1000.000000)
StarCannon.SetCritical(0)
StarCannon.SetTargetable(1)
StarCannon.SetPrimary(1)
StarCannon.SetPosition(0.535687, 8.389760, 0.099316)
StarCannon.SetPosition2D(113.000000, 45.000000)
StarCannon.SetRepairComplexity(9.000000)
StarCannon.SetDisabledPercentage(0.750000)
StarCannon.SetRadius(0.250000)
StarCannon.SetDumbfire(1)
StarCannon.SetWeaponID(2)
StarCannon.SetGroups(1)
StarCannon.SetDamageRadiusFactor(1.000000)
StarCannon.SetIconNum(365)
StarCannon.SetIconPositionX(82.000000)
StarCannon.SetIconPositionY(28.000000)
StarCannon.SetIconAboveShip(1)
StarCannon.SetFireSound("ThNor HCannon")
StarCannon.SetMaxCharge(7.000000)
StarCannon.SetMaxDamage(100.000000)
StarCannon.SetMaxDamageDistance(75.000000)
StarCannon.SetMinFiringCharge(7.000000)
StarCannon.SetNormalDischargeRate(1.000000)
StarCannon.SetRechargeRate(3.000000)
StarCannon.SetIndicatorIconNum(513)
StarCannon.SetIndicatorIconPositionX(78.000000)
StarCannon.SetIndicatorIconPositionY(21.000000)
StarCannonForward = App.TGPoint3()
StarCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannonUp = App.TGPoint3()
StarCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon.SetOrientation(StarCannonForward, StarCannonUp)
StarCannon.SetArcWidthAngles(-0.436332, 0.436332)
StarCannon.SetArcHeightAngles(-0.436332, 0.436332)
StarCannon.SetCooldownTime(1.000000)
StarCannon.SetModuleName("Tactical.Projectiles.Thnor_Energy")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
#################################################
DisruptorCannons = App.WeaponSystemProperty_Create("Disruptor Cannons")

DisruptorCannons.SetMaxCondition(1300.000000)
DisruptorCannons.SetCritical(0)
DisruptorCannons.SetTargetable(0)
DisruptorCannons.SetPrimary(1)
DisruptorCannons.SetPosition(1.380370, 2.996730, 0.444457)
DisruptorCannons.SetPosition2D(64.000000, 44.000000)
DisruptorCannons.SetRepairComplexity(9.000000)
DisruptorCannons.SetDisabledPercentage(0.750000)
DisruptorCannons.SetRadius(0.040000)
DisruptorCannons.SetNormalPowerPerSecond(80.000000)
DisruptorCannons.SetWeaponSystemType(DisruptorCannons.WST_PULSE)
DisruptorCannons.SetSingleFire(0)
DisruptorCannons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DisruptorCannons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorCannons)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(1500.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(-0.195792, 2.719010, 1.152300)
Engineering.SetPosition2D(64.000000, 34.000000)
Engineering.SetRepairComplexity(4.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(1.000000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(7.000000)
Engineering.SetNumRepairTeams(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.894427, 0.447214, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.143623, 5.493420, 0.431859)
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
ViewscreenBackPosition.SetXYZ(0.038106, -5.960970, 0.991600)
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
ViewscreenLeftPosition.SetXYZ(-2.784390, 1.062490, 0.523164)
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
ViewscreenRightPosition.SetXYZ(2.828550, 1.326200, 0.508483)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.074058, 0.690461, 1.478350)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.118990, 0.731401, -1.471910)
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
FirstPersonCameraPosition.SetXYZ(0.034428, 0.693920, 1.484030)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
MainReactor = App.PowerProperty_Create("Main Reactor")

MainReactor.SetMaxCondition(1500.000000)
MainReactor.SetCritical(1)
MainReactor.SetTargetable(1)
MainReactor.SetPrimary(1)
MainReactor.SetPosition(-0.022251, 2.596080, -0.966430)
MainReactor.SetPosition2D(65.000000, 55.000000)
MainReactor.SetRepairComplexity(2.000000)
MainReactor.SetDisabledPercentage(0.500000)
MainReactor.SetRadius(1.000000)
MainReactor.SetMainBatteryLimit(80000.000000)
MainReactor.SetBackupBatteryLimit(40000.000000)
MainReactor.SetMainConduitCapacity(800.000000)
MainReactor.SetBackupConduitCapacity(350.000000)
MainReactor.SetPowerOutput(1000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainReactor)
#################################################
JumpEngine = App.WarpEngineProperty_Create("Jump Engine")

JumpEngine.SetMaxCondition(1500.000000)
JumpEngine.SetCritical(0)
JumpEngine.SetTargetable(0)
JumpEngine.SetPrimary(1)
JumpEngine.SetPosition(-0.025556, -1.414330, 0.661875)
JumpEngine.SetPosition2D(64.000000, 70.000000)
JumpEngine.SetRepairComplexity(1.000000)
JumpEngine.SetDisabledPercentage(1.500000)
JumpEngine.SetRadius(0.250000)
JumpEngine.SetNormalPowerPerSecond(50.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpEngine)
#################################################
Jump = App.EngineProperty_Create("Jumpspace Drive 1")

Jump.SetMaxCondition(1500.000000)
Jump.SetCritical(0)
Jump.SetTargetable(1)
Jump.SetPrimary(1)
Jump.SetPosition(-0.033092, -6.404870, -0.145745)
Jump.SetPosition2D(66.000000, 34.000000)
Jump.SetRepairComplexity(1.000000)
Jump.SetDisabledPercentage(0.500000)
Jump.SetRadius(3.500000)
Jump.SetEngineType(Jump.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Jump)




#################################################
Topengine = App.ImpulseEngineProperty_Create("Main SubJump ENGINES")

Topengine.SetMaxCondition(1000.000000)
Topengine.SetCritical(0)
Topengine.SetTargetable(1)
Topengine.SetPrimary(1)
Topengine.SetPosition(0.010137, -1.949710, 0.479570)
Topengine.SetPosition2D(64.000000, 34.000000)
Topengine.SetRepairComplexity(4.000000)
Topengine.SetDisabledPercentage(0.500000)
Topengine.SetRadius(0.550000)
Topengine.SetNormalPowerPerSecond(50.000000)
Topengine.SetMaxAccel(3.500000)
Topengine.SetMaxAngularAccel(0.550000)
Topengine.SetMaxAngularVelocity(0.500000)
Topengine.SetMaxSpeed(9.700000)
Topengine.SetEngineSound("ThNor Engine")
App.g_kModelPropertyManager.RegisterLocalTemplate(Topengine)
#################################################
Bottporteng = App.EngineProperty_Create("Bott port eng")

Bottporteng.SetMaxCondition(1000.000000)
Bottporteng.SetCritical(0)
Bottporteng.SetTargetable(1)
Bottporteng.SetPrimary(0)
Bottporteng.SetPosition(-1.058580, -5.131870, 0.127166)
Bottporteng.SetPosition2D(62.000000, 54.000000)
Bottporteng.SetRepairComplexity(4.000000)
Bottporteng.SetDisabledPercentage(0.500000)
Bottporteng.SetRadius(5.000000)
Bottporteng.SetEngineType(Bottporteng.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Bottporteng)
#################################################
bottstareng = App.EngineProperty_Create("Bott star eng")

bottstareng.SetMaxCondition(1000.000000)
bottstareng.SetCritical(0)
bottstareng.SetTargetable(1)
bottstareng.SetPrimary(0)
bottstareng.SetPosition(1.113980, -5.139560, 0.127214)
bottstareng.SetPosition2D(66.000000, 54.000000)
bottstareng.SetRepairComplexity(4.000000)
bottstareng.SetDisabledPercentage(0.500000)
bottstareng.SetRadius(5.000000)
bottstareng.SetEngineType(bottstareng.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(bottstareng)
#################################################
Bottportgl = App.BlinkingLightProperty_Create("Bott port gl")

BottportglForward = App.TGPoint3()
BottportglForward.SetXYZ(0.000000, 1.000000, 0.000000)
BottportglUp = App.TGPoint3()
BottportglUp.SetXYZ(0.000000, 0.000000, 1.000000)
BottportglRight = App.TGPoint3()
BottportglRight.SetXYZ(1.000000, 0.000000, 0.000000)
Bottportgl.SetOrientation(BottportglForward, BottportglUp, BottportglRight)
BottportglPosition = App.TGPoint3()
BottportglPosition.SetXYZ(-1.081130, -5.137770, 0.104094)
Bottportgl.SetPosition(BottportglPosition)
BottportglLightColor = App.TGColorA()
BottportglLightColor.SetRGBA(1.000000, 0.501961, 0.501961, 1.000000)
Bottportgl.SetColor(BottportglLightColor)
Bottportgl.SetRadius(15.000000)
Bottportgl.SetPeriod(1.000000)
Bottportgl.SetDuration(0.000000)
Bottportgl.SetTextureName("scripts/Custom/NanoFXv2/SpecialFX/Gfx/Blinker/Blank.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Bottportgl)
#################################################
Bottstargl = App.BlinkingLightProperty_Create("Bott star gl")

BottstarglForward = App.TGPoint3()
BottstarglForward.SetXYZ(0.000000, 1.000000, 0.000000)
BottstarglUp = App.TGPoint3()
BottstarglUp.SetXYZ(0.000000, 0.000000, 1.000000)
BottstarglRight = App.TGPoint3()
BottstarglRight.SetXYZ(1.000000, 0.000000, 0.000000)
Bottstargl.SetOrientation(BottstarglForward, BottstarglUp, BottstarglRight)
BottstarglPosition = App.TGPoint3()
BottstarglPosition.SetXYZ(1.090060, -5.147880, 0.127265)
Bottstargl.SetPosition(BottstarglPosition)
BottstarglLightColor = App.TGColorA()
BottstarglLightColor.SetRGBA(1.000000, 0.501961, 0.501961, 1.000000)
Bottstargl.SetColor(BottstarglLightColor)
Bottstargl.SetRadius(15.000000)
Bottstargl.SetPeriod(1.000000)
Bottstargl.SetDuration(0.000000)
Bottstargl.SetTextureName("scripts/Custom/NanoFXv2/SpecialFX/Gfx/Blinker/Blank.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Bottstargl)
#################################################
ThNor = App.ShipProperty_Create("ThNor")

ThNor.SetGenus(1)
ThNor.SetSpecies(401)
ThNor.SetMass(700.000000)
ThNor.SetRotationalInertia(7000.000000)
ThNor.SetShipName("ThNor")
ThNor.SetModelFilename("data/Models/Ships/ThNor.nif")
ThNor.SetDamageResolution(5.000000)
ThNor.SetAffiliation(0)
ThNor.SetStationary(0)
ThNor.SetAIString("NonFedAttack")
ThNor.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(ThNor)
#################################################
MissleSystem = App.TorpedoSystemProperty_Create("Missle System")

MissleSystem.SetMaxCondition(1000.000000)
MissleSystem.SetCritical(0)
MissleSystem.SetTargetable(1)
MissleSystem.SetPrimary(1)
MissleSystem.SetPosition(-0.125343, 5.523160, -0.423257)
MissleSystem.SetPosition2D(0.000000, 0.000000)
MissleSystem.SetRepairComplexity(1.000000)
MissleSystem.SetDisabledPercentage(0.500000)
MissleSystem.SetRadius(0.250000)
MissleSystem.SetNormalPowerPerSecond(50.000000)
MissleSystem.SetWeaponSystemType(MissleSystem.WST_TORPEDO)
MissleSystem.SetSingleFire(1)
MissleSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MissleSystem.SetFiringChainString(kFiringChainString)
MissleSystem.SetMaxTorpedoes(0, 50)
MissleSystem.SetTorpedoScript(0, "Tactical.Projectiles.GQgun")
MissleSystem.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissleSystem)
#################################################
MissleLauncherPort = App.TorpedoTubeProperty_Create("Missle Launcher Port")

MissleLauncherPort.SetMaxCondition(1000.000000)
MissleLauncherPort.SetCritical(0)
MissleLauncherPort.SetTargetable(1)
MissleLauncherPort.SetPrimary(1)
MissleLauncherPort.SetPosition(-1.046540, 8.124570, 0.075785)
MissleLauncherPort.SetPosition2D(0.000000, 0.000000)
MissleLauncherPort.SetRepairComplexity(1.000000)
MissleLauncherPort.SetDisabledPercentage(0.500000)
MissleLauncherPort.SetRadius(0.250000)
MissleLauncherPort.SetDumbfire(1)
MissleLauncherPort.SetWeaponID(2)
MissleLauncherPort.SetGroups(2)
MissleLauncherPort.SetDamageRadiusFactor(0.600000)
MissleLauncherPort.SetIconNum(370)
MissleLauncherPort.SetIconPositionX(69.000000)
MissleLauncherPort.SetIconPositionY(39.000000)
MissleLauncherPort.SetIconAboveShip(1)
MissleLauncherPort.SetImmediateDelay(0.250000)
MissleLauncherPort.SetReloadDelay(10.000000)
MissleLauncherPort.SetMaxReady(1)
MissleLauncherPortDirection = App.TGPoint3()
MissleLauncherPortDirection.SetXYZ(0.000000, 1.000000, 0.000000)
MissleLauncherPort.SetDirection(MissleLauncherPortDirection)
MissleLauncherPortRight = App.TGPoint3()
MissleLauncherPortRight.SetXYZ(1.000000, 0.000000, 0.000000)
MissleLauncherPort.SetRight(MissleLauncherPortRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissleLauncherPort)
#################################################
Misslaunstar = App.TorpedoTubeProperty_Create("Miss laun star")

Misslaunstar.SetMaxCondition(1000.000000)
Misslaunstar.SetCritical(0)
Misslaunstar.SetTargetable(1)
Misslaunstar.SetPrimary(1)
Misslaunstar.SetPosition(0.928224, 8.127020, 0.124990)
Misslaunstar.SetPosition2D(0.000000, 0.000000)
Misslaunstar.SetRepairComplexity(1.000000)
Misslaunstar.SetDisabledPercentage(0.500000)
Misslaunstar.SetRadius(0.250000)
Misslaunstar.SetDumbfire(1)
Misslaunstar.SetWeaponID(2)
Misslaunstar.SetGroups(2)
Misslaunstar.SetDamageRadiusFactor(0.600000)
Misslaunstar.SetIconNum(370)
Misslaunstar.SetIconPositionX(88.000000)
Misslaunstar.SetIconPositionY(39.000000)
Misslaunstar.SetIconAboveShip(1)
Misslaunstar.SetImmediateDelay(0.250000)
Misslaunstar.SetReloadDelay(10.000000)
Misslaunstar.SetMaxReady(1)
MisslaunstarDirection = App.TGPoint3()
MisslaunstarDirection.SetXYZ(0.000000, 1.000000, 0.000000)
Misslaunstar.SetDirection(MisslaunstarDirection)
MisslaunstarRight = App.TGPoint3()
MisslaunstarRight.SetXYZ(1.000000, 0.000000, 0.000000)
Misslaunstar.SetRight(MisslaunstarRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(Misslaunstar)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Main Reactor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Jumpspace Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main SubJump ENGINES", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bott port eng", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bott star eng", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bott port gl", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bott star gl", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ThNor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missle System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missle Launcher Port", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Miss laun star", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
