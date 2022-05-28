# by USS Sovereign system def

import App

def Initialize():
        # Create the set ("DeepSpace91")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DeepSpace91")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DeepSpace9.DeepSpace91")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("DeepSpace91")
        LoadBackdrops(pSet)

        # Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DeepSpace91_S.py" file with an Initialize function that creates them.
        try:
                import DeepSpace91_S
                DeepSpace91_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DeepSpace91"

def GetSet():
        return App.g_kSetManager.GetSet("DeepSpace91")

def Terminate():
        App.g_kSetManager.DeleteSet("DeepSpace91")

def LoadPlacements(sSetName):
        # Light position "Ambient Light"
        kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.000000, 350000.0000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, -1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(1.000000, 0.898039, 0.341176, 1.000000)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light"

        # Light position "Ambient Light"
        kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigAmbientLight(0.517647, 0.176471, 0.094118, 0.200000)
        kThis.Update(0)
        kThis = None
        # End position "Ambient Light"

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

        # Position "Wormhole Location"
        kThis = App.Waypoint_Create("Wormhole Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(908, 728, 325)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Wormhole Location"

        # Position "Excal Location"
        kThis = App.Waypoint_Create("Excal Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(278, 671, 118)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Excal Location"

        # Position "DS9 Location"
        kThis = App.Waypoint_Create("DS9 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(413, 728, 318)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0, 0, 0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0, 0, 0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "DS9 Location"

        # Position "Defiant Location"
        kThis = App.Waypoint_Create("Defiant Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(413, 451, 262)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Defiant Location"

        # Position "Oregon Location"
        kThis = App.Waypoint_Create("Oregon Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-785, -151, -298)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Oregon Location"

        # Position "Lakota Location"
        kThis = App.Waypoint_Create("Lakota Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-901, -451, -498)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Lakota Location"


        # Position "ExitPoint Location"
        kThis = App.Waypoint_Create("ExitPoint Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(888, 708, 305)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "ExitPoint Location"

        # Position "Random 1 Location"
        kThis = App.Waypoint_Create("Random 1 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(900, 720, 320)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Random 1 Location"


        # Position "Random 2 Location"
        kThis = App.Waypoint_Create("Random 2 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(890, 710, 315)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Random 2 Location"


        # Position "Random 3 Location"
        kThis = App.Waypoint_Create("Random 3 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(880, 710, 305)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Random 3 Location"


        # Position "Random 4 Location"
        kThis = App.Waypoint_Create("Random 4 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(870, 700, 300)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Random 4 Location"

        # Position "Random 5 Location"
        kThis = App.Waypoint_Create("Random 5 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(860, 690, 290)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Random 5 Location" 

        # Position "Comet Location"
        kThis = App.Waypoint_Create("Comet Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-213, 3228, -218)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0, 0, 0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0, 0, 0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Comet Location"

        # Position "Sun"
        kThis = App.Waypoint_Create("Sun", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.0, 350000.0, 0.0)
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
        kThis.SetTranslateXYZ(0.0, 360000.0, 0.0)
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
        kThis.SetTranslateXYZ(400, 121000.0, 35.0)
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
        kThis.SetTranslateXYZ(3100, 107000.0, 2150.0)
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
        kThis.SetTranslateXYZ(-4210, 95000.0, -2150.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet3"

        # Position "Planet4"
        kThis = App.Waypoint_Create("Planet4", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-6210, 81000.0, -3880.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet4"


        # Position "Planet5"
        kThis = App.Waypoint_Create("Planet5", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(5710, 68000.0, -4000.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet5"

        # Position "Planet6"
        kThis = App.Waypoint_Create("Planet6", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(4210, 49000.0, 1070.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet6" 

        # Position "Planet7"
        kThis = App.Waypoint_Create("Planet7", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-3210, 35000.0, 140.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet7"  

        # Position "Planet8"
        kThis = App.Waypoint_Create("Planet8", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-1710, 17000.0, 40.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet8"  

        # Position "Planet9"
        kThis = App.Waypoint_Create("Planet9", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-1210, 7000.0, 1440.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet9"  

        # Position "Planet10"
        kThis = App.Waypoint_Create("Planet10", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-3510, -8000.0, 1740.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet10"  

        # Position "Planet11"
        kThis = App.Waypoint_Create("Planet11", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1810, -21000.0, -2740.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet11"  

        # Position "Planet12"
        kThis = App.Waypoint_Create("Planet12", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(2510, -34000.0, -1740.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet12"  

        # Position "Planet13"
        kThis = App.Waypoint_Create("Planet13", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(2110, -51000.0, 1740.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet13"  

        # Position "Planet14"
        kThis = App.Waypoint_Create("Planet14", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1410, -68000.0, -740.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet14"   

        # Position "Way1"
        kThis = App.Waypoint_Create("Way1", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(444, 7778, 777)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0, 0 ,0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0, 0, 0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Way1"

        # Position "Way2"
        kThis = App.Waypoint_Create("Way2", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(557, 370000, 899)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0, 0 ,0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0, 0, 0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Way2"


        # Position "Way3"
        kThis = App.Waypoint_Create("Way3", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1203, 150000, -7777)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0, 0, 0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0, 0, 0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Way3"


        # Position "Way4"
        kThis = App.Waypoint_Create("Way4", sSetName, None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-477, 10000, -777)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0, 0, 0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0, 0, 0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Way4"

        # Position "WarpIn 1"
        kThis = App.Waypoint_Create("WarpIn 1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(255, 656, 117)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "WarpIn 1"

        # Position "WarpIn 2"
        kThis = App.Waypoint_Create("WarpIn 2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(299, 575, 128)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "WarpIn 2"


        # Position "WarpIn 3"
        kThis = App.Waypoint_Create("WarpIn 3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(414, 444, 130)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "WarpIn 3"

        # Position "WarpIn 4"
        kThis = App.Waypoint_Create("WarpIn 4", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(313, 525, 201)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "WarpIn 4"

        # Position "Help1"
        kThis = App.Waypoint_Create("Help1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(2002, 1987, 1777)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Help1"

        # Position "Help2"
        kThis = App.Waypoint_Create("Help2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(2097, 2002, 1877)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Help2"


        # Position "Help3"
        kThis = App.Waypoint_Create("Help3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(2122, 2117, 2004)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Help3"

        # Position "RetakePlayerPos"
        kThis = App.Waypoint_Create("RetakePlayerPos", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1410, -2000.0, -740.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "RetakePlayerPos"   

        # Position "FriendlyPos1"
        kThis = App.Waypoint_Create("FriendlyPos1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1430, -2789.0, -750.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "FriendlyPos1" 

        # Position "FriendlyPos2"
        kThis = App.Waypoint_Create("FriendlyPos2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1429, -2912.0, -760.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "FriendlyPos2" 

        # Position "FriendlyPos3"
        kThis = App.Waypoint_Create("FriendlyPos3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1447, -2616.0, -757.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "FriendlyPos3" 

        # Position "FriendlyPos3"
        kThis = App.Waypoint_Create("FriendlyPos4", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1437, -2716.0, -752.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "FriendlyPos4" 

        # Position "FriendlyPos5"
        kThis = App.Waypoint_Create("FriendlyPos5", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1412, -2719.0, -724.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "FriendlyPos5" 

        # Position "EnemyPos1"
        kThis = App.Waypoint_Create("EnemyPos1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1412, -1019.0, -731.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "EnemyPos1"


        # Position "EnemyPos2"
        kThis = App.Waypoint_Create("EnemyPos2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1412, -988.0, -631.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "EnemyPos2"

        # Position "EnemyPos3"
        kThis = App.Waypoint_Create("EnemyPos3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1312, -988.0, -631.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "EnemyPos3"

        # Position "EnemyPos4"
        kThis = App.Waypoint_Create("EnemyPos4", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1412, -1001.0, -712.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "EnemyPos4"

        # Position "EnemyPos5"
        kThis = App.Waypoint_Create("EnemyPos5", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1412, -1055.0, -731.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "EnemyPos5"

        # Position "EnemyPos6"
        kThis = App.Waypoint_Create("EnemyPos6", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1369, -1064.0, -705.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "EnemyPos6"

        # Position "EnemyPos7"
        kThis = App.Waypoint_Create("EnemyPos7", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(1369, -1079.0, -755.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "EnemyPos7"

        # Position "MalinchePos"
        kThis = App.Waypoint_Create("MalinchePos", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(2369, -2079.0, -745.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "MalinchePos"

        # Position "DomDread Pos"
        kThis = App.Waypoint_Create("DomDread Pos", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(4369, -5079.0, -2745.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "DomDread Pos"

        # Position "Entry Location"
        kThis = App.Waypoint_Create("Entry Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(758, 728, 325)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Entry Location"


        # Insert waypoints
        kThis = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Comet Location") )
        kPrevious = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Way1") )
        kThis.InsertAfterObj( kPrevious )
        kThis = kPrevious = None

        kThis = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Way1") )
        kPrevious = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Way2") )
        kThis.InsertAfterObj( kPrevious )
        kThis = kPrevious = None

        kThis = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Way2") )
        kPrevious = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Way3") )
        kThis.InsertAfterObj( kPrevious )
        kThis = kPrevious = None

        kThis = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Way3") )
        kPrevious = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "Way4") )
        kThis.InsertAfterObj( kPrevious )
        kThis = kPrevious = None



import App

def LoadBackdrops(pSet):

        # Draw order is implicit. First object gets drawn first

        # Star Sphere "Backdrop sovstars"
        kThis = App.StarSphere_Create()
        kThis.SetName("Backdrop sovstars")
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
        pSet.AddBackdropToSet(kThis,"Backdrop sovstars")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop sovstars"

        # Backdrop Sphere "Backdrop Bajor01"
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Bajor01")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.999987, 0.000499, -0.005087)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.005087, -0.000011, 0.999987)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Bajor01.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.252500)
        kThis.SetVerticalSpan(0.505000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop back1")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop Bajor01"

