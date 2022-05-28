from bcdebug import debug
import App
import Custom.GalaxyCharts.TravelerSystems.AISpaceSet
import Custom.GalaxyCharts.Cartographer
SET_NAME = "SpaceSector100"
def Initialize():
	debug(__name__ + ", Initialize")
	global SET_NAME
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, SET_NAME)
	pSet.SetRegionModule(__name__)
	pSet.SetProximityManagerActive(1)
	Custom.GalaxyCharts.TravelerSystems.AISpaceSet.LoadPlacements(SET_NAME)
	Custom.GalaxyCharts.TravelerSystems.AISpaceSet.LoadBackdrops(pSet)
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)
	Custom.GalaxyCharts.Cartographer.RegionManager.AddRegion(SET_NAME, __name__, None, None)
	return pSet
def GetSetName():
	debug(__name__ + ", GetSetName")
	return SET_NAME
def GetSet():
	debug(__name__ + ", GetSet")
	return App.g_kSetManager.GetSet(SET_NAME)
def Terminate():
	debug(__name__ + ", Terminate")
	App.g_kSetManager.DeleteSet(SET_NAME)
