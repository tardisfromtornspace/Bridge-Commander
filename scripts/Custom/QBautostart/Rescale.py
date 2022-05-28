from bcdebug import debug
import App
import MissionLib

MODINFO = { "needBridge": 0 }

# use the ShipName of the Hardpoint file as key here
g_dShipScales = {
#        "ExcelsiorRefitTNG": 0.4,
}


def ObjectCreatedHandler(pObject, pEvent):
        debug(__name__ + ", ObjectCreatedHandler")
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if pShip:
		rescale(pShip)
	pObject.CallNextHandler(pEvent)


def rescale(pShip):
	if not pShip:
		return
	if not pShip.GetShipProperty():
		return
	sShipProbName = pShip.GetShipProperty().GetShipName()
	for sCurName in g_dShipScales.keys():
		if sCurName == sShipProbName:
			pShip.SetScale(g_dShipScales[sCurName])
        

def init():
        debug(__name__ + ", init")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED, MissionLib.GetMission(), __name__ + ".ObjectCreatedHandler")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, MissionLib.GetMission(), __name__ + ".ObjectCreatedHandler")

	# Adjust existing ships
	lSets = App.g_kSetManager.GetAllSets()
	for pSet in lSets:
		for pShip in pSet.GetClassObjectList(App.CT_SHIP):
			rescale(pShip)
