################################################################
#######  Gravity FX GUI Script     ##########################
################################################################ 
#################        by Fernando Aluani aka USS Frontier
############################################################
# As i divided what was this script into 2 separate scripts (GravSensorsOptGUI and SystemMapGUI) to handle
# their distinct GUI features, i changed this to be the "master" of both of them, so that upon loading GravityFX
# the LoadGravityFX script only imports this script to start both GUIs.
################################################################
import SystemMapGUI
import GravSensorsOptGUI
import GravGeneratorGUI

def StartGSOGUI():
    GravSensorsOptGUI.CreateGSOGUI()


def StartGravGenGUI():
    GravGeneratorGUI.CreateGravGenGUI()


def StartSystemMapGUI():
    SystemMapGUI.CreateSystemMapGUI()
