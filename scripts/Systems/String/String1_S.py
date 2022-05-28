###############################################################################
#	Filename:	String1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates String 1 static objects.  Called by String1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	03/15/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(5.0, 5, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Node1")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Add a sun, far far away
	pSunx = App.Sun_Create(6.0, 6, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSunx, "Node2")
	
	# Place the object at the specified location.
	pSunx.PlaceObjectByName( "Sunx" )
	pSunx.UpdateNodeOnly()

	# Add a sun, far far away
	pSuny = App.Sun_Create(8.0, 8, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSuny, "Node3")
	
	# Place the object at the specified location.
	pSuny.PlaceObjectByName( "Suny" )
	pSuny.UpdateNodeOnly()

	# Add a sun, far far away
	pSuna = App.Sun_Create(10.0, 10, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSuna, "Node4")
	
	# Place the object at the specified location.
	pSuna.PlaceObjectByName( "Suna" )
	pSuna.UpdateNodeOnly()

	# Add a sun, far far away
	pSunax = App.Sun_Create(12.0, 12, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSunax, "Node5")
	
	# Place the object at the specified location.
	pSunax.PlaceObjectByName( "Sunax" )
	pSunax.UpdateNodeOnly()

	# Add a sun, far far away
	pSun2 = App.Sun_Create(14.0, 18, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun2, "Node6")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Add a sun, far far away
	pSun2x = App.Sun_Create(16.0, 20, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun2x, "Node7")
	
	# Place the object at the specified location.
	pSun2x.PlaceObjectByName( "Sun2x" )
	pSun2x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun2y = App.Sun_Create(18.0, 25, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun2y, "Node8")
	
	# Place the object at the specified location.
	pSun2y.PlaceObjectByName( "Sun2y" )
	pSun2y.UpdateNodeOnly()

	# Add a sun, far far away
	pSun2a = App.Sun_Create(19.0, 35, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2a, "Node9")
	
	# Place the object at the specified location.
	pSun2a.PlaceObjectByName( "Sun2a" )
	pSun2a.UpdateNodeOnly()

	# Add a sun, far far away
	pSun2ax = App.Sun_Create(20.0, 25, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun2ax, "Node10")
	
	# Place the object at the specified location.
	pSun2ax.PlaceObjectByName( "Sun2ax" )
	pSun2ax.UpdateNodeOnly()

	# Add a sun, far far away
	pSun3 = App.Sun_Create(21.0, 30, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun3, "Node11")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# Add a sun, far far away
	pSun3x = App.Sun_Create(22.0, 30, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun3x, "Node12")
	
	# Place the object at the specified location.
	pSun3x.PlaceObjectByName( "Sun3x" )
	pSun3x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun3a = App.Sun_Create(23.0, 50, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun3a, "Node13")
	
	# Place the object at the specified location.
	pSun3a.PlaceObjectByName( "Sun3a" )
	pSun3a.UpdateNodeOnly()

	# Add a sun, far far away
	pSun4 = App.Sun_Create(40.0, 150, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun4, "Knot Alpha")
	
	# Place the object at the specified location.
	pSun4.PlaceObjectByName( "Sun4" )
	pSun4.UpdateNodeOnly()

	# Add a sun, far far away
	pSun4a = App.Sun_Create(30.0, 50, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun4a, "Node14")
	
	# Place the object at the specified location.
	pSun4a.PlaceObjectByName( "Sun4a" )
	pSun4a.UpdateNodeOnly()

	# Add a sun, far far away
	pSun4ax = App.Sun_Create(29.0, 30, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun4ax, "Node15")
	
	# Place the object at the specified location.
	pSun4ax.PlaceObjectByName( "Sun4ax" )
	pSun4ax.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5 = App.Sun_Create(27.0, 25, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun5, "Node16")
	
	# Place the object at the specified location.
	pSun5.PlaceObjectByName( "Sun5" )
	pSun5.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5x = App.Sun_Create(25.0, 20, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun5x, "Node17")
	
	# Place the object at the specified location.
	pSun5x.PlaceObjectByName( "Sun5x" )
	pSun5x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5y = App.Sun_Create(24.0, 25, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun5y, "Node18")
	
	# Place the object at the specified location.
	pSun5y.PlaceObjectByName( "Sun5y" )
	pSun5y.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5a = App.Sun_Create(23.0, 20, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun5a, "Node19")
	
	# Place the object at the specified location.
	pSun5a.PlaceObjectByName( "Sun5a" )
	pSun5a.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5ax = App.Sun_Create(22.0, 25, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun5ax, "Node20")
	
	# Place the object at the specified location.
	pSun5ax.PlaceObjectByName( "Sun5ax" )
	pSun5ax.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5ay = App.Sun_Create(21.0, 30, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun5ay, "Node21")
	
	# Place the object at the specified location.
	pSun5ay.PlaceObjectByName( "Sun5ay" )
	pSun5ay.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6 = App.Sun_Create(20.0, 20, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun6, "Node22")
	
	# Place the object at the specified location.
	pSun6.PlaceObjectByName( "Sun6" )
	pSun6.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6x = App.Sun_Create(19.0, 25, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun6x, "Node23")
	
	# Place the object at the specified location.
	pSun6x.PlaceObjectByName( "Sun6x" )
	pSun6x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6a = App.Sun_Create(18.0, 15, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun6a, "Node24")
	
	# Place the object at the specified location.
	pSun6a.PlaceObjectByName( "Sun6a" )
	pSun6a.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6ax = App.Sun_Create(19.0, 12, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun6ax, "Node25")
	
	# Place the object at the specified location.
	pSun6ax.PlaceObjectByName( "Sun6ax" )
	pSun6ax.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6b = App.Sun_Create(20.0, 20, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun6b, "Node26")
	
	# Place the object at the specified location.
	pSun6b.PlaceObjectByName( "Sun6b" )
	pSun6b.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6bx = App.Sun_Create(19.0, 15, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun6bx, "Node27")
	
	# Place the object at the specified location.
	pSun6bx.PlaceObjectByName( "Sun6bx" )
	pSun6bx.UpdateNodeOnly()

	# Add a sun, far far away
	pSun7 = App.Sun_Create(18.0, 10, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun7, "Node28")
	
	# Place the object at the specified location.
	pSun7.PlaceObjectByName( "Sun7" )
	pSun7.UpdateNodeOnly()

	# Add a sun, far far away
	pSun7x = App.Sun_Create(19.0, 18, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun7x, "Node29")
	
	# Place the object at the specified location.
	pSun7x.PlaceObjectByName( "Sun7x" )
	pSun7x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun7a = App.Sun_Create(20.0, 15, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun7a, "Node30")
	
	# Place the object at the specified location.
	pSun7a.PlaceObjectByName( "Sun7a" )
	pSun7a.UpdateNodeOnly()

	# Add a sun, far far away
	pSun7ax = App.Sun_Create(21.0, 20, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun7ax, "Node31")
	
	# Place the object at the specified location.
	pSun7ax.PlaceObjectByName( "Sun7ax" )
	pSun7ax.UpdateNodeOnly()

	# Add a sun, far far away
	pSun8 = App.Sun_Create(20.0, 20, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun8, "Node32")
	
	# Place the object at the specified location.
	pSun8.PlaceObjectByName( "Sun8" )
	pSun8.UpdateNodeOnly()

	# Add a sun, far far away
	pSun8x = App.Sun_Create(21.0, 20, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun8x, "Node33")
	
	# Place the object at the specified location.
	pSun8x.PlaceObjectByName( "Sun8x" )
	pSun8x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun8a = App.Sun_Create(24.0, 20, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun8a, "Node34")
	
	# Place the object at the specified location.
	pSun8a.PlaceObjectByName( "Sun8a" )
	pSun8a.UpdateNodeOnly()

	# Add a sun, far far away
	pSun9 = App.Sun_Create(35.0, 80, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun9, "Knot Beta")
	
	# Place the object at the specified location.
	pSun9.PlaceObjectByName( "Sun9" )
	pSun9.UpdateNodeOnly()

	# Add a sun, far far away
	pSun10 = App.Sun_Create(32.0, 55, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun10, "Node35")
	
	# Place the object at the specified location.
	pSun10.PlaceObjectByName( "Sun10" )
	pSun10.UpdateNodeOnly()

	# Add a sun, far far away
	pSun10x = App.Sun_Create(28.0, 55, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun10x, "Node36")
	
	# Place the object at the specified location.
	pSun10x.PlaceObjectByName( "Sun10x" )
	pSun10x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun11 = App.Sun_Create(25.0, 30, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun11, "Node37")
	
	# Place the object at the specified location.
	pSun11.PlaceObjectByName( "Sun11" )
	pSun11.UpdateNodeOnly()

	# Add a sun, far far away
	pSun11x = App.Sun_Create(20.0, 30, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun11x, "Node38")
	
	# Place the object at the specified location.
	pSun11x.PlaceObjectByName( "Sun11x" )
	pSun11x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun12 = App.Sun_Create(17.0, 30, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun12, "Node39")
	
	# Place the object at the specified location.
	pSun12.PlaceObjectByName( "Sun12" )
	pSun12.UpdateNodeOnly()

	# Add a sun, far far away
	pSun12x = App.Sun_Create(16.0, 20, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun12x, "Node40")
	
	# Place the object at the specified location.
	pSun12x.PlaceObjectByName( "Sun12x" )
	pSun12x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun13 = App.Sun_Create(14.0, 15, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun13, "Node41")
	
	# Place the object at the specified location.
	pSun13.PlaceObjectByName( "Sun13" )
	pSun13.UpdateNodeOnly()

	# Add a sun, far far away
	pSun13x = App.Sun_Create(10.0, 15, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun13x, "Node42")
	
	# Place the object at the specified location.
	pSun13x.PlaceObjectByName( "Sun13x" )
	pSun13x.UpdateNodeOnly()

	# Add a sun, far far away
	pSun13y = App.Sun_Create(6.0, 12, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun13y, "Node43")
	
	# Place the object at the specified location.
	pSun13y.PlaceObjectByName( "Sun13y" )
	pSun13y.UpdateNodeOnly()

        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        loadspacehelper.CreateShip("CardStarbase", pSet, "Observatory", "Station")
	
	        # Create our static stations and such
	        pRegStation	= loadspacehelper.CreateShip("FedOutpost", pSet, "Science Station", "Station2")
	        if (pRegStation != None):
		        pRegStation.SetAlertLevel(App.ShipClass.GREEN_ALERT)
