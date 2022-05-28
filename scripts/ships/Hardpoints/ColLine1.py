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
SublightSys = App.ImpulseEngineProperty_Create("Sublight Sys")

SublightSys.SetMaxCondition(200.000000)
SublightSys.SetCritical(0)
SublightSys.SetTargetable(0)
SublightSys.SetPrimary(1)
SublightSys.SetPosition(0.000000, 0.000000, 0.000000)
SublightSys.SetPosition2D(0.000000, 0.000000)
SublightSys.SetRepairComplexity(2.000000)
SublightSys.SetDisabledPercentage(0.500000)
SublightSys.SetRadius(0.250000)
SublightSys.SetNormalPowerPerSecond(100.000000)
SublightSys.SetMaxAccel(0.400000)
SublightSys.SetMaxAngularAccel(0.010000)
SublightSys.SetMaxAngularVelocity(0.050000)
SublightSys.SetMaxSpeed(3.000000)
SublightSys.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightSys)
#################################################
PowerCore = App.PowerProperty_Create("Power Core")

PowerCore.SetMaxCondition(320.000000)
PowerCore.SetCritical(1)
PowerCore.SetTargetable(1)
PowerCore.SetPrimary(1)
PowerCore.SetPosition(0.000000, -1.000000, 0.000000)
PowerCore.SetPosition2D(64.000000, 75.000000)
PowerCore.SetRepairComplexity(2.000000)
PowerCore.SetDisabledPercentage(0.750000)
PowerCore.SetRadius(0.450000)
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

SensorArray.SetMaxCondition(250.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 1.600000, -0.050000)
SensorArray.SetPosition2D(64.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.250000)
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
PortSublight = App.EngineProperty_Create("Port Sublight")

PortSublight.SetMaxCondition(100.000000)
PortSublight.SetCritical(0)
PortSublight.SetTargetable(1)
PortSublight.SetPrimary(1)
PortSublight.SetPosition(-0.185000, -1.900000, -0.012500)
PortSublight.SetPosition2D(55.000000, 80.000000)
PortSublight.SetRepairComplexity(2.000000)
PortSublight.SetDisabledPercentage(0.500000)
PortSublight.SetRadius(0.250000)
PortSublight.SetEngineType(PortSublight.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortSublight)
#################################################
StarSublight = App.EngineProperty_Create("Star Sublight")

StarSublight.SetMaxCondition(100.000000)
StarSublight.SetCritical(0)
StarSublight.SetTargetable(1)
StarSublight.SetPrimary(1)
StarSublight.SetPosition(0.185000, -1.900000, -0.012500)
StarSublight.SetPosition2D(75.000000, 80.000000)
StarSublight.SetRepairComplexity(2.000000)
StarSublight.SetDisabledPercentage(0.500000)
StarSublight.SetRadius(0.250000)
StarSublight.SetEngineType(StarSublight.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarSublight)
#################################################
FTLCoil = App.EngineProperty_Create("FTL Coil")

FTLCoil.SetMaxCondition(220.000000)
FTLCoil.SetCritical(0)
FTLCoil.SetTargetable(1)
FTLCoil.SetPrimary(1)
FTLCoil.SetPosition(0.000000, -1.600000, 0.107500)
FTLCoil.SetPosition2D(64.000000, 100.000000)
FTLCoil.SetRepairComplexity(3.000000)
FTLCoil.SetDisabledPercentage(0.750000)
FTLCoil.SetRadius(0.500000)
FTLCoil.SetEngineType(FTLCoil.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLCoil)
#################################################
Liner = App.ShipProperty_Create("Liner")

Liner.SetGenus(1)
Liner.SetSpecies(108)
Liner.SetMass(80.000000)
Liner.SetRotationalInertia(10000.000000)
Liner.SetShipName("Gemon Liner")
Liner.SetModelFilename("data/Models/Ships/ColLiners/ColLine1.nif")
Liner.SetDamageResolution(10.000000)
Liner.SetAffiliation(0)
Liner.SetStationary(0)
Liner.SetAIString("NonFedAttack")
Liner.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Liner)
#################################################
CentreSublight = App.EngineProperty_Create("Centre Sublight")

CentreSublight.SetMaxCondition(100.000000)
CentreSublight.SetCritical(0)
CentreSublight.SetTargetable(1)
CentreSublight.SetPrimary(1)
CentreSublight.SetPosition(0.000000, -1.650000, 0.010000)
CentreSublight.SetPosition2D(65.000000, 80.000000)
CentreSublight.SetRepairComplexity(2.000000)
CentreSublight.SetDisabledPercentage(0.500000)
CentreSublight.SetRadius(0.250000)
CentreSublight.SetEngineType(CentreSublight.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(CentreSublight)

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
	prop = App.g_kModelPropertyManager.FindByName("Port Sublight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Sublight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Coil", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Liner", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Centre Sublight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
