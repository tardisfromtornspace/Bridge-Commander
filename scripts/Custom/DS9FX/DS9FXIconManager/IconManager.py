# by USS Sovereign

# Imports
import App

# Icon name list
sIconList = ["Icon1", "Icon2", "Icon3", "Icon4", "Icon5", "Icon6", "Icon7", "Icon8", "Icon9", "Icon10", "Icon11", "Icon12", "Icon13", "Icon14", "Icon15", "Icon16", "Icon17"]
sIconExtension = ".tga"

# Register Icon Group
def LoadDS9FX_Icons(pDS9FXIconGroup = None):
        App.g_kIconManager.RegisterIconGroup("DS9FX_Icons", __name__, "DS9FXIcons")
        
# Load icons
def DS9FXIcons(pDS9FXIconGroup = None):    
    	if not pDS9FXIconGroup:
	    pDS9FXIconGroup = App.g_kIconManager.CreateIconGroup("DS9FX_Icons")
	    App.g_kIconManager.AddIconGroup(pDS9FXIconGroup)

	sLocation = None	
        sLocation = 1

        for icon in sIconList:
            kTextureHandle = pDS9FXIconGroup.LoadIconTexture("scripts/Custom/DS9FX/DS9FXIconManager/Icons/" + icon + sIconExtension)
            pDS9FXIconGroup.SetIconLocation(sLocation, kTextureHandle, 0, 0, 256, 256)

            sLocation = sLocation + 1
