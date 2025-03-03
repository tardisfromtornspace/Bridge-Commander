# C:\Utopia\Current\Build\scripts\ships\Hardpoints\sunbuster.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(26000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.300000)
Hull.SetPosition2D(66.000000, 64.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(4.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(6000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(54.000000, 64.000000)
ImpulseEngines.SetRepairComplexity(3.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(100.000000)
ImpulseEngines.SetMaxAccel(0.200000)
ImpulseEngines.SetMaxAngularAccel(0.010000)
ImpulseEngines.SetMaxAngularVelocity(0.150000)
ImpulseEngines.SetMaxSpeed(3.000000)
ImpulseEngines.SetEngineSound("Kessok Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(6000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.420000, -1.200000)
WarpCore.SetPosition2D(78.000000, 64.000000)
WarpCore.SetRepairComplexity(4.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(1.500000)
WarpCore.SetMainBatteryLimit(200000.000000)
WarpCore.SetBackupBatteryLimit(50000.000000)
WarpCore.SetMainConduitCapacity(1550.000000)
WarpCore.SetBackupConduitCapacity(100.000000)
WarpCore.SetPowerOutput(1500.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(3000.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(1)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(1.400000, -0.420000, 1.200000)
RepairSystem.SetPosition2D(54.000000, 64.000000)
RepairSystem.SetRepairComplexity(20.000000)
RepairSystem.SetDisabledPercentage(0.000000)
RepairSystem.SetRadius(1.000000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(15.000000)
RepairSystem.SetNumRepairTeams(6)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(10000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 1.200000, 0.200000)
SensorArray.SetPosition2D(66.000000, 32.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(1.000000)
SensorArray.SetNormalPowerPerSecond(200.000000)
SensorArray.SetBaseSensorRange(2000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(10000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(-1.400000, -0.420000, 1.200000)
ShieldGenerator.SetPosition2D(66.000000, 64.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(1.000000)
ShieldGenerator.SetNormalPowerPerSecond(300.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.294118, 0.184314, 0.811765, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 10000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 8000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 5000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 13.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 13.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 13.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 13.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 13.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 13.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(200.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, 0.000000)
WarpEngines.SetPosition2D(54.000000, 64.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.750000)
WarpEngines.SetRadius(0.250000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Impulse1 = App.EngineProperty_Create("Impulse 1")

Impulse1.SetMaxCondition(2000.000000)
Impulse1.SetCritical(0)
Impulse1.SetTargetable(1)
Impulse1.SetPrimary(1)
Impulse1.SetPosition(3.500000, -0.200000, -1.700000)
Impulse1.SetPosition2D(44.000000, 58.000000)
Impulse1.SetRepairComplexity(2.000000)
Impulse1.SetDisabledPercentage(0.750000)
Impulse1.SetRadius(1.200000)
Impulse1.SetEngineType(Impulse1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse1)
#################################################
Impulse2 = App.EngineProperty_Create("Impulse 2")

Impulse2.SetMaxCondition(2000.000000)
Impulse2.SetCritical(0)
Impulse2.SetTargetable(1)
Impulse2.SetPrimary(1)
Impulse2.SetPosition(-3.500000, -0.200000, -1.700000)
Impulse2.SetPosition2D(66.000000, 48.000000)
Impulse2.SetRepairComplexity(2.000000)
Impulse2.SetDisabledPercentage(0.750000)
Impulse2.SetRadius(1.200000)
Impulse2.SetEngineType(Impulse2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse2)
#################################################
Impulse3 = App.EngineProperty_Create("Impulse 3")

Impulse3.SetMaxCondition(2000.000000)
Impulse3.SetCritical(0)
Impulse3.SetTargetable(1)
Impulse3.SetPrimary(1)
Impulse3.SetPosition(0.000000, -0.200000, 4.200000)
Impulse3.SetPosition2D(88.000000, 58.000000)
Impulse3.SetRepairComplexity(2.000000)
Impulse3.SetDisabledPercentage(0.750000)
Impulse3.SetRadius(1.200000)
Impulse3.SetEngineType(Impulse3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse3)
#################################################
SunBuster = App.ShipProperty_Create("Sun Buster")

SunBuster.SetGenus(1)
SunBuster.SetSpecies(713)
SunBuster.SetMass(800.000000)
SunBuster.SetRotationalInertia(60000.000000)
SunBuster.SetShipName("Device")
SunBuster.SetModelFilename("")
SunBuster.SetDamageResolution(15.000000)
SunBuster.SetAffiliation(0)
SunBuster.SetStationary(0)
SunBuster.SetAIString("NonFedAttack")
SunBuster.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(SunBuster)
#################################################
Warp1 = App.EngineProperty_Create("Warp 1")

Warp1.SetMaxCondition(4000.000000)
Warp1.SetCritical(0)
Warp1.SetTargetable(1)
Warp1.SetPrimary(1)
Warp1.SetPosition(2.000000, -3.300000, -1.000000)
Warp1.SetPosition2D(60.000000, 82.000000)
Warp1.SetRepairComplexity(3.000000)
Warp1.SetDisabledPercentage(0.500000)
Warp1.SetRadius(2.100000)
Warp1.SetEngineType(Warp1.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp1)
#################################################
Warp2 = App.EngineProperty_Create("Warp 2")

Warp2.SetMaxCondition(4000.000000)
Warp2.SetCritical(0)
Warp2.SetTargetable(1)
Warp2.SetPrimary(1)
Warp2.SetPosition(-2.000000, -3.300000, -1.000000)
Warp2.SetPosition2D(66.000000, 82.000000)
Warp2.SetRepairComplexity(3.000000)
Warp2.SetDisabledPercentage(0.500000)
Warp2.SetRadius(2.100000)
Warp2.SetEngineType(Warp2.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp2)
#################################################
Warp3 = App.EngineProperty_Create("Warp 3")

Warp3.SetMaxCondition(4000.000000)
Warp3.SetCritical(0)
Warp3.SetTargetable(1)
Warp3.SetPrimary(1)
Warp3.SetPosition(0.000000, -3.300000, 2.500000)
Warp3.SetPosition2D(72.000000, 82.000000)
Warp3.SetRepairComplexity(3.000000)
Warp3.SetDisabledPercentage(0.500000)
Warp3.SetRadius(2.100000)
Warp3.SetEngineType(Warp3.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp3)
#################################################
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloaking Device")

CloakingDevice.SetMaxCondition(2000.000000)
CloakingDevice.SetCritical(0)
CloakingDevice.SetTargetable(0)
CloakingDevice.SetPrimary(1)
CloakingDevice.SetPosition(0.000000, 0.000000, 0.000000)
CloakingDevice.SetPosition2D(64.000000, 40.000000)
CloakingDevice.SetRepairComplexity(1.000000)
CloakingDevice.SetDisabledPercentage(0.750000)
CloakingDevice.SetRadius(1.000000)
CloakingDevice.SetNormalPowerPerSecond(10.000000)
CloakingDevice.SetCloakStrength(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
#################################################
BeamEmitter = App.WeaponSystemProperty_Create("Beam Emitter")

BeamEmitter.SetMaxCondition(200.000000)
BeamEmitter.SetCritical(0)
BeamEmitter.SetTargetable(0)
BeamEmitter.SetPrimary(1)
BeamEmitter.SetPosition(0.000000, 0.000000, 0.000000)
BeamEmitter.SetPosition2D(64.000000, 120.000000)
BeamEmitter.SetRepairComplexity(4.000000)
BeamEmitter.SetDisabledPercentage(0.750000)
BeamEmitter.SetRadius(0.250000)
BeamEmitter.SetNormalPowerPerSecond(500.000000)
BeamEmitter.SetWeaponSystemType(BeamEmitter.WST_PHASER)
BeamEmitter.SetSingleFire(1)
BeamEmitter.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
BeamEmitter.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(BeamEmitter)
#################################################
Emitter = App.PhaserProperty_Create("Emitter")

Emitter.SetMaxCondition(10000.000000)
Emitter.SetCritical(0)
Emitter.SetTargetable(1)
Emitter.SetPrimary(1)
Emitter.SetPosition(0.000000, -6.700000, 0.300000)
Emitter.SetPosition2D(66.000000, 102.000000)
Emitter.SetRepairComplexity(4.000000)
Emitter.SetDisabledPercentage(0.750000)
Emitter.SetRadius(0.350000)
Emitter.SetDumbfire(0)
Emitter.SetWeaponID(1)
Emitter.SetGroups(0)
Emitter.SetDamageRadiusFactor(0.900000)
Emitter.SetIconNum(370)
Emitter.SetIconPositionX(75.000000)
Emitter.SetIconPositionY(90.000000)
Emitter.SetIconAboveShip(1)
Emitter.SetFireSound("Tractor Beam")
Emitter.SetMaxCharge(5.000000)
Emitter.SetMaxDamage(1900.000000)
Emitter.SetMaxDamageDistance(300.000000)
Emitter.SetMinFiringCharge(3.000000)
Emitter.SetNormalDischargeRate(1.000000)
Emitter.SetRechargeRate(1.100000)
Emitter.SetIndicatorIconNum(370)
Emitter.SetIndicatorIconPositionX(0.000000)
Emitter.SetIndicatorIconPositionY(5.000000)
EmitterForward = App.TGPoint3()
EmitterForward.SetXYZ(0.000000, -1.000000, 0.000000)
EmitterUp = App.TGPoint3()
EmitterUp.SetXYZ(0.000000, 0.000000, 1.000000)
Emitter.SetOrientation(EmitterForward, EmitterUp)
Emitter.SetWidth(0.100000)
Emitter.SetLength(0.100000)
Emitter.SetArcWidthAngles(-0.087266, 0.087266)
Emitter.SetArcHeightAngles(-0.087266, 0.087266)
Emitter.SetPhaserTextureStart(0)
Emitter.SetPhaserTextureEnd(0)
Emitter.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.082353, 0.047059, 0.721569, 1.000000)
Emitter.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.247059, 1.000000)
Emitter.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 0.247059, 0.501961, 1.000000)
Emitter.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.227451, 0.176471, 0.819608, 1.000000)
Emitter.SetInnerCoreColor(kColor)
Emitter.SetNumSides(6)
Emitter.SetMainRadius(0.150000)
Emitter.SetTaperRadius(0.010000)
Emitter.SetCoreScale(0.300000)
Emitter.SetTaperRatio(0.250000)
Emitter.SetTaperMinLength(5.000000)
Emitter.SetTaperMaxLength(30.000000)
Emitter.SetLengthTextureTilePerUnit(0.500000)
Emitter.SetPerimeterTile(1.000000)
Emitter.SetTextureSpeed(2.500000)
Emitter.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Emitter)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sun Buster", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Cloaking Device", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam Emitter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Emitter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
