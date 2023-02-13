# C:\Utopia\Current\Build\scripts\ships\Hardpoints\Dalek2005Gold.py
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.Dalek2005Black"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.Dalek2005Black", globals(), locals(), ['*'])
	reload(ParentModule)

#################################################
Dalek2005Black = App.ShipProperty_Create("Dalek2005Black")

Dalek2005Black.SetGenus(1)
Dalek2005Black.SetSpecies(301)
Dalek2005Black.SetMass(1.000000)
Dalek2005Black.SetRotationalInertia(12220.000000)
Dalek2005Black.SetShipName("DalekSec")
Dalek2005Black.SetModelFilename("data/Models/Ships/Dalek2005/Dalek2005Black.nif")
Dalek2005Black.SetDamageResolution(0.000100)
Dalek2005Black.SetAffiliation(0)
Dalek2005Black.SetStationary(0)
Dalek2005Black.SetAIString("NonFedAttack")
Dalek2005Black.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Dalek2005Black)
#################################################
JumpspaceDriveB = App.HullProperty_Create("TimeVortex Drive 1")

JumpspaceDriveB.SetMaxCondition(960000.000000)
JumpspaceDriveB.SetCritical(0)
JumpspaceDriveB.SetTargetable(0)
JumpspaceDriveB.SetPrimary(0)
JumpspaceDriveB.SetPosition(0.000000, 0.000000, 0.000000)
JumpspaceDriveB.SetPosition2D(75.000000, 40.000000)
JumpspaceDriveB.SetRepairComplexity(3.000000)
JumpspaceDriveB.SetDisabledPercentage(0.750000)
JumpspaceDriveB.SetRadius(0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpspaceDriveB)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Dalek2005Black", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("TimeVortex Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)