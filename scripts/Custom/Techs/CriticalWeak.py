# This is a little hardpoint, which is just to add a weak system
# I've literally used the Stock Sovereign Hull and nerfed it

import App
import GlobalPropertyTemplates

#################################################
LeNewHull = App.HullProperty_Create("Le New Hull")

LeNewHull.SetMaxCondition(1.000000)
LeNewHull.SetCritical(1)
LeNewHull.SetTargetable(1)
LeNewHull.SetPrimary(1)
LeNewHull.SetPosition(0.000000, 0.000000, 0.000000)
LeNewHull.SetPosition2D(62.000000, 42.000000)
LeNewHull.SetRepairComplexity(2.000000)
LeNewHull.SetDisabledPercentage(0.000000)
LeNewHull.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(LeNewHull)
################################################

def LoadPropertySet(pObj):

        prop = App.g_kModelPropertyManager.FindByName("Le New Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
        if (prop != None):
                pObj.AddToSet("Scene Root", prop)
