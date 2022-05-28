import App
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def Initialize():
        # Create the set ("DS9FXBadlands1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DS9FXBadlands1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DS9FXBadlands.DS9FXBadlands1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("DS9FXBadlands1")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DS9FXBadlands1_S.py" file with an Initialize function that creates them.
        try:
                import DS9FXBadlands1_S
                DS9FXBadlands1_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DS9FXBadlands1"

def GetSet():
        return App.g_kSetManager.GetSet("DS9FXBadlands1")

def Terminate():
        App.g_kSetManager.DeleteSet("DS9FXBadlands1")

def LoadPlacements(sSetName):
        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.BadlandsBrightness == 1:        
                fLight = 0.400000
        else:
                fLight = 0.200000
        
        # Light position "Ambient Light"
        kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
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
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light"

        # Light position "Light 1"
        kThis = App.LightPlacement_Create("Light 1", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(22.816555, 100.199013, -2.373867)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.636835, 0.769229, 0.052230)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.270453, 0.159439, 0.949439)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 1"

        # Light position "Light 2"
        kThis = App.LightPlacement_Create("Light 2", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-35.835716, 87.190208, -4.359001)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.523202, 0.852007, 0.018555)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.040974, -0.046897, 0.998059)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 2"

        # Light position "Light 3"
        kThis = App.LightPlacement_Create("Light 3", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-91.354164, -34.524147, -6.250582)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.971755, -0.233996, -0.030633)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.035329, 0.015901, 0.999249)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 3"

        # Light position "Light 4"
        kThis = App.LightPlacement_Create("Light 4", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(80.335770, -80.028511, -2.042613)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.755354, -0.651704, 0.068716)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.195508, -0.124028, 0.972828)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 4"

        # Light position "Light 5"
        kThis = App.LightPlacement_Create("Light 5", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-52.849483, 77.849579, -59.237331)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.549713, 0.158058, -0.820264)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.396852, 0.814640, 0.422931)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 5"

        # Light position "Light 6"
        kThis = App.LightPlacement_Create("Light 6", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-14.603709, 8.136326, 74.999237)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.132176, -0.185158, 0.973779)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.952907, -0.246777, -0.176266)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 6"

        # Light position "Light 7"
        kThis = App.LightPlacement_Create("Light 7", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(6.279407, -247.139999, 52.899818)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.270445, -0.959662, 0.076866)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.003883, -0.078753, -0.996887)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 7"

        # Light position "Light 8"
        kThis = App.LightPlacement_Create("Light 8", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-168.619034, -184.544968, 56.375729)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.880809, -0.466229, -0.082495)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.028104, 0.122446, -0.992077)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 8"

        # Light position "Light 9"
        kThis = App.LightPlacement_Create("Light 9", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-2.732174, -89.645470, 160.156570)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.143443, 0.341388, 0.928913)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.541613, 0.812662, -0.215028)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 9"

        # Light position "Light 10"
        kThis = App.LightPlacement_Create("Light 10", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-45.746567, -51.219769, -113.326035)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.077031, 0.333891, -0.939459)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.166362, -0.924745, -0.342303)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.790000, 0.590000, fLight)
        kThis.Update(0)
        kThis = None
        # End position "Light 10"

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

        # Position "Vortex 0"
        kThis = App.Waypoint_Create("Vortex 0", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(86.949493, 457.541687, 32.938492)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.040498, 0.997710, 0.054172)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.002645, -0.054109, 0.998532)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 0"

        # Position "Vortex 1"
        kThis = App.Waypoint_Create("Vortex 1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-327.280945, 350.763794, 28.008827)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.084057, 0.994772, 0.057993)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000392, -0.058166, 0.998307)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 1"

        # Position "Vortex 2"
        kThis = App.Waypoint_Create("Vortex 2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-53.590317, 1481.336670, 57.162407)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.048389, 0.998297, 0.032589)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.001695, -0.032709, 0.999463)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 2"

        # Position "Vortex 3"
        kThis = App.Waypoint_Create("Vortex 3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(1095.308472, 2074.256348, 120.289238)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.385474, 0.921599, 0.045438)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.027851, -0.037601, 0.998905)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 3"

        # Position "Vortex 4"
        kThis = App.Waypoint_Create("Vortex 4", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1621.632935, 4372.299316, 217.854462)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.364896, 0.929983, 0.044528)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.031454, -0.035485, 0.998875)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 4"

        # Position "Vortex 5"
        kThis = App.Waypoint_Create("Vortex 5", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(644.671265, 10073.892578, 352.086639)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.064523, 0.997370, 0.033009)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.024555, -0.034655, 0.999098)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 5"

        # Position "Vortex 6"
        kThis = App.Waypoint_Create("Vortex 6", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(1165.535278, 1349.436035, 135.651016)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.590992, 0.804108, 0.064340)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.095756, -0.009266, 0.995362)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 6"

        # Position "Vortex 7"
        kThis = App.Waypoint_Create("Vortex 7", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-2613.330322, 2195.183594, 31.454712)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.766778, 0.641870, 0.007453)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.036376, 0.031857, 0.998830)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 7"

        # Position "Vortex 8"
        kThis = App.Waypoint_Create("Vortex 8", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-3870.676025, 4107.680664, 128.523193)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.686410, 0.726909, 0.021081)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.035962, 0.004977, 0.999341)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 8"

        # Position "Vortex 9"
        kThis = App.Waypoint_Create("Vortex 9", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-626.749939, 1315.430664, 22.206167)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.432520, 0.901585, 0.008469)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.051108, 0.015138, 0.998578)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 9"

        # Position "Vortex 10"
        kThis = App.Waypoint_Create("Vortex 10", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(405.572723, 2841.945557, 63.690464)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.044255, 0.998728, 0.024181)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.053454, -0.026537, 0.998218)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 10"

        # Position "Vortex 11"
        kThis = App.Waypoint_Create("Vortex 11", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(963.338379, -876.211243, 35.278805)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.731813, -0.681311, 0.016288)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.142507, 0.176355, 0.973956)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 11"

        # Position "Vortex 12"
        kThis = App.Waypoint_Create("Vortex 12", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(1305.163574, -1705.833130, 101.487434)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.599682, -0.799053, 0.043546)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.028887, 0.075996, 0.996690)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 12"

        # Position "Vortex 13"
        kThis = App.Waypoint_Create("Vortex 13", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(1144.993652, -2083.700195, 61.740738)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.490600, -0.871056, 0.023946)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.053604, 0.057597, 0.996900)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 13"

        # Position "Vortex 14"
        kThis = App.Waypoint_Create("Vortex 14", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(451.430298, -2068.365234, 35.161118)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.215330, -0.976492, 0.009862)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.143613, 0.041655, 0.988757)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 14"

        # Position "Vortex 15"
        kThis = App.Waypoint_Create("Vortex 15", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-105.706322, -573.158264, 11.592282)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.161375, -0.986891, 0.002214)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.005769, 0.001300, 0.999983)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 15"

        # Position "Vortex 16"
        kThis = App.Waypoint_Create("Vortex 16", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(93.568024, -1038.719116, -1.485175)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.091919, -0.995707, -0.010873)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.009696, -0.011813, 0.999883)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 16"

        # Position "Vortex 17"
        kThis = App.Waypoint_Create("Vortex 17", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-992.290955, -2594.120117, 99.064034)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.295304, -0.954826, 0.033212)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.047736, 0.019974, 0.998660)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 17"

        # Position "Vortex 18"
        kThis = App.Waypoint_Create("Vortex 18", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1257.357544, -1990.445923, 114.217628)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.520613, -0.852463, 0.047639)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.081022, 0.006218, 0.996693)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 18"

        # Position "Vortex 19"
        kThis = App.Waypoint_Create("Vortex 19", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-872.022400, -875.516968, 18.284718)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.642657, -0.766120, 0.007282)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.060467, -0.041243, 0.997318)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 19"

        # Position "Vortex 20"
        kThis = App.Waypoint_Create("Vortex 20", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-2232.804199, -1301.305054, 14.475795)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.852579, -0.522598, 0.000254)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.069006, -0.112096, 0.991298)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 20"

        # Position "Vortex 21"
        kThis = App.Waypoint_Create("Vortex 21", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-2083.214111, -248.622528, 0.524430)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.984735, -0.173989, -0.005046)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.003551, -0.008907, 0.999954)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 21"

        # Position "Vortex 22"
        kThis = App.Waypoint_Create("Vortex 22", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(102.414871, -5043.463867, 28.138664)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.056360, -0.998403, 0.003908)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.010761, 0.003306, 0.999937)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 22"

        # Position "Vortex 23"
        kThis = App.Waypoint_Create("Vortex 23", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1382.220581, -5044.903809, 15.668537)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.252116, -0.967696, 0.000961)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.014448, -0.002771, 0.999892)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 23"

        # Position "Vortex 24"
        kThis = App.Waypoint_Create("Vortex 24", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-593.309265, 2499.481689, 9.208636)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.374334, 0.927294, 0.000266)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.004449, 0.001510, 0.999989)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 24"

        # Position "Vortex 25"
        kThis = App.Waypoint_Create("Vortex 25", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1306.286255, 195.580139, 12.623600)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.993978, 0.108282, -0.016823)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.004973, 0.108787, 0.994053)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 25"

        # Position "Vortex 26"
        kThis = App.Waypoint_Create("Vortex 26", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-11505.244141, 19251.587891, 808.944580)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.730851, 0.681261, 0.041717)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.061804, 0.005185, 0.998075)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 26"

        # Position "Vortex 27"
        kThis = App.Waypoint_Create("Vortex 27", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-11009.881836, 11836.295898, 678.377930)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.316703, 0.946490, 0.062091)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.035574, -0.053562, 0.997931)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 27"

        # Position "Vortex 28"
        kThis = App.Waypoint_Create("Vortex 28", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-4944.472656, 9053.967773, 619.921448)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.943450, -0.330116, -0.030411)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.003154, -0.082793, 0.996562)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 28"

        # Position "Vortex 29"
        kThis = App.Waypoint_Create("Vortex 29", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(598.302185, 24022.365234, 1280.159180)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.225090, -0.970946, -0.081237)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.111795, -0.108562, 0.987783)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 29"

        # Position "Vortex 30"
        kThis = App.Waypoint_Create("Vortex 30", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(6940.606445, 19823.121094, 156.439377)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.621995, -0.781966, -0.040625)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.083655, -0.117948, 0.989490)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 30"

        # Position "Vortex 31"
        kThis = App.Waypoint_Create("Vortex 31", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(6621.495117, 15078.964844, -382.087189)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.621995, -0.781966, -0.040625)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.083655, -0.117948, 0.989490)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 31"

        # Position "Vortex 32"
        kThis = App.Waypoint_Create("Vortex 32", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(11561.260742, 10979.786133, -868.696228)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.779929, -0.622141, 0.068202)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.136952, -0.063316, 0.988552)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 32"

        # Position "Vortex 33"
        kThis = App.Waypoint_Create("Vortex 33", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(10992.105469, 4646.536133, -1058.408936)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.950937, -0.296084, 0.089742)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.116038, -0.072435, 0.990600)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 33"

        # Position "Vortex 34"
        kThis = App.Waypoint_Create("Vortex 34", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(10081.468750, -428.047852, -1003.691101)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.995691, 0.070334, 0.060433)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.057367, -0.044827, 0.997346)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 34"

        # Position "Vortex 35"
        kThis = App.Waypoint_Create("Vortex 35", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(8544.920898, 2338.947754, -789.744080)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.956003, 0.247420, 0.157614)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.126975, -0.135350, 0.982628)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 35"

        # Position "Vortex 36"
        kThis = App.Waypoint_Create("Vortex 36", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(5259.770508, 5537.853516, -161.858017)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.951224, 0.280055, 0.129390)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.110877, -0.081039, 0.990525)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 36"

        # Position "Vortex 37"
        kThis = App.Waypoint_Create("Vortex 37", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1187.246338, 6774.581543, 522.377319)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.848745, 0.518430, 0.104220)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.081446, -0.066577, 0.994452)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 37"

        # Position "Vortex 38"
        kThis = App.Waypoint_Create("Vortex 38", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-5955.792480, -12626.959961, 827.679871)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.206278, 0.975692, -0.073990)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.007725, 0.073990, 0.997229)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 38"

        # Position "Vortex 39"
        kThis = App.Waypoint_Create("Vortex 39", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-6679.241699, -9583.584961, 607.328979)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.206278, 0.975692, -0.073990)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.007725, 0.073990, 0.997229)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 39"

        # Position "Vortex 40"
        kThis = App.Waypoint_Create("Vortex 40", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-6968.830078, -6969.419922, 320.137024)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.782735, 0.622131, -0.016686)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.041024, 0.078330, 0.996083)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 40"

        # Position "Vortex 41"
        kThis = App.Waypoint_Create("Vortex 41", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(3347.081055, -9944.903320, 1087.289673)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.322459, 0.914945, -0.242684)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.051829, 0.238928, 0.969653)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 41"

        # Position "Vortex 42"
        kThis = App.Waypoint_Create("Vortex 42", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(8109.206055, -6582.547363, 666.958252)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.919555, 0.382587, -0.089700)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.039379, 0.137400, 0.989733)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 42"

        # Position "Vortex 43"
        kThis = App.Waypoint_Create("Vortex 43", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(10184.394531, -2176.901123, 107.498550)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.994330, 0.097814, 0.041711)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.052759, 0.113228, 0.992167)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 43"

        # Position "Vortex 44"
        kThis = App.Waypoint_Create("Vortex 44", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(8565.247070, 1303.141602, -203.551956)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.994330, 0.097814, 0.041711)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.052759, 0.113228, 0.992167)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 44"

        # Position "Vortex 45"
        kThis = App.Waypoint_Create("Vortex 45", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(5956.151367, 6072.016602, -554.213928)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.874012, -0.470552, 0.121179)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.070777, 0.123443, 0.989825)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 45"

        # Position "Vortex 46"
        kThis = App.Waypoint_Create("Vortex 46", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(3015.418701, 5921.202148, 223.781052)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 46"

        # Position "Vortex 47"
        kThis = App.Waypoint_Create("Vortex 47", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(1492.249023, 11064.059570, 65.549187)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 47"

        # Position "Vortex 48"
        kThis = App.Waypoint_Create("Vortex 48", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(6561.430664, 9434.124023, -508.188110)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 48"

        # Position "Vortex 49"
        kThis = App.Waypoint_Create("Vortex 49", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(9170.939453, 7672.881348, -738.010437)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 49"

        # Position "Vortex 50"
        kThis = App.Waypoint_Create("Vortex 50", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(10243.831055, 4428.596680, -653.434937)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 50"

        # Position "Vortex 51"
        kThis = App.Waypoint_Create("Vortex 51", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(6440.665039, 4247.380859, -123.220413)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 51"

        # Position "Vortex 52"
        kThis = App.Waypoint_Create("Vortex 52", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(1197.164673, 5541.957031, 498.057068)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 52"

        # Position "Vortex 53"
        kThis = App.Waypoint_Create("Vortex 53", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1000.386536, 8741.585938, 569.635498)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.878928, 0.469095, 0.086227)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.134454, 0.070233, 0.988428)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 53"

        # Position "Vortex 54"
        kThis = App.Waypoint_Create("Vortex 54", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(10913.216797, -4630.005859, 576.584656)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.985502, 0.152296, -0.074774)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.053202, 0.141100, 0.988565)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 54"

        # Position "Vortex 55"
        kThis = App.Waypoint_Create("Vortex 55", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(11464.730469, -21.027002, -51.481888)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.997363, -0.062512, -0.036857)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.045399, 0.141249, 0.988933)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 55"

        # Position "Vortex 56"
        kThis = App.Waypoint_Create("Vortex 56", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(10237.010742, 2336.816162, -444.613495)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.997363, -0.062512, -0.036857)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.045399, 0.141249, 0.988933)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Vortex 56"

def LoadBackdrops(pSet):
        reload(DS9FXSavedConfig)
        # Type 1, 2, 3 or 4?
        if DS9FXSavedConfig.BadlandsBackground == 3:
                # Star Sphere "Backdrop stars"
                kThis = App.StarSphere_Create()
                kThis.SetName("Backdrop stars")
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.185766, 0.947862, -0.258937)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.049823, 0.254099, 0.965894)
                kThis.AlignToVectors(kForward, kUp)
                kThis.SetTextureFileName("data/DS9FXBadlandsBackground.tga")
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

        elif DS9FXSavedConfig.BadlandsBackground == 2:
                # Backdrop Sphere "Backdrop stars"
                kThis = App.StarSphere_Create()
                kThis.SetName("Backdrop stars")
                kThis.SetModelName("data\Models\Environment\DS9FX\DS9FXBadlands3\Badlands.nif")
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"

        elif DS9FXSavedConfig.BadlandsBackground == 1:
                # Select proper detail setting
                if DS9FXSavedConfig.BadlandsBackground == 2:
                        # Backdrop Sphere "Backdrop stars"
                        kThis = App.StarSphere_Create()
                        kThis.SetName("Backdrop stars")
                        kThis.SetModelName("data\Models\Environment\DS9FX\DS9FXBadlands2\High\Badlands.nif")
                        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                        kForward = App.TGPoint3()
                        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                        kUp = App.TGPoint3()
                        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                        kThis.AlignToVectors(kForward, kUp)
                        pSet.AddBackdropToSet(kThis,"Backdrop stars")
                        kThis.Update(0)
                        kThis = None
                        # End Backdrop Sphere "Backdrop stars"                
                elif DS9FXSavedConfig.BadlandsBackground == 1:
                        # Backdrop Sphere "Backdrop stars"
                        kThis = App.StarSphere_Create()
                        kThis.SetName("Backdrop stars")
                        kThis.SetModelName("data\Models\Environment\DS9FX\DS9FXBadlands2\Med\Badlands.nif")
                        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                        kForward = App.TGPoint3()
                        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                        kUp = App.TGPoint3()
                        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                        kThis.AlignToVectors(kForward, kUp)
                        pSet.AddBackdropToSet(kThis,"Backdrop stars")
                        kThis.Update(0)
                        kThis = None
                        # End Backdrop Sphere "Backdrop stars"
                else:
                        # Backdrop Sphere "Backdrop stars"
                        kThis = App.StarSphere_Create()
                        kThis.SetName("Backdrop stars")
                        kThis.SetModelName("data\Models\Environment\DS9FX\DS9FXBadlands2\Low\Badlands.nif")
                        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                        kForward = App.TGPoint3()
                        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                        kUp = App.TGPoint3()
                        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                        kThis.AlignToVectors(kForward, kUp)
                        pSet.AddBackdropToSet(kThis,"Backdrop stars")
                        kThis.Update(0)
                        kThis = None
                        # End Backdrop Sphere "Backdrop stars"

        else:         
                # Backdrop Sphere "Backdrop stars"
                kThis = App.StarSphere_Create()
                kThis.SetName("Backdrop stars")
                kThis.SetModelName("data\Models\Environment\DS9FX\DS9FXBadlands\Badlands.nif")
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"



