# This is a little hardpoint, which is just to add a Cloaking Device to a ship
# I've literally used the Stock Romulan Warbird's Cloak

import App
import GlobalPropertyTemplates
################################################
# THESE ARE ONLY FOR THE DICOHESIVE 0.2 MOD
#################################################
FrontShieldIndicator = App.HullProperty_Create("FrontShieldIndicator")

FrontShieldIndicator.SetMaxCondition(1.000000)
FrontShieldIndicator.SetCritical(0)
FrontShieldIndicator.SetTargetable(0)
FrontShieldIndicator.SetPrimary(0)
FrontShieldIndicator.SetPosition(0.000000, 1.300000, 0.000000)
FrontShieldIndicator.SetPosition2D(0.000000, 0.000000)
FrontShieldIndicator.SetRepairComplexity(0.000001)
FrontShieldIndicator.SetDisabledPercentage(0.000000)
FrontShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FrontShieldIndicator)
#################################################
BackShieldIndicator = App.HullProperty_Create("BackShieldIndicator")

BackShieldIndicator.SetMaxCondition(1.000000)
BackShieldIndicator.SetCritical(0)
BackShieldIndicator.SetTargetable(0)
BackShieldIndicator.SetPrimary(0)
BackShieldIndicator.SetPosition(0.000000, -1.300000, 0.000000)
BackShieldIndicator.SetPosition2D(0.000000, 0.000000)
BackShieldIndicator.SetRepairComplexity(0.000001)
BackShieldIndicator.SetDisabledPercentage(0.000000)
BackShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(BackShieldIndicator)
#################################################
PortShieldIndicator = App.HullProperty_Create("PortShieldIndicator")

PortShieldIndicator.SetMaxCondition(1.000000)
PortShieldIndicator.SetCritical(0)
PortShieldIndicator.SetTargetable(1)
PortShieldIndicator.SetPrimary(0)
PortShieldIndicator.SetPosition(-1.300000, 0.000000, 0.000000)
PortShieldIndicator.SetPosition2D(0.000000, 0.000000)
PortShieldIndicator.SetRepairComplexity(0.000001)
PortShieldIndicator.SetDisabledPercentage(0.000000)
PortShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortShieldIndicator)
#################################################
StarShieldIndicator = App.HullProperty_Create("StarShieldIndicator")

StarShieldIndicator.SetMaxCondition(1.000000)
StarShieldIndicator.SetCritical(0)
StarShieldIndicator.SetTargetable(1)
StarShieldIndicator.SetPrimary(0)
StarShieldIndicator.SetPosition(1.300000, 0.000000, 0.000000)
StarShieldIndicator.SetPosition2D(0.000000, 0.000000)
StarShieldIndicator.SetRepairComplexity(0.000001)
StarShieldIndicator.SetDisabledPercentage(0.000000)
StarShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarShieldIndicator)
#################################################
TopShieldIndicator = App.HullProperty_Create("TopShieldIndicator")

TopShieldIndicator.SetMaxCondition(1.000000)
TopShieldIndicator.SetCritical(0)
TopShieldIndicator.SetTargetable(1)
TopShieldIndicator.SetPrimary(0)
TopShieldIndicator.SetPosition(0.000000, 0.000000, 1.300000)
TopShieldIndicator.SetPosition2D(0.000000, 0.000000)
TopShieldIndicator.SetRepairComplexity(0.000001)
TopShieldIndicator.SetDisabledPercentage(0.000000)
TopShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(TopShieldIndicator)
#################################################
BottomShieldIndicator = App.HullProperty_Create("BottomShieldIndicator")

BottomShieldIndicator.SetMaxCondition(1.000000)
BottomShieldIndicator.SetCritical(0)
BottomShieldIndicator.SetTargetable(1)
BottomShieldIndicator.SetPrimary(0)
BottomShieldIndicator.SetPosition(0.000000, 0.000000, -1.300000)
BottomShieldIndicator.SetPosition2D(0.000000, 0.000000)
BottomShieldIndicator.SetRepairComplexity(0.000001)
BottomShieldIndicator.SetDisabledPercentage(0.000000)
BottomShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(BottomShieldIndicator)
################################################
################################################

def LoadPropertySet(pObj):

	prop = App.g_kModelPropertyManager.FindByName("FrontShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BackShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("PortShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("StarShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("TopShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BottomShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)

