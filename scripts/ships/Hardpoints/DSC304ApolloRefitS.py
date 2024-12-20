# C:\Utopia\Current\Build\scripts\ships\Hardpoints\DSC304ApolloRefitS.py
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.DSC304ApolloRefit"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.DSC304ApolloRefit", globals(), locals(), ['*'])
	reload(ParentModule)

#################################################
DSC304Apollo = App.ShipProperty_Create("DSC304Apollo")

DSC304Apollo.SetGenus(1)
DSC304Apollo.SetSpecies(754)
DSC304Apollo.SetMass(18000.000000)
DSC304Apollo.SetRotationalInertia(5000.000000)
DSC304Apollo.SetShipName("DSC304ApolloRefitS")
DSC304Apollo.SetModelFilename("data/Models/Ships/DSC304/DSC304Apollo.nif")
DSC304Apollo.SetDamageResolution(0.000100)
DSC304Apollo.SetAffiliation(0)
DSC304Apollo.SetStationary(0)
DSC304Apollo.SetAIString("FedAttack")
DSC304Apollo.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(DSC304Apollo)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("DSC304Apollo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)