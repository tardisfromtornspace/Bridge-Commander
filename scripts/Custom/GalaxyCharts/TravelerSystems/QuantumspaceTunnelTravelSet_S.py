# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod, patch an old one or add new Sytems for the plugin as long as the source files remain unmodified.
# AIQuantumspaceTunnelTravelSet.py, file made by Alex SL Gato
# Based on the prototype TravelSet template set by USS Frontier (TravelSet.py, original template) and certain common Systems like Vesuvi (by Totally Games).
# 13th April 2025
# Version 0.1

import App
import loadspacehelper
import Maelstrom.Maelstrom

def Initialize(pSet):
	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
	# name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	pNebula = App.MetaNebula_Create(1.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 145.0, 1.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")

	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.0, 0.00001)

	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (15000.0 in this case)
	pNebula.AddNebulaSphere(0.0, 0.0, 0.0, 15000.0)

	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "B5 hyperspace foggy nebula")