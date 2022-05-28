import App

def Initialize():
        # Create the set ("DS9FXKurill1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DS9FXKurill1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DS9FXKurill.DS9FXKurill1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("DS9FXKurill1")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DS9FXKurill1_S.py" file with an Initialize function that creates them.
        try:
                import DS9FXKurill1_S
                DS9FXKurill1_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DS9FXKurill1"

def GetSet():
        return App.g_kSetManager.GetSet("DS9FXKurill1")

def Terminate():
        App.g_kSetManager.DeleteSet("DS9FXKurill1")

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
        kThis.ConfigAmbientLight(0.552941, 0.717647, 0.960784, 0.411765)
        kThis.Update(0)
        kThis = None
        # End position "Ambient Light"

        # Light position "Directional Light"
        kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-729.447221, 299863.998545, -1012.110665)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.0, -1.0, 0.0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.274510, 0.294118, 0.882353)
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
        kThis.SetTranslateXYZ(-12.663001, 2198.115002, -5117.711009)
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
        kThis.SetTranslateXYZ(1098.313008, 789.3005998, 1006.313669)
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
        kThis.SetTranslateXYZ(-6603.336998, -3001.779880, 101.445998)
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
        kThis.SetTranslateXYZ(-101.002556, -3012.449332, 54.721556)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship4 Location"

        # Position "Ship5 Location"
        kThis = App.Waypoint_Create("Ship5 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-721.772827, 4430.243378, 4450.013559)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship5 Location"

        # Position "Sun"
        kThis = App.Waypoint_Create("Sun", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-729.447221, 299863.998545, -1012.110665)
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
        kThis.SetTranslateXYZ(-729.447221, 309863.998545, -1012.110665)
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
        kThis.SetTranslateXYZ(-667.313556, 75601.889302, -3011.001396)
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
        kThis.SetTranslateXYZ(-801.364789, 32021.336995, 2107.313001)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet2"

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
        kThis.SetName("Backdrop Kurrill01")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.6, 0.2, 0.7)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Kurrill01.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.802500)
        kThis.SetVerticalSpan(0.855000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Kurrill01")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere
