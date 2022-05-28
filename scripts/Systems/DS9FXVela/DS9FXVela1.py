import App

def Initialize():
        # Create the set ("DS9FXVela1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DS9FXVela1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DS9FXVela.DS9FXVela1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("DS9FXVela1")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DS9FXVela1_S.py" file with an Initialize function that creates them.
        try:
                import DS9FXVela1_S
                DS9FXVela1_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DS9FXVela1"

def GetSet():
        return App.g_kSetManager.GetSet("DS9FXVela1")

def Terminate():
        App.g_kSetManager.DeleteSet("DS9FXVela1")
        
def LoadPlacements(sSetName):
        # Light position "Ambient Light"
        kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigAmbientLight(0.960784, 0.960784, 0.160784, 0.372549)
        kThis.Update(0)
        kThis = None
        # End position "Ambient Light"

        # Light position "Directional Light"
        kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(17099.0, 405163.0, 1573.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.921569, 0.945098, 0.945098, 1)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light"

        # Position "Player Start"
        kThis = App.Waypoint_Create("Player Start", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(771.669336, -529.177553, 0.696633)
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
        kThis.SetTranslateXYZ(17099.0, 405163.0, 1573.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Sun"
        
        kThis = App.Waypoint_Create("FlashPosition", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(17599.0, 390163.0, 2073.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None     
        
        kThis = App.Waypoint_Create("SunBeamPosition", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(17099.0, 410163.0, 1573.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, -1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None   
        
        kThis = App.Waypoint_Create("Pulsar Direction", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(1)
        kThis.SetTranslateXYZ(17099.0, 150000.0, 1573.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 1.000000, 0.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.0)
        kThis.Update(0)
        kThis = None        

import App

def LoadBackdrops(pSet):

        #Draw order is implicit. First object gets drawn first

        # Star Sphere "Backdrop stars"
        kThis = App.StarSphere_Create()
        kThis.SetName("Backdrop stars")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.196336, 0.973113, -0.293112)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.047141, 0.475512, 0.981001)
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

        # Backdrop Sphere "Backdrop Vela01"
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Vela01")
        kThis.SetTranslateXYZ(0.000000, 1.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.65, 0.71, 0.6)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.44, 0.56, 0.62)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Vela01.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.801010)
        kThis.SetVerticalSpan(0.770011)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Vela01")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop Vela01"	        