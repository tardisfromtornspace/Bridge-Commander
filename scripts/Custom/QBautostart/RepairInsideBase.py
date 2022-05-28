"""
Repair ship with damaged impulse engines that can't dock by placing them inside a base.
"""

import App
import AI.Compound.DockWithStarbaseLong
from Libs.LibQBautostart import *
from Construct import *


MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }


g_pInsideBaseTimer = None
NonSerializedObjects = (
"g_pInsideBaseTimer"
)



class InsideBaseTimer:
	def __init__(self):
		self.pTimerProcess = None
		self.SetupTimer()

        def SetupTimer(self):
                if self.pTimerProcess:
                        # We already have a timer.
                        return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)
		self.SetDelay()
		
	def SetDelay(self):
		self.pTimerProcess.SetDelay(60)
	
	def Update(self, dTimeAvailable):
		for pSet in App.g_kSetManager.GetAllSets():
			lShips = pSet.GetClassObjectList(App.CT_SHIP)
			# collect stations in this set
			lBases = []
			for pObject in lShips:
				pShip = App.ShipClass_Cast(pObject)
				if pShip.GetShipProperty().IsStationary():
					lBases.append(pShip)
			# detect ship in stations in this set
			for pObject in lShips:
				pShip = App.ShipClass_Cast(pObject)
				pImpulse = pShip.GetImpulseEngineSubsystem()
				if not pImpulse:
					continue
				for pStation in lBases:
					pConstructor = GetConstructInstanceFor(pStation, 1)
					if not pConstructor:
						continue
					if pStation.GetName() == pShip.GetName() or pConstructor.GetMode() == "Construct":
						continue

					if pImpulse.IsDisabled() and AI.Compound.DockWithStarbaseLong.IsInViewOfInsidePoints(pShip, pStation) and IsSameGroup(pShip, pStation):
						AI.Compound.DockWithStarbaseLong.NonPlayerDocked(pShip, pStation.GetName())


def init():
	global g_pInsideBaseTimer

	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	elif not App.g_kUtopiaModule.IsMultiplayer():
		g_pInsideBaseTimer = InsideBaseTimer()
