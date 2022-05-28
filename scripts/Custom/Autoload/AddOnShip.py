from bcdebug import debug
import App
import Foundation

sAddOnShipString = 'Custom.AddOn.ships.'
sAddOnHPString = 'Custom.AddOn.ships.Hardpoints.'

def CheckFolders():
	if sAddOnShipString not in Foundation.FolderManager.folders['ship']:
		Foundation.FolderManager.Add('ship', sAddOnShipString)
	if sAddOnHPString not in Foundation.FolderManager.folders['hp']:
		Foundation.FolderManager.Add('hp', sAddOnHPString)
	if App.g_kUtopiaModule.IsMultiplayer():
		Foundation.FolderManager.Remove('ship', sAddOnShipString)
		Foundation.FolderManager.Remove('hp', sAddOnHPString)


class AddOnShipTrigger(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                debug(__name__ + ", __init__")
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
		CheckFolders()

CheckFolders()
AddOnShipTrigger('AddOn Ship Trigger', App.ET_MISSION_START)

