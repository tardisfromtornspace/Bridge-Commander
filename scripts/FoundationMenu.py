import App
import Foundation


class TextButtonFactory:
	def __init__(self, tglDatabase):
		self.isTGL = 0
		self.text = None
		self.tglDatabase = tglDatabase

	def __call__(self, text):
		if self.tglDatabase.HasString(text):
			self.text = self.tglDatabase.GetString(text)
			self.isTGL = 1
			return self.text
		else:
			self.text = text
			self.isTGL = 0
			return text

	def MakeSubMenu(self):
		if self.isTGL:					return App.STCharacterMenu_CreateW(self.text)
		elif self.text is not None:		return App.STCharacterMenu_Create(self.text)
		else:							return App.STCharacterMenu_Create('?!?')

	def MakeIntButton(self, eType, iSubType, uiHandler, fWidth = 0.0, fHeight = 0.0):
		pEvent = App.TGIntEvent_Create()
		pEvent.SetEventType(eType)
		pEvent.SetDestination(uiHandler)
		pEvent.SetInt(iSubType)

		if self.isTGL:
			if fWidth == 0.0:
				return App.STButton_CreateW(self.text, pEvent)
			return App.STRoundedButton_CreateW(self.text, pEvent, fWidth, fHeight)
		elif self.text is not None:
			if fWidth == 0.0:
				return App.STButton_Create(self.text, pEvent)
			return App.STRoundedButton_Create(self.text, pEvent, fWidth, fHeight)
		else:
			if fWidth == 0.0:
				return App.STButton_Create('?!?', pEvent)
			return App.STRoundedButton_Create('?!?', pEvent, fWidth, fHeight)

	def MakeStringButton(self, eType, sSubType, uiHandler, fWidth = 0.0, fHeight = 0.0):
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(eType)
		pEvent.SetDestination(uiHandler)
		pEvent.SetString(sSubType)

		if self.isTGL:
			return App.STButton_CreateW(self.text, pEvent)
		elif self.text is not None:
			return App.STButton_Create(self.text, pEvent)
		else:
			return App.STButton_Create('?!?', pEvent)

	def MakeYesNoButton(self, eType, sString, uiHandler, iState, fWidth = 0.0, fHeight = 0.0):
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(eType)
		pEvent.SetDestination(uiHandler)

		if self.isTGL:
			pMenuButton = App.STButton_CreateW(self.text, pEvent, fWidth, fHeight)
		elif self.text is not None:
			pMenuButton = App.STButton_Create(self.text, pEvent, fWidth, fHeight)
		else:
			pMenuButton = App.STButton_Create('?!?', pEvent, fWidth, fHeight)

		pEvent.SetString(sString)
		pEvent.SetSource(pMenuButton)

		pMenuButton.SetChoosable (1)
		pMenuButton.SetAutoChoose (1)
		if (iState):
			pMenuButton.SetChosen (1)
		else:
			pMenuButton.SetChosen (0)

		return pMenuButton


class MenuBuilderDef:
	def __init__(self, tglDatabase):
		self.tglDatabase = tglDatabase
		self.textButton = TextButtonFactory(tglDatabase)

	def __call__(self, menu):
		pass


class ShipMenuBuilderDef(MenuBuilderDef):
	def __init__(self, tglDatabase):
		MenuBuilderDef.__init__(self, tglDatabase)

	def __call__(self, raceShipList, menu, buttonType, uiHandler, fWidth = 0.0, fHeight = 0.0):
		foundShips = {}
		for race in raceShipList.keys():
			for ship in raceShipList[race][0]:
				foundShips[race] = 1
				break

		raceList = foundShips.keys()
		raceList.sort()

		for race in raceList:
			self.textButton(race)
			pRaceButton = self.textButton.MakeSubMenu()
			menu.AddChild(pRaceButton)

			shipList = raceShipList[race][1].keys()
			shipList.sort()

			for key in shipList:
				ship = raceShipList[race][1][key]
				self.textButton(ship.name)
				pRaceButton.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))

			pRaceButton.ForceUpdate(0)


class BridgeMenuBuilderDef(MenuBuilderDef):
	def __init__(self, tglDatabase):
		MenuBuilderDef.__init__(self, tglDatabase)

	def __call__(self, bridges, menu, buttonType, uiHandler):
		bridgeList = bridges._arrayList
		bridgeList.sort()

		for pBridge in bridgeList:
			i = bridges[pBridge]
			self.textButton(pBridge)
			menu.AddChild(self.textButton.MakeIntButton(buttonType, i.num, uiHandler))


class SystemMenuBuilderDef(MenuBuilderDef):
	def __init__(self, tglDatabase):
		MenuBuilderDef.__init__(self, tglDatabase)

	def BuildSubMenu(self, buttonString, minPlanets, numPlanets, buttonType, uiHandler):
		self.textButton(buttonString)
		pMenu = self.textButton.MakeSubMenu()
		for iIndex in range(minPlanets, numPlanets):
			planetString = buttonString + " " + str (iIndex + 1)
			self.textButton(planetString)
			pMenu.AddChild(self.textButton.MakeStringButton(buttonType, buttonString + str(iIndex + 1), uiHandler))

		pMenu.ForceUpdate(0)

		return pMenu

	def __call__(self, systems, menu, buttonType, uiHandler):
		systemList = systems.keys()
		systemList.sort()

		self.textButton('DeepSpace')
		menu.AddChild(self.textButton.MakeStringButton(buttonType, 'DeepSpace', uiHandler))

		for sSystem in systemList:
			if sSystem == 'DeepSpace':
				continue
			i = systems[sSystem]
			if i.maximum > 1:	menu.AddChild(self.BuildSubMenu(i.name, i.minimum, i.maximum, buttonType, uiHandler))
			else:
				if i.maximum == 1:
					self.textButton(sSystem)
					menu.AddChild(self.textButton.MakeStringButton(buttonType, i.name + '1', uiHandler))
				else:
					self.textButton(sSystem)
					menu.AddChild(self.textButton.MakeStringButton(buttonType, i.name, uiHandler))



