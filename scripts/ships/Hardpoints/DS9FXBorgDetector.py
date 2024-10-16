import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(25000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(45.000000, 100.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.150000)
Hull.SetRadius(0.350000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(30000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(-0.100000, 0.000000, 0.300000)
ShieldGenerator.SetPosition2D(64.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.150000)
ShieldGenerator.SetRadius(0.003000)
ShieldGenerator.SetNormalPowerPerSecond(1200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 30000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 30000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 30000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 30000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 30000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 30000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 50.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 50.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 50.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 50.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 50.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 50.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(25000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, -0.010000, 0.000000)
SensorArray.SetPosition2D(52.000000, 100.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.150000)
SensorArray.SetRadius(0.050000)
SensorArray.SetNormalPowerPerSecond(800.000000)
SensorArray.SetBaseSensorRange(2000.000000)
SensorArray.SetMaxProbes(50)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
CoriticallNode = App.PowerProperty_Create("Coriticall Node")

CoriticallNode.SetMaxCondition(30000.000000)
CoriticallNode.SetCritical(1)
CoriticallNode.SetTargetable(1)
CoriticallNode.SetPrimary(1)
CoriticallNode.SetPosition(0.000000, -0.520000, 0.000000)
CoriticallNode.SetPosition2D(43.000000, 90.000000)
CoriticallNode.SetRepairComplexity(1.000000)
CoriticallNode.SetDisabledPercentage(0.100000)
CoriticallNode.SetRadius(0.150000)
CoriticallNode.SetMainBatteryLimit(600000.000000)
CoriticallNode.SetBackupBatteryLimit(600000.000000)
CoriticallNode.SetMainConduitCapacity(6875.000000)
CoriticallNode.SetBackupConduitCapacity(1000.000000)
CoriticallNode.SetPowerOutput(5875.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CoriticallNode)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(6000.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(-0.100000, -0.100000, 0.000000)
Phasers.SetPosition2D(0.000000, 0.000000)
Phasers.SetRepairComplexity(1.000000)
Phasers.SetDisabledPercentage(0.150000)
Phasers.SetRadius(0.050000)
Phasers.SetNormalPowerPerSecond(300.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(0)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
BorgTorpedoes = App.WeaponSystemProperty_Create("Borg Torpedoes")

BorgTorpedoes.SetMaxCondition(20000.000000)
BorgTorpedoes.SetCritical(0)
BorgTorpedoes.SetTargetable(0)
BorgTorpedoes.SetPrimary(1)
BorgTorpedoes.SetPosition(0.000000, 0.000000, 0.000000)
BorgTorpedoes.SetPosition2D(0.000000, 0.000000)
BorgTorpedoes.SetRepairComplexity(1.000000)
BorgTorpedoes.SetDisabledPercentage(0.150000)
BorgTorpedoes.SetRadius(0.250000)
BorgTorpedoes.SetNormalPowerPerSecond(500.000000)
BorgTorpedoes.SetWeaponSystemType(BorgTorpedoes.WST_PULSE)
BorgTorpedoes.SetSingleFire(1)
BorgTorpedoes.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
BorgTorpedoes.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(BorgTorpedoes)
#################################################
RawMaterialStorage = App.RepairSubsystemProperty_Create("Raw Material Storage")

RawMaterialStorage.SetMaxCondition(20000.000000)
RawMaterialStorage.SetCritical(0)
RawMaterialStorage.SetTargetable(1)
RawMaterialStorage.SetPrimary(1)
RawMaterialStorage.SetPosition(-0.300000, 0.000000, 0.000000)
RawMaterialStorage.SetPosition2D(64.000000, 70.000000)
RawMaterialStorage.SetRepairComplexity(1.000000)
RawMaterialStorage.SetDisabledPercentage(0.150000)
RawMaterialStorage.SetRadius(0.100000)
RawMaterialStorage.SetNormalPowerPerSecond(30.000000)
RawMaterialStorage.SetMaxRepairPoints(550.000000)
RawMaterialStorage.SetNumRepairTeams(9)
App.g_kModelPropertyManager.RegisterLocalTemplate(RawMaterialStorage)
#################################################
BorgDetector = App.ShipProperty_Create("BorgDetector")

BorgDetector.SetGenus(1)
BorgDetector.SetSpecies(703)
BorgDetector.SetMass(190.000000)
BorgDetector.SetRotationalInertia(9000.000000)
BorgDetector.SetShipName("BorgDetector")
BorgDetector.SetModelFilename("data/Models/Ships/DS9FX/BorgDetector.nif")
BorgDetector.SetDamageResolution(10.000000)
BorgDetector.SetAffiliation(0)
BorgDetector.SetStationary(0)
BorgDetector.SetAIString("BorgAttack")
BorgDetector.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(BorgDetector)
#################################################
TorpedoT1 = App.PulseWeaponProperty_Create("Torpedo T 1")

TorpedoT1.SetMaxCondition(10000.000000)
TorpedoT1.SetCritical(0)
TorpedoT1.SetTargetable(1)
TorpedoT1.SetPrimary(1)
TorpedoT1.SetPosition(-0.360000, 0.570000, 0.000000)
TorpedoT1.SetPosition2D(32.000000, 100.000000)
TorpedoT1.SetRepairComplexity(1.000000)
TorpedoT1.SetDisabledPercentage(0.500000)
TorpedoT1.SetRadius(1.000000)
TorpedoT1.SetDumbfire(1)
TorpedoT1.SetWeaponID(0)
TorpedoT1.SetGroups(0)
TorpedoT1.SetDamageRadiusFactor(0.999999)
TorpedoT1.SetIconNum(370)
TorpedoT1.SetIconPositionX(20.000000)
TorpedoT1.SetIconPositionY(40.000000)
TorpedoT1.SetIconAboveShip(1)
TorpedoT1.SetFireSound("")
TorpedoT1.SetMaxCharge(6.000000)
TorpedoT1.SetMaxDamage(100.000000)
TorpedoT1.SetMaxDamageDistance(100.000000)
TorpedoT1.SetMinFiringCharge(6.000000)
TorpedoT1.SetNormalDischargeRate(1.000000)
TorpedoT1.SetRechargeRate(0.120000)
TorpedoT1.SetIndicatorIconNum(370)
TorpedoT1.SetIndicatorIconPositionX(0.000000)
TorpedoT1.SetIndicatorIconPositionY(5.000000)
TorpedoT1Forward = App.TGPoint3()
TorpedoT1Forward.SetXYZ(0.258799, 0.965931, 0.000000)
TorpedoT1Up = App.TGPoint3()
TorpedoT1Up.SetXYZ(0.000000, 0.000000, 1.000000)
TorpedoT1.SetOrientation(TorpedoT1Forward, TorpedoT1Up)
TorpedoT1.SetArcWidthAngles(-0.959931, 0.959931)
TorpedoT1.SetArcHeightAngles(-0.959931, 0.959931)
TorpedoT1.SetCooldownTime(0.600000)
TorpedoT1.SetModuleName("Tactical.Projectiles.DGDiamondTorp")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoT1)
#################################################
TorpedoT2 = App.PulseWeaponProperty_Create("Torpedo T 2")

TorpedoT2.SetMaxCondition(10000.000000)
TorpedoT2.SetCritical(0)
TorpedoT2.SetTargetable(1)
TorpedoT2.SetPrimary(1)
TorpedoT2.SetPosition(-0.400000, 0.540000, -0.400000)
TorpedoT2.SetPosition2D(32.000000, 100.000000)
TorpedoT2.SetRepairComplexity(1.000000)
TorpedoT2.SetDisabledPercentage(0.500000)
TorpedoT2.SetRadius(1.000000)
TorpedoT2.SetDumbfire(1)
TorpedoT2.SetWeaponID(0)
TorpedoT2.SetGroups(0)
TorpedoT2.SetDamageRadiusFactor(0.999999)
TorpedoT2.SetIconNum(370)
TorpedoT2.SetIconPositionX(40.000000)
TorpedoT2.SetIconPositionY(40.000000)
TorpedoT2.SetIconAboveShip(1)
TorpedoT2.SetFireSound("")
TorpedoT2.SetMaxCharge(6.000000)
TorpedoT2.SetMaxDamage(100.000000)
TorpedoT2.SetMaxDamageDistance(100.000000)
TorpedoT2.SetMinFiringCharge(6.000000)
TorpedoT2.SetNormalDischargeRate(1.000000)
TorpedoT2.SetRechargeRate(0.120000)
TorpedoT2.SetIndicatorIconNum(370)
TorpedoT2.SetIndicatorIconPositionX(0.000000)
TorpedoT2.SetIndicatorIconPositionY(5.000000)
TorpedoT2Forward = App.TGPoint3()
TorpedoT2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
TorpedoT2Up = App.TGPoint3()
TorpedoT2Up.SetXYZ(0.000000, 0.000000, 1.000000)
TorpedoT2.SetOrientation(TorpedoT2Forward, TorpedoT2Up)
TorpedoT2.SetArcWidthAngles(-0.610865, 0.959931)
TorpedoT2.SetArcHeightAngles(-0.959931, 0.959931)
TorpedoT2.SetCooldownTime(0.600000)
TorpedoT2.SetModuleName("Tactical.Projectiles.DGDiamondTorp")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoT2)
#################################################
TorpedoT3 = App.PulseWeaponProperty_Create("Torpedo T 3")

TorpedoT3.SetMaxCondition(10000.000000)
TorpedoT3.SetCritical(0)
TorpedoT3.SetTargetable(1)
TorpedoT3.SetPrimary(1)
TorpedoT3.SetPosition(0.360000, 0.530000, 0.200000)
TorpedoT3.SetPosition2D(81.000000, 80.000000)
TorpedoT3.SetRepairComplexity(1.000000)
TorpedoT3.SetDisabledPercentage(0.500000)
TorpedoT3.SetRadius(1.000000)
TorpedoT3.SetDumbfire(1)
TorpedoT3.SetWeaponID(0)
TorpedoT3.SetGroups(0)
TorpedoT3.SetDamageRadiusFactor(0.999999)
TorpedoT3.SetIconNum(370)
TorpedoT3.SetIconPositionX(60.000000)
TorpedoT3.SetIconPositionY(40.000000)
TorpedoT3.SetIconAboveShip(1)
TorpedoT3.SetFireSound("")
TorpedoT3.SetMaxCharge(6.000000)
TorpedoT3.SetMaxDamage(100.000000)
TorpedoT3.SetMaxDamageDistance(100.000000)
TorpedoT3.SetMinFiringCharge(6.000000)
TorpedoT3.SetNormalDischargeRate(1.000000)
TorpedoT3.SetRechargeRate(0.120000)
TorpedoT3.SetIndicatorIconNum(370)
TorpedoT3.SetIndicatorIconPositionX(0.000000)
TorpedoT3.SetIndicatorIconPositionY(5.000000)
TorpedoT3Forward = App.TGPoint3()
TorpedoT3Forward.SetXYZ(0.000000, 1.000000, 0.000000)
TorpedoT3Up = App.TGPoint3()
TorpedoT3Up.SetXYZ(0.000000, 0.000000, 1.000000)
TorpedoT3.SetOrientation(TorpedoT3Forward, TorpedoT3Up)
TorpedoT3.SetArcWidthAngles(-0.959931, 0.959931)
TorpedoT3.SetArcHeightAngles(-0.959931, 0.959931)
TorpedoT3.SetCooldownTime(0.600000)
TorpedoT3.SetModuleName("Tactical.Projectiles.DGDiamondTorp")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoT3)
#################################################
BorgImpulse1 = App.EngineProperty_Create("Borg Impulse 1")

BorgImpulse1.SetMaxCondition(4800.000000)
BorgImpulse1.SetCritical(0)
BorgImpulse1.SetTargetable(1)
BorgImpulse1.SetPrimary(1)
BorgImpulse1.SetPosition(0.380000, 0.000000, 0.000000)
BorgImpulse1.SetPosition2D(0.000000, 0.000000)
BorgImpulse1.SetRepairComplexity(3.000000)
BorgImpulse1.SetDisabledPercentage(0.500000)
BorgImpulse1.SetRadius(0.006000)
BorgImpulse1.SetEngineType(BorgImpulse1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(BorgImpulse1)
#################################################
Impulse = App.ImpulseEngineProperty_Create("Impulse")

Impulse.SetMaxCondition(10000.000000)
Impulse.SetCritical(0)
Impulse.SetTargetable(0)
Impulse.SetPrimary(1)
Impulse.SetPosition(0.000000, 0.000000, 0.000000)
Impulse.SetPosition2D(0.000000, 0.000000)
Impulse.SetRepairComplexity(1.000000)
Impulse.SetDisabledPercentage(0.250000)
Impulse.SetRadius(0.250000)
Impulse.SetNormalPowerPerSecond(300.000000)
Impulse.SetMaxAccel(5.900000)
Impulse.SetMaxAngularAccel(1.500000)
Impulse.SetMaxAngularVelocity(1.500000)
Impulse.SetMaxSpeed(9.990000)
Impulse.SetEngineSound("borgengine")
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse)
#################################################
BorgImpulse2 = App.EngineProperty_Create("Borg Impulse 2")

BorgImpulse2.SetMaxCondition(4800.000000)
BorgImpulse2.SetCritical(0)
BorgImpulse2.SetTargetable(1)
BorgImpulse2.SetPrimary(1)
BorgImpulse2.SetPosition(-0.400000, -0.400000, 0.000000)
BorgImpulse2.SetPosition2D(0.000000, 0.000000)
BorgImpulse2.SetRepairComplexity(3.000000)
BorgImpulse2.SetDisabledPercentage(0.500000)
BorgImpulse2.SetRadius(0.000600)
BorgImpulse2.SetEngineType(BorgImpulse2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(BorgImpulse2)
#################################################
TractorBeams = App.WeaponSystemProperty_Create("Tractor Beams")

TractorBeams.SetMaxCondition(6000.000000)
TractorBeams.SetCritical(0)
TractorBeams.SetTargetable(1)
TractorBeams.SetPrimary(1)
TractorBeams.SetPosition(0.000000, 0.000000, 0.000000)
TractorBeams.SetPosition2D(0.000000, 0.000000)
TractorBeams.SetRepairComplexity(5.000000)
TractorBeams.SetDisabledPercentage(0.500000)
TractorBeams.SetRadius(0.250000)
TractorBeams.SetNormalPowerPerSecond(900.000000)
TractorBeams.SetWeaponSystemType(TractorBeams.WST_TRACTOR)
TractorBeams.SetSingleFire(1)
TractorBeams.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
TractorBeams.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(TractorBeams)
#################################################
Tractor1 = App.TractorBeamProperty_Create("Tractor 1")

Tractor1.SetMaxCondition(3000.000000)
Tractor1.SetCritical(0)
Tractor1.SetTargetable(1)
Tractor1.SetPrimary(1)
Tractor1.SetPosition(0.360000, 0.499000, -0.030000)
Tractor1.SetPosition2D(71.000000, 13.000000)
Tractor1.SetRepairComplexity(4.000000)
Tractor1.SetDisabledPercentage(0.500000)
Tractor1.SetRadius(0.250000)
Tractor1.SetDumbfire(0)
Tractor1.SetWeaponID(0)
Tractor1.SetGroups(0)
Tractor1.SetDamageRadiusFactor(0.999999)
Tractor1.SetIconNum(0)
Tractor1.SetIconPositionX(79.000000)
Tractor1.SetIconPositionY(35.000000)
Tractor1.SetIconAboveShip(1)
Tractor1.SetFireSound("UCB")
Tractor1.SetMaxCharge(2.000000)
Tractor1.SetMaxDamage(250.000000)
Tractor1.SetMaxDamageDistance(50.000000)
Tractor1.SetMinFiringCharge(2.000000)
Tractor1.SetNormalDischargeRate(1.000000)
Tractor1.SetRechargeRate(0.100000)
Tractor1.SetIndicatorIconNum(0)
Tractor1.SetIndicatorIconPositionX(0.000000)
Tractor1.SetIndicatorIconPositionY(0.000000)
Tractor1Forward = App.TGPoint3()
Tractor1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Tractor1Up = App.TGPoint3()
Tractor1Up.SetXYZ(0.000000, 0.000000, 1.000000)
Tractor1.SetOrientation(Tractor1Forward, Tractor1Up)
Tractor1.SetArcWidthAngles(-0.872665, 0.872665)
Tractor1.SetArcHeightAngles(-0.872665, 0.872665)
Tractor1.SetTractorBeamWidth(0.300000)
Tractor1.SetTextureStart(0)
Tractor1.SetTextureEnd(0)
Tractor1.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.501961, 1.000000, 0.000000, 1.000000)
Tractor1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
Tractor1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.501961, 1.000000)
Tractor1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.000000, 1.000000)
Tractor1.SetInnerCoreColor(kColor)
Tractor1.SetNumSides(12)
Tractor1.SetMainRadius(1.000000)
Tractor1.SetTaperRadius(0.050000)
Tractor1.SetCoreScale(0.250000)
Tractor1.SetTaperRatio(0.900000)
Tractor1.SetTaperMinLength(100.000000)
Tractor1.SetTaperMaxLength(400.000000)
Tractor1.SetLengthTextureTilePerUnit(0.250000)
Tractor1.SetPerimeterTile(1.000000)
Tractor1.SetTextureSpeed(0.500000)
Tractor1.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractor1)
#################################################
Tractor2 = App.TractorBeamProperty_Create("Tractor 2")

Tractor2.SetMaxCondition(3000.000000)
Tractor2.SetCritical(0)
Tractor2.SetTargetable(1)
Tractor2.SetPrimary(1)
Tractor2.SetPosition(-0.360000, 0.580000, 0.200000)
Tractor2.SetPosition2D(0.000000, 0.000000)
Tractor2.SetRepairComplexity(4.000000)
Tractor2.SetDisabledPercentage(0.500000)
Tractor2.SetRadius(0.250000)
Tractor2.SetDumbfire(0)
Tractor2.SetWeaponID(0)
Tractor2.SetGroups(0)
Tractor2.SetDamageRadiusFactor(0.999999)
Tractor2.SetIconNum(0)
Tractor2.SetIconPositionX(0.000000)
Tractor2.SetIconPositionY(0.000000)
Tractor2.SetIconAboveShip(1)
Tractor2.SetFireSound("UCB")
Tractor2.SetMaxCharge(2.000000)
Tractor2.SetMaxDamage(250.000000)
Tractor2.SetMaxDamageDistance(50.000000)
Tractor2.SetMinFiringCharge(2.000000)
Tractor2.SetNormalDischargeRate(1.000000)
Tractor2.SetRechargeRate(0.100000)
Tractor2.SetIndicatorIconNum(0)
Tractor2.SetIndicatorIconPositionX(0.000000)
Tractor2.SetIndicatorIconPositionY(0.000000)
Tractor2Forward = App.TGPoint3()
Tractor2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Tractor2Up = App.TGPoint3()
Tractor2Up.SetXYZ(0.000000, 0.000000, 1.000000)
Tractor2.SetOrientation(Tractor2Forward, Tractor2Up)
Tractor2.SetArcWidthAngles(-0.872665, 0.872665)
Tractor2.SetArcHeightAngles(-0.872665, 0.872665)
Tractor2.SetTractorBeamWidth(0.300000)
Tractor2.SetTextureStart(0)
Tractor2.SetTextureEnd(0)
Tractor2.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 1.000000, 0.501961, 1.000000)
Tractor2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
Tractor2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 0.000000, 1.000000)
Tractor2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.247059, 1.000000)
Tractor2.SetInnerCoreColor(kColor)
Tractor2.SetNumSides(12)
Tractor2.SetMainRadius(1.000000)
Tractor2.SetTaperRadius(0.050000)
Tractor2.SetCoreScale(0.250000)
Tractor2.SetTaperRatio(1.900000)
Tractor2.SetTaperMinLength(100.000000)
Tractor2.SetTaperMaxLength(400.000000)
Tractor2.SetLengthTextureTilePerUnit(0.250000)
Tractor2.SetPerimeterTile(1.000000)
Tractor2.SetTextureSpeed(0.500000)
Tractor2.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractor2)
#################################################
Tractor3 = App.TractorBeamProperty_Create("Tractor 3")

Tractor3.SetMaxCondition(3000.000000)
Tractor3.SetCritical(0)
Tractor3.SetTargetable(1)
Tractor3.SetPrimary(1)
Tractor3.SetPosition(0.360000, 0.480000, -0.400000)
Tractor3.SetPosition2D(52.000000, 100.000000)
Tractor3.SetRepairComplexity(4.000000)
Tractor3.SetDisabledPercentage(0.500000)
Tractor3.SetRadius(0.250000)
Tractor3.SetDumbfire(0)
Tractor3.SetWeaponID(0)
Tractor3.SetGroups(0)
Tractor3.SetDamageRadiusFactor(0.999999)
Tractor3.SetIconNum(0)
Tractor3.SetIconPositionX(0.000000)
Tractor3.SetIconPositionY(0.000000)
Tractor3.SetIconAboveShip(1)
Tractor3.SetFireSound("UCB")
Tractor3.SetMaxCharge(2.000000)
Tractor3.SetMaxDamage(250.000000)
Tractor3.SetMaxDamageDistance(40.000000)
Tractor3.SetMinFiringCharge(2.000000)
Tractor3.SetNormalDischargeRate(1.000000)
Tractor3.SetRechargeRate(0.100000)
Tractor3.SetIndicatorIconNum(0)
Tractor3.SetIndicatorIconPositionX(0.000000)
Tractor3.SetIndicatorIconPositionY(0.000000)
Tractor3Forward = App.TGPoint3()
Tractor3Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Tractor3Up = App.TGPoint3()
Tractor3Up.SetXYZ(0.000000, 0.000000, 1.000000)
Tractor3.SetOrientation(Tractor3Forward, Tractor3Up)
Tractor3.SetArcWidthAngles(-0.872665, 0.872665)
Tractor3.SetArcHeightAngles(-0.872665, 0.872665)
Tractor3.SetTractorBeamWidth(0.600000)
Tractor3.SetTextureStart(0)
Tractor3.SetTextureEnd(0)
Tractor3.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
Tractor3.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.247059, 1.000000)
Tractor3.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.501961, 1.000000)
Tractor3.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.247059, 0.501961, 0.501961, 1.000000)
Tractor3.SetInnerCoreColor(kColor)
Tractor3.SetNumSides(12)
Tractor3.SetMainRadius(1.000000)
Tractor3.SetTaperRadius(0.050000)
Tractor3.SetCoreScale(0.250000)
Tractor3.SetTaperRatio(1.900000)
Tractor3.SetTaperMinLength(100.000000)
Tractor3.SetTaperMaxLength(400.000000)
Tractor3.SetLengthTextureTilePerUnit(0.250000)
Tractor3.SetPerimeterTile(1.000000)
Tractor3.SetTextureSpeed(0.500000)
Tractor3.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractor3)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(10000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, 0.000000)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(3.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.100000)
WarpEngines.SetNormalPowerPerSecond(300.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
BorgWarp = App.EngineProperty_Create("Borg Warp")

BorgWarp.SetMaxCondition(5000.000000)
BorgWarp.SetCritical(0)
BorgWarp.SetTargetable(1)
BorgWarp.SetPrimary(1)
BorgWarp.SetPosition(0.400000, 0.000000, 0.000000)
BorgWarp.SetPosition2D(0.000000, 0.000000)
BorgWarp.SetRepairComplexity(3.000000)
BorgWarp.SetDisabledPercentage(0.500000)
BorgWarp.SetRadius(0.250000)
BorgWarp.SetEngineType(BorgWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(BorgWarp)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Coriticall Node", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Raw Material Storage", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BorgDetector", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Borg Impulse 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Borg Impulse 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Borg Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo T 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo T 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo T 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractor Beams", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractor 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractor 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractor 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Borg Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
