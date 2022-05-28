import App
import Bridge.BridgeUtils
import MissionLib
import ftb.ShipHandlers

Form = None
ET_SELECT_SECOND = App.UtopiaModule_GetNextEventType()
IsVisible = 0

def ToggleForm(pObject, pEvent):
	global Form, ET_SELECT_SECOND, IsVisible
	wChar = pEvent.GetUnicode()
	GoOn = 0
	if(wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TALK_TO_TACTICAL, App.KeyboardBinding.GET_EVENT, 0.0) or App.TopWindow_GetTopWindow().IsTacticalVisible() == 1):
		GoOn = 1
	elif(wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_BRIDGE_AND_TACTICAL, App.KeyboardBinding.GET_EVENT, 0.0)):
		if(App.TopWindow_GetTopWindow().IsTacticalVisible() == 1):
			GoOn = 1
		else:
			if(Form):
				if(Form.IsVisible() or IsVisible):
					Form.SetNotVisible()
					IsVisible = 0
			GoOn = 0
	else:
		if(Form):
			if(Form.IsVisible() or IsVisible):
				Form.SetNotVisible()
				IsVisible = 0
	if(GoOn):
		pMenu = App.TacticalControlWindow_GetTacticalControlWindow()
		if(pMenu):
			if(Form):
				Form.KillChildren()
				if(Form.GetParent()):
					Form.GetParent().DeleteChild(Form)
			Form = App.STStylizedWindow_CreateW("StylizedWindow", "NormalStyle", App.TGString("Select Targets"), 0.8, 0.2, None, 1, 0.2, 0.4, App.g_kSTButtonColors)

			if(Form == None):
				print "Form Creation didn't work!"
				return
			Form.SetUseScrolling(1)
			pMenu.AddChild(Form, 0.8, 0.2, 0)
			Form.SetVisible()
			IsVisible = 1
			lList = GetObjectsInSet(App.Game_GetCurrentGame().GetPlayer().GetContainingSet())
			if(lList != None and lList != []):
				lList.reverse()# I don't want to have the last object first.
				lColors = []
				lColors.append(App.g_kRadarEnemyColor)
				lColors.append(App.g_kRadarFriendlyColor)
				lColors.append(App.g_kRadarNeutralColor)

				for i in range(len(lList)):
					if(lList[i] != None and lList[i].IsDying() == 0 and lList[i].IsDead() == 0):
						pEvent = App.TGIntEvent_Create()
						pEvent.SetEventType(ET_SELECT_SECOND)
						pEvent.SetInt((len(lList) - 1) - i)
						pEvent.SetDestination(Form)
						pButton = App.STButton_Create(lList[i].GetName(), pEvent)
						pButton.SetChoosable(1)
						pButton.SetAutoChoose(1)
						pMyShip = ftb.ShipHandlers.GetShip(App.Game_GetCurrentPlayer())
						pButton.SetChosen(pMyShip.HasAsSecondaryTarget(lList[i]))
						pEvent.SetSource(pButton)
						if(pButton):
							pButton.SetNormalColor(lColors[GetGroup(lList[i])])
							pButton.SetVisible()
							Form.AddChild(pButton)
			return

def ToggleSelection(pObject, pEvent):
	pMyShip = ftb.ShipHandlers.GetShip(App.Game_GetCurrentPlayer())
	pButton = App.STButton_Cast(pEvent.GetSource())
	if(pButton.IsChosen()):
		pMyShip.lSecondaryTargets.append(ftb.ShipHandlers.GetTargetByIdx(pEvent.GetInt()))
	else:
		pMyShip.lSecondaryTargets.remove(ftb.ShipHadnlers.GetTargetByIdx(pEvent.GetInt()))

def GetObjectsInSet(pSet):
	lList = []
	if(pSet):
		groups = []
#		groups.append(MissionLib.GetFriendlyGroup())
		groups.append(MissionLib.GetEnemyGroup())
#		groups.append(MissionLib.GetNeutralGroup())
		for pObjectGroup in groups:
			ObjTuple = pObjectGroup.GetActiveObjectTupleInSet(App.Game_GetCurrentGame().GetPlayer().GetContainingSet())
			if len(ObjTuple):
				for i in ObjTuple:
					pShip = App.ShipClass_Cast(i)
					if(pShip):
						if(pShip.GetObjID() != App.Game_GetCurrentGame().GetPlayer().GetObjID()):
							lList.append(pShip)
	return lList

def GetGroup(pShip):
	if(MissionLib.GetFriendlyGroup().IsNameInGroup(pShip.GetName())):
		return 1
	elif(MissionLib.GetEnemyGroup().IsNameInGroup(pShip.GetName())):
		return 0
	else:
		return 2
