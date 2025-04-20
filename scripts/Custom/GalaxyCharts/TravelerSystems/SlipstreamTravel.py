import App
import Custom.GalaxyCharts.Cartographer
import loadspacehelper
import MissionLib

SET_NAME = "SlipstreamTravel"

def LoadTunnel(pSet):
        scale = 1000
        TunnelString = "Slipstream Outer"
        pTunnel = loadspacehelper.CreateShip("slipstream", pSet, TunnelString, "Player Start")
        fTunnel = MissionLib.GetShip(TunnelString, pSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.4, 0)
        fTunnel.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
        fTunnel.SetInvincible(1)
        fTunnel.SetHurtable(0)
        fTunnel.SetTargetable(0)
        fTunnel.SetCollisionsOn(0)
        fTunnel.SetScale(scale)

        TunnelString2 = "Slipstream Inner"
        pTunnel = loadspacehelper.CreateShip("slipstream", pSet, TunnelString2, "Player Start")
        fTunnel2 = MissionLib.GetShip(TunnelString2, pSet)

	fTunnel2.EnableCollisionsWith(fTunnel, 0)
        vCurVelocity2 = App.TGPoint3()
        vCurVelocity2.SetXYZ(0, 0.8, 0)
        fTunnel2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
        fTunnel2.SetInvincible(1)
        fTunnel2.SetHurtable(0)
        fTunnel2.SetTargetable(0)
        fTunnel2.SetCollisionsOn(0)
        fTunnel2.SetScale(scale)

def Initialize():
	global SET_NAME
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, SET_NAME)

	pSet.SetRegionModule("Custom.GalaxyCharts.TravelerSystems.SlipstreamTravel")

	pSet.SetProximityManagerActive(1)

	LoadPlacements(SET_NAME)
	LoadBackdrops(pSet)

	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	LoadTunnel(pSet)

	Custom.GalaxyCharts.Cartographer.RegionManager.AddRegion(SET_NAME, "Custom.GalaxyCharts.TravelerSystems.SlipstreamTravel", None, None)

	return pSet

def GetSetName():
	return SET_NAME

def GetSet():
	return App.g_kSetManager.GetSet(SET_NAME)

def Terminate():
	App.g_kSetManager.DeleteSet(SET_NAME)

def LoadPlacements(sSetName):
	vPlayer = (0.0, 0.0, 0.0)
	vAmbientLight = (0.0, 0.0, 0.0)
	vLight = (3714.28564453, 3000.0, 0.0)
	vLight2 = (3714.28564453, -3000.0, 0.0)

	# --------------------------------------------- AMBIENT LIGHTNING

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vAmbientLight[0], vAmbientLight[1], vAmbientLight[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.0, 1.0, 1.0, 0.1)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# --------------------------------------------------- DIRECTIONAL LIGHTNING
	
	# Light position "Sun Light"
	kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vLight[0], vLight[1], vLight[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.0, 1.0, 1.0, 0.80)
	kThis.Update(0)
	kThis = None
	# End position "Sun Light"

	# Light position "Sun Light"
	kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vLight2[0], vLight2[1], vLight2[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.0, 1.0, 1.0, 0.80)
	kThis.Update(0)
	kThis = None
	# End position "Sun Light"

	# ----------------------------------------------------- A Few Waypoints...

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vPlayer[0], vPlayer[1], vPlayer[2])
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
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049821, 0.254100, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(35000.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"
