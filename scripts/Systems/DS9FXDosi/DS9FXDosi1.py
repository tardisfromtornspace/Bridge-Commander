import App

def Initialize():
        # Create the set ("DS9FXDosi1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DS9FXDosi1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DS9FXDosi.DS9FXDosi1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("DS9FXDosi1")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DS9FXDosi1_S.py" file with an Initialize function that creates them.
        try:
                import DS9FXDosi1_S
                DS9FXDosi1_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DS9FXDosi1"

def GetSet():
        return App.g_kSetManager.GetSet("DS9FXDosi1")

def Terminate():
        App.g_kSetManager.DeleteSet("DS9FXDosi1")

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
        kThis.ConfigAmbientLight(0.792157, 0.066667, 1.000000, 0.117647)
        kThis.Update(0)
        kThis = None
        # End position "Ambient Light"

        # Light position "Directional Light"
        kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-329.474894, 317863.785256, -2975.656789)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.0, -1.0, 0.0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.657891, 0.901289, 0.957788, 0.900000)
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

        # Position "Sun"
        kThis = App.Waypoint_Create("Sun", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-329.474894, 317863.785256, -2975.656789)
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
        kThis.SetTranslateXYZ(-329.474894, 327863.785256, -2975.656789)
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
        kThis.SetTranslateXYZ(574.626789, 12297.713074, 275.998574)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet1"

        # Position "Planet2"
        kThis = App.Waypoint_Create("Planet2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-976.111785, 57201.667031, -1303.112371)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet2"

        # Position "Planet3"
        kThis = App.Waypoint_Create("Planet3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(2704.115589, 92703.338912, 1907.369878)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet3"

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
        kThis.SetName("Backdrop Dosi01")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.8, 0.5, 0.3)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Dosi01.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.512500)
        kThis.SetVerticalSpan(0.525000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Dosi01")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere
