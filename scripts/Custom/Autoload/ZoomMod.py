#########################
#			#
#      Zooming Mod	#
#			#
#	   by		#
#			#
#      MLeoDaalder	#
#			#
#########################

import App
import Foundation
import MissionLib
import Camera

# deactivated - crashing problems?
#mode = Foundation.MutatorDef("Fix Zoom On Target")

ZOOMTRIGGER = 0#App.UtopiaModule_GetNextEventType()

Zooming = 0

class ZoomTrigger(Foundation.TriggerDef):
	def __init__(self, dict = {}):
		global ZOOMTRIGGER
		Foundation.TriggerDef.__init__(self, "Zooming Mod", ZOOMTRIGGER, dict = {})

	def __call__(self, pObject, pEvent):
		if(pEvent.GetBool() == 0):
			return

		global Zooming
		if(Zooming):
			# Disable zoom mode.
			pGame = App.Game_GetCurrentGame()
			Camera.Pop(None, "ZoomTarget")
			Zooming = 0
		else:
			pTarget = MissionLib.GetPlayer().GetTarget()
			if not pTarget:
				return

			Camera.ZoomTarget(MissionLib.GetPlayer().GetName(), pTarget.GetName(), None, 1, 0)
			Zooming = 1

#ZOOMTRIGGER = Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Fixed Zoom", "ZOOMTRIGGER", ZOOMTRIGGER, App.KeyboardBinding.GET_BOOL_EVENT, 1, "Camera", dict = {"modes": [mode]}))

#oZoomTrigger = ZoomTrigger(dict = {"modes": [mode]})

