#####  Created by:
#####  Bridge Commander Universal Tool



import App
import GlobalPropertyTemplates

# Local Templates
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(75.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(5.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SublightSys = App.ImpulseEngineProperty_Create("Sublight Sys")

SublightSys.SetMaxCondition(40.000000)
SublightSys.SetCritical(0)
SublightSys.SetTargetable(0)
SublightSys.SetPrimary(1)
SublightSys.SetPosition(0.000000, 0.000000, 0.000000)
SublightSys.SetPosition2D(0.000000, 0.000000)
SublightSys.SetRepairComplexity(2.000000)
SublightSys.SetDisabledPercentage(0.500000)
SublightSys.SetRadius(0.250000)
SublightSys.SetNormalPowerPerSecond(30.000000)
SublightSys.SetMaxAccel(0.900000)
SublightSys.SetMaxAngularAccel(1.000000)
SublightSys.SetMaxAngularVelocity(1.000000)
SublightSys.SetMaxSpeed(5.000000)
SublightSys.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightSys)
#################################################
PowerCore = App.PowerProperty_Create("Power Core")

PowerCore.SetMaxCondition(120.000000)
PowerCore.SetCritical(1)
PowerCore.SetTargetable(1)
PowerCore.SetPrimary(1)
PowerCore.SetPosition(0.000000, -0.075000, -0.050000)
PowerCore.SetPosition2D(64.000000, 75.000000)
PowerCore.SetRepairComplexity(2.000000)
PowerCore.SetDisabledPercentage(0.750000)
PowerCore.SetRadius(0.450000)
PowerCore.SetMainBatteryLimit(70000.000000)
PowerCore.SetBackupBatteryLimit(40000.000000)
PowerCore.SetMainConduitCapacity(650.000000)
PowerCore.SetBackupConduitCapacity(400.000000)
PowerCore.SetPowerOutput(100.000000)
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
DamageControl.SetRadius(2.500000)
DamageControl.SetNormalPowerPerSecond(1.000000)
DamageControl.SetMaxRepairPoints(0.100000)
DamageControl.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(DamageControl)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(100.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.350000, -0.075000)
SensorArray.SetPosition2D(64.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.500000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(2000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(1.000000)
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

FTLDrive.SetMaxCondition(22.000000)
FTLDrive.SetCritical(0)
FTLDrive.SetTargetable(0)
FTLDrive.SetPrimary(1)
FTLDrive.SetPosition(0.000000, 0.000000, 0.000000)
FTLDrive.SetPosition2D(0.000000, 0.000000)
FTLDrive.SetRepairComplexity(1.000000)
FTLDrive.SetDisabledPercentage(0.500000)
FTLDrive.SetRadius(0.250000)
FTLDrive.SetNormalPowerPerSecond(30.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLDrive)
#################################################
SublightEngine1 = App.EngineProperty_Create("Sublight Engine 1")

SublightEngine1.SetMaxCondition(30.000000)
SublightEngine1.SetCritical(0)
SublightEngine1.SetTargetable(1)
SublightEngine1.SetPrimary(0)
SublightEngine1.SetPosition(-0.087500, -0.350000, 0.037500)
SublightEngine1.SetPosition2D(75.000000, 80.000000)
SublightEngine1.SetRepairComplexity(2.000000)
SublightEngine1.SetDisabledPercentage(0.500000)
SublightEngine1.SetRadius(0.400000)
SublightEngine1.SetEngineType(SublightEngine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngine1)
#################################################
FTLCoil = App.EngineProperty_Create("FTL Coil")

FTLCoil.SetMaxCondition(50.000000)
FTLCoil.SetCritical(0)
FTLCoil.SetTargetable(1)
FTLCoil.SetPrimary(1)
FTLCoil.SetPosition(0.000000, -0.030000, -0.010000)
FTLCoil.SetPosition2D(64.000000, 100.000000)
FTLCoil.SetRepairComplexity(3.000000)
FTLCoil.SetDisabledPercentage(0.750000)
FTLCoil.SetRadius(0.500000)
FTLCoil.SetEngineType(FTLCoil.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLCoil)
#################################################
ColShuttle = App.ShipProperty_Create("ColShuttle")

ColShuttle.SetGenus(1)
ColShuttle.SetSpecies(108)
ColShuttle.SetMass(80.000000)
ColShuttle.SetRotationalInertia(10000.000000)
ColShuttle.SetShipName("ColShuttle")
ColShuttle.SetModelFilename("data/Models/Ships/ColShuttle/ColShuttle.nif")
ColShuttle.SetDamageResolution(0.000100)
ColShuttle.SetAffiliation(0)
ColShuttle.SetStationary(0)
ColShuttle.SetAIString("NonFedAttack")
ColShuttle.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(ColShuttle)
#################################################
SublightEngine2 = App.EngineProperty_Create("Sublight Engine 2")

SublightEngine2.SetMaxCondition(30.000000)
SublightEngine2.SetCritical(0)
SublightEngine2.SetTargetable(1)
SublightEngine2.SetPrimary(0)
SublightEngine2.SetPosition(0.087500, -0.350000, 0.037500)
SublightEngine2.SetPosition2D(75.000000, 80.000000)
SublightEngine2.SetRepairComplexity(2.000000)
SublightEngine2.SetDisabledPercentage(0.500000)
SublightEngine2.SetRadius(0.400000)
SublightEngine2.SetEngineType(SublightEngine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngine2)
#################################################
SublightEngine3 = App.EngineProperty_Create("Sublight Engine 3")

SublightEngine3.SetMaxCondition(30.000000)
SublightEngine3.SetCritical(0)
SublightEngine3.SetTargetable(1)
SublightEngine3.SetPrimary(0)
SublightEngine3.SetPosition(-0.140000, -0.350000, -0.032500)
SublightEngine3.SetPosition2D(75.000000, 80.000000)
SublightEngine3.SetRepairComplexity(2.000000)
SublightEngine3.SetDisabledPercentage(0.500000)
SublightEngine3.SetRadius(0.400000)
SublightEngine3.SetEngineType(SublightEngine3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngine3)
#################################################
SublightEngine4 = App.EngineProperty_Create("Sublight Engine 4")

SublightEngine4.SetMaxCondition(30.000000)
SublightEngine4.SetCritical(0)
SublightEngine4.SetTargetable(1)
SublightEngine4.SetPrimary(0)
SublightEngine4.SetPosition(0.140000, -0.350000, -0.032500)
SublightEngine4.SetPosition2D(75.000000, 80.000000)
SublightEngine4.SetRepairComplexity(2.000000)
SublightEngine4.SetDisabledPercentage(0.500000)
SublightEngine4.SetRadius(0.400000)
SublightEngine4.SetEngineType(SublightEngine4.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngine4)

# Property Set
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Damage Control", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engine 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engine 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Coil", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ColShuttle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
