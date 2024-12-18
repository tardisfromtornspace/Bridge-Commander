#################################################################################################################
#         SystemsChangedWithGCOn by Alex SL Gato
#         17th December 2024     
#################################################################################################################
# Little simple tech. Any ships with this tech will have a certain hardpoint property disabled percentage modified if GalaxyCharts mutator is on. This works so, f.ex., a ship without Warp but another similar GalaxyCharts FTL TravellingMethod can warp out of a system if GalaxyCharts is offline.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file but modify the values accordingly to what you want, and for actual values since the following is just a general example
# "Message": this field will throw subtitles when the ship is a player and is loaded to explain to the player what is going on. Don't add this field to not add subtitles.
# - "Content": is a key whose value stores the message string you want to send. There's a default that only works to indicate some things might have changed on GC.
# - "Time": is a key whose value indicates how many seconds the subtitle lasts. Default is 3 seconds.
# "Hardpoints": this field is a dictionary which stores in a key-value format the subsystem name and its modified disabled percentage. A value above 1 will guarantee the system is kept disabled.
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"Systems Changed With GC On": {"Message": {"Content": "This vessel has warp-drives disabled on GC. Please use its Mass Effect Drive instead.", "Time": 4.0}, "Hardpoints": {"Subsystem Name 1": 1.15, "Subsystem Name 2": 1.12},},
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.1",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

from bcdebug import debug

import App
import FoundationTech
import traceback

class SystemsChangedWithGCOn(FoundationTech.TechDef):

	def __init__(self, name):
		FoundationTech.TechDef.__init__(self, name)
		self.mode = None
		modeI = None
		isGCEnabled = 0
		doneWell = 0
		try:
			from Custom.Autoload.LoadGalaxyCharts import mode
			if mode == None or not hasattr(mode, "IsEnabled"):
				isGCEnabled = 0
			else:
				isGCEnabled = mode.IsEnabled()
				#modeI = mode
				doneWell = 1
		except:
			isGCEnabled = 0
			doneWell = 0
		
		if doneWell == 1:
			self.mode = mode

	def checkAdjust(self, pInstanceDict, pSubsystem, subsystemNames):
		if hasattr(pSubsystem, "GetName") and pSubsystem.GetName() in subsystemNames:
			pSubsystemProperty = pSubsystem.GetProperty()
			if pSubsystemProperty:
				pSubsystemProperty.SetDisabledPercentage(pInstanceDict["Systems Changed With GC On"]["Hardpoints"][pSubsystem.GetName()])

	def AdjustHardpoint(self, pShip, pInstanceDict):
		if pInstanceDict["Systems Changed With GC On"].has_key("Hardpoints"):
			#subsystemNames = pInstanceDict["Systems Changed With GC On"]["Hardpoints"].keys():
			subsystemNames = []
			for elementName in pInstanceDict["Systems Changed With GC On"]["Hardpoints"].keys():
				subsystemNames.append(elementName)
			if len(subsystemNames) > 0:
				kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				while (1):
					pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
					if not pSubsystem:
						break

					self.checkAdjust(pInstanceDict, pSubsystem, subsystemNames)
					
					for i in range(pSubsystem.GetNumChildSubsystems()):
						pChild = pSubsystem.GetChildSubsystem(i)
						if pChild:
							self.checkAdjust(pInstanceDict, pChild, subsystemNames)

				pShip.EndGetSubsystemMatch(kIterator)
		
	def SendMessage(self, pInstanceDict, pShipID):
		pPlayer = App.Game_GetCurrentPlayer()
		if not pPlayer:
			return

		pPlayerID = App.NULL_ID
		if hasattr(pPlayer, "GetObjID"):
			 pPlayerID = pPlayer.GetObjID()

		if not pPlayerID  or pPlayerID == App.NULL_ID:
			return

		if pInstanceDict["Systems Changed With GC On"].has_key("Message") and pShipID == pPlayerID:
			myMessage = "Computer: Some system's status may have changed with GalaxyCharts enabled."
			myTime = 3.0
			if pInstanceDict["Systems Changed With GC On"]["Message"].has_key("Content") and pInstanceDict["Systems Changed With GC On"]["Message"]["Content"] != None:
				myMessage = pInstanceDict["Systems Changed With GC On"]["Message"]["Content"]
			if pInstanceDict["Systems Changed With GC On"]["Message"].has_key("Time") and pInstanceDict["Systems Changed With GC On"]["Message"]["Time"] != None and pInstanceDict["Systems Changed With GC On"]["Message"]["Time"] > 0:
				myTime = pInstanceDict["Systems Changed With GC On"]["Message"]["Time"]

			pSequence = App.TGSequence_Create ()
			pSubtitleAction = App.SubtitleAction_CreateC(myMessage)
			pSubtitleAction.SetDuration(myTime)
			pSequence.AddAction(pSubtitleAction)
			pSequence.Play()
				
	def Attach(self, pInstance):
		pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)
		if pShip != None:
			if not pInstance.__dict__.has_key("Systems Changed With GC On"):
				#print "Systems Changed With GC On: cancelling, ship does not have Systems Changed With GC On equipped..."
				return
			isGCEnabled = 0
			if not hasattr(self, "mode") or self.mode == None or not hasattr(self.mode, "IsEnabled"):
				try:
					from Custom.Autoload.LoadGalaxyCharts import mode
					if mode == None or not hasattr(mode, "IsEnabled"):
						isGCEnabled = 0
					else:
						isGCEnabled = mode.IsEnabled()
						self.mode = mode
				except:
					isGCEnabled = 0
			else:
				isGCEnabled = self.mode.IsEnabled()
						
			if isGCEnabled:
				pInstanceDict = pInstance.__dict__
				self.AdjustHardpoint(pShip, pInstanceDict)
				self.SendMessage(pInstanceDict, pInstance.pShipID)
		else:
			print "Systems Changed With GC On (at Attach): couldn't acquire ship of id", pInstance.pShipID
			pass

		pInstance.lTechs.append(self)
    
oSystemsChangedWithGCOn = SystemsChangedWithGCOn('Systems Changed With GC On')
