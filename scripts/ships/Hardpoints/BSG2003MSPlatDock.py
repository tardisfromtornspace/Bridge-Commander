# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\BSG2003MSPlatDock.py
# 

import App
import GlobalPropertyTemplates


	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.BSG2003MSPlat"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__(ParentPropertyScript, globals(), locals(), ['*'])
	reload(ParentModule)

# Neat trick I found, reduces space used immensely
from ships.Hardpoints.BSG2003MSPlat import *

# Setting up local templates.
#################################################
#MobileShipyard = App.ShipProperty_Create("Mobile Shipyard")
#
#MobileShipyard.SetGenus(1)
#MobileShipyard.SetSpecies(108)
#MobileShipyard.SetMass(1000.000000)
#MobileShipyard.SetRotationalInertia(10000.000000)
MobileShipyard.SetShipName("BSG2003MSPlatDock")
#MobileShipyard.SetModelFilename("data/Models/Ships/MSPlat/MSPlat.nif")
#MobileShipyard.SetDamageResolution(0.001000)
#MobileShipyard.SetAffiliation(0)
MobileShipyard.SetStationary(1)
#MobileShipyard.SetAIString("NonFedAttack")
#MobileShipyard.SetDeathExplosionSound("g_lsDeathExplosions")
#App.g_kModelPropertyManager.RegisterLocalTemplate(MobileShipyard)


# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	#prop = App.g_kModelPropertyManager.FindByName("Mobile Shipyard", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)