import App

def LoadPlacements(sSetName):
	# Position "Warbird 1 Start"
	kThis = App.Waypoint_Create("Warbird 1 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-41.316586, 944.160065, 50.949215)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.252946, -0.919324, -0.301433)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.293666, -0.223908, 0.929315)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird 1 Start"

	# Position "Warbird 2 Start"
	kThis = App.Waypoint_Create("Warbird 2 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1.670154, 959.980103, 41.357456)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.168154, -0.953186, -0.251318)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.287709, -0.196391, 0.937366)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird 2 Start"

	# Position "Warbird 3 Start"
	kThis = App.Waypoint_Create("Warbird 3 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-31.051445, 1017.028564, 63.353218)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.168154, -0.953186, -0.251318)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.287709, -0.196391, 0.937366)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird 3 Start"

	# Position "Warbird 4 Start"
	kThis = App.Waypoint_Create("Warbird 4 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-41.316586, 1044.160065, 50.949215)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.252946, -0.919324, -0.301433)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.293666, -0.223908, 0.929315)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird 4 Start"

	# Position "WarpIn(player)"
	kThis = App.PlacementObject_Create("WarpIn(player)", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(24.741774, 800.865669, 10.162049)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.Update(0)
	kThis = None
	# End position "WarpIn(player)"

	# Position "Cutscene Camera Placement"
	kThis = App.Waypoint_Create("Cutscene Camera Placement", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-3.952585, 800.302399, 44.542595)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.229200, 0.973280, 0.013879)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.175090, 0.027198, 0.984177)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cutscene Camera Placement"

