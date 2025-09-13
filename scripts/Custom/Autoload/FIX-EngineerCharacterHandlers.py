# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 12th September 2025
# VERSION 0.1
# By Alex SL Gato
# EngineerCharacterHandlers.py by Totally Games -> v1.1 fix
#
# Changes: 
# - Currently the EngineerCharacterHandler.py is not made to handle ships with 0 shield strength, which leads to several 0-division errors, while ScienceCharacterHandlers has a check

from bcdebug import debug
import traceback

import App
import MissionLib

necessaryToUpdate = 0
patchDone = 0
scriptToPatch = None
toPatchPath = "Bridge.EngineerCharacterHandlers"
VERSION = 20250913
originalReport = None
originalAnnounceShields = None
originalAnnounceSpecificShield = None
try:
	try:
		scriptToPatch = __import__(toPatchPath)
	except:
		scriptToPatch = None
		traceback.print_exc()

	if scriptToPatch != None:	
		if hasattr(scriptToPatch,"VERSION"):
			if scriptToPatch.VERSION < VERSION:
				necessaryToUpdate = 1
			else :
				necessaryToUpdate = 0
				print __name__, ":Congrats! Your ", scriptToPatch, " version doesn't require of any fix we are aware of - feel free to delete ", __name__
		else:
			necessaryToUpdate = 1 # the oldest versions have no signature
	else:
		necessaryToUpdate = 0
except:
	traceback.print_exc()

if necessaryToUpdate and scriptToPatch != None:
	try:
		originalReport = scriptToPatch.Report
		originalAnnounceShields = scriptToPatch.AnnounceShields
		originalAnnounceSpecificShield = scriptToPatch.AnnounceSpecificShield
	except:
		originalReport = None
		originalAnnounceShields = None
		originalAnnounceSpecificShield = None
		print __name__, ": your ", scriptToPatch, " exists, but lacks stuff:"
		traceback.print_exc()

if originalReport != None and originalAnnounceShields != None and originalAnnounceSpecificShield != None:
	def provideShieldPercentage(pShip, specificId = None):
		iNumShields = -1
		pShields = None
		fShields = 0
		inexistantFacets = 0
		if pShip:
			pShields = pShip.GetShields()
			if pShields:
				if specificId == None:
					iNumShields = pShields.NUM_SHIELDS

					for i in range (iNumShields):
						maxShieldsi = pShip.GetShields().GetMaxShields(i)
						if maxShieldsi > 0:
							fShields = fShields + (pShip.GetShields().GetCurShields(i)/pShip.GetShields().GetMaxShields(i))
						else:
							inexistantFacets = inexistantFacets + 1
				else:
					try:
						maxShieldsi = pShip.GetShields().GetMaxShields(specificId)
						if maxShieldsi == None:
							iNumShields = -1
							inexistantFacets = inexistantFacets + 1
						else:
							iNumShields = 1
							if maxShieldsi > 0:
								fShields = fShields + (pShip.GetShields().GetCurShields(specificId)/pShip.GetShields().GetMaxShields(specificId))
							else:
								inexistantFacets = inexistantFacets + 1
					except:
						iNumShields = -1
						fShields = 0
						traceback.print_exc()


			else:
				pShields = None

		validShieldsToGauge = (pShields != None and iNumShields >= 0 and inexistantFacets < iNumShields)

		return fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge
				
	def NewReport(pObject = None, pEvent = None):
		debug(__name__ + ", Report")
		pSet = App.g_kSetManager.GetSet("bridge")
		if not pSet:
			return 0
		pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
		if not pEngineer:
			return 0

		pDatabase = pEngineer.GetDatabase()

		pGame = App.Game_GetCurrentGame()
		if not pGame:
			return 0

		pShip = App.ShipClass_Cast(pGame.GetPlayer())
		if not pShip:
			return 0

		pSequence = None
		pHull = pShip.GetHull()

		fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip)
		if pHull or validShieldsToGauge:
			pSequence = App.TGSequence_Create()

		if pHull: # Nothing to report if there is no hull!
			fHull = pHull.GetConditionPercentage()

			if (fHull <= 0.05):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull05", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fHull <= 0.1):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull10", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fHull <= 0.15):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull15", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fHull <= 0.2):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull20", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fHull <= 0.25):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull25", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fHull <= 0.5):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull50", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fHull <= 0.75):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull75", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			else:
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Hull100", None, 0, pDatabase, App.CSP_SPONTANEOUS))

		if validShieldsToGauge: # Nothing to report if there are no shields!
			if (fShields <= 0.0):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "ShieldsFailed", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fShields <= 0.05):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields05", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fShields <= 0.1):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields10", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fShields <= 0.15):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields15", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fShields <= 0.2):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields20", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fShields <= 0.25):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields25", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fShields <= 0.5):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields50", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			elif (fShields <= 0.75):
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields75", None, 0, pDatabase, App.CSP_SPONTANEOUS))
			else:
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "Shields100", None, 0, pDatabase, App.CSP_SPONTANEOUS))

		if (pObject):
			if (pEvent):
#				debug("This is an event handled call")
				pObject.CallNextHandler(pEvent)
				if pSequence != None:
					pSequence.Play()
				return

			# This might be called as a script action, so return after the sequence if it is
#			debug("An action called us..")
			pEvent = App.TGObjPtrEvent_Create()
			pEvent.SetDestination(App.g_kTGActionManager)
			pEvent.SetEventType(App.ET_ACTION_COMPLETED)
			pEvent.SetObjPtr(pObject)
			if pSequence == None:
				pSequence = App.TGSequence_Create()

			pSequence.AddCompletedEvent(pEvent)

			pSequence.Play()

		return 1

	def NewAnnounceShields(pAction):
		debug(__name__ + ", AnnounceShields")
		pShip = MissionLib.GetPlayer()
		if not (pShip):
			return 0

		if (pShip.IsDying()):
			return 0

		pSet = App.g_kSetManager.GetSet("bridge")
		if not pSet:
			return 0

		pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
		if not pEngineer or (pEngineer.IsHidden() or pEngineer.IsAnimatingNonInterruptable() or pEngineer.IsSpeaking() or pShip.GetAlertLevel() == pShip.GREEN_ALERT):
			return 0

		fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip)
		if validShieldsToGauge:
			pDatabase = pEngineer.GetDatabase()
			fLastTime = App.g_kUtopiaModule.GetGameTime() - pEngineer.GetLastTalkTime()

			if (fShields <= 0.0 and fLastTime > 1.0):
				pEngineer.SayLine(pDatabase, "ShieldsFailed", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields Failed!")
			elif (fShields <= 0.05 and fLastTime > 2.0):
				pEngineer.SayLine(pDatabase, "Shields05", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields 05")
			elif (fShields <= 0.1 and fLastTime > 2.0):
				pEngineer.SayLine(pDatabase, "Shields10", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields 10")
			elif (fShields <= 0.15 and fLastTime > 2.0):
				pEngineer.SayLine(pDatabase, "Shields15", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields 15")
			elif (fShields <= 0.2 and fLastTime > 2.0):
				pEngineer.SayLine(pDatabase, "Shields20", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields 20")
			elif (fShields <= 0.25 and fLastTime > 2.0):
				pEngineer.SayLine(pDatabase, "Shields25", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields 25")
			elif (fShields <= 0.5 and fLastTime > 2.0):
				pEngineer.SayLine(pDatabase, "Shields50", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields 50")
			elif (fShields <= 0.75 and fLastTime > 2.0):
				pEngineer.SayLine(pDatabase, "Shields75", "Captain", 1, App.CSP_SPONTANEOUS)
#				debug("Shields 75")

		return 0

	def NewAnnounceSpecificShield(pAction, iEventType):
		debug(__name__ + ", AnnounceSpecificShield")
		pShip = MissionLib.GetPlayer()
		if not (pShip):
			return 0

		if (pShip.IsDying()):
			return 0

		pSet = App.g_kSetManager.GetSet("bridge")
		if not pSet:
			return 0

		pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
		if not pEngineer or (pEngineer.IsHidden() or pEngineer.IsAnimatingNonInterruptable() or pEngineer.IsSpeaking() or pShip.GetAlertLevel() == pShip.GREEN_ALERT):
			return 0

		fLastTime = App.g_kUtopiaModule.GetGameTime() - pEngineer.GetLastTalkTime()
		if (fLastTime < 1.0):
			return 0

		fShields = None
		iNumShields = None
		inexistantFacets = None
		pShields = None
		validShieldsToGauge = 0
		if (iEventType == App.ET_TACTICAL_SHIELD_0_LEVEL_CHANGE):
			fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip, specificId = App.ShieldClass.FRONT_SHIELDS)
			pString = "Front"
		elif (iEventType == App.ET_TACTICAL_SHIELD_1_LEVEL_CHANGE):
			fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip, specificId = App.ShieldClass.REAR_SHIELDS)
			pString = "Rear"
		elif (iEventType == App.ET_TACTICAL_SHIELD_2_LEVEL_CHANGE):
			fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip, specificId = App.ShieldClass.TOP_SHIELDS)
			pString = "Top"
		elif (iEventType == App.ET_TACTICAL_SHIELD_3_LEVEL_CHANGE):
			fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip, specificId = App.ShieldClass.BOTTOM_SHIELDS)
			pString = "Bottom"
		elif (iEventType == App.ET_TACTICAL_SHIELD_4_LEVEL_CHANGE):
			fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip, specificId = App.ShieldClass.LEFT_SHIELDS)
			pString = "Left"
		elif (iEventType == App.ET_TACTICAL_SHIELD_5_LEVEL_CHANGE):
			fShields, iNumShields, inexistantFacets, pShields, validShieldsToGauge = provideShieldPercentage(pShip, specificId = App.ShieldClass.RIGHT_SHIELDS)
			pString = "Right"
		else:
#			debug("Uh oh, we don't know what shield we just got hit on (number " + str(iEventType) + ")?")
			return 0

		if validShieldsToGauge > 0:
			pString = pString + "Shield"

			if (fShields < 0.1):
				pString = pString + "Failed"
			elif (fShields < 0.5):
				pString = pString + "Draining"
			else:
				return 0

			pDatabase = pEngineer.GetDatabase()
#			debug(pString)
			pEngineer.SayLine(pDatabase, pString, "Captain", 1, App.CSP_SPONTANEOUS)

		return 0
	try:
		scriptToPatch.Report = NewReport
		scriptToPatch.AnnounceShields = NewAnnounceShields
		scriptToPatch.AnnounceSpecificShield = NewAnnounceSpecificShield
		patchDone = 1
	except:
		patchDone = 0
		traceback.print_exc()

	if patchDone:
		scriptToPatch.VERSION = VERSION
		print __name__, ": Patched your ", toPatchPath, " to cover 0-shield-strength ships"