import App

def LoadPlacements(sSetName):
	# Position "Galor1 Start"
	kThis = App.Waypoint_Create("Galor1 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-57.461971, 1103.761841, -3.648164)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.052110, -0.994599, 0.089758)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.019226, 0.090862, 0.995678)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor1 Start"

	# Position "Galor2 Start"
	kThis = App.Waypoint_Create("Galor2 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(14.752338, 1098.282715, 2.866162)
	kForward = App.TGPoint3()		   
	kForward.SetXYZ(-0.159718, -0.986624, -0.032621)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.095375, -0.048314, 0.994268)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor2 Start"

	# Position "Galor3 Start"
	kThis = App.Waypoint_Create("Galor3 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-50.46835, 700.0, 2.866162)
	kForward = App.TGPoint3()		   
	kForward.SetXYZ(-0.159718, 0.986624, -0.032621)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.095375, -0.048314, 0.994268)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor3 Start"

	# Position "Ferengi Start"
	kThis = App.Waypoint_Create("Ferengi Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-24.752338, 1000.0, 2.866162)
	kForward = App.TGPoint3()		   
	kForward.SetXYZ(-0.159718, 0.986624, -0.032621)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.095375, -0.048314, 0.994268)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Ferengi Start"
