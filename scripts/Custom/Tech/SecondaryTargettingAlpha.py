from bcdebug import debug
# Setup function - does whatever needed to be in LoadBridge.py
# This shouldn't need anything more...
import App

def Setup():
	debug(__name__ + ", Setup")
	if ( App.Game_GetCurrentGame() != None ):
		# Importing Secondary Targetting Mod by sleight42
		import ftb.Ship
		import ftb.ShipHandlers
		ftb.ShipHandlers.MissionStart()
