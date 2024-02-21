# C:\Utopia\Current\Build\scripts\ships\Hardpoints\GenericTurretTemplate.py
# 

# This is a turret generic template which will be used for other turrets, those turret hardpoint will import this one and add modifications
# We would later make more specific ship turret templates acccording to a ship, so they have similar engine techs (such as jumpspace, slipstream and such; or disabling warp engines), if necessary.
# Later on, an specific ship turrets would import the generic turret for an specific ship and add the weapons required.
# In any of those two mentioned above, it would be useful to also redefine if necessary the weapon system controls for firing chains, torpedoes and such

import App
import GlobalPropertyTemplates
#	# The line below is needed by the editor to restore
#	# the name of the parent script.
#ParentPropertyScript = "ships.Hardpoints.GenericTemplate" # TO-DO Change "ships.Hardpoints.GenericTemplate" for "ships.Hardpoints.GenericTurretTemplate" or the ones needed
#if not ('g_bIsModelPropertyEditor' in dir(App)):
#	ParentModule = __import__("ships.Hardpoints.GenericTemplate", globals(), locals(), ['*']) # TO-DO Change "ships.Hardpoints.GenericTemplate" for "ships.Hardpoints.GenericTurretTemplate" or the ones needed
#	reload(ParentModule)

# Setting up local templates.
#################################################
# TO-DO REMEMBER TO REALISTICALLY CHANGE MASS (15.000000 is Shuttle Mass, 18000.000000 is Sovereign Mass), ROTATIONAL INERTIA, SHIP NAME, AND POSSIBLY SETMODELFILENAME, ALBEIT THE LATTER IS UNUSED
#################################################
Ship = App.ShipProperty_Create("Ship")

Ship.SetGenus(1)
Ship.SetSpecies(1)
Ship.SetMass(0.400000)
Ship.SetRotationalInertia(20000.000000)
Ship.SetShipName("GenericTurret")
Ship.SetModelFilename("data/Models/Ships/Warbird.nif")
Ship.SetDamageResolution(12.000000)
Ship.SetAffiliation(0)
Ship.SetStationary(0)
Ship.SetAIString("NonFedAttack")
Ship.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Ship)
#################################################
# TO-DO THIS BELOW ARE CAMERA THINGS JUST IN CASE, DO NOT TOUCH THEM UNLESS REQUIRED
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
ViewscreenForwardPosition.SetXYZ(0.000000, 6.100000, 0.200000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
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
ViewscreenLeftPosition.SetXYZ(-0.800000, 5.000000, 0.200000)
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
ViewscreenRightPosition.SetXYZ(0.800000, 5.000000, 0.200000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
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
ViewscreenBackPosition.SetXYZ(0.000000, -6.400000, 0.000000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
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
ViewscreenUpPosition.SetXYZ(0.000000, 5.000000, 1.400000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 5.000000, -1.600000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 6.100000, 0.200000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
# TO-DO MAYBE YOUR TURRETS CAN SUPPORT SHUTTLE BAYS, MAYBE NOT - ANYWAYS, TO AVOID SOME ISSUES WITH A FEW SCRIPTS, THESE HAVE BEEN LEFT HERE - FEEL FREE TO  MODIFY THEM ON THE OTHER TURRET HARDPOINTS
#################################################
ShuttleBay1OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 1 OEP")

ShuttleBay1OEPForward = App.TGPoint3()
ShuttleBay1OEPForward.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBay1OEPUp = App.TGPoint3()
ShuttleBay1OEPUp.SetXYZ(-1.000000, 0.000000, 0.000000)
ShuttleBay1OEPRight = App.TGPoint3()
ShuttleBay1OEPRight.SetXYZ(-0.219878, 0.968905, 0.113474)
ShuttleBay1OEP.SetOrientation(ShuttleBay1OEPForward, ShuttleBay1OEPUp, ShuttleBay1OEPRight)
ShuttleBay1OEPPosition = App.TGPoint3()
ShuttleBay1OEPPosition.SetXYZ(0.000000, 7.500000, -0.300000)
ShuttleBay1OEP.SetPosition(ShuttleBay1OEPPosition)
ShuttleBay1OEP.SetEmittedObjectType(ShuttleBay1OEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay1OEP)
#################################################
ShuttleBay1 = App.HullProperty_Create("Shuttle Bay 1")

ShuttleBay1.SetMaxCondition(2400.000000)
ShuttleBay1.SetCritical(0)
ShuttleBay1.SetTargetable(1)
ShuttleBay1.SetPrimary(0)
ShuttleBay1.SetPosition(0.000000, 7.500000, -0.300000)
ShuttleBay1.SetPosition2D(64.000000, 25.000000)
ShuttleBay1.SetRepairComplexity(4.000000)
ShuttleBay1.SetDisabledPercentage(0.000000)
ShuttleBay1.SetRadius(0.130000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay1)
#################################################
ShuttleBay2OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 2 OEP")

ShuttleBay2OEPForward = App.TGPoint3()
ShuttleBay2OEPForward.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBay2OEPUp = App.TGPoint3()
ShuttleBay2OEPUp.SetXYZ(-1.000000, 0.000000, 0.000000)
ShuttleBay2OEPRight = App.TGPoint3()
ShuttleBay2OEPRight.SetXYZ(-0.601395, 0.188891, 0.776301)
ShuttleBay2OEP.SetOrientation(ShuttleBay2OEPForward, ShuttleBay2OEPUp, ShuttleBay2OEPRight)
ShuttleBay2OEPPosition = App.TGPoint3()
ShuttleBay2OEPPosition.SetXYZ(0.000000, 6.500000, -0.300000)
ShuttleBay2OEP.SetPosition(ShuttleBay2OEPPosition)
ShuttleBay2OEP.SetEmittedObjectType(ShuttleBay2OEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay2OEP)
#################################################
ShuttleBay2 = App.HullProperty_Create("Shuttle Bay 2")

ShuttleBay2.SetMaxCondition(2400.000000)
ShuttleBay2.SetCritical(0)
ShuttleBay2.SetTargetable(1)
ShuttleBay2.SetPrimary(0)
ShuttleBay2.SetPosition(0.000000, 6.500000, -0.300000)
ShuttleBay2.SetPosition2D(64.000000, 25.000000)
ShuttleBay2.SetRepairComplexity(4.000000)
ShuttleBay2.SetDisabledPercentage(0.000000)
ShuttleBay2.SetRadius(0.130000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay2)
#################################################
ShuttleBay3OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 3 OEP")

ShuttleBay3OEPForward = App.TGPoint3()
ShuttleBay3OEPForward.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBay3OEPUp = App.TGPoint3()
ShuttleBay3OEPUp.SetXYZ(-1.000000, 0.000000, 0.000000)
ShuttleBay3OEPRight = App.TGPoint3()
ShuttleBay3OEPRight.SetXYZ(-0.578850, -0.566995, -0.586045)
ShuttleBay3OEP.SetOrientation(ShuttleBay3OEPForward, ShuttleBay3OEPUp, ShuttleBay3OEPRight)
ShuttleBay3OEPPosition = App.TGPoint3()
ShuttleBay3OEPPosition.SetXYZ(0.000000, 5.400000, -0.300000)
ShuttleBay3OEP.SetPosition(ShuttleBay3OEPPosition)
ShuttleBay3OEP.SetEmittedObjectType(ShuttleBay3OEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay3OEP)
#################################################
ShuttleBay3 = App.HullProperty_Create("Shuttle Bay 3")

ShuttleBay3.SetMaxCondition(2400.000000)
ShuttleBay3.SetCritical(0)
ShuttleBay3.SetTargetable(1)
ShuttleBay3.SetPrimary(0)
ShuttleBay3.SetPosition(0.000000, 5.400000, -0.300000)
ShuttleBay3.SetPosition2D(64.000000, 25.000000)
ShuttleBay3.SetRepairComplexity(4.000000)
ShuttleBay3.SetDisabledPercentage(0.000000)
ShuttleBay3.SetRadius(0.130000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay3)
#################################################
# Generic Template things - Do not touch them
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(1000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(0.000000, 0.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.500000)
Hull.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngineSystem = App.ImpulseEngineProperty_Create("Impulse Engine System")

ImpulseEngineSystem.SetMaxCondition(200.000000)
ImpulseEngineSystem.SetCritical(0)
ImpulseEngineSystem.SetTargetable(1)
ImpulseEngineSystem.SetPrimary(1)
ImpulseEngineSystem.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngineSystem.SetPosition2D(0.000000, 0.000000)
ImpulseEngineSystem.SetRepairComplexity(1.000000)
ImpulseEngineSystem.SetDisabledPercentage(0.500000)
ImpulseEngineSystem.SetRadius(0.250000)
ImpulseEngineSystem.SetNormalPowerPerSecond(1.000000)
ImpulseEngineSystem.SetMaxAccel(20.000000)
ImpulseEngineSystem.SetMaxAngularAccel(0.100000)
ImpulseEngineSystem.SetMaxAngularVelocity(0.250000)
ImpulseEngineSystem.SetMaxSpeed(20.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngineSystem)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(200.000000)
PowerPlant.SetCritical(0)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, 0.000000)
PowerPlant.SetPosition2D(0.000000, 0.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.250000)
PowerPlant.SetMainBatteryLimit(70000.000000)
PowerPlant.SetBackupBatteryLimit(10000.000000)
PowerPlant.SetMainConduitCapacity(400.000000)
PowerPlant.SetBackupConduitCapacity(200.000000)
PowerPlant.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(200.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(1)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.250000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(15.000000)
RepairSystem.SetNumRepairTeams(3)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(200.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.000000, 0.000000)
SensorArray.SetPosition2D(0.000000, 0.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.250000)
SensorArray.SetNormalPowerPerSecond(1.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(200.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(0.000000, 0.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.250000)
ShieldGenerator.SetNormalPowerPerSecond(1.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 1.000000, 1.000000, 1.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 1000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 1000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 1000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 1000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 1000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 1000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
PhaserSystem = App.WeaponSystemProperty_Create("Phaser System")

PhaserSystem.SetMaxCondition(200.000000)
PhaserSystem.SetCritical(0)
PhaserSystem.SetTargetable(1)
PhaserSystem.SetPrimary(1)
PhaserSystem.SetPosition(0.000000, 0.000000, 0.000000)
PhaserSystem.SetPosition2D(0.000000, 0.000000)
PhaserSystem.SetRepairComplexity(1.000000)
PhaserSystem.SetDisabledPercentage(0.500000)
PhaserSystem.SetRadius(0.250000)
PhaserSystem.SetNormalPowerPerSecond(1.000000)
PhaserSystem.SetWeaponSystemType(PhaserSystem.WST_PHASER)
PhaserSystem.SetSingleFire(0)
PhaserSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PhaserSystem.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PhaserSystem)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(200.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(1)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(0.000000, 0.000000)
Torpedoes.SetRepairComplexity(1.000000)
Torpedoes.SetDisabledPercentage(0.500000)
Torpedoes.SetRadius(0.250000)
Torpedoes.SetNormalPowerPerSecond(1.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 400)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.PhotonTorpedo")
Torpedoes.SetMaxTorpedoes(1, 400)
Torpedoes.SetTorpedoScript(1, "Tactical.Projectiles.QuantumTorpedo")
Torpedoes.SetMaxTorpedoes(2, 400)
Torpedoes.SetTorpedoScript(2, "Tactical.Projectiles.QuantumTorpedo")
Torpedoes.SetMaxTorpedoes(3, 400)
Torpedoes.SetTorpedoScript(3, "Tactical.Projectiles.QuantumTorpedo")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
TractorBeamSystem = App.WeaponSystemProperty_Create("Tractor Beam System")

TractorBeamSystem.SetMaxCondition(200.000000)
TractorBeamSystem.SetCritical(0)
TractorBeamSystem.SetTargetable(1)
TractorBeamSystem.SetPrimary(1)
TractorBeamSystem.SetPosition(0.000000, 0.000000, 0.000000)
TractorBeamSystem.SetPosition2D(0.000000, 0.000000)
TractorBeamSystem.SetRepairComplexity(1.000000)
TractorBeamSystem.SetDisabledPercentage(0.500000)
TractorBeamSystem.SetRadius(0.250000)
TractorBeamSystem.SetNormalPowerPerSecond(1.000000)
TractorBeamSystem.SetWeaponSystemType(TractorBeamSystem.WST_TRACTOR)
TractorBeamSystem.SetSingleFire(0)
TractorBeamSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
TractorBeamSystem.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(TractorBeamSystem)
#################################################
PulseWeaponSystem = App.WeaponSystemProperty_Create("Pulse Weapon System")

PulseWeaponSystem.SetMaxCondition(200.000000)
PulseWeaponSystem.SetCritical(0)
PulseWeaponSystem.SetTargetable(1)
PulseWeaponSystem.SetPrimary(1)
PulseWeaponSystem.SetPosition(0.000000, 0.000000, 0.000000)
PulseWeaponSystem.SetPosition2D(0.000000, 0.000000)
PulseWeaponSystem.SetRepairComplexity(1.000000)
PulseWeaponSystem.SetDisabledPercentage(0.500000)
PulseWeaponSystem.SetRadius(0.250000)
PulseWeaponSystem.SetNormalPowerPerSecond(1.000000)
PulseWeaponSystem.SetWeaponSystemType(PulseWeaponSystem.WST_PULSE)
PulseWeaponSystem.SetSingleFire(0)
PulseWeaponSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PulseWeaponSystem.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PulseWeaponSystem)
#################################################
CloakingSystem = App.CloakingSubsystemProperty_Create("Cloaking System")

CloakingSystem.SetMaxCondition(200.000000)
CloakingSystem.SetCritical(0)
CloakingSystem.SetTargetable(1)
CloakingSystem.SetPrimary(1)
CloakingSystem.SetPosition(0.000000, 0.000000, 0.000000)
CloakingSystem.SetPosition2D(0.000000, 0.000000)
CloakingSystem.SetRepairComplexity(1.000000)
CloakingSystem.SetDisabledPercentage(0.500000)
CloakingSystem.SetRadius(0.250000)
CloakingSystem.SetNormalPowerPerSecond(1.000000)
CloakingSystem.SetCloakStrength(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingSystem)
#################################################
ImpulseEngine = App.EngineProperty_Create("Impulse Engine")

ImpulseEngine.SetMaxCondition(200.000000)
ImpulseEngine.SetCritical(0)
ImpulseEngine.SetTargetable(1)
ImpulseEngine.SetPrimary(1)
ImpulseEngine.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngine.SetPosition2D(0.000000, 0.000000)
ImpulseEngine.SetRepairComplexity(1.000000)
ImpulseEngine.SetDisabledPercentage(0.500000)
ImpulseEngine.SetRadius(0.250000)
ImpulseEngine.SetEngineType(ImpulseEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngine)
#################################################
# TO-DO IF YOU NEED TO DISABLE WARP ENGINES, BETTER DISABLE THE WARP ENGINE PROPERTY, NO THE ENGINES THEMSELVES, AS THOSE MAY BE USED FOR SOME TECHNOLOGIES, WHILE THE WARP ENGINE IS NOT.
# The property commented below explains how to do it, just add it to the turret one - NOT TO THE TURRET GENERIC TEMPLATE!!!
# If both are needed to be absent, then just create a new template without the Warp Engines
#################################################
#WarpEngineSystem = App.WarpEngineProperty_Create("Warp Engine System")
#
#WarpEngineSystem.SetMaxCondition(8000.000000)
#WarpEngineSystem.SetCritical(0)
#WarpEngineSystem.SetTargetable(0)
#WarpEngineSystem.SetPrimary(1)
#WarpEngineSystem.SetPosition(0.049999, -6.750000, 0.900000)
#WarpEngineSystem.SetPosition2D(67.000000, 109.000000)
#WarpEngineSystem.SetRepairComplexity(3.000000)
#WarpEngineSystem.SetDisabledPercentage(1.500000)
#WarpEngineSystem.SetRadius(0.200000)
#WarpEngineSystem.SetNormalPowerPerSecond(0.000000)
#App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngineSystem)
#################################################
# TO-DO The property below is the default generic one for adding warp capabilities
#################################################
WarpEngineSystem = App.WarpEngineProperty_Create("Warp Engine System")

WarpEngineSystem.SetMaxCondition(8000.000000)
WarpEngineSystem.SetCritical(0)
WarpEngineSystem.SetTargetable(0)
WarpEngineSystem.SetPrimary(1)
WarpEngineSystem.SetPosition(0.049999, -6.750000, 0.900000)
WarpEngineSystem.SetPosition2D(67.000000, 109.000000)
WarpEngineSystem.SetRepairComplexity(3.000000)
WarpEngineSystem.SetDisabledPercentage(0.500000)
WarpEngineSystem.SetRadius(0.200000)
WarpEngineSystem.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngineSystem)
#################################################
WarpEngine = App.EngineProperty_Create("Warp Engine")

WarpEngine.SetMaxCondition(200.000000)
WarpEngine.SetCritical(0)
WarpEngine.SetTargetable(1)
WarpEngine.SetPrimary(1)
WarpEngine.SetPosition(0.000000, 0.000000, 0.000000)
WarpEngine.SetPosition2D(0.000000, 0.000000)
WarpEngine.SetRepairComplexity(1.000000)
WarpEngine.SetDisabledPercentage(0.500000)
WarpEngine.SetRadius(0.250000)
WarpEngine.SetEngineType(WarpEngine.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngine)
#################################################
# TO-DO Below are examples of other drives which may require an extra hardpoint property, each one may require an specific technology to be pre-installed before they work
# However, due to how the tech works and how other techs work, it is ABSOLUTELY NOT recommended to add those to the turrets
#################################################
# TO-DO Add the property below uncommented on the specific turret for Slipstream Drive Technology
#################################################
#SlipstreamDrive1 = App.HullProperty_Create("Slipstream Drive 1")
#
#SlipstreamDrive1.SetMaxCondition(12000.000000)
#SlipstreamDrive1.SetCritical(0)
#SlipstreamDrive1.SetTargetable(1)
#SlipstreamDrive1.SetPrimary(0)
#SlipstreamDrive1.SetPosition(0.050000, 0.270000, -0.300000)
#SlipstreamDrive1.SetPosition2D(0.000000, 0.000000)
#SlipstreamDrive1.SetRepairComplexity(0.900000)
#SlipstreamDrive1.SetDisabledPercentage(0.500000)
#SlipstreamDrive1.SetRadius(0.200000)
#App.g_kModelPropertyManager.RegisterLocalTemplate(SlipstreamDrive1)
#################################################
# TO-DO Add the property below uncommented on the specific turret for Hyperdrive Technology
#################################################
#Hyperdrive1 = App.HullProperty_Create("Hyperdrive 1")
#
#Hyperdrive1.SetMaxCondition(7000.000000)
#Hyperdrive1.SetCritical(0)
#Hyperdrive1.SetTargetable(1)
#Hyperdrive1.SetPrimary(0)
#Hyperdrive1.SetPosition(0.000000, 0.000000, 0.200000)
#Hyperdrive1.SetPosition2D(65, 75)
#Hyperdrive1.SetRepairComplexity(1.000000)
#Hyperdrive1.SetDisabledPercentage(0.000000)
#Hyperdrive1.SetRadius(0.025000)
#App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive1)
#################################################
# TO-DO Add the property below uncommented on the specific turret for Jumpspace Drive Technology
#################################################
#PrimaryDrive = App.EngineProperty_Create("Jumpspace Drive 1")
#
#PrimaryDrive.SetMaxCondition(8000.000000)
#PrimaryDrive.SetCritical(0)
#PrimaryDrive.SetTargetable(1)
#PrimaryDrive.SetPrimary(1)
#PrimaryDrive.SetPosition(-0.200000, -2.350000, 0.000000)
#PrimaryDrive.SetPosition2D(4.000000, 60.000000)
#PrimaryDrive.SetRepairComplexity(3.000000)
#PrimaryDrive.SetDisabledPercentage(0.500000)
#PrimaryDrive.SetRadius(0.500000)
#PrimaryDrive.SetEngineType(PrimaryDrive.EP_WARP)
#App.g_kModelPropertyManager.RegisterLocalTemplate(PrimaryDrive)
#################################################
# TO-DO Add the property below uncommented on the specific turret for TimeVortex Drive Technology
#################################################
#SecondaryDrive = App.EngineProperty_Create("TimeVortex Drive 1")
#
#SecondaryDrive.SetMaxCondition(8000.000000)
#SecondaryDrive.SetCritical(0)
#SecondaryDrive.SetTargetable(1)
#SecondaryDrive.SetPrimary(1)
#SecondaryDrive.SetPosition(-0.450000, -3.150000, 0.000000)
#SecondaryDrive.SetPosition2D(124.000000, 60.000000)
#SecondaryDrive.SetRepairComplexity(3.000000)
#SecondaryDrive.SetDisabledPercentage(0.500000)
#SecondaryDrive.SetRadius(0.500000)
#SecondaryDrive.SetEngineType(SecondaryDrive.EP_WARP)
#App.g_kModelPropertyManager.RegisterLocalTemplate(SecondaryDrive)



# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
        ### TO-DO GENERIC TEMPLATE SECTION ###
	prop = App.g_kModelPropertyManager.FindByName("Ship", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engine System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Phaser System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractor Beam System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pulse Weapon System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cloaking System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
        ### TO-DO CAMERA SECTION ###
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
        ### TO-DO SHUTTLE BAY SECTION ###
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 1 OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 2 OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 3 OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
        ### TO-DO IF YOU MODIFY THE WARP ENGINE CONTROL SYSTEM, UNCOMMENT THIS ONE ###
	prop = App.g_kModelPropertyManager.FindByName("Warp Engine System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
        ### TO-DO SPECIFIC ENGINE SECTIONS, UNCOMMENT THESE ACCORDINGLY ###
        ## TO-DO SLIPSTREAM ##
	#prop = App.g_kModelPropertyManager.FindByName("Slipstream Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ## TO-DO HYPERDRIVE ##
	#prop = App.g_kModelPropertyManager.FindByName("Hyperdrive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ## TO-DO JUMPSPACE ##
	#prop = App.g_kModelPropertyManager.FindByName("Jumpspace Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ## TO-DO TIME VORTEX ##
	#prop = App.g_kModelPropertyManager.FindByName("TimeVortex Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)