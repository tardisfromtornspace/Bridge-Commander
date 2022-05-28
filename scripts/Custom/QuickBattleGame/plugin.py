gPluginData = {}

def setProperty(name, value):
	gPluginData[name] = value
	
def getProperty(name):
	if (gPluginData.has_key(name)):
		return gPluginData[name]
	else:
		return None
		
def removeProperty(name):
	del gPluginData[name]
	
def getMainMenu():
	import QBGUI
	return QBGUI.g_pMainMenu

def getMainPanel():
	import QBGUI
	return QBGUI.g_pMainPanel
	
def getActivePanel():
	import QBGUI
	return QBGUI.g_pActivePanel

def setActivePanel(pPanel):
	import QBGUI
	QBGUI.g_pActivePanel = pPanel
