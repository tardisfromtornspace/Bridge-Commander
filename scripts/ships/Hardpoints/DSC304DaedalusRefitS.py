# C:\Utopia\Current\Build\scripts\ships\Hardpoints\DSC304DaedalusRefitS.py
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.DSC304DaedalusRefit"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.DSC304DaedalusRefit", globals(), locals(), ['*'])
	reload(ParentModule)

#################################################
DSC304Daedalus = App.ShipProperty_Create("DSC304Daedalus")

DSC304Daedalus.SetGenus(1)
DSC304Daedalus.SetSpecies(754)
DSC304Daedalus.SetMass(18000.000000)
DSC304Daedalus.SetRotationalInertia(5000.000000)
DSC304Daedalus.SetShipName("DSC304DaedalusRefitS")
DSC304Daedalus.SetModelFilename("data/Models/Ships/DSC304/DSC304Daedalus.nif")
DSC304Daedalus.SetDamageResolution(0.000100)
DSC304Daedalus.SetAffiliation(0)
DSC304Daedalus.SetStationary(0)
DSC304Daedalus.SetAIString("FedAttack")
DSC304Daedalus.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(DSC304Daedalus)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("DSC304Daedalus", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)