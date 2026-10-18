# File: S (Python 1.5)

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.SWDreadnought"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__(ParentPropertyScript, globals(), locals(), ['*'])
	reload(ParentModule)

#################################################
SWDreadnought = App.ShipProperty_Create('SWDreadnought')
SWDreadnought.SetGenus(1)
SWDreadnought.SetSpecies(419)
SWDreadnought.SetMass(3000.0)
SWDreadnought.SetRotationalInertia(2000.0)
SWDreadnought.SetShipName('SWDreadnoughtE')
SWDreadnought.SetModelFilename('')
SWDreadnought.SetDamageResolution(10.0)
SWDreadnought.SetAffiliation(0)
SWDreadnought.SetStationary(0)
SWDreadnought.SetAIString('NonFedAttack')
SWDreadnought.SetDeathExplosionSound('g_lsDeathExplosions')
App.g_kModelPropertyManager.RegisterLocalTemplate(SWDreadnought)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("SWDreadnought", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)