import App
import Foundation


## MVAM Maps Class
class MVAMMaps(Foundation.BridgePluginDef):

	oObject = None
	bMVAMInstalled  = 1

	def __call__(self, Plug, pBridgeSet, oBridgeInfo):
		self.oInfoModule	= oBridgeInfo

		## If we don't have MVAM installed then BAIL
		if (MVAMMaps.bMVAMInstalled == 0):
			return 0

		## Get the XO Menu
		import Bridge.BridgeUtils
		pXOMenu = Bridge.BridgeUtils.GetBridgeMenu("XO")
		if pXOMenu:
			pMVAMMenu = pXOMenu.GetSubmenuW(App.TGString("MVAM Menu"))
			if pMVAMMenu:
				if pMVAMMenu.GetNumChildren() > 1:
					pGame = App.Game_GetCurrentGame()

					pReint = App.STButton_Cast(pMVAMMenu.GetLastChild())
					if pReint:
						pEvent = pReint.GetActivationEvent()
						if pEvent:
							print "added activation event for re-intergration sequence"
							App.g_kEventManager.AddBroadcastPythonFuncHandler(pEvent.GetEventType(), pGame, __name__ + ".HandleReintegration")

			   
					for i in range(pMVAMMenu.GetNumChildren()-1):
						pButton = App.STButton_Cast(pMVAMMenu.GetNthChild(i))
						if pButton:
							pEvent = pButton.GetActivationEvent()
							if pEvent:
								App.g_kEventManager.AddBroadcastPythonFuncHandler(pEvent.GetEventType(), pGame, __name__ + ".HandleSeperation")

	def GetLastBridgeInfo(self):
		return self.oInfoModule



## Do we have MVAM Installed?
try:
	__import__("Custom.Sneaker.Mvam.SneakerMenuAdd")
	MVAMMaps.bMVAMInstalled = 1
   
except:
	MVAMMaps.bMVAMInstalled = 0


## Create an instance of the class
MVAMMaps.oObject = MVAMMaps("MVAM Maps Bridge Plugin")


oBPCore = __import__("Custom.Autoload.000-Fixes20040612-LCBridgeAddon")
NonSerializedObjects = (
"oBPCore"
)

def HandleSeperation(pObject, pEvent):

	## Set MVAM Maps to seperation
	MVAMMaps.oObject.GetLastBridgeInfo().bMVAM = 1
	global oBPCore

	if oBPCore:
		pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
		sBridgeConfig = pBridgeSet.GetConfig()
		oBPCore.AttachPlayerEvents(Foundation.bridgeList._keyList[sBridgeConfig], pBridgeSet)

	## Update the maps
	oBPCore.AlertLevel(None, None)

	## Process
	if (pObject and pEvent):
		pObject.CallNextHandler(pEvent)


def HandleReintegration(pObject, pEvent):

	print "handleing re-intergration"

	global oBPCore

	if oBPCore:
		pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
		sBridgeConfig = pBridgeSet.GetConfig()
		oBPCore.AttachPlayerEvents(Foundation.bridgeList._keyList[sBridgeConfig], pBridgeSet)

	## Set the MVAM Maps to null
	#MVAMMaps.oObject.GetLastBridgeInfo().bMVAM = 0
	##MVAMMaps.oObject.GetLastBridgeInfo().bMVAM = -1		# (went with 0 becuase this will bypass the reintergration maps)
	MVAMMaps.oObject.GetLastBridgeInfo().bMVAM = -1 # I'm afraid we do need this identifier.

	# Set to Red Alert condition.  Dark bridges are cool.
	RedAlert = App.TGIntEvent_Create()
	RedAlert.SetDestination(App.Game_GetCurrentGame().GetPlayer())
	RedAlert.SetEventType(App.ET_SET_ALERT_LEVEL)
	RedAlert.SetInt(App.Game_GetCurrentGame().GetPlayer().RED_ALERT)
	App.g_kEventManager.AddEvent(RedAlert)


	## Update the maps
	#pBridgePlugin = __import__("Custom.Autoload.000-Fixes20040612-LCBridgeAddon")
	#pBridgePlugin.AlertLevel(None,None)

	## Process
	if (pObject and pEvent):
		pObject.CallNextHandler(pEvent) 
