import App
import Foundation
import MissionLib

# Author: Admiral_Ames
# Email: admiral_ames@sfhq.net
# Website: http://www.sfhq.net
# Legal: Please do not redistribute this script without my permission

pLeft = "Off"
pRight = "Off"
pUp = "Off"
pDown = "Off"
pImpulse = 0.4
fImpulse = 0

KeyBindingsConfig = __import__ ("Custom.TechnologyExpansion.Scripts.Thrusters.KeyBindings")
pThrusterUp, pThrusterDown, pThrusterLeft, pThrusterRight = KeyBindingsConfig.KeyBindings()

ET_THRUSTERS = App.UtopiaModule_GetNextEventType()

mode = Foundation.MutatorDef("Thrusters")

class Thrusters(Foundation.TriggerDef):
	def __init__(self, dict = {}):
		Foundation.TriggerDef.__init__(self, "Thrusters", ET_THRUSTERS, dict = {})
                # do we have Foundation keys?
                if hasattr(Foundation, "g_kKeyBucket"):
                        # get the key bindings
                        pThrusterLeft = App.g_kKeyboardBinding.FindKey(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 1)
                        pThrusterRight = App.g_kKeyboardBinding.FindKey(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 3)
                        pThrusterDown = App.g_kKeyboardBinding.FindKey(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 5)
                        pThrusterUp = App.g_kKeyboardBinding.FindKey(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 7)
                        # clear old bindings for KEY_UP
                        App.g_kKeyboardBinding.ClearBinding(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 2)
                        App.g_kKeyboardBinding.ClearBinding(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 4)
                        App.g_kKeyboardBinding.ClearBinding(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 6)
                        App.g_kKeyboardBinding.ClearBinding(ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 8)
                        # do new bindings for KEY_UP
                        App.g_kKeyboardBinding.BindKey(pThrusterLeft, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 2)
                        App.g_kKeyboardBinding.BindKey(pThrusterRight, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 4)
                        App.g_kKeyboardBinding.BindKey(pThrusterDown, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 6)
                        App.g_kKeyboardBinding.BindKey(pThrusterUp, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 8)

	def __call__(self, pObject, pEvent):
		vImpPoint = App.TGPoint3()
		global pLeft, pRight, pUp, pDown, g_pThrustersEngine, pImpulse, fImpulse
		pPlayer = MissionLib.GetPlayer()
		pNeutrals = MissionLib.GetNeutralGroup()
		pSet = pPlayer.GetContainingSet()


		if (fImpulse == 0.0):
			pSetY = 0.0
			pTSpeed = pImpulse
			fImpulse2 = pImpulse
		else:
			pSetY = 1.0
			if (fImpulse <= 0.0):
				pTSpeed = -pImpulse
			else:
				pTSpeed = pImpulse
			fImpulse2 = fImpulse
			
		
		dir = pEvent.GetInt()
		if (dir == 1):
			pLeft = "On"
		elif (dir == 2):
			pLeft = "Off"
		elif (dir == 3):
			pRight = "On"
		elif (dir == 4):
			pRight = "Off"
		elif (dir == 5):
			pUp = "On"
		elif (dir == 6):
			pUp = "Off"
		elif (dir == 7):
			pDown = "On"
		elif (dir == 8):
			pDown = "Off"

		if (pLeft == "On" and pRight == "On" and pUp == "On" and pDown == "On"): # Nowhere
			vImpPoint.SetXYZ(0.0, pSetY, 0.0)
		elif (pLeft == "Off" and pRight == "On" and pUp == "On" and pDown == "On"): # Right
			vImpPoint.SetXYZ(pTSpeed, pSetY, 0.0)
		elif (pLeft == "On" and pRight == "Off" and pUp == "On" and pDown == "On"): # Left
			vImpPoint.SetXYZ(-pTSpeed, pSetY, 0.0)
		elif (pLeft == "On" and pRight == "On" and pUp == "Off" and pDown == "On"): # Down
			vImpPoint.SetXYZ(0.0, pSetY, pTSpeed)
		elif (pLeft == "On" and pRight == "On" and pUp == "On" and pDown == "Off"): # Up
			vImpPoint.SetXYZ(0.0, pSetY, -pTSpeed)
		elif (pLeft == "Off" and pRight == "Off" and pUp == "On" and pDown == "On"): # Nowhere
			vImpPoint.SetXYZ(0.0, pSetY, 0.0)
		elif (pLeft == "On" and pRight == "Off" and pUp == "Off" and pDown == "On"): # Left and Down
			vImpPoint.SetXYZ(-pTSpeed, pSetY, pTSpeed)
		elif (pLeft == "On" and pRight == "On" and pUp == "Off" and pDown == "Off"): # Nowhere
			vImpPoint.SetXYZ(0.0, pSetY, 0.0)
		elif (pLeft == "Off" and pRight == "Off" and pUp == "Off" and pDown == "On"): # Down
			vImpPoint.SetXYZ(0.0, pSetY, pTSpeed)
		elif (pLeft == "On" and pRight == "Off" and pUp == "Off" and pDown == "Off"): # Left
			vImpPoint.SetXYZ(-pTSpeed, pSetY, 0.0)
		elif (pLeft == "On" and pRight == "Off" and pUp == "On" and pDown == "Off"): # Left and Up
			vImpPoint.SetXYZ(-pTSpeed, pSetY, -pTSpeed)
		elif (pLeft == "Off" and pRight == "On" and pUp == "Off" and pDown == "On"): # Right and Down
			vImpPoint.SetXYZ(pTSpeed, pSetY, pTSpeed)
		elif (pLeft == "Off" and pRight == "Off" and pUp == "On" and pDown == "On"): # Nowhere
			vImpPoint.SetXYZ(0.0, pSetY, 0.0)
		elif (pLeft == "On" and pRight == "On" and pUp == "Off" and pDown == "On"): # Down
			vImpPoint.SetXYZ(0.0, pSetY, pTSpeed)
		elif (pLeft == "Off" and pRight == "On" and pUp == "On" and pDown == "Off"): # Right and Up
			vImpPoint.SetXYZ(pTSpeed, pSetY, -pTSpeed)
		elif (pLeft == "Off" and pRight == "On" and pUp == "Off" and pDown == "Off"): # Right
			vImpPoint.SetXYZ(pTSpeed, pSetY, 0.0)
		elif (pLeft == "Off" and pRight == "Off" and pUp == "On" and pDown == "Off"): # Up
			vImpPoint.SetXYZ(0.0, pSetY, -pTSpeed)
		elif (pLeft == "Off" and pRight == "Off" and pUp == "Off" and pDown == "Off"): # Nowhere
			vImpPoint.SetXYZ(0.0, pSetY, 0.0)
		else:
			print ("Direction Unknown")
			print pLeft
			print pRight
			print pUp
			print pDown
			vImpPoint.SetXYZ(0.0, 0.0, 0.0)

		pPlayer.SetImpulse(fImpulse2, vImpPoint, App.ShipClass.DIRECTION_MODEL_SPACE)
		
		return 0

Thrusters(dict = {"modes": [mode]})

# do we have Foundation keys?
if hasattr(Foundation, "g_kKeyBucket"):
        # do key bindings for KEY_DOWN
        KeyBindingsConfig.AddKeyBind("Thrusters Left", ET_THRUSTERS, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Thrusters Right", ET_THRUSTERS, 3, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Thrusters Down", ET_THRUSTERS, 5, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Thrusters Up", ET_THRUSTERS, 7, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
else:
        App.g_kKeyboardBinding.BindKey(pThrusterLeft, App.TGKeyboardEvent.KS_KEYDOWN, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 1)
        App.g_kKeyboardBinding.BindKey(pThrusterLeft, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 2)
        App.g_kKeyboardBinding.BindKey(pThrusterRight, App.TGKeyboardEvent.KS_KEYDOWN, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 3)
        App.g_kKeyboardBinding.BindKey(pThrusterRight, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 4)
        App.g_kKeyboardBinding.BindKey(pThrusterDown, App.TGKeyboardEvent.KS_KEYDOWN, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 5)
        App.g_kKeyboardBinding.BindKey(pThrusterDown, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 6)
        App.g_kKeyboardBinding.BindKey(pThrusterUp, App.TGKeyboardEvent.KS_KEYDOWN, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 7)
        App.g_kKeyboardBinding.BindKey(pThrusterUp, App.TGKeyboardEvent.KS_KEYUP, ET_THRUSTERS, App.KeyboardBinding.GET_INT_EVENT, 8)

class ThrustersPart2(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		PrepareThrusters()

ThrustersPart2('ThrustersPart2', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )

def PrepareThrusters():
	global g_pThrustersEngine, g_pPlayer
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	g_pPlayer = pPlayer
        if pPlayer:
	        pSet = pPlayer.GetContainingSet()
	        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_INPUT_SET_IMPULSE, pMission, __name__ + ".SetImpulse" )
	        CreateMenu()

	return 0

def SetImpulse(pMission, pEvent):
	global fImpulse
	fImpulse = pEvent.GetFloat()

	return 0

def CreateMenu():
  	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet('bridge') 
	g_pHelm = App.CharacterClass_GetObject(pBridge, "Helm") 
	pHelmMenu = GetBridgeMenu("Helm")
	pDatabaseBlank = App.g_kLocalizationManager.Load("data/TGL/TechnologyExpansion.tgl")
	pThrustersName = pDatabaseBlank.GetString("CloakedFiring")
	pThrustersName.SetString("Thrusters")
	pThrustersMenu = App.STCharacterMenu_CreateW(pThrustersName)
	pHelmMenu.AddChild(pThrustersMenu)
	import Custom.TechnologyExpansion.Scripts.GUIUtils

	VELOCITY_1 = App.Game_GetNextEventType()
        VELOCITY_2 = App.Game_GetNextEventType()
        VELOCITY_3 = App.Game_GetNextEventType()
        VELOCITY_4 = App.Game_GetNextEventType()
        VELOCITY_5 = App.Game_GetNextEventType()

	pVelocity1 = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("1/8 Thrusters", VELOCITY_1, pThrustersMenu, 1)
	pThrustersMenu.AddChild(pVelocity1)
	pVelocity2 = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("1/4 Thrusters", VELOCITY_2, pThrustersMenu, 1)
	pThrustersMenu.AddChild(pVelocity2)
	pVelocity3 = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("1/2 Thrusters", VELOCITY_3, pThrustersMenu, 1)
	pThrustersMenu.AddChild(pVelocity3)
	pVelocity4 = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("3/4 Thrusters", VELOCITY_4, pThrustersMenu, 1)
	pThrustersMenu.AddChild(pVelocity4)
	pVelocity5 = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Full Thrusters", VELOCITY_5, pThrustersMenu, 1)
	pThrustersMenu.AddChild(pVelocity5)

	pThrustersMenu.AddPythonFuncHandlerForInstance(VELOCITY_1, __name__ + ".Velocity1")
	pThrustersMenu.AddPythonFuncHandlerForInstance(VELOCITY_2, __name__ + ".Velocity2")
	pThrustersMenu.AddPythonFuncHandlerForInstance(VELOCITY_3, __name__ + ".Velocity3")
	pThrustersMenu.AddPythonFuncHandlerForInstance(VELOCITY_4, __name__ + ".Velocity4")
	pThrustersMenu.AddPythonFuncHandlerForInstance(VELOCITY_5, __name__ + ".Velocity5")

	return 0

def Velocity1(pObject, pEvent):
	global pImpulse
	pImpulse = 0.1
def Velocity2(pObject, pEvent):
	global pImpulse
	pImpulse = 0.2
def Velocity3(pObject, pEvent):
	global pImpulse
	pImpulse = 0.3
def Velocity4(pObject, pEvent):
	global pImpulse
	pImpulse = 0.4
def Velocity5(pObject, pEvent):
	global pImpulse
	pImpulse = 0.5

def GetBridgeMenu(Person):
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString(Person))
        App.g_kLocalizationManager.Unload(pDatabase)
        return pMenu
