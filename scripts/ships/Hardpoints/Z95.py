# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\Z95.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Engine1 = App.EngineProperty_Create("Engine 1")

Engine1.SetMaxCondition(12.000000)
Engine1.SetCritical(0)
Engine1.SetTargetable(1)
Engine1.SetPrimary(1)
Engine1.SetPosition(-0.019500, -0.070000, 0.009200)
Engine1.SetPosition2D(49.000000, 96.000000)
Engine1.SetRepairComplexity(1.000000)
Engine1.SetDisabledPercentage(0.500000)
Engine1.SetRadius(0.010000)
Engine1.SetEngineType(Engine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine1)
#################################################
Engine2 = App.EngineProperty_Create("Engine 2")

Engine2.SetMaxCondition(12.000000)
Engine2.SetCritical(0)
Engine2.SetTargetable(1)
Engine2.SetPrimary(1)
Engine2.SetPosition(0.019500, -0.070000, 0.009200)
Engine2.SetPosition2D(80.000000, 96.000000)
Engine2.SetRepairComplexity(1.000000)
Engine2.SetDisabledPercentage(0.500000)
Engine2.SetRadius(0.010000)
Engine2.SetEngineType(Engine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine2)
#################################################
Engine3 = App.EngineProperty_Create("Engine 3")

Engine3.SetMaxCondition(12.000000)
Engine3.SetCritical(0)
Engine3.SetTargetable(1)
Engine3.SetPrimary(1)
Engine3.SetPosition(-0.019500, -0.070000, -0.005900)
Engine3.SetPosition2D(55.000000, 102.000000)
Engine3.SetRepairComplexity(1.000000)
Engine3.SetDisabledPercentage(0.500000)
Engine3.SetRadius(0.010000)
Engine3.SetEngineType(Engine3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine3)
#################################################
Engine4 = App.EngineProperty_Create("Engine 4")

Engine4.SetMaxCondition(12.000000)
Engine4.SetCritical(0)
Engine4.SetTargetable(1)
Engine4.SetPrimary(1)
Engine4.SetPosition(0.019500, -0.070000, -0.005900)
Engine4.SetPosition2D(75.000000, 102.000000)
Engine4.SetRepairComplexity(1.000000)
Engine4.SetDisabledPercentage(0.500000)
Engine4.SetRadius(0.010000)
Engine4.SetEngineType(Engine4.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine4)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(14.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(66.000000, 83.000000)
Hull.SetRepairComplexity(100.000000)
Hull.SetDisabledPercentage(0.750000)
Hull.SetRadius(0.035000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
IonEngines = App.ImpulseEngineProperty_Create("Ion Engines")

IonEngines.SetMaxCondition(6.000000)
IonEngines.SetCritical(0)
IonEngines.SetTargetable(0)
IonEngines.SetPrimary(1)
IonEngines.SetPosition(0.000000, -0.020000, 0.009000)
IonEngines.SetPosition2D(0.000000, 0.000000)
IonEngines.SetRepairComplexity(1.000000)
IonEngines.SetDisabledPercentage(0.500000)
IonEngines.SetRadius(0.006000)
IonEngines.SetNormalPowerPerSecond(5.000000)
IonEngines.SetMaxAccel(3.700000)
IonEngines.SetMaxAngularAccel(2.200000)
IonEngines.SetMaxAngularVelocity(1.700000)
IonEngines.SetMaxSpeed(4.900000)
IonEngines.SetEngineSound("xwingengine")
App.g_kModelPropertyManager.RegisterLocalTemplate(IonEngines)
#################################################
Reactor = App.PowerProperty_Create("Reactor")

Reactor.SetMaxCondition(10.000000)
Reactor.SetCritical(1)
Reactor.SetTargetable(1)
Reactor.SetPrimary(1)
Reactor.SetPosition(0.000000, -0.030000, 0.000000)
Reactor.SetPosition2D(66.000000, 90.000000)
Reactor.SetRepairComplexity(1.000000)
Reactor.SetDisabledPercentage(0.500000)
Reactor.SetRadius(0.005000)
Reactor.SetMainBatteryLimit(150000.000000)
Reactor.SetBackupBatteryLimit(100000.000000)
Reactor.SetMainConduitCapacity(50.000000)
Reactor.SetBackupConduitCapacity(12.000000)
Reactor.SetPowerOutput(60.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Reactor)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(15.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, -0.010000, 0.010000)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.003000)
RepairSystem.SetNormalPowerPerSecond(0.100000)
RepairSystem.SetMaxRepairPoints(10.000000)
RepairSystem.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(6.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.060000, 0.000000)
SensorArray.SetPosition2D(66.000000, 10.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.004000)
SensorArray.SetNormalPowerPerSecond(0.100000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(12.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.018500, 0.010000)
ShieldGenerator.SetPosition2D(66.000000, 74.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.004000)
ShieldGenerator.SetNormalPowerPerSecond(18.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 24.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 21.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 21.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 20.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 20.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 20.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 9.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 9.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 9.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 9.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 8.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Z95 = App.ShipProperty_Create("Z95")

Z95.SetGenus(0)
Z95.SetSpecies(401)
Z95.SetMass(6.100000)
Z95.SetRotationalInertia(2500.000000)
Z95.SetShipName("Z 95")
Z95.SetModelFilename("data/Models/Ships/Z-95.nif")
Z95.SetDamageResolution(4.000000)
Z95.SetAffiliation(0)
Z95.SetStationary(0)
Z95.SetAIString("NonFedAttack")
Z95.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Z95)
#################################################
LaserEmiter = App.WeaponSystemProperty_Create("Laser Emiter")

LaserEmiter.SetMaxCondition(12.000000)
LaserEmiter.SetCritical(0)
LaserEmiter.SetTargetable(0)
LaserEmiter.SetPrimary(1)
LaserEmiter.SetPosition(0.100000, 0.100000, 0.100000)
LaserEmiter.SetPosition2D(0.000000, 0.000000)
LaserEmiter.SetRepairComplexity(6.000000)
LaserEmiter.SetDisabledPercentage(0.750000)
LaserEmiter.SetRadius(0.010000)
LaserEmiter.SetNormalPowerPerSecond(10.000000)
LaserEmiter.SetWeaponSystemType(LaserEmiter.WST_PULSE)
LaserEmiter.SetSingleFire(0)
LaserEmiter.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
LaserEmiter.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(LaserEmiter)
#################################################
Torpedosystem = App.WeaponSystemProperty_Create("Torpedo system")

Torpedosystem.SetMaxCondition(6.000000)
Torpedosystem.SetCritical(0)
Torpedosystem.SetTargetable(1)
Torpedosystem.SetPrimary(1)
Torpedosystem.SetPosition(0.000000, 0.000000, 0.000000)
Torpedosystem.SetPosition2D(0.000000, 0.000000)
Torpedosystem.SetRepairComplexity(1.000000)
Torpedosystem.SetDisabledPercentage(0.500000)
Torpedosystem.SetRadius(0.250000)
Torpedosystem.SetNormalPowerPerSecond(0.100000)
Torpedosystem.SetWeaponSystemType(Torpedosystem.WST_TORPEDO)
Torpedosystem.SetSingleFire(1)
Torpedosystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedosystem.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedosystem)
#################################################
Hyperdrive = App.WarpEngineProperty_Create("Hyperdrive")

Hyperdrive.SetMaxCondition(8.000000)
Hyperdrive.SetCritical(0)
Hyperdrive.SetTargetable(0)
Hyperdrive.SetPrimary(1)
Hyperdrive.SetPosition(0.000000, -0.020000, 0.009000)
Hyperdrive.SetPosition2D(0.000000, 0.000000)
Hyperdrive.SetRepairComplexity(1.000000)
Hyperdrive.SetDisabledPercentage(0.500000)
Hyperdrive.SetRadius(0.004000)
Hyperdrive.SetNormalPowerPerSecond(0.100000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive)
#################################################
TorpedoSystem = App.TorpedoSystemProperty_Create("Torpedo System")

TorpedoSystem.SetMaxCondition(7.000000)
TorpedoSystem.SetCritical(0)
TorpedoSystem.SetTargetable(1)
TorpedoSystem.SetPrimary(1)
TorpedoSystem.SetPosition(0.000000, 0.020000, -0.006000)
TorpedoSystem.SetPosition2D(59.000000, 83.000000)
TorpedoSystem.SetRepairComplexity(2.000000)
TorpedoSystem.SetDisabledPercentage(0.750000)
TorpedoSystem.SetRadius(0.003000)
TorpedoSystem.SetNormalPowerPerSecond(5.000000)
TorpedoSystem.SetWeaponSystemType(TorpedoSystem.WST_TORPEDO)
TorpedoSystem.SetSingleFire(0)
TorpedoSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single;1;Dual")
TorpedoSystem.SetFiringChainString(kFiringChainString)
TorpedoSystem.SetMaxTorpedoes(0, 8)
TorpedoSystem.SetTorpedoScript(0, "Tactical.Projectiles.cmissile")
TorpedoSystem.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoSystem)
#################################################
Torpedo1 = App.TorpedoTubeProperty_Create("Torpedo 1")

Torpedo1.SetMaxCondition(7.000000)
Torpedo1.SetCritical(0)
Torpedo1.SetTargetable(0)
Torpedo1.SetPrimary(1)
Torpedo1.SetPosition(-0.006900, -0.005000, -0.004000)
Torpedo1.SetPosition2D(59.000000, 64.000000)
Torpedo1.SetRepairComplexity(1.000000)
Torpedo1.SetDisabledPercentage(0.500000)
Torpedo1.SetRadius(0.002000)
Torpedo1.SetDumbfire(1)
Torpedo1.SetWeaponID(0)
Torpedo1.SetGroups(1)
Torpedo1.SetDamageRadiusFactor(0.600000)
Torpedo1.SetIconNum(370)
Torpedo1.SetIconPositionX(70.000000)
Torpedo1.SetIconPositionY(77.000000)
Torpedo1.SetIconAboveShip(1)
Torpedo1.SetImmediateDelay(0.250000)
Torpedo1.SetReloadDelay(5.000000)
Torpedo1.SetMaxReady(1)
Torpedo1Direction = App.TGPoint3()
Torpedo1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
Torpedo1.SetDirection(Torpedo1Direction)
Torpedo1Right = App.TGPoint3()
Torpedo1Right.SetXYZ(-0.514496, 0.000000, -0.857493)
Torpedo1.SetRight(Torpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedo1)
#################################################
Torpedo2 = App.TorpedoTubeProperty_Create("Torpedo 2")

Torpedo2.SetMaxCondition(7.000000)
Torpedo2.SetCritical(0)
Torpedo2.SetTargetable(0)
Torpedo2.SetPrimary(1)
Torpedo2.SetPosition(0.006900, -0.005000, -0.004000)
Torpedo2.SetPosition2D(73.000000, 64.000000)
Torpedo2.SetRepairComplexity(1.000000)
Torpedo2.SetDisabledPercentage(0.500000)
Torpedo2.SetRadius(0.002000)
Torpedo2.SetDumbfire(1)
Torpedo2.SetWeaponID(0)
Torpedo2.SetGroups(1)
Torpedo2.SetDamageRadiusFactor(0.600000)
Torpedo2.SetIconNum(370)
Torpedo2.SetIconPositionX(86.000000)
Torpedo2.SetIconPositionY(77.000000)
Torpedo2.SetIconAboveShip(1)
Torpedo2.SetImmediateDelay(0.250000)
Torpedo2.SetReloadDelay(5.000000)
Torpedo2.SetMaxReady(1)
Torpedo2Direction = App.TGPoint3()
Torpedo2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
Torpedo2.SetDirection(Torpedo2Direction)
Torpedo2Right = App.TGPoint3()
Torpedo2Right.SetXYZ(0.457496, 0.000000, -0.889212)
Torpedo2.SetRight(Torpedo2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedo2)
#################################################
Laser1 = App.PulseWeaponProperty_Create("Laser 1")

Laser1.SetMaxCondition(6.000000)
Laser1.SetCritical(0)
Laser1.SetTargetable(1)
Laser1.SetPrimary(1)
Laser1.SetPosition(0.048300, 0.022000, 0.003100)
Laser1.SetPosition2D(16.000000, 43.000000)
Laser1.SetRepairComplexity(1.000000)
Laser1.SetDisabledPercentage(0.500000)
Laser1.SetRadius(0.002000)
Laser1.SetDumbfire(1)
Laser1.SetWeaponID(0)
Laser1.SetGroups(0)
Laser1.SetDamageRadiusFactor(0.300000)
Laser1.SetIconNum(365)
Laser1.SetIconPositionX(44.000000)
Laser1.SetIconPositionY(66.000000)
Laser1.SetIconAboveShip(1)
Laser1.SetFireSound("")
Laser1.SetMaxCharge(4.000000)
Laser1.SetMaxDamage(0.000000)
Laser1.SetMaxDamageDistance(40.000000)
Laser1.SetMinFiringCharge(1.000000)
Laser1.SetNormalDischargeRate(1.000000)
Laser1.SetRechargeRate(0.300000)
Laser1.SetIndicatorIconNum(0)
Laser1.SetIndicatorIconPositionX(15.000000)
Laser1.SetIndicatorIconPositionY(15.000000)
Laser1Forward = App.TGPoint3()
Laser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Laser1Up = App.TGPoint3()
Laser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
Laser1.SetOrientation(Laser1Forward, Laser1Up)
Laser1.SetArcWidthAngles(-0.087266, 0.087266)
Laser1.SetArcHeightAngles(-0.087266, 0.087266)
Laser1.SetCooldownTime(0.200000)
Laser1.SetModuleName("Tactical.Projectiles.RebFighterLaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(Laser1)
#################################################
Laser2 = App.PulseWeaponProperty_Create("Laser 2")

Laser2.SetMaxCondition(6.000000)
Laser2.SetCritical(0)
Laser2.SetTargetable(1)
Laser2.SetPrimary(1)
Laser2.SetPosition(-0.048300, 0.022000, 0.003100)
Laser2.SetPosition2D(112.000000, 43.000000)
Laser2.SetRepairComplexity(1.000000)
Laser2.SetDisabledPercentage(0.500000)
Laser2.SetRadius(0.002000)
Laser2.SetDumbfire(1)
Laser2.SetWeaponID(0)
Laser2.SetGroups(0)
Laser2.SetDamageRadiusFactor(0.300000)
Laser2.SetIconNum(365)
Laser2.SetIconPositionX(111.000000)
Laser2.SetIconPositionY(65.000000)
Laser2.SetIconAboveShip(1)
Laser2.SetFireSound("")
Laser2.SetMaxCharge(4.000000)
Laser2.SetMaxDamage(0.000000)
Laser2.SetMaxDamageDistance(40.000000)
Laser2.SetMinFiringCharge(1.000000)
Laser2.SetNormalDischargeRate(1.000000)
Laser2.SetRechargeRate(0.300000)
Laser2.SetIndicatorIconNum(0)
Laser2.SetIndicatorIconPositionX(15.000000)
Laser2.SetIndicatorIconPositionY(15.000000)
Laser2Forward = App.TGPoint3()
Laser2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Laser2Up = App.TGPoint3()
Laser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
Laser2.SetOrientation(Laser2Forward, Laser2Up)
Laser2.SetArcWidthAngles(-0.087266, 0.087266)
Laser2.SetArcHeightAngles(-0.087266, 0.087266)
Laser2.SetCooldownTime(0.200000)
Laser2.SetModuleName("Tactical.Projectiles.RebFighterLaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(Laser2)
#################################################
Cockpit = App.HullProperty_Create("Cockpit")

Cockpit.SetMaxCondition(15.000000)
Cockpit.SetCritical(1)
Cockpit.SetTargetable(1)
Cockpit.SetPrimary(0)
Cockpit.SetPosition(0.000000, 0.000000, 0.006000)
Cockpit.SetPosition2D(0.000000, 0.000000)
Cockpit.SetRepairComplexity(1.000000)
Cockpit.SetDisabledPercentage(0.500000)
Cockpit.SetRadius(0.006000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cockpit)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ion Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Reactor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Laser Emiter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperdrive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Laser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Laser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cockpit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Z95", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
