# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# AIHyperdriveTravel.py
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# Based on SlipstreamTravel TravelerSystem by BCXtreme (https://www.gamefront.com/games/bridge-commander/file/slipstream-for-galaxy-charts), to provide an AI-only alternative to regular HyperdriveTravel, by Alex SL Gato.
# This plugin was originally released without a license, which means it defaults to All Rights Reserved. While the original readme includes the line "As far as I am concerned, anyone can take this and finish it if they want to," that grants permission to continue development — but not to relicense or attach a license such as LGPL. The absence of an explicit license means the work cannot be treated as open source.
# Hyperdrive Module, which this system relies on, and Slipstream Module remain ALL RIGHTS RESERVED, by USS Sovereign.

import App
import Custom.GalaxyCharts.Cartographer
import loadspacehelper
import MissionLib

SET_NAME = "AIHyperdriveTravel"

def LoadTunnel(pSet):
        scale = 1000
        TunnelString = "Hyperdrive Outer"
        pTunnel = loadspacehelper.CreateShip("hyperdrive", pSet, TunnelString, "Player Start")
        fTunnel = MissionLib.GetShip(TunnelString, pSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.4, 0)
        fTunnel.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
        fTunnel.SetInvincible(1)
        fTunnel.SetHurtable(0)
        fTunnel.SetTargetable(0)
        fTunnel.SetCollisionsOn(0)
        fTunnel.SetScale(scale)
def Initialize():
	global SET_NAME
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, SET_NAME)

	pSet.SetRegionModule("Custom.GalaxyCharts.TravelerSystems.AIHyperdriveTravel")

	pSet.SetProximityManagerActive(1)

	LoadPlacements(SET_NAME)
	LoadBackdrops(pSet)

	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	LoadTunnel(pSet)

	Custom.GalaxyCharts.Cartographer.RegionManager.AddRegion(SET_NAME, "Custom.GalaxyCharts.TravelerSystems.AIHyperdriveTravel", None, None)

	return pSet

def GetSetName():
	return SET_NAME

def GetSet():
	return App.g_kSetManager.GetSet(SET_NAME)

def Terminate():
	App.g_kSetManager.DeleteSet(SET_NAME)

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.1)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

        
	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-0.044018, 0.572347, 0.029146)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.076971, 0.995795, 0.049676)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.006766, -0.050345, 0.998709)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.75, 1.0, 1.0, 1)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"


	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"


def LoadBackdrops(pSet):
	# Star Sphere "Backdrop stars"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/hyperdriveback.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"
