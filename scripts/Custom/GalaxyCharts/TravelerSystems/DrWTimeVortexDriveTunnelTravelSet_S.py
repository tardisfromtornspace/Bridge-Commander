# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod, patch an old one or add new Sytems for the plugin as long as the source files remain unmodified.
# AIDrWTimeVortexDriveTunnelTravelSet.py, file made by Alex SL Gato
# Based on the prototype TravelSet template set by USS Frontier (TravelSet.py, original template) and certain common Systems like Vesuvi (by Totally Games).
# 14th April 2025
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
	pNebula = App.MetaNebula_Create(25.0 / 255.0, 25.0 / 255.0, 25.0 / 255.0, 38000.0, 1.0, "scripts/Custom/TravellingMethods/GFX/TimeVortexFlashEntry.tga", "data/timeVortexback.tga")

	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(2000.0, 15.0)

	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (15000.0 in this case)
	pNebula.AddNebulaSphere(0.0, 0.0, 0.0, 15000.0)

	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Mycelial Network details 1")