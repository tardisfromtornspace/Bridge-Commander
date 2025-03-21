#####  Created by:
#####  Bridge Commander Universal Tool



import App
import GlobalPropertyTemplates

# Local Templates
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(400.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SubLightSys = App.ImpulseEngineProperty_Create("Sub Light Sys")

SubLightSys.SetMaxCondition(200.000000)
SubLightSys.SetCritical(0)
SubLightSys.SetTargetable(0)
SubLightSys.SetPrimary(1)
SubLightSys.SetPosition(0.000000, 0.000000, 0.000000)
SubLightSys.SetPosition2D(0.000000, 0.000000)
SubLightSys.SetRepairComplexity(2.000000)
SubLightSys.SetDisabledPercentage(0.500000)
SubLightSys.SetRadius(0.250000)
SubLightSys.SetNormalPowerPerSecond(100.000000)
SubLightSys.SetMaxAccel(0.400000)
SubLightSys.SetMaxAngularAccel(0.010000)
SubLightSys.SetMaxAngularVelocity(0.050000)
SubLightSys.SetMaxSpeed(3.000000)
SubLightSys.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SubLightSys)
#################################################
PowerCore = App.PowerProperty_Create("Power Core")

PowerCore.SetMaxCondition(420.000000)
PowerCore.SetCritical(1)
PowerCore.SetTargetable(1)
PowerCore.SetPrimary(1)
PowerCore.SetPosition(0.000000, -1.000000, 0.000000)
PowerCore.SetPosition2D(64.000000, 75.000000)
PowerCore.SetRepairComplexity(2.000000)
PowerCore.SetDisabledPercentage(0.750000)
PowerCore.SetRadius(0.250000)
PowerCore.SetMainBatteryLimit(70000.000000)
PowerCore.SetBackupBatteryLimit(40000.000000)
PowerCore.SetMainConduitCapacity(650.000000)
PowerCore.SetBackupConduitCapacity(400.000000)
PowerCore.SetPowerOutput(600.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerCore)
#################################################
DamageControl = App.RepairSubsystemProperty_Create("Damage Control")

DamageControl.SetMaxCondition(200.000000)
DamageControl.SetCritical(0)
DamageControl.SetTargetable(0)
DamageControl.SetPrimary(1)
DamageControl.SetPosition(0.000000, 0.000000, 0.000000)
DamageControl.SetPosition2D(0.000000, 0.000000)
DamageControl.SetRepairComplexity(1.000000)
DamageControl.SetDisabledPercentage(0.500000)
DamageControl.SetRadius(0.250000)
DamageControl.SetNormalPowerPerSecond(1.000000)
DamageControl.SetMaxRepairPoints(8.000000)
DamageControl.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(DamageControl)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(300.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.950000, 2.000000, -0.100000)
SensorArray.SetPosition2D(64.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.250000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(2000.000000)
SensorArray.SetMaxProbes(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(240.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(64.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.250000)
ShieldGenerator.SetNormalPowerPerSecond(0.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
FTLDrive = App.WarpEngineProperty_Create("FTL Drive")

FTLDrive.SetMaxCondition(220.000000)
FTLDrive.SetCritical(0)
FTLDrive.SetTargetable(0)
FTLDrive.SetPrimary(1)
FTLDrive.SetPosition(0.000000, 0.000000, 0.000000)
FTLDrive.SetPosition2D(0.000000, 0.000000)
FTLDrive.SetRepairComplexity(1.000000)
FTLDrive.SetDisabledPercentage(0.500000)
FTLDrive.SetRadius(0.250000)
FTLDrive.SetNormalPowerPerSecond(50.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLDrive)
#################################################
SubLight2 = App.EngineProperty_Create("Sub Light 2")

SubLight2.SetMaxCondition(320.000000)
SubLight2.SetCritical(0)
SubLight2.SetTargetable(1)
SubLight2.SetPrimary(1)
SubLight2.SetPosition(-0.035000, -5.500000, 0.200000)
SubLight2.SetPosition2D(54.000000, 80.000000)
SubLight2.SetRepairComplexity(2.000000)
SubLight2.SetDisabledPercentage(0.500000)
SubLight2.SetRadius(0.250000)
SubLight2.SetEngineType(SubLight2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SubLight2)
#################################################
SubLight1 = App.EngineProperty_Create("Sub Light 1")

SubLight1.SetMaxCondition(320.000000)
SubLight1.SetCritical(0)
SubLight1.SetTargetable(1)
SubLight1.SetPrimary(1)
SubLight1.SetPosition(-0.590000, -5.500000, 0.030000)
SubLight1.SetPosition2D(75.000000, 80.000000)
SubLight1.SetRepairComplexity(2.000000)
SubLight1.SetDisabledPercentage(0.500000)
SubLight1.SetRadius(0.250000)
SubLight1.SetEngineType(SubLight1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SubLight1)
#################################################
FTLCoils = App.EngineProperty_Create("FTL Coils")

FTLCoils.SetMaxCondition(320.000000)
FTLCoils.SetCritical(0)
FTLCoils.SetTargetable(1)
FTLCoils.SetPrimary(1)
FTLCoils.SetPosition(-0.025000, -2.500000, 0.000000)
FTLCoils.SetPosition2D(64.000000, 100.000000)
FTLCoils.SetRepairComplexity(3.000000)
FTLCoils.SetDisabledPercentage(0.750000)
FTLCoils.SetRadius(0.250000)
FTLCoils.SetEngineType(FTLCoils.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLCoils)
#################################################
CloudNine = App.ShipProperty_Create("CloudNine")

CloudNine.SetGenus(1)
CloudNine.SetSpecies(108)
CloudNine.SetMass(80.000000)
CloudNine.SetRotationalInertia(10000.000000)
CloudNine.SetShipName("Cloud9")
CloudNine.SetModelFilename("data/Models/Ships/Cloud9/Cloud9.nif")
CloudNine.SetDamageResolution(0.001000)
CloudNine.SetAffiliation(0)
CloudNine.SetStationary(0)
CloudNine.SetAIString("NonFedAttack")
CloudNine.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(CloudNine)
#################################################
SubLight3 = App.EngineProperty_Create("Sub Light 3")

SubLight3.SetMaxCondition(320.000000)
SubLight3.SetCritical(0)
SubLight3.SetTargetable(1)
SubLight3.SetPrimary(1)
SubLight3.SetPosition(0.530000, -5.500000, 0.030000)
SubLight3.SetPosition2D(54.000000, 80.000000)
SubLight3.SetRepairComplexity(2.000000)
SubLight3.SetDisabledPercentage(0.500000)
SubLight3.SetRadius(0.250000)
SubLight3.SetEngineType(SubLight3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SubLight3)

# Property Set
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
	prop = App.g_kModelPropertyManager.FindByName("CloudNine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sub Light 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sub Light 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sub Light Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Coils", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Damage Control", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sub Light 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
