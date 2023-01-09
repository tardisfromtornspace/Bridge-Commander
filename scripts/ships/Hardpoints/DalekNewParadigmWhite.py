# C:\Utopia\Current\Build\scripts\ships\Hardpoints\Dalek2005Gold.py
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.DalekNewParadigmBlue"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.DalekNewParadigmBlue", globals(), locals(), ['*'])
	reload(ParentModule)

#################################################
Dalek2005Black = App.ShipProperty_Create("Dalek2005Black")

Dalek2005Black.SetGenus(1)
Dalek2005Black.SetSpecies(301)
Dalek2005Black.SetMass(1.000000)
Dalek2005Black.SetRotationalInertia(12220.000000)
Dalek2005Black.SetShipName("DalekNewParadigmWhite")
Dalek2005Black.SetModelFilename("data/Models/Ships/NewParadigmDalek/NewParadigmDalekWhite.nif")
Dalek2005Black.SetDamageResolution(0.000100)
Dalek2005Black.SetAffiliation(0)
Dalek2005Black.SetStationary(0)
Dalek2005Black.SetAIString("NonFedAttack")
Dalek2005Black.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Dalek2005Black)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Dalek2005Black", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)