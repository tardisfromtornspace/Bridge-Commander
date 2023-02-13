# C:\Program Files\Activision\QBR 2.2\Bridge Commander\scripts\ships\Hardpoints\Tardis.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates

	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.DalekVoidShip"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.DalekVoidShip", globals(), locals(), ['*'])
	reload(ParentModule)

# Neat trick I found, reduces space used immensely
from ships.Hardpoints.DalekVoidShip import *

#################################################
#Tardis = App.ShipProperty_Create("Tardis")

#Tardis.SetGenus(1)
#Tardis.SetSpecies(601)
#Tardis.SetMass(190.000000)
#Tardis.SetRotationalInertia(999999999999999999999990.000000)
Tardis.SetShipName("DalekVoidShipOpen")
#Tardis.SetModelFilename("data/Models/Ships/Dalek2005/DalekVoidShip.nif")
#Tardis.SetDamageResolution(1.000000)
#Tardis.SetAffiliation(0)
#Tardis.SetStationary(0)
#Tardis.SetAIString("FedAttack")
#Tardis.SetDeathExplosionSound("g_lsDeathExplosions")
#App.g_kModelPropertyManager.RegisterLocalTemplate(Tardis)

#################################################
enginelight = App.BlinkingLightProperty_Create("engine light")

enginelightForward = App.TGPoint3()
enginelightForward.SetXYZ(0.000000, 1.000000, 0.000000)
enginelightUp = App.TGPoint3()
enginelightUp.SetXYZ(0.000000, 0.000000, 1.000000)
enginelightRight = App.TGPoint3()
enginelightRight.SetXYZ(1.000000, 0.000000, 0.000000)
enginelight.SetOrientation(enginelightForward, enginelightUp, enginelightRight)
enginelightPosition = App.TGPoint3()
enginelightPosition.SetXYZ(0.000000, 0.000000, 0.000000)
enginelight.SetPosition(enginelightPosition)
enginelightLightColor = App.TGColorA()
enginelightLightColor.SetRGBA(1.000000, 1.000000, 0.796999, 0.300000)
enginelight.SetColor(enginelightLightColor)
enginelight.SetRadius(140.000000)
enginelight.SetPeriod(1.000000)
enginelight.SetDuration(0.000000)
enginelight.SetTextureName("scripts/Custom/NanoFXv2/SpecialFX/Gfx/Blinker/Blank.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(enginelight)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	#prop = App.g_kModelPropertyManager.FindByName("Tardis", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("engine light", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)