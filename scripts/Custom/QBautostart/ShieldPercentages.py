from bcdebug import debug
import App
import MissionLib

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }


ICON_POS_BASE_X = 640
ICON_POS_BASE_Y = 480

RIGHT_SHIELD_X = 0.2
RIGHT_SHIELD_Y = 0.11
LEFT_SHIELD_X = 0.0
LEFT_SHIELD_Y = 0.11
FORWARD_SHIELD_X = 0.1
FORWARD_SHIELD_Y = -0.01
BACK_SHIELD_X = 0.1
BACK_SHIELD_Y = 0.215
LOWER_SHIELD_X = 0.17
LOWER_SHIELD_Y = 0.18
UPPER_SHIELD_X = 0.17
UPPER_SHIELD_Y = 0.05

NonSerializedObjects = (
"g_pShieldPercentageTimer"
)

class ShieldPercentageTimer:
	def __init__(self):
		debug(__name__ + ", __init__")
		
		pUtopiaApp = App.UtopiaApp_GetApp()
		iWidth = pUtopiaApp.GetWidth()
		iHeight = pUtopiaApp.GetHeight()
		fWidthMult = float(ICON_POS_BASE_X)/iWidth
		fHeightMult = float(ICON_POS_BASE_Y)/iHeight
		
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pDisplay = pTCW.GetShipDisplay()
		self.pShieldsDisplay = pDisplay.GetShieldsDisplay()
		self.pEnemyShipDisplay = pTCW.GetEnemyShipDisplay()
		
		self.pRightChild = App.TGParagraph_Create("")
		self.pLeftChild = App.TGParagraph_Create("")
		self.pForwardChild = App.TGParagraph_Create("")
		self.pBackChild = App.TGParagraph_Create("")
		self.pLowerChild = App.TGParagraph_Create("")
		self.pUpperChild = App.TGParagraph_Create("")

		self.pTargetRightChild = App.TGParagraph_Create("")
		self.pTargetLeftChild = App.TGParagraph_Create("")
		self.pTargetForwardChild = App.TGParagraph_Create("")
		self.pTargetBackChild = App.TGParagraph_Create("")
		self.pTargetLowerChild = App.TGParagraph_Create("")
		self.pTargetUpperChild = App.TGParagraph_Create("")
		
		self.pShieldsDisplay.AddChild(self.pRightChild, RIGHT_SHIELD_X*fWidthMult, RIGHT_SHIELD_Y*fHeightMult)
		self.pShieldsDisplay.AddChild(self.pLeftChild, LEFT_SHIELD_X*fWidthMult, LEFT_SHIELD_Y*fHeightMult)
		self.pShieldsDisplay.AddChild(self.pForwardChild, FORWARD_SHIELD_X*fWidthMult, FORWARD_SHIELD_Y*fHeightMult)
		self.pShieldsDisplay.AddChild(self.pBackChild, BACK_SHIELD_X*fWidthMult, BACK_SHIELD_Y*fHeightMult)
		self.pShieldsDisplay.AddChild(self.pLowerChild, LOWER_SHIELD_X*fWidthMult, LOWER_SHIELD_Y*fHeightMult)
		self.pShieldsDisplay.AddChild(self.pUpperChild, UPPER_SHIELD_X*fWidthMult, UPPER_SHIELD_Y*fHeightMult)

		self.pEnemyShipDisplay.AddChild(self.pTargetRightChild, RIGHT_SHIELD_X*fWidthMult, RIGHT_SHIELD_Y*fHeightMult)
		self.pEnemyShipDisplay.AddChild(self.pTargetLeftChild, LEFT_SHIELD_X*fWidthMult, LEFT_SHIELD_Y*fHeightMult)
		self.pEnemyShipDisplay.AddChild(self.pTargetForwardChild, FORWARD_SHIELD_X*fWidthMult, FORWARD_SHIELD_Y*fHeightMult)
		self.pEnemyShipDisplay.AddChild(self.pTargetBackChild, BACK_SHIELD_X*fWidthMult, BACK_SHIELD_Y*fHeightMult)
		self.pEnemyShipDisplay.AddChild(self.pTargetLowerChild, LOWER_SHIELD_X*fWidthMult, LOWER_SHIELD_Y*fHeightMult)
		self.pEnemyShipDisplay.AddChild(self.pTargetUpperChild, UPPER_SHIELD_X*fWidthMult, UPPER_SHIELD_Y*fHeightMult)
		
		self.pTimerProcess = None
		self.SetupTimer()

	def SetupTimer(self):
		debug(__name__ + ", SetupTimer")
		if self.pTimerProcess:
			# We already have a timer.
			return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)
		self.pTimerProcess.SetDelay(1)
	
	def Update(self, dTimeAvailable):
		debug(__name__ + ", Update")
			
		pPlayer = MissionLib.GetPlayer()
		if pPlayer and pPlayer.GetShields():
			pShields = pPlayer.GetShields()
			
			fRightShield = pShields.GetSingleShieldPercentage(App.ShieldClass.RIGHT_SHIELDS)
			fLeftShield = pShields.GetSingleShieldPercentage(App.ShieldClass.LEFT_SHIELDS)
			fForwardShield = pShields.GetSingleShieldPercentage(App.ShieldClass.FRONT_SHIELDS)
			fBackShield = pShields.GetSingleShieldPercentage(App.ShieldClass.REAR_SHIELDS)
			fLowerShield = pShields.GetSingleShieldPercentage(App.ShieldClass.BOTTOM_SHIELDS)
			fUpperShield = pShields.GetSingleShieldPercentage(App.ShieldClass.TOP_SHIELDS)
			
			self.pRightChild.SetString("%3.0f" % (fRightShield*100))
			self.pLeftChild.SetString("%3.0f" % (fLeftShield*100))
			self.pForwardChild.SetString("%3.0f" % (fForwardShield*100))
			self.pBackChild.SetString("%3.0f" % (fBackShield*100))
			self.pLowerChild.SetString("%3.0f" % (fLowerShield*100))
			self.pUpperChild.SetString("%3.0f" % (fUpperShield*100))
		
		if pPlayer and App.ShipClass_Cast(pPlayer.GetTarget()) and App.ShipClass_Cast(pPlayer.GetTarget()).GetShields() and \
		    pPlayer.GetSensorSubsystem() and pPlayer.GetSensorSubsystem().IsObjectNear(pPlayer.GetTarget()) and \
		    pPlayer.GetSensorSubsystem().IsObjectKnown(pPlayer.GetTarget()):

			pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
			pShields = pTarget.GetShields()

			fRightShield = pShields.GetSingleShieldPercentage(App.ShieldClass.RIGHT_SHIELDS)
			fLeftShield = pShields.GetSingleShieldPercentage(App.ShieldClass.LEFT_SHIELDS)
			fForwardShield = pShields.GetSingleShieldPercentage(App.ShieldClass.FRONT_SHIELDS)
			fBackShield = pShields.GetSingleShieldPercentage(App.ShieldClass.REAR_SHIELDS)
			fLowerShield = pShields.GetSingleShieldPercentage(App.ShieldClass.BOTTOM_SHIELDS)
			fUpperShield = pShields.GetSingleShieldPercentage(App.ShieldClass.TOP_SHIELDS)

			self.pTargetRightChild.SetString("%3.0f" % (fRightShield*100))
			self.pTargetLeftChild.SetString("%3.0f" % (fLeftShield*100))
			self.pTargetForwardChild.SetString("%3.0f" % (fForwardShield*100))
			self.pTargetBackChild.SetString("%3.0f" % (fBackShield*100))
			self.pTargetLowerChild.SetString("%3.0f" % (fLowerShield*100))
			self.pTargetUpperChild.SetString("%3.0f" % (fUpperShield*100))
		else:
			self.pTargetRightChild.SetString("")
			self.pTargetLeftChild.SetString("")
			self.pTargetForwardChild.SetString("")
			self.pTargetBackChild.SetString("")
			self.pTargetLowerChild.SetString("")
			self.pTargetUpperChild.SetString("")


def init():
	debug(__name__ + ", init")
	global g_pShieldPercentageTimer
	g_pShieldPercentageTimer = ShieldPercentageTimer()
