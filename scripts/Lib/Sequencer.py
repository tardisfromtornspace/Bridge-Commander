import App

class Sequence:
	def __init__(self):
		self.pSequence = App.TGSequence_Create()
		
	def play(self):
		self.pSequence.Play()
		
	def appendAction(self, pAction, time=0):
		self.pSequence.AppendAction(pAction, time)

	def appendPreloadLines(self):
		self.pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "PreloadSequenceLines"))
	
	def appendTextBanner(self, text, x, y, time=0):
		self.pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "TextBanner", App.TGString(text), x, y), time)
		
	def appendPlacementWatch(self, setname, placement, camera, bReplace=0, time=0):
		self.pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "PlacementWatch", setname, placement, camera, bReplace), time)

	def appendFadeIn(self, length, time=0):
		self.pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeIn", length), time)
		
	def appendFadeOut(self, length, time=0):
		self.pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeOut", length), time)
	
	def appendThinkLine(self, pDatabase, pCharacter, sLine, sLookAt=None, time=0):
		self.pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SPEAK_LINE_NO_FLAP_LIPS, sLine, sLookAt, 0, pDatabase), time)
		
	def appendSayLine(self, pDatabase, pCharacter, sLine, sLookAt=None, time=0):
		self.pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SAY_LINE, sLine, sLookAt, 1, pDatabase), time)

	def appendSubtitledLine(self, pDatabase, sLine, time=0):
		self.pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "SubtitledLine", pDatabase, sLine), time)
		
	def appendPlayAnimation(self, pCharacter, sAnimation, time=0):
		self.pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_PLAY_ANIMATION_FILE, sAnimation), time)

	def appendDeactivateCharacter(self, pCharacter, time=0):
		self.pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BECOME_INACTIVE), time)

	def appendActivateCharacter(self, pCharacter, time=0):
		self.pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BECOME_ACTIVE), time)
		