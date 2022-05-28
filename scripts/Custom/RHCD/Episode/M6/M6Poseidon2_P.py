import App

def LoadPlacements(sSetName):
	# Position "Starbase Start"
	kThis = App.Waypoint_Create("Starbase Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(45.439926, 400.169525, 1.324787)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.256715, 0.940928, 0.220798)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.033777, -0.219580, 0.975010)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Starbase Start"

	# Position "Galaxy Start"
	kThis = App.Waypoint_Create("Galaxy Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(45.439926, 100.169525, 1.324787)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.256715, 0.940928, 0.220798)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.033777, -0.219580, 0.975010)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galaxy Start"

	# Position "Akira Start"
	kThis = App.Waypoint_Create("Akira Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(45.439926, 120.169525, 21.324787)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.256715, 0.940928, 0.220798)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.033777, -0.219580, 0.975010)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Akira Start"

	# Position "Nebula Start"
	kThis = App.Waypoint_Create("Nebula Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(20.439926, 110.169525, 1.324787)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.256715, 0.940928, 0.220798)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.033777, -0.219580, 0.975010)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nebula Start"
	
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
	kThis.SetTranslateXYZ(-41.316586, 944.160065, 50.949215)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.252946, -0.919324, -0.301433)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.293666, -0.223908, 0.929315)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird 4 Start"

	# Position "Warbird 5 Start"
	kThis = App.Waypoint_Create("Warbird 5 Start", sSetName, None)
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
	# End position "Warbird 5 Start"

	# Position "Warbird 6 Start"
	kThis = App.Waypoint_Create("Warbird 6 Start", sSetName, None)
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
	# End position "Warbird 6 Start"

	# Position "Warbird 7 Start"
	kThis = App.Waypoint_Create("Warbird 7 Start", sSetName, None)
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
	# End position "Warbird 7 Start"

	# Position "Warbird 8 Start"
	kThis = App.Waypoint_Create("Warbird 8 Start", sSetName, None)
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
	# End position "Warbird 8 Start"

	# Position "Warbird 9 Start"
	kThis = App.Waypoint_Create("Warbird 9 Start", sSetName, None)
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
	# End position "Warbird 9 Start"

	# Position "Warbird 10 Start"
	kThis = App.Waypoint_Create("Warbird 10 Start", sSetName, None)
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
	# End position "Warbird 10 Start"

	# Position "Warbird 11 Start"
	kThis = App.Waypoint_Create("Warbird 11 Start", sSetName, None)
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
	# End position "Warbird 11 Start"

	# Position "Warbird 12 Start"
	kThis = App.Waypoint_Create("Warbird 12 Start", sSetName, None)
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
	# End position "Warbird 12 Start"

	# Position "Warbird 13 Start"
	kThis = App.Waypoint_Create("Warbird 13 Start", sSetName, None)
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
	# End position "Warbird 13 Start"

	# Position "Warbird 14 Start"
	kThis = App.Waypoint_Create("Warbird 14 Start", sSetName, None)
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
	# End position "Warbird 14 Start"

	# Position "Warbird 15 Start"
	kThis = App.Waypoint_Create("Warbird 15 Start", sSetName, None)
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
	# End position "Warbird 15 Start"

	# Position "Warbird 16 Start"
	kThis = App.Waypoint_Create("Warbird 16 Start", sSetName, None)
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
	# End position "Warbird 16 Start"

	# Position "Warbird 17 Start"
	kThis = App.Waypoint_Create("Warbird 17 Start", sSetName, None)
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
	# End position "Warbird 17 Start"

	# Position "Warbird 18 Start"
	kThis = App.Waypoint_Create("Warbird 18 Start", sSetName, None)
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
	# End position "Warbird 18 Start"

	# Position "Warbird 19 Start"
	kThis = App.Waypoint_Create("Warbird 19 Start", sSetName, None)
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
	# End position "Warbird 19 Start"

	# Position "Warbird 20 Start"
	kThis = App.Waypoint_Create("Warbird 20 Start", sSetName, None)
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
	# End position "Warbird 20 Start"

	# Position "Warbird 21 Start"
	kThis = App.Waypoint_Create("Warbird 21 Start", sSetName, None)
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
	# End position "Warbird 21 Start"

	# Position "Warbird 22 Start"
	kThis = App.Waypoint_Create("Warbird 22 Start", sSetName, None)
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
	# End position "Warbird 22 Start"

	# Position "Warbird 23 Start"
	kThis = App.Waypoint_Create("Warbird 23 Start", sSetName, None)
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
	# End position "Warbird 23 Start"

	# Position "Warbird 24 Start"
	kThis = App.Waypoint_Create("Warbird 24 Start", sSetName, None)
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
	# End position "Warbird 24 Start"

	# Position "Warbird 25 Start"
	kThis = App.Waypoint_Create("Warbird 25 Start", sSetName, None)
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
	# End position "Warbird 25 Start"

	# Position "Warbird 26 Start"
	kThis = App.Waypoint_Create("Warbird 26 Start", sSetName, None)
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
	# End position "Warbird 26 Start"

	# Position "Warbird 27 Start"
	kThis = App.Waypoint_Create("Warbird 27 Start", sSetName, None)
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
	# End position "Warbird 27 Start"

	# Position "Warbird 28 Start"
	kThis = App.Waypoint_Create("Warbird 28 Start", sSetName, None)
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
	# End position "Warbird 28 Start"

	# Position "Warbird 29 Start"
	kThis = App.Waypoint_Create("Warbird 29 Start", sSetName, None)
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
	# End position "Warbird 29 Start"

	# Position "Warbird 30 Start"
	kThis = App.Waypoint_Create("Warbird 30 Start", sSetName, None)
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
	# End position "Warbird 30 Start"
	
	# Position "WarpIn(player)"
	kThis = App.PlacementObject_Create("WarpIn(player)", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(24.741774, -31.865669, 10.162049)
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
	kThis.SetTranslateXYZ(-3.952585, 879.302399, 44.542595)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.229200, 0.973280, 0.013879)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.175090, 0.027198, 0.984177)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cutscene Camera Placement"

