# C:\Utopia\Current\Build\scripts\ships\Hardpoints\DalekCrucibleBomb.py
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.DalekCrucible"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.DalekCrucible", globals(), locals(), ['*'])
	reload(ParentModule)

#################################################
DalekCrucible = App.ShipProperty_Create("DalekCrucible")

DalekCrucible.SetGenus(1)
DalekCrucible.SetSpecies(301)
DalekCrucible.SetMass(7000000.000000)
DalekCrucible.SetRotationalInertia(500000000000.000000)
DalekCrucible.SetShipName("DalekCrucibleBomb")
DalekCrucible.SetModelFilename("data/Models/Ships/DalekCrucible/DalekCrucible.nif")
DalekCrucible.SetDamageResolution(0.000100)
DalekCrucible.SetAffiliation(0)
DalekCrucible.SetStationary(0)
DalekCrucible.SetAIString("NonFedAttack")
DalekCrucible.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(DalekCrucible)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("DalekCrucible", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)