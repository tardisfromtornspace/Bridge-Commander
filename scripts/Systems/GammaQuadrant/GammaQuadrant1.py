# by USS Sovereign a system def

import App

def Initialize():
        # Create the set ("GammaQuadrant1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "GammaQuadrant1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.GammaQuadrant.GammaQuadrant1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("GammaQuadrant1")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "GammaQuadrant1_S.py" file with an Initialize function that creates them.
        try:
                import GammaQuadrant1_S
                GammaQuadrant1_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "GammaQuadrant1"

def GetSet():
        return App.g_kSetManager.GetSet("GammaQuadrant1")

def Terminate():
        App.g_kSetManager.DeleteSet("GammaQuadrant1")

def LoadPlacements(sSetName):
        # Light position "Directional Light 1"
        #This will be the light comming from Sun 1
        kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(0.000000, -350000.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.764706, 0.949020, 1.000000, 1.000000)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light 1"

        # Light position "Directional Light 2"
        #This will be the light comming from Sun 2
        kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-50000.000000, -350000.000000, -35000.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.764706, 0.949020, 1.000000, 1.000000)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light 2"

        # Light position "Directional Light 3"
        #This will be the light comming from Sun 3
        kThis = App.LightPlacement_Create("Directional Light 3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(50000.000000, -350000.000000, 35000.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.764706, 0.949020, 1.000000, 1.000000)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light 3"

        # Light position "Ambient Light"
        #Fill light, this will be the illum coming from distant stars/ nebulae.
        kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-0.044018, 0.572347, 0.029146)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.076971, 0.995795, 0.049677)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.006752, -0.050344, 0.998709)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigAmbientLight(0.317647, 0.419608, 0.450980, 0.250000)
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

        # Position "Bugship1 Location"
        kThis = App.Waypoint_Create("Bugship1 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-301, -351, -398)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Bugship1 Location"

        # Position "Bugship2 Location"
        kThis = App.Waypoint_Create("Bugship2 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-501, -451, -298)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Bugship2 Location"


        # Position "Bugship3 Location"
        kThis = App.Waypoint_Create("Bugship3 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-401, -651, -598)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Bugship3 Location"

        # Position "Wormhole Location"
        kThis = App.Waypoint_Create("Wormhole Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(801, 700, 600)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Wormhole Location"

        # Position "ExitPoint Location"
        kThis = App.Waypoint_Create("ExitPoint Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(781, 680, 580)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "ExitPoint Location"

        # Position "Odyssey"
        kThis = App.Waypoint_Create("Odyssey", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(771, 670, 570)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Odyssey"

        # Position "Sun"
        kThis = App.Waypoint_Create("Sun", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.0, -350000.0, 0.0)
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
        kThis.SetTranslateXYZ(0.0, -360000.0, 0.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None        

        # Position "Sun2"
        kThis = App.Waypoint_Create("Sun2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-50000, -350000.0, -35000.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Sun2"
        
        kThis = App.Waypoint_Create("Sun2Str", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-50000, -360000.0, -35000.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None

        # Position "Sun3"
        kThis = App.Waypoint_Create("Sun3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(50000, -350000.0, 35000.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Sun3"
        
        kThis = App.Waypoint_Create("Sun3Str", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(50000, -360000.0, 35000.0)
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
        kThis.SetTranslateXYZ(-900, -71000.0, -35.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet1"

        # Position "Bugship 4 Mission Location"
        kThis = App.Waypoint_Create("Bugship 4 Mission Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1901, -2551, -498)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Bugship 4 Mission Location"

        # Position "Location 1"
        kThis = App.Waypoint_Create("Location 1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-777, -654, -498)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Location 1"


        # Position "Location 2"
        kThis = App.Waypoint_Create("Location 2", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-652, -444, -515)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Location 2"

        # Position "Location 3"
        kThis = App.Waypoint_Create("Location 3", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-2007, -4597, -271)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Location 3"

        # Position "Location 4"
        kThis = App.Waypoint_Create("Location 4", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-678, -212, -414)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Location 4"


        # Position "Location 5"
        kThis = App.Waypoint_Create("Location 5", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1111, -414, -201)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Location 5"

        # Position "Location 6"
        kThis = App.Waypoint_Create("Location 6", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1278, -641, -713)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Location 6"

        # Position "Location 7"
        kThis = App.Waypoint_Create("Location 7", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1347, -215, -401)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Location 7"

        # Position "Entry Location"
        kThis = App.Waypoint_Create("Entry Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(951, 700, 600)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.417716, -0.620277, -0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.898685, -0.389602, -0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Entry Location"


import App

def LoadBackdrops(pSet):

        #Draw order is implicit. First object gets drawn first

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

        # Backdrop Sphere "Backdrop Gamma01"
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Gamma01")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(1.0, -0.5, 0.2)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Gamma01.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.302500)
        kThis.SetVerticalSpan(0.605000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Gamma01")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop Gamma01"
