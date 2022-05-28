# by USS Sovereign a system creation file

import App
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def Initialize():
        # Create the set ("BajoranWormhole1")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "BajoranWormhole1")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.BajoranWormhole.BajoranWormhole1")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)


        # Load the placements and backdrops for this set.
        LoadPlacements("BajoranWormhole1")
        LoadBackdrops(pSet)

        # Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)
        # Done.

def GetSetName():
        return "BajoranWormhole1"

def GetSet():
        return App.g_kSetManager.GetSet("BajoranWormhole1")

def Terminate():
        App.g_kSetManager.DeleteSet("BajoranWormhole1")

def LoadPlacements(sSetName):
        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.InsideWormholeBackgroundTexture == 0:
                # Configure "Directional Light 1" for Blaxxer's Wormhole Model
                kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, 5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(-1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 2.000000)
                kThis.Update(0)
                kThis = None

                # Configure "Directional Light 2" for Blaxxer's Wormhole Model
                kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, -5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 2.000000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light for Blaxxer's Wormhole Model
                kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.000000, 0.800000, 1.000000, 0.600000)
                kThis.Update(0)
                kThis = None

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 1:
                # Configure "Directional light 1" for Blaxxer's wormhole model alternate texture 1
                kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, 5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(-1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 0.800000)
                kThis.Update(0)
                kThis = None

                # Configure "directional light 2" for Blaxxer's wormhole model alternate texture 1
                kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, -5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 0.800000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light 1 for Blaxxer's wormhole model alternate texture 1
                kThis = App.LightPlacement_Create("Ambient Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.000000, 0.800000, 1.000000, 0.300000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light 2 for Blaxxer's wormhole model alternate texture 1
                kThis = App.LightPlacement_Create("Ambient Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.921569, 1.000000, 0.396078, 0.300000)
                kThis.Update(0)
                kThis = None

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 2:
                # Configure "Directional light 1" for Blaxxer's wormhole model alternate texture 2
                kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, 5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(-1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 0.800000)
                kThis.Update(0)
                kThis = None

                # Configure "directional light 2" for Blaxxer's wormhole model alternate texture 2
                kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, -5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 0.800000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light 1 for Blaxxer's wormhole model alternate texture 1
                kThis = App.LightPlacement_Create("Ambient Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(1.000000, 0.270588, 0.270588, 0.700000)
                kThis.Update(0)
                kThis = None

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 3:
                # Configure "Directional light 1" for Blaxxer's wormhole model alternate texture 3
                kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, 5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(-1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 0.400000)
                kThis.Update(0)
                kThis = None

                # Configure "directional light 2" for Blaxxer's wormhole model alternate texture 3
                kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, -5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 0.400000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light 1 for Blaxxer's wormhole model alternate texture 1
                kThis = App.LightPlacement_Create("Ambient Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.662745, 0.513725, 0.000000, 0.300000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light 2 for Blaxxer's wormhole model alternate texture 2
                kThis = App.LightPlacement_Create("Ambient Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.062745, 0.254902, 0.737255, 0.3500000)
                kThis.Update(0)
                kThis = None

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 4:
                # Configure "Directional light 1" for Blaxxer's wormhole model alternate texture 4
                kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(1.000000, 1.000000, 1.000000, 0.000000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light 1 for Blaxxer's wormhole model alternate texture 1
                kThis = App.LightPlacement_Create("Ambient Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.000000, 0.725490, 0.619608, 0.600000)
                kThis.Update(0)
                kThis = None

                # Configure ambient light 2 for Blaxxer's wormhole model alternate texture 2
                kThis = App.LightPlacement_Create("Ambient Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(1.000000, 0.164706, 0.000000, 0.3500000)
                kThis.Update(0)
                kThis = None        

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 5:
                # Configure "Directional Light 1" for Cordanilus' Wormhole Model
                kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, 5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(-1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(0.870588, 0.701961, 1.000000, 0.700000)
                kThis.Update(0)
                kThis = None

                # Configure "Directional Light 2" for Cordanilus' Wormhole Model
                kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, -5500.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(1.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(0.870588, 0.701961, 1.000000, 0.700000)
                kThis.Update(0)
                kThis = None

                # Configure Ambient Light 1 for Cordanilus' Wormhole Model
                kThis = App.LightPlacement_Create("Ambient Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.682353, 0.274510, 1.000000, 0.400000)
                kThis.Update(0)
                kThis = None		

                # Configure Ambient Light 2 for Cordanilus' Wormhole Model
                kThis = App.LightPlacement_Create("Ambient Light 2", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 50.000000, 50.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 1.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 1.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.309804, 0.960784, 1.000000, 0.200000)
                kThis.Update(0)
                kThis = None		        

        else:
                # Configure "Directional Light" for mess-up
                kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.0, 0.0, 0.0)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.0, 0.0, 0.0)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigDirectionalLight(0.000000, 0.000000, 0.000000, 0.000000)
                kThis.Update(0)
                kThis = None

                # Configure Ambient Light for mess-up
                kThis = App.LightPlacement_Create("Ambient Light 1", sSetName, None)
                kThis.SetStatic(1)
                kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                kForward = App.TGPoint3()
                kForward.SetXYZ(0.000000, 0.000000, 0.000000)
                kUp = App.TGPoint3()
                kUp.SetXYZ(0.000000, 0.000000, 0.000000)
                kThis.AlignToVectors(kForward, kUp)
                kThis.ConfigAmbientLight(0.000000, 0.000000, 0.000000, 0.100000)
                kThis.Update(0)
                kThis = None		                

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

        # Position "WormholeCone Position"
        kThis = App.Waypoint_Create("WormholeCone Position", sSetName, None)
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
        # End position "WormholeCone Position"

        # Position "WormholeCone2 Position"
        kThis = App.Waypoint_Create("WormholeCone2 Position", sSetName, None)
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
        # End position "WormholeCone2 Position"

import App

def LoadBackdrops(pSet):
        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.InsideWormholeBackgroundTexture == 1:
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
                kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphics2.tga")
                kThis.SetTargetPolyCount(256)
                kThis.SetHorizontalSpan(300.000000)
                kThis.SetVerticalSpan(300.000000)
                kThis.SetSphereRadius(300.000000)
                kThis.SetTextureHTile(300.000000)
                kThis.SetTextureVTile(300.000000)
                kThis.Rebuild()
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 2:
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
                kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsChrome.tga")
                kThis.SetTargetPolyCount(256)
                kThis.SetHorizontalSpan(300.000000)
                kThis.SetVerticalSpan(300.000000)
                kThis.SetSphereRadius(300.000000)
                kThis.SetTextureHTile(300.000000)
                kThis.SetTextureVTile(300.000000)
                kThis.Rebuild()
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 3:
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
                kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsDarkBlue.tga")
                kThis.SetTargetPolyCount(256)
                kThis.SetHorizontalSpan(300.000000)
                kThis.SetVerticalSpan(300.000000)
                kThis.SetSphereRadius(300.000000)
                kThis.SetTextureHTile(300.000000)
                kThis.SetTextureVTile(300.000000)
                kThis.Rebuild()
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"


        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 4:
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
                kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsWaterBlue.tga")
                kThis.SetTargetPolyCount(256)
                kThis.SetHorizontalSpan(300.000000)
                kThis.SetVerticalSpan(300.000000)
                kThis.SetSphereRadius(300.000000)
                kThis.SetTextureHTile(300.000000)
                kThis.SetTextureVTile(300.000000)
                kThis.Rebuild()
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 5:
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
                kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsWierd.tga")
                kThis.SetTargetPolyCount(256)
                kThis.SetHorizontalSpan(300.000000)
                kThis.SetVerticalSpan(300.000000)
                kThis.SetSphereRadius(300.000000)
                kThis.SetTextureHTile(300.000000)
                kThis.SetTextureVTile(300.000000)
                kThis.Rebuild()
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"

        elif DS9FXSavedConfig.InsideWormholeBackgroundTexture == 6:
                # Nothing here
                return 0

        else:
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
                kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphics.tga")
                kThis.SetTargetPolyCount(256)
                kThis.SetHorizontalSpan(300.000000)
                kThis.SetVerticalSpan(300.000000)
                kThis.SetSphereRadius(300.000000)
                kThis.SetTextureHTile(300.000000)
                kThis.SetTextureVTile(300.000000)
                kThis.Rebuild()
                pSet.AddBackdropToSet(kThis,"Backdrop stars")
                kThis.Update(0)
                kThis = None
                # End Backdrop Sphere "Backdrop stars"
