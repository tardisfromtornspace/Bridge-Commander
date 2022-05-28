from bcdebug import debug
# Setup function - does whatever needed to be in LoadBridge.py
# This shouldn't need anything more...
import App

def Setup():
	debug(__name__ + ", Setup")
	if ( App.Game_GetCurrentGame() != None ):
		#print("Loading Carrier System")
		
		#Importing Shuttle Launch Framework
		import ftb.LaunchShipHandlers
                ftb.LaunchShipHandlers.MissionStart()
