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
	
	# Position "Keldon 1 Start"
	kThis = App.Waypoint_Create("Keldon 1 Start", sSetName, None)
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
	# End position "Keldon 1 Start"

	# Position "Keldon 2 Start"
	kThis = App.Waypoint_Create("Keldon 2 Start", sSetName, None)
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
	# End position "Keldon 2 Start"

	# Position "Keldon 3 Start"
	kThis = App.Waypoint_Create("Keldon 3 Start", sSetName, None)
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
	# End position "Keldon 3 Start"

	# Position "Keldon 4 Start"
	kThis = App.Waypoint_Create("Keldon 4 Start", sSetName, None)
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
	# End position "Keldon 4 Start"

	# Position "Keldon 5 Start"
	kThis = App.Waypoint_Create("Keldon 5 Start", sSetName, None)
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
	# End position "Keldon 5 Start"

	# Position "Keldon 6 Start"
	kThis = App.Waypoint_Create("Keldon 6 Start", sSetName, None)
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
	# End position "Keldon 6 Start"

	# Position "Keldon 7 Start"
	kThis = App.Waypoint_Create("Keldon 7 Start", sSetName, None)
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
	# End position "Keldon 7 Start"

	# Position "Keldon 8 Start"
	kThis = App.Waypoint_Create("Keldon 8 Start", sSetName, None)
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
	# End position "Keldon 8 Start"

	# Position "Keldon 9 Start"
	kThis = App.Waypoint_Create("Keldon 9 Start", sSetName, None)
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
	# End position "Keldon 9 Start"

	# Position "Keldon 10 Start"
	kThis = App.Waypoint_Create("Keldon 10 Start", sSetName, None)
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
	# End position "Keldon 10 Start"

	# Position "Keldon 11 Start"
	kThis = App.Waypoint_Create("Keldon 11 Start", sSetName, None)
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
	# End position "Keldon 11 Start"

	# Position "Keldon 12 Start"
	kThis = App.Waypoint_Create("Keldon 12 Start", sSetName, None)
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
	# End position "Keldon 12 Start"

	# Position "Keldon 13 Start"
	kThis = App.Waypoint_Create("Keldon 13 Start", sSetName, None)
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
	# End position "Keldon 13 Start"

	# Position "Keldon 14 Start"
	kThis = App.Waypoint_Create("Keldon 14 Start", sSetName, None)
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
	# End position "Keldon 14 Start"

	# Position "Keldon 15 Start"
	kThis = App.Waypoint_Create("Keldon 15 Start", sSetName, None)
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
	# End position "Keldon 15 Start"

	# Position "Keldon 16 Start"
	kThis = App.Waypoint_Create("Keldon 16 Start", sSetName, None)
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
	# End position "Keldon 16 Start"

	# Position "Keldon 17 Start"
	kThis = App.Waypoint_Create("Keldon 17 Start", sSetName, None)
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
	# End position "Keldon 17 Start"

	# Position "Keldon 18 Start"
	kThis = App.Waypoint_Create("Keldon 18 Start", sSetName, None)
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
	# End position "Keldon 18 Start"

	# Position "Keldon 19 Start"
	kThis = App.Waypoint_Create("Keldon 19 Start", sSetName, None)
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
	# End position "Keldon 19 Start"

	# Position "Keldon 20 Start"
	kThis = App.Waypoint_Create("Keldon 20 Start", sSetName, None)
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
	# End position "Keldon 20 Start"

	# Position "Keldon 21 Start"
	kThis = App.Waypoint_Create("Keldon 21 Start", sSetName, None)
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
	# End position "Keldon 21 Start"

	# Position "Keldon 22 Start"
	kThis = App.Waypoint_Create("Keldon 22 Start", sSetName, None)
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
	# End position "Keldon 22 Start"

	# Position "Keldon 23 Start"
	kThis = App.Waypoint_Create("Keldon 23 Start", sSetName, None)
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
	# End position "Keldon 23 Start"

	# Position "Keldon 24 Start"
	kThis = App.Waypoint_Create("Keldon 24 Start", sSetName, None)
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
	# End position "Keldon 24 Start"

	# Position "Keldon 25 Start"
	kThis = App.Waypoint_Create("Keldon 25 Start", sSetName, None)
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
	# End position "Keldon 25 Start"

	# Position "Keldon 26 Start"
	kThis = App.Waypoint_Create("Keldon 26 Start", sSetName, None)
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
	# End position "Keldon 26 Start"

	# Position "Keldon 27 Start"
	kThis = App.Waypoint_Create("Keldon 27 Start", sSetName, None)
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
	# End position "Keldon 27 Start"

	# Position "Keldon 28 Start"
	kThis = App.Waypoint_Create("Keldon 28 Start", sSetName, None)
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
	# End position "Keldon 28 Start"

	# Position "Keldon 29 Start"
	kThis = App.Waypoint_Create("Keldon 29 Start", sSetName, None)
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
	# End position "Keldon 29 Start"

	# Position "Keldon 30 Start"
	kThis = App.Waypoint_Create("Keldon 30 Start", sSetName, None)
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
	# End position "Keldon 30 Start"
	
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

