# C:\Utopia\Current\Build\scripts\ships\Hardpoints\victoryturret.py
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.victory"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.victory", globals(), locals(), ['*'])
	reload(ParentModule)

#################################################
Warbird = App.ShipProperty_Create("Warbird")

Warbird.SetGenus(1)
Warbird.SetSpecies(301)
Warbird.SetMass(4000.000000)
Warbird.SetRotationalInertia(20000.000000)
Warbird.SetShipName("VictoryTurretTwo")
Warbird.SetModelFilename("data/Models/Ships/Warbird.nif")
Warbird.SetDamageResolution(12.000000)
Warbird.SetAffiliation(0)
Warbird.SetStationary(0)
Warbird.SetAIString("NonFedAttack")
Warbird.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Warbird)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Warbird", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)