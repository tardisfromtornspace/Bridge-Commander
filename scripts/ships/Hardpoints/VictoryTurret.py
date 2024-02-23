# C:\Utopia\Current\Build\scripts\ships\Hardpoints\VictoryTurret.py
# 

# This will import the generic template and add the appropiate weapons

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.GenericVictoryTurretTemplate" # TO-DO Change "ships.Hardpoints.GenericTemplate" for "ships.Hardpoints.GenericTurretTemplate" or the ones needed
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.GenericVictoryTurretTemplate", globals(), locals(), ['*']) # TO-DO Change "ships.Hardpoints.GenericTemplate" for "ships.Hardpoints.GenericTurretTemplate" or the ones needed
	reload(ParentModule)


# Setting up local templates.
# TO-DO REMEMBER TO REALISTICALLY CHANGE MASS (15.000000 is Shuttle Mass, 18000.000000 is Sovereign Mass), ROTATIONAL INERTIA, SHIP NAME, AND POSSIBLY SETMODELFILENAME, ALBEIT THE LATTER IS UNUSED
#################################################
Ship = App.ShipProperty_Create("Ship")

Ship.SetGenus(1)
Ship.SetSpecies(1)
Ship.SetMass(0.400000)
Ship.SetRotationalInertia(20000.000000)
Ship.SetShipName("VictoryTurret")
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
Quantom12 = App.PhaserProperty_Create("Quantom 12")

Quantom12.SetMaxCondition(550.000000)
Quantom12.SetCritical(0)
Quantom12.SetTargetable(1)
Quantom12.SetPrimary(1)
Quantom12.SetPosition(0.000000, 0.50000, 0.000000)
Quantom12.SetPosition2D(64.000000, 15.000000)
Quantom12.SetRepairComplexity(8.000000)
Quantom12.SetDisabledPercentage(0.750000)
Quantom12.SetRadius(0.200000)
Quantom12.SetDumbfire(0)
Quantom12.SetWeaponID(1)
Quantom12.SetGroups(0)
Quantom12.SetDamageRadiusFactor(0.100000)
Quantom12.SetIconNum(363)
Quantom12.SetIconPositionX(63.000000)
Quantom12.SetIconPositionY(60.000000)
Quantom12.SetIconAboveShip(1)
Quantom12.SetFireSound("Xray")
Quantom12.SetMaxCharge(3.100000)
Quantom12.SetMaxDamage(300.000000)
Quantom12.SetMaxDamageDistance(60.000000)
Quantom12.SetMinFiringCharge(10.000000)
Quantom12.SetNormalDischargeRate(3.000000)
Quantom12.SetRechargeRate(1.000000)
Quantom12.SetIndicatorIconNum(511)
Quantom12.SetIndicatorIconPositionX(57.000000)
Quantom12.SetIndicatorIconPositionY(60.000000)
Quantom12Forward = App.TGPoint3()
Quantom12Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Quantom12Up = App.TGPoint3()
Quantom12Up.SetXYZ(0.000000, 0.000000, 1.000000)
Quantom12.SetOrientation(Quantom12Forward, Quantom12Up)
Quantom12.SetWidth(0.001000)
Quantom12.SetLength(0.010000)
Quantom12.SetArcWidthAngles(-1.047198, 1.404533)
Quantom12.SetArcHeightAngles(-2.274533, 2.274533)
Quantom12.SetPhaserTextureStart(24)
Quantom12.SetPhaserTextureEnd(31)
Quantom12.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.801961, 1.000000, 0.501961, 1.000000)
Quantom12.SetOuterShellColor(kColor)
kColor.SetRGBA(0.300000, 1.000000, 0.000000, 1.000000)
Quantom12.SetInnerShellColor(kColor)
kColor.SetRGBA(0.300000, 1.000000, 0.247059, 1.000000)
Quantom12.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
Quantom12.SetInnerCoreColor(kColor)
Quantom12.SetNumSides(6)
Quantom12.SetMainRadius(0.080000)
Quantom12.SetTaperRadius(0.000000)
Quantom12.SetCoreScale(0.400000)
Quantom12.SetTaperRatio(0.000000)
Quantom12.SetTaperMinLength(0.000000)
Quantom12.SetTaperMaxLength(0.000000)
Quantom12.SetLengthTextureTilePerUnit(0.500000)
Quantom12.SetPerimeterTile(1.000000)
Quantom12.SetTextureSpeed(2.500000)
Quantom12.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Quantom12)
#################################################
Quantom13 = App.PhaserProperty_Create("Quantom 13")

Quantom13.SetMaxCondition(500.000000)
Quantom13.SetCritical(0)
Quantom13.SetTargetable(1)
Quantom13.SetPrimary(1)
Quantom13.SetPosition(0.100000, 0.50000, 0.000000)
Quantom13.SetPosition2D(64.000000, 15.000000)
Quantom13.SetRepairComplexity(8.000000)
Quantom13.SetDisabledPercentage(0.750000)
Quantom13.SetRadius(0.200000)
Quantom13.SetDumbfire(0)
Quantom13.SetWeaponID(1)
Quantom13.SetGroups(0)
Quantom13.SetDamageRadiusFactor(0.100000)
Quantom13.SetIconNum(363)
Quantom13.SetIconPositionX(63.000000)
Quantom13.SetIconPositionY(60.000000)
Quantom13.SetIconAboveShip(1)
Quantom13.SetFireSound("Xray")
Quantom13.SetMaxCharge(3.200000)
Quantom13.SetMaxDamage(250.000000)
Quantom13.SetMaxDamageDistance(60.000000)
Quantom13.SetMinFiringCharge(10.000000)
Quantom13.SetNormalDischargeRate(3.000000)
Quantom13.SetRechargeRate(1.000000)
Quantom13.SetIndicatorIconNum(511)
Quantom13.SetIndicatorIconPositionX(57.000000)
Quantom13.SetIndicatorIconPositionY(60.000000)
Quantom13Forward = App.TGPoint3()
Quantom13Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Quantom13Up = App.TGPoint3()
Quantom13Up.SetXYZ(0.000000, 0.000000, 1.000000)
Quantom13.SetOrientation(Quantom13Forward, Quantom13Up)
Quantom13.SetWidth(0.001000)
Quantom13.SetLength(0.010000)
Quantom13.SetArcWidthAngles(-1.047198, 1.404533)
Quantom13.SetArcHeightAngles(-2.274533, 2.274533)
Quantom13.SetPhaserTextureStart(24)
Quantom13.SetPhaserTextureEnd(31)
Quantom13.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.801961, 1.000000, 0.501961, 1.000000)
Quantom13.SetOuterShellColor(kColor)
kColor.SetRGBA(0.300000, 1.000000, 0.000000, 1.000000)
Quantom13.SetInnerShellColor(kColor)
kColor.SetRGBA(0.300000, 1.000000, 0.247059, 1.000000)
Quantom13.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
Quantom13.SetInnerCoreColor(kColor)
Quantom13.SetNumSides(6)
Quantom13.SetMainRadius(0.080000)
Quantom13.SetTaperRadius(0.000000)
Quantom13.SetCoreScale(0.400000)
Quantom13.SetTaperRatio(0.000000)
Quantom13.SetTaperMinLength(0.000000)
Quantom13.SetTaperMaxLength(0.000000)
Quantom13.SetLengthTextureTilePerUnit(0.500000)
Quantom13.SetPerimeterTile(1.000000)
Quantom13.SetTextureSpeed(2.500000)
Quantom13.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Quantom13)
#################################################
Quantom14 = App.PhaserProperty_Create("Quantom 14")

Quantom14.SetMaxCondition(500.000000)
Quantom14.SetCritical(0)
Quantom14.SetTargetable(1)
Quantom14.SetPrimary(1)
Quantom14.SetPosition(-0.100000, 0.50000, 0.000000)
Quantom14.SetPosition2D(64.000000, 15.000000)
Quantom14.SetRepairComplexity(8.000000)
Quantom14.SetDisabledPercentage(0.750000)
Quantom14.SetRadius(0.200000)
Quantom14.SetDumbfire(0)
Quantom14.SetWeaponID(1)
Quantom14.SetGroups(0)
Quantom14.SetDamageRadiusFactor(0.100000)
Quantom14.SetIconNum(363)
Quantom14.SetIconPositionX(63.000000)
Quantom14.SetIconPositionY(60.000000)
Quantom14.SetIconAboveShip(1)
Quantom14.SetFireSound("Xray")
Quantom14.SetMaxCharge(3.200000)
Quantom14.SetMaxDamage(250.000000)
Quantom14.SetMaxDamageDistance(60.000000)
Quantom14.SetMinFiringCharge(10.000000)
Quantom14.SetNormalDischargeRate(3.000000)
Quantom14.SetRechargeRate(1.000000)
Quantom14.SetIndicatorIconNum(511)
Quantom14.SetIndicatorIconPositionX(57.000000)
Quantom14.SetIndicatorIconPositionY(60.000000)
Quantom14Forward = App.TGPoint3()
Quantom14Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Quantom14Up = App.TGPoint3()
Quantom14Up.SetXYZ(0.000000, 0.000000, 1.000000)
Quantom14.SetOrientation(Quantom14Forward, Quantom14Up)
Quantom14.SetWidth(0.001000)
Quantom14.SetLength(0.010000)
Quantom14.SetArcWidthAngles(-1.047198, 1.404533)
Quantom14.SetArcHeightAngles(-2.274533, 2.274533)
Quantom14.SetPhaserTextureStart(24)
Quantom14.SetPhaserTextureEnd(31)
Quantom14.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.801961, 1.000000, 0.501961, 1.000000)
Quantom14.SetOuterShellColor(kColor)
kColor.SetRGBA(0.300000, 1.000000, 0.000000, 1.000000)
Quantom14.SetInnerShellColor(kColor)
kColor.SetRGBA(0.300000, 1.000000, 0.247059, 1.000000)
Quantom14.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
Quantom14.SetInnerCoreColor(kColor)
Quantom14.SetNumSides(6)
Quantom14.SetMainRadius(0.080000)
Quantom14.SetTaperRadius(0.000000)
Quantom14.SetCoreScale(0.400000)
Quantom14.SetTaperRatio(0.000000)
Quantom14.SetTaperMinLength(0.000000)
Quantom14.SetTaperMaxLength(0.000000)
Quantom14.SetLengthTextureTilePerUnit(0.500000)
Quantom14.SetPerimeterTile(1.000000)
Quantom14.SetTextureSpeed(2.500000)
Quantom14.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Quantom14)



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
	prop = App.g_kModelPropertyManager.FindByName("Quantom 12", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Quantom 13", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Quantom 14", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)