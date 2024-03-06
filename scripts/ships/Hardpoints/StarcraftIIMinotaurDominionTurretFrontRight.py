# C:\Utopia\Current\Build\scripts\ships\Hardpoints\VictoryTurret.py
# 

# This will import the generic template and add the appropiate weapons

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.GenericStarcraftIIMinotaurDominionTurretTemplate" # TO-DO Change "ships.Hardpoints.GenericTemplate" for "ships.Hardpoints.GenericTurretTemplate" or the ones needed
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.GenericStarcraftIIMinotaurDominionTurretTemplate", globals(), locals(), ['*']) # TO-DO Change "ships.Hardpoints.GenericTemplate" for "ships.Hardpoints.GenericTurretTemplate" or the ones needed
	reload(ParentModule)


# Setting up local templates.
# TO-DO REMEMBER TO REALISTICALLY CHANGE MASS (15.000000 is Shuttle Mass, 18000.000000 is Sovereign Mass), ROTATIONAL INERTIA, SHIP NAME, AND POSSIBLY SETMODELFILENAME, ALBEIT THE LATTER IS UNUSED
#################################################
Ship = App.ShipProperty_Create("Ship")

Ship.SetGenus(1)
Ship.SetSpecies(1)
Ship.SetMass(0.400000)
Ship.SetRotationalInertia(20000.000000)
Ship.SetShipName("StarcraftIIMinotaurDominionTurretFrontRight")
Ship.SetModelFilename("data/Models/Ships/Warbird.nif")
Ship.SetDamageResolution(12.000000)
Ship.SetAffiliation(0)
Ship.SetStationary(0)
Ship.SetAIString("NonFedAttack")
Ship.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Ship)
#################################################
# TO-DO THIS BELOW ARE CAMERA THINGS JUST IN CASE, DO NOT TOUCH THEM UNLESS REQUIRED - If needed, copy the camera section from the GenericTurretTemplate
#################################################
#################################################
# TO-DO MAYBE YOUR TURRETS CAN SUPPORT SHUTTLE BAYS, MAYBE NOT - ANYWAYS, TO AVOID SOME ISSUES WITH A FEW SCRIPTS, shuttle support has been included on the generic Turret Template. If those need to be edited, uncomment below
#################################################
#ShuttleBay1OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 1 OEP")
#
#ShuttleBay1OEPForward = App.TGPoint3()
#ShuttleBay1OEPForward.SetXYZ(0.000000, 0.000000, 1.000000)
#ShuttleBay1OEPUp = App.TGPoint3()
#ShuttleBay1OEPUp.SetXYZ(-1.000000, 0.000000, 0.000000)
#ShuttleBay1OEPRight = App.TGPoint3()
#ShuttleBay1OEPRight.SetXYZ(-0.219878, 0.968905, 0.113474)
#ShuttleBay1OEP.SetOrientation(ShuttleBay1OEPForward, ShuttleBay1OEPUp, ShuttleBay1OEPRight)
#ShuttleBay1OEPPosition = App.TGPoint3()
#ShuttleBay1OEPPosition.SetXYZ(0.000000, 7.500000, -0.300000)
#ShuttleBay1OEP.SetPosition(ShuttleBay1OEPPosition)
#ShuttleBay1OEP.SetEmittedObjectType(ShuttleBay1OEP.OEP_SHUTTLE)
#App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay1OEP)
#################################################
#ShuttleBay1 = App.HullProperty_Create("Shuttle Bay 1")
#
#ShuttleBay1.SetMaxCondition(2400.000000)
#ShuttleBay1.SetCritical(0)
#ShuttleBay1.SetTargetable(1)
#ShuttleBay1.SetPrimary(0)
#ShuttleBay1.SetPosition(0.000000, 7.500000, -0.300000)
#ShuttleBay1.SetPosition2D(64.000000, 25.000000)
#ShuttleBay1.SetRepairComplexity(4.000000)
#ShuttleBay1.SetDisabledPercentage(0.000000)
#ShuttleBay1.SetRadius(0.130000)
#App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay1)
#################################################
#ShuttleBay2OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 2 OEP")
#
#ShuttleBay2OEPForward = App.TGPoint3()
#ShuttleBay2OEPForward.SetXYZ(0.000000, 0.000000, 1.000000)
#ShuttleBay2OEPUp = App.TGPoint3()
#ShuttleBay2OEPUp.SetXYZ(-1.000000, 0.000000, 0.000000)
#ShuttleBay2OEPRight = App.TGPoint3()
#ShuttleBay2OEPRight.SetXYZ(-0.601395, 0.188891, 0.776301)
#ShuttleBay2OEP.SetOrientation(ShuttleBay2OEPForward, ShuttleBay2OEPUp, ShuttleBay2OEPRight)
#ShuttleBay2OEPPosition = App.TGPoint3()
#ShuttleBay2OEPPosition.SetXYZ(0.000000, 6.500000, -0.300000)
#ShuttleBay2OEP.SetPosition(ShuttleBay2OEPPosition)
#ShuttleBay2OEP.SetEmittedObjectType(ShuttleBay2OEP.OEP_SHUTTLE)
#App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay2OEP)
#################################################
#ShuttleBay2 = App.HullProperty_Create("Shuttle Bay 2")
#
#ShuttleBay2.SetMaxCondition(2400.000000)
#ShuttleBay2.SetCritical(0)
#ShuttleBay2.SetTargetable(1)
#ShuttleBay2.SetPrimary(0)
#ShuttleBay2.SetPosition(0.000000, 6.500000, -0.300000)
#ShuttleBay2.SetPosition2D(64.000000, 25.000000)
#ShuttleBay2.SetRepairComplexity(4.000000)
#ShuttleBay2.SetDisabledPercentage(0.000000)
#ShuttleBay2.SetRadius(0.130000)
#App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay2)
#################################################
#ShuttleBay3OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 3 OEP")
#
#ShuttleBay3OEPForward = App.TGPoint3()
#ShuttleBay3OEPForward.SetXYZ(0.000000, 0.000000, 1.000000)
#ShuttleBay3OEPUp = App.TGPoint3()
#ShuttleBay3OEPUp.SetXYZ(-1.000000, 0.000000, 0.000000)
#ShuttleBay3OEPRight = App.TGPoint3()
#ShuttleBay3OEPRight.SetXYZ(-0.578850, -0.566995, -0.586045)
#ShuttleBay3OEP.SetOrientation(ShuttleBay3OEPForward, ShuttleBay3OEPUp, ShuttleBay3OEPRight)
#ShuttleBay3OEPPosition = App.TGPoint3()
#ShuttleBay3OEPPosition.SetXYZ(0.000000, 5.400000, -0.300000)
#ShuttleBay3OEP.SetPosition(ShuttleBay3OEPPosition)
#ShuttleBay3OEP.SetEmittedObjectType(ShuttleBay3OEP.OEP_SHUTTLE)
#App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay3OEP)
#################################################
#ShuttleBay3 = App.HullProperty_Create("Shuttle Bay 3")
#
#ShuttleBay3.SetMaxCondition(2400.000000)
#ShuttleBay3.SetCritical(0)
#ShuttleBay3.SetTargetable(1)
#ShuttleBay3.SetPrimary(0)
#ShuttleBay3.SetPosition(0.000000, 5.400000, -0.300000)
#ShuttleBay3.SetPosition2D(64.000000, 25.000000)
#ShuttleBay3.SetRepairComplexity(4.000000)
#ShuttleBay3.SetDisabledPercentage(0.000000)
#ShuttleBay3.SetRadius(0.130000)
#App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay3)
#################################################
# Generic Template things - Do not touch them - and for that reason, they have not been included on this Generic Ship Turret Hardpoint, except those which could be affected by firing chains, single fire, ammo, probes or cloak strength
# - and they are still commented until needed in any other way
#################################################
#SensorArray = App.SensorProperty_Create("Sensor Array")
#
#SensorArray.SetMaxCondition(200.000000)
#SensorArray.SetCritical(0)
#SensorArray.SetTargetable(1)
#SensorArray.SetPrimary(1)
#SensorArray.SetPosition(0.000000, 0.000000, 0.000000)
#SensorArray.SetPosition2D(0.000000, 0.000000)
#SensorArray.SetRepairComplexity(1.000000)
#SensorArray.SetDisabledPercentage(0.500000)
#SensorArray.SetRadius(0.250000)
#SensorArray.SetNormalPowerPerSecond(1.000000)
#SensorArray.SetBaseSensorRange(1000.000000)
#SensorArray.SetMaxProbes(10)
#App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
#PhaserSystem = App.WeaponSystemProperty_Create("Phaser System")
#
#PhaserSystem.SetMaxCondition(200.000000)
#PhaserSystem.SetCritical(0)
#PhaserSystem.SetTargetable(1)
#PhaserSystem.SetPrimary(1)
#PhaserSystem.SetPosition(0.000000, 0.000000, 0.000000)
#PhaserSystem.SetPosition2D(0.000000, 0.000000)
#PhaserSystem.SetRepairComplexity(1.000000)
#PhaserSystem.SetDisabledPercentage(0.500000)
#PhaserSystem.SetRadius(0.250000)
#PhaserSystem.SetNormalPowerPerSecond(1.000000)
#PhaserSystem.SetWeaponSystemType(PhaserSystem.WST_PHASER)
#PhaserSystem.SetSingleFire(0)
#PhaserSystem.SetAimedWeapon(0)
#kFiringChainString = App.TGString()
#kFiringChainString.SetString("")
#PhaserSystem.SetFiringChainString(kFiringChainString)
#App.g_kModelPropertyManager.RegisterLocalTemplate(PhaserSystem)
#################################################
#Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")
#
#Torpedoes.SetMaxCondition(200.000000)
#Torpedoes.SetCritical(0)
#Torpedoes.SetTargetable(1)
#Torpedoes.SetPrimary(1)
#Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
#Torpedoes.SetPosition2D(0.000000, 0.000000)
#Torpedoes.SetRepairComplexity(1.000000)
#Torpedoes.SetDisabledPercentage(0.500000)
#Torpedoes.SetRadius(0.250000)
#Torpedoes.SetNormalPowerPerSecond(1.000000)
#Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
#Torpedoes.SetSingleFire(0)
#Torpedoes.SetAimedWeapon(0)
#kFiringChainString = App.TGString()
#kFiringChainString.SetString("")
#Torpedoes.SetFiringChainString(kFiringChainString)
#Torpedoes.SetMaxTorpedoes(0, 99999)
#Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.VorlonWeapon")
#Torpedoes.SetNumAmmoTypes(1)
#App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
#TractorBeamSystem = App.WeaponSystemProperty_Create("Tractor Beam System")
#
#TractorBeamSystem.SetMaxCondition(200.000000)
#TractorBeamSystem.SetCritical(0)
#TractorBeamSystem.SetTargetable(1)
#TractorBeamSystem.SetPrimary(1)
#TractorBeamSystem.SetPosition(0.000000, 0.000000, 0.000000)
#TractorBeamSystem.SetPosition2D(0.000000, 0.000000)
#TractorBeamSystem.SetRepairComplexity(1.000000)
#TractorBeamSystem.SetDisabledPercentage(0.500000)
#TractorBeamSystem.SetRadius(0.250000)
#TractorBeamSystem.SetNormalPowerPerSecond(1.000000)
#TractorBeamSystem.SetWeaponSystemType(TractorBeamSystem.WST_TRACTOR)
#TractorBeamSystem.SetSingleFire(0)
#TractorBeamSystem.SetAimedWeapon(0)
#kFiringChainString = App.TGString()
#kFiringChainString.SetString("")
#TractorBeamSystem.SetFiringChainString(kFiringChainString)
#App.g_kModelPropertyManager.RegisterLocalTemplate(TractorBeamSystem)
#################################################
#PulseWeaponSystem = App.WeaponSystemProperty_Create("Pulse Weapon System")
#
#PulseWeaponSystem.SetMaxCondition(200.000000)
#PulseWeaponSystem.SetCritical(0)
#PulseWeaponSystem.SetTargetable(1)
#PulseWeaponSystem.SetPrimary(1)
#PulseWeaponSystem.SetPosition(0.000000, 0.000000, 0.000000)
#PulseWeaponSystem.SetPosition2D(0.000000, 0.000000)
#PulseWeaponSystem.SetRepairComplexity(1.000000)
#PulseWeaponSystem.SetDisabledPercentage(0.500000)
#PulseWeaponSystem.SetRadius(0.250000)
#PulseWeaponSystem.SetNormalPowerPerSecond(1.000000)
#PulseWeaponSystem.SetWeaponSystemType(PulseWeaponSystem.WST_PULSE)
#PulseWeaponSystem.SetSingleFire(0)
#PulseWeaponSystem.SetAimedWeapon(0)
#kFiringChainString = App.TGString()
#kFiringChainString.SetString("")
#PulseWeaponSystem.SetFiringChainString(kFiringChainString)
#App.g_kModelPropertyManager.RegisterLocalTemplate(PulseWeaponSystem)
#################################################
#CloakingSystem = App.CloakingSubsystemProperty_Create("Cloaking System")
#
#CloakingSystem.SetMaxCondition(200.000000)
#CloakingSystem.SetCritical(0)
#CloakingSystem.SetTargetable(1)
#CloakingSystem.SetPrimary(1)
#CloakingSystem.SetPosition(0.000000, 0.000000, 0.000000)
#CloakingSystem.SetPosition2D(0.000000, 0.000000)
#CloakingSystem.SetRepairComplexity(1.000000)
#CloakingSystem.SetDisabledPercentage(0.500000)
#CloakingSystem.SetRadius(0.250000)
#CloakingSystem.SetNormalPowerPerSecond(1.000000)
#CloakingSystem.SetCloakStrength(0.000000)
#App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingSystem)
#################################################
# TO-DO IF YOU NEED TO DISABLE WARP ENGINES, BETTER DISABLE THE WARP ENGINE PROPERTY, NOT THE ENGINES THEMSELVES, AS THOSE MAY BE USED FOR SOME TECHNOLOGIES, WHILE THE WARP ENGINE IS NOT.
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
# TO-DO Below are examples of other drives which may require an extra hardpoint property, each one may require an specific technology to be pre-installed before they work
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
#################################################
# TO-DO HERE WE ADD THE NEW WEAPONS
#################################################
StarDisruptor1 = App.PulseWeaponProperty_Create("Dorsal Laser Battery 2")

StarDisruptor1.SetMaxCondition(500.000000)
StarDisruptor1.SetCritical(0)
StarDisruptor1.SetTargetable(1)
StarDisruptor1.SetPrimary(0)
StarDisruptor1.SetPosition(0.090000, -0.030000, 0.000000)
StarDisruptor1.SetPosition2D(70.000000, 53.000000)
StarDisruptor1.SetRepairComplexity(1.000000)
StarDisruptor1.SetDisabledPercentage(0.500000)
StarDisruptor1.SetRadius(0.250000)
StarDisruptor1.SetDumbfire(0)
StarDisruptor1.SetWeaponID(0)
StarDisruptor1.SetGroups(1)
StarDisruptor1.SetDamageRadiusFactor(0.300000)
StarDisruptor1.SetIconNum(365)
StarDisruptor1.SetIconPositionX(89.000000)
StarDisruptor1.SetIconPositionY(89.000000)
StarDisruptor1.SetIconAboveShip(1)
StarDisruptor1.SetFireSound("")
StarDisruptor1.SetMaxCharge(1.000000)
StarDisruptor1.SetMaxDamage(25.000000)
StarDisruptor1.SetMaxDamageDistance(100.000000)
StarDisruptor1.SetMinFiringCharge(1.000000)
StarDisruptor1.SetNormalDischargeRate(1.000000)
StarDisruptor1.SetRechargeRate(1.500000)
StarDisruptor1.SetIndicatorIconNum(370)
StarDisruptor1.SetIndicatorIconPositionX(92.000000)
StarDisruptor1.SetIndicatorIconPositionY(89.000000)
StarDisruptor1Forward = App.TGPoint3()
StarDisruptor1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
StarDisruptor1Up = App.TGPoint3()
StarDisruptor1Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarDisruptor1.SetOrientation(StarDisruptor1Forward, StarDisruptor1Up)
StarDisruptor1.SetArcWidthAngles(-1.576332, 1.576332)
StarDisruptor1.SetArcHeightAngles(1.576332, -1.576332)
StarDisruptor1.SetCooldownTime(0.300000)
StarDisruptor1.SetModuleName("Tactical.Projectiles.SCIIATALaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarDisruptor1)
#################################################
StarDisruptor2 = App.PulseWeaponProperty_Create("Dorsal Laser Battery 2B")

StarDisruptor2.SetMaxCondition(500.000000)
StarDisruptor2.SetCritical(0)
StarDisruptor2.SetTargetable(1)
StarDisruptor2.SetPrimary(0)
StarDisruptor2.SetPosition(-0.090000, 0.030000, 0.000000)
StarDisruptor2.SetPosition2D(70.000000, 53.000000)
StarDisruptor2.SetRepairComplexity(1.000000)
StarDisruptor2.SetDisabledPercentage(0.500000)
StarDisruptor2.SetRadius(0.250000)
StarDisruptor2.SetDumbfire(0)
StarDisruptor2.SetWeaponID(0)
StarDisruptor2.SetGroups(1)
StarDisruptor2.SetDamageRadiusFactor(0.300000)
StarDisruptor2.SetIconNum(365)
StarDisruptor2.SetIconPositionX(89.000000)
StarDisruptor2.SetIconPositionY(89.000000)
StarDisruptor2.SetIconAboveShip(1)
StarDisruptor2.SetFireSound("")
StarDisruptor2.SetMaxCharge(1.000000)
StarDisruptor2.SetMaxDamage(25.000000)
StarDisruptor2.SetMaxDamageDistance(100.000000)
StarDisruptor2.SetMinFiringCharge(1.000000)
StarDisruptor2.SetNormalDischargeRate(1.000000)
StarDisruptor2.SetRechargeRate(1.500000)
StarDisruptor2.SetIndicatorIconNum(370)
StarDisruptor2.SetIndicatorIconPositionX(92.000000)
StarDisruptor2.SetIndicatorIconPositionY(89.000000)
StarDisruptor2Forward = App.TGPoint3()
StarDisruptor2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
StarDisruptor2Up = App.TGPoint3()
StarDisruptor2Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarDisruptor2.SetOrientation(StarDisruptor2Forward, StarDisruptor2Up)
StarDisruptor2.SetArcWidthAngles(-1.576332, 1.576332)
StarDisruptor2.SetArcHeightAngles(1.576332, -1.576332)
StarDisruptor2.SetCooldownTime(0.300000)
StarDisruptor2.SetModuleName("Tactical.Projectiles.SCIIATALaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarDisruptor2)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
        ### TO-DO GENERIC TEMPLATE SECTION ###
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Ship", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
        ### *** TO-DO UNCOMMENT WHEN NEEDED (F.EX. BECAUSE THE TURRETS MAY USE TORPEDOES OR A FIRING CHAIN) *** ###
	#prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ### *** TO-DO UNCOMMENT WHEN NEEDED (F.EX. BECAUSE THE TURRETS MAY USE A PHASER FIRING CHAIN) *** ###
	#prop = App.g_kModelPropertyManager.FindByName("Phaser System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ### *** TO-DO UNCOMMENT TORPEDOES WHEN NEEDED (F.EX. BECAUSE THE TURRETS MAY USE TORPEDOES OR A FIRING CHAIN) *** ###
	#prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ### *** TO-DO UNCOMMENT WHEN NEEDED (F.EX. BECAUSE THE TURRETS MAY USE A TRACTOR BEAM FIRING CHAIN) *** ###
	#prop = App.g_kModelPropertyManager.FindByName("Tractor Beam System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ### *** TO-DO UNCOMMENT WHEN NEEDED (F.EX. BECAUSE THE TURRETS MAY USE A PULSE WEAPON FIRING CHAIN) *** ###
	#prop = App.g_kModelPropertyManager.FindByName("Pulse Weapon System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ### *** TO-DO UNCOMMENT WHEN NEEDED (F.EX. BECAUSE THE TURRETS MAY USE A DIFFERENT CLOAK STRENGTH OR THE PARENT USES A TECH THAT TAKES THAT INTO ACCOUNT) *** ###
	#prop = App.g_kModelPropertyManager.FindByName("Cloaking System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ### TO-DO SHUTTLE BAY SECTION ###
	#prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 1 OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
	#prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
	#prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 2 OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
	#prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
	#prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 3 OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
	#prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
        ### TO-DO IF YOU MODIFY THE WARP ENGINE CONTROL SYSTEM, UNCOMMENT THIS ONE ###
	#prop = App.g_kModelPropertyManager.FindByName("Warp Engine System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
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
        ### TO-DO HERE COME THE NEW WEAPONS ###
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Laser Battery 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Laser Battery 2B", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)