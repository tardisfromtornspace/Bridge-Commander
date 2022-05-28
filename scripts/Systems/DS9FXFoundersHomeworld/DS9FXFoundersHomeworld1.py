import App

def Initialize():
        # Create the set ("DS9FXFoundersHomeworld1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DS9FXFoundersHomeworld1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DS9FXFoundersHomeworld.DS9FXFoundersHomeworld1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("DS9FXFoundersHomeworld1")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DS9FXFoundersHomeworld1_S.py" file with an Initialize function that creates them.
        try:
                import DS9FXFoundersHomeworld1_S
                DS9FXFoundersHomeworld1_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DS9FXFoundersHomeworld1"

def GetSet():
        return App.g_kSetManager.GetSet("DS9FXFoundersHomeworld1")

def Terminate():
        App.g_kSetManager.DeleteSet("DS9FXFoundersHomeworld1")

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
        kThis.ConfigAmbientLight(0.858824, 0.964706, 0.854902, 0.352941)
        kThis.Update(0)
        kThis = None
        # End position "Ambient Light"

        # Light position "Directional Light"
        kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(789.112557, 327998.663998, 9997.889003)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.0, -1.0, 0.0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.752941, 0.000000, 0.752941, 0.850000)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light"

        # Position "Player Start"
        kThis = App.Waypoint_Create("Player Start", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-3.792000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Player Start"

        # Position "Ship1 Location"
        kThis = App.Waypoint_Create("Ship1 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(99.117889, 10212.712008, 2369.007889)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.355461, -0.867025, 0.349163)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.833241, 0.463199, 0.301922)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship1 Location"

        # Position "Ship2 Location"
        kThis = App.Waypoint_Create("Ship2 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-257.001369, 9957.808669, -1145.631631)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship2 Location"

        # Position "Ship3 Location"
        kThis = App.Waypoint_Create("Ship3 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(1011.663892, 8896.819007, -127.315889)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship3 Location"

        # Position "Ship4 Location"
        kThis = App.Waypoint_Create("Ship4 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-2500.887006, 7987.112669, -2367.314333)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship4 Location"

        # Position "Dummy Location"
        kThis = App.Waypoint_Create("Dummy Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-15000.117772, -15000.117772, -15000.117772)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Dummy Location"

        # Position "Sun"
        kThis = App.Waypoint_Create("Sun", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(789.112557, 327998.663998, 9997.889003)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Sun"
        
        kThis = App.Waypoint_Create("SunStr", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(789.112557, 337998.663998, 9997.889003)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None        

        # Position "Planet1"
        kThis = App.Waypoint_Create("Planet1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(897.774413, 51669.001774, 9919.880564)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet1"

import App

def LoadBackdrops(pSet):

        #Draw order is implicit. First object gets drawn first

        # Star Sphere "Backdrop stars"
        kThis = App.StarSphere_Create()
        kThis.SetName("Backdrop stars")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.185766, 0.947862, -0.258937)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.049823, 0.254099, 0.965894)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/sovstars.tga")
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

        # Backdrop Sphere
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Founders01")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.9, 0.5, 0.6)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Founders01.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(1.000000)
        kThis.SetVerticalSpan(1.000000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Founders01")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere
