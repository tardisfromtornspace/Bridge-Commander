###############################################################################
#       Filename:       Sirius_B2_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates Sirius_B static objects.  Called by Sirius_B2.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
# Modified for the Multi-Player all out inter-race war 'escape' system Dec. 2003 - Chris Jones
###############################################################################
import App
import Tactical.LensFlares
import loadspacehelper

def Initialize(pSet):
 ##     pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSun = App.Sun_Create(1350.2857, 2380.0, 700, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun, "Sirius A")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        pSun2 = App.Sun_Create(79.42857, 14.0000, 100, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
##      pSun2 = App.Sun_Create(135028.57, 23800.0, 700, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun2, "Sirius B")

        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()  
        



