#####  Created by:
#####  Bridge Commander Universal Tool



import App
import GlobalPropertyTemplates

# Local Templates
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(600.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SublightSys = App.ImpulseEngineProperty_Create("Sublight Sys")

SublightSys.SetMaxCondition(200.000000)
SublightSys.SetCritical(0)
SublightSys.SetTargetable(0)
SublightSys.SetPrimary(1)
SublightSys.SetPosition(0.000000, -0.138200, 0.000000)
SublightSys.SetPosition2D(0.000000, 0.000000)
SublightSys.SetRepairComplexity(2.000000)
SublightSys.SetDisabledPercentage(0.500000)
SublightSys.SetRadius(0.250000)
SublightSys.SetNormalPowerPerSecond(100.000000)
SublightSys.SetMaxAccel(0.400000)
SublightSys.SetMaxAngularAccel(0.100000)
SublightSys.SetMaxAngularVelocity(0.250000)
SublightSys.SetMaxSpeed(3.000000)
SublightSys.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightSys)
#################################################
PowerCore = App.PowerProperty_Create("Power Core")

PowerCore.SetMaxCondition(120.000000)
PowerCore.SetCritical(1)
PowerCore.SetTargetable(1)
PowerCore.SetPrimary(1)
PowerCore.SetPosition(0.000000, 0.350000, 0.000000)
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
DamageControl.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(DamageControl)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(100.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.867500, 0.125000)
SensorArray.SetPosition2D(64.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(10.250000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(2000.000000)
SensorArray.SetMaxProbes(1)
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
ShieldGenerator.SetShieldGlowDecay(1.000000)
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
Sublight1 = App.EngineProperty_Create("Sublight 1")

Sublight1.SetMaxCondition(500.000000)
Sublight1.SetCritical(0)
Sublight1.SetTargetable(1)
Sublight1.SetPrimary(0)
Sublight1.SetPosition(-0.225000, -0.575000, 0.110000)
Sublight1.SetPosition2D(54.000000, 80.000000)
Sublight1.SetRepairComplexity(2.000000)
Sublight1.SetDisabledPercentage(0.500000)
Sublight1.SetRadius(0.400000)
Sublight1.SetEngineType(Sublight1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sublight1)
#################################################
Sublight2 = App.EngineProperty_Create("Sublight 2")

Sublight2.SetMaxCondition(500.000000)
Sublight2.SetCritical(0)
Sublight2.SetTargetable(1)
Sublight2.SetPrimary(0)
Sublight2.SetPosition(0.225000, -0.575000, 0.110000)
Sublight2.SetPosition2D(75.000000, 80.000000)
Sublight2.SetRepairComplexity(2.000000)
Sublight2.SetDisabledPercentage(0.500000)
Sublight2.SetRadius(0.400000)
Sublight2.SetEngineType(Sublight2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sublight2)
#################################################
FTLCoils = App.EngineProperty_Create("FTL Coils")

FTLCoils.SetMaxCondition(400.000000)
FTLCoils.SetCritical(0)
FTLCoils.SetTargetable(1)
FTLCoils.SetPrimary(1)
FTLCoils.SetPosition(0.000000, -0.750000, 0.000000)
FTLCoils.SetPosition2D(64.000000, 100.000000)
FTLCoils.SetRepairComplexity(3.000000)
FTLCoils.SetDisabledPercentage(0.750000)
FTLCoils.SetRadius(0.250000)
FTLCoils.SetEngineType(FTLCoils.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLCoils)
#################################################
ColonialOne = App.ShipProperty_Create("Colonial One")

ColonialOne.SetGenus(1)
ColonialOne.SetSpecies(108)
ColonialOne.SetMass(80.000000)
ColonialOne.SetRotationalInertia(10000.000000)
ColonialOne.SetShipName("Colonial One")
ColonialOne.SetModelFilename("data/Models/Ships/Col1/Col1.nif")
ColonialOne.SetDamageResolution(0.010000)
ColonialOne.SetAffiliation(0)
ColonialOne.SetStationary(0)
ColonialOne.SetAIString("NonFedAttack")
ColonialOne.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(ColonialOne)
#################################################
Sublight3 = App.EngineProperty_Create("Sublight 3")

Sublight3.SetMaxCondition(500.000000)
Sublight3.SetCritical(0)
Sublight3.SetTargetable(1)
Sublight3.SetPrimary(1)
Sublight3.SetPosition(0.000000, -0.575000, -0.160000)
Sublight3.SetPosition2D(0.000000, 0.000000)
Sublight3.SetRepairComplexity(1.000000)
Sublight3.SetDisabledPercentage(0.500000)
Sublight3.SetRadius(0.250000)
Sublight3.SetEngineType(Sublight3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sublight3)

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
	prop = App.g_kModelPropertyManager.FindByName("Sublight Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Coils", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Damage Control", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Colonial One", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
