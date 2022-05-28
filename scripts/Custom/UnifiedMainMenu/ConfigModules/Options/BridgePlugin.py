# Bridge Plugin Configurations Menu v1
#
# By MLeo Daalder
#
# Features:
#  Ability to turn off improvements on a per bridge level
#  Enable/Disable active lcars
#  Enable/Disable LCARS flickering
#  Enable/Disable Plugins

import App
import Foundation
import string
import nt

import LibConfig

#sConfigPath = "scripts\\Custom\\BridgePluginConfig.py"
oConfigModule = None
oBridgePlugin = __import__("Custom.Autoload.000-Fixes20040612-LCBridgeAddon")

def GetName():
	return "Bridge Plugin"

ET_EVENT = 0xffffff
def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	# Load the config
	#LoadConfig()
	global oConfigModule, ET_EVENT
	oConfigModule = LibConfig.Config("BridgePluginConfig")

	ET_EVENT = App.UtopiaModule_GetNextEventType()


	CreateButton("Disable Active LCARs", pContentPanel, pOptionsPane)


	CreateButton("Disable Animated Maps", pContentPanel, pOptionsPane)

	CreateButton("Disable Animations", pContentPanel, pOptionsPane)


	CreateButton("Disable Extra Models", pContentPanel, pOptionsPane)


	CreateButton("Disable Extra Crew Extensions", pContentPanel, pOptionsPane)


	pOptionsPane.AddPythonFuncHandlerForInstance(ET_EVENT, __name__ + ".HandleFeature")

	pBridgeMenu = App.STCharacterMenu_Create("Per Bridge Extension Disables")
	pContentPanel.AddChild(pBridgeMenu)

	for key in Foundation.bridgeList._arrayList:
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET_EVENT)
		pButton = App.STButton_Create(Foundation.bridgeList[key].name, pEvent)
		pEvent.SetString(key)
		pEvent.SetSource(pButton)
		pEvent.SetDestination(pOptionsPane)
		pButton.SetChoosable(1)
		pButton.SetAutoChoose(1)

		pButton.SetChosen(oConfigModule.get(key, 0))

		pBridgeMenu.AddChild(pButton)


	# Plugin sections
	CreateButton("Disable Plugins", pContentPanel, pOptionsPane)

	pPluginMenu = App.STCharacterMenu_Create("Individual Plugin Control")
	if len(oBridgePlugin.lBridgePluginList):
		pContentPanel.AddChild(pPluginMenu)
		for plugin in oBridgePlugin.lBridgePluginList:
			#if plugin.__dict__.has_key("CreateMenu"):
			pPosMenu = App.STCharacterMenu_Create(plugin.name)
			pPluginMenu.AddChild(pPosMenu)
			CreateButton("Disable", pPosMenu, pOptionsPane, "Disable " + plugin.name)
			pExtra = plugin.CreateMenu(pOptionsPane, pPosMenu, bGameEnded)
			if pExtra:
				pPosMenu.AddChild(pExtra)

			if pPosMenu.GetNumChildren() == 1:
				pDisable = pPosMenu.GetButton("Disable")
				if pDisable:
					pDisable.SetName(App.TGString("Disable " + plugin.name))
					pPosMenu.RemoveChild(pDisable)
					pPluginMenu.AddChild(pDisable)
					pPluginMenu.DeleteChild(pPosMenu)

	if App.g_kUtopiaModule.GetTestMenuState() >= 2:
		CreateButton("Debug Mode", pContentPanel, pOptionsPane)

	return App.TGPane_Create(0,0)

def HandleFeature(pObject, pEvent):
	global oConfigModule
	pButton = App.STButton_Cast(pEvent.GetSource())
	pString = pEvent.GetCString()

	oConfigModule[pString] = pButton.IsChosen()

	pObject.CallNextHandler(pEvent)

def CreateButton(name, pContentPanel, pOptionsPane, config = None):
	global ET_EVENT, oConfigModule
	if not config: config = name
	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(ET_EVENT)
	pButton = App.STButton_Create(name, pEvent)
	pEvent.SetSource(pButton)
	pButton.SetChoosable(1)
	pButton.SetAutoChoose(1)
	pEvent.SetDestination(pOptionsPane)
	pEvent.SetString(config)

	pButton.SetChosen(oConfigModule.get(config, 0))

	pContentPanel.AddChild(pButton)

