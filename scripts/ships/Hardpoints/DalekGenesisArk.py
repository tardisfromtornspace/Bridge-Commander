# C:\Utopia\Current\Build\scripts\ships\Hardpoints\Dalek2005Gold.py
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.TardisType89"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.TardisType89", globals(), locals(), ['*'])
	reload(ParentModule)

# Neat trick I found, reduces space used immensely
from ships.Hardpoints.TardisType89 import *

#################################################
#Tardis = App.ShipProperty_Create("Tardis")

#Tardis.SetGenus(1)
#Tardis.SetSpecies(601)
#Tardis.SetMass(190.000000)
#Tardis.SetRotationalInertia(999999999999999999999990.000000)
Tardis.SetShipName("GenesisArk")
#Tardis.SetModelFilename("data/Models/Ships/Dalek2005/DalekVoidShip.nif")
#Tardis.SetDamageResolution(1.000000)
#Tardis.SetAffiliation(0)
#Tardis.SetStationary(0)
#Tardis.SetAIString("FedAttack")
#Tardis.SetDeathExplosionSound("g_lsDeathExplosions")
#App.g_kModelPropertyManager.RegisterLocalTemplate(Tardis)

def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
#	prop = App.g_kModelPropertyManager.FindByName("Dalek2005Black", App.TGModelPropertyManager.LOCAL_TEMPLATES)
#	if (prop != None):
#		pObj.AddToSet("Scene Root", prop)