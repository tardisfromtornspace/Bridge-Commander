import App

def Initialize():
        # Create the set ("DS9FXQonos1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DS9FXQonos1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DS9FXQonos.DS9FXQonos1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("DS9FXQonos1")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DS9FXQonos1_S.py" file with an Initialize function that creates them.
        try:
                import DS9FXQonos1_S
                DS9FXQonos1_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DS9FXQonos1"

def GetSet():
        return App.g_kSetManager.GetSet("DS9FXQonos1")

def Terminate():
        App.g_kSetManager.DeleteSet("DS9FXQonos1")

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
        kThis.ConfigAmbientLight(0.098039, 0.882353, 0.098039, 0.196078)
        kThis.Update(0)
        kThis = None
        # End position "Ambient Light"

        # Light position "Directional Light"
        kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(2507.885527, -350000.4433678, 0.885750)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.984314, 0.623529, 0.301961, 0.884314)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light"

        # Position "Player Start"
        kThis = App.Waypoint_Create("Player Start", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.417716, 0.620277, 0.663905)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.898685, 0.389602, 0.201435)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Player Start"

        # Position "Colony"
        kThis = App.Waypoint_Create("Colony", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.000000, -70784.442678, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Colony"
        
        # Position "Planet1"
        kThis = App.Waypoint_Create("Planet1", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(8970.789445, -132784.442678, -657.661678)
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
        kThis.SetTranslateXYZ(1126.456112, -107112.636977, -717.555788)
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
        kThis.SetTranslateXYZ(-4456.721556, -49669.442678, 7269.721557)
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
        kThis.SetTranslateXYZ(1027.102788, -9121.442678, -3012.446993)
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
        kThis.SetTranslateXYZ(3069.992339, 3798.000717, 101.499313)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Planet5"            
                
        # Asteroid Field Position "Praxis Remains"
        kThis = App.AsteroidFieldPlacement_Create("Praxis Remains", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(3500.0, -19000.776635, 1200.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 1.000000, 0.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetFieldRadius(700.0)
        kThis.SetNumTilesPerAxis(3)
        kThis.SetNumAsteroidsPerTile(15)
        kThis.SetAsteroidSizeFactor(10.0)
        kThis.UpdateNodeOnly()
        kThis.ConfigField()
        kThis.Update(0)
        kThis = None
        # End position "Praxis Remains"

        # Position "Nav Field"
        kThis = App.Waypoint_Create("Praxis Remains", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(1)
        kThis.SetTranslateXYZ(3500.0, -67000.776635, 1200.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 1.000000, 0.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.0)
        kThis.Update(0)
        kThis = None
        # End position "Nav Field"	

        # Position "Sun"
        kThis = App.Waypoint_Create("Sun", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(2507.885527, -350000.4433678, 0.885750)
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
        kThis.SetTranslateXYZ(2507.885527, -360000.4433678, 0.885750)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None        

        # Position "Ship1 Location"
        kThis = App.Waypoint_Create("Ship1 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-7789.236778, -3578.890789, -3314.449678)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship1 Location"	
        
        # Position "Ship2 Location"
        kThis = App.Waypoint_Create("Ship2 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-4237.556637, -9919.815769, 2278.721565)
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
        kThis.SetTranslateXYZ(4478.896001, 1089.890789, -12369.800017)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.240966, -0.644563, 0.725586)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.921099, 0.387441, 0.038282)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Ship3 Location"	        

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

        # Backdrop Sphere "Backdrop Qonos01"
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Qonos01")
        kThis.SetTranslateXYZ(0.000000, 1.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(1.0, 2.5, 0.0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 1.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Qonos01.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.200000)
        kThis.SetVerticalSpan(0.200000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Qonos01")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop Qonos01"
