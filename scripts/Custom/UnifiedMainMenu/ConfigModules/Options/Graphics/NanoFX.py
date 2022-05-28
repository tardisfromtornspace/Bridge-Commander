# NanoFXv2 Beta Configurations panel
#
# by MLeo Daalder
#
# This is a rewrite of the original configurations panel (also by me) for the Unified Main Menu system

import App
import MainMenu.mainmenu
from Custom.NanoFXv2 import NanoFX_Config

ConfigPath = "scripts\\Custom\\NanoFXv2\\NanoFX_Config.py"

def GetName():
    return "NanoFX v2 Beta Configurations"

ET_TOGGLE_BUTTON = App.UtopiaModule_GetNextEventType()
ET_STATE_BUTTON  = App.UtopiaModule_GetNextEventType()
ET_ONOFF_BUTTON  = App.UtopiaModule_GetNextEventType()

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_TOGGLE_BUTTON, __name__ + ".HandleToggleButton")
    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_STATE_BUTTON,  __name__ + ".HandleStateButton")
    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_ONOFF_BUTTON,  __name__ + ".HandleOnOffButton")

    pBridgeFX = App.STCharacterMenu_Create("BridgeFX")
    pContentPanel.AddChild(pBridgeFX)

    pBridgeFXEnabled = CreateMenuYesNoButton(App.TGString("Enable BridgeFX"), "bFX_Enabled", NanoFX_Config.bFX_Enabled)
    pBridgeFX.AddChild(pBridgeFXEnabled)

    pBridgeFXExpSpkLvl = CreateStateButton(App.TGString("Explosion Spark Level: "), "bFX_ExpSparkFXLevel", [App.TGString("Low"), App.TGString("Medium"), App.TGString("High"), App.TGString("Ultra")], NanoFX_Config.bFX_ExpSparkFXLevel-1)
    pBridgeFX.AddChild(pBridgeFXExpSpkLvl)

    pBridgeFXDamSpkLvl = CreateStateButton(App.TGString("Damage Spark Level: "), "bFX_DamageSparkFXLevel", [App.TGString("Low"), App.TGString("Medium"), App.TGString("High"), App.TGString("Ultra")], NanoFX_Config.bFX_DamageSparkFXLevel-1)
    pBridgeFX.AddChild(pBridgeFXDamSpkLvl)

    pBridgeFXDamSpkDur = CreateTextField(App.TGString("Damage Spark Duration: "), "bFX_DamageSparkFXDuration")
    pBridgeFX.AddChild(pBridgeFXDamSpkDur)

    pBridgeFXParContr  = CreateTextField(App.TGString("Particle Control: "), "bFX_ParticleControl")
    pBridgeFX.AddChild(pBridgeFXParContr)


    pCameraFX = App.STCharacterMenu_Create("CameraFX")
    pContentPanel.AddChild(pCameraFX)

    pCameraFXEnabled = CreateMenuYesNoButton(App.TGString("Enable CameraFX"), "cFX_Enabled", NanoFX_Config.cFX_Enabled)
    pCameraFX.AddChild(pCameraFXEnabled)

    pCameraFXViewScreenDefault = CreateTextField(App.TGString("Viewscreen Default Zoom: "), "cFX_ViewScreenDefault")
    pCameraFX.AddChild(pCameraFXViewScreenDefault)

    pCameraFXMaxZoom = CreateTextField(App.TGString("Viewscreen Maximum Zoom: "), "cFX_ViewScreenMax")
    pCameraFX.AddChild(pCameraFXMaxZoom)

    pCameraFXAwayDist = CreateTextField(App.TGString("Away Distance: "), "cFX_AwayDistance")
    pCameraFX.AddChild(pCameraFXAwayDist)

    pCameraFXForwardDist=CreateTextField(App.TGString("Forward Distance: "), "cFX_ForwardDistance")
    pCameraFX.AddChild(pCameraFXForwardDist)


    pExplosionFX = App.STCharacterMenu_Create("ExplosionFX")
    pContentPanel.AddChild(pExplosionFX)

    pExplosionFXEnabled = CreateMenuYesNoButton(App.TGString("Enable ExplosionFX"), "eFX_Enabled", NanoFX_Config.eFX_Enabled)
    pExplosionFX.AddChild(pExplosionFXEnabled)

    pExplosionFXFlickerLight = CreateOnOffButton(App.TGString("Flickering Lights: "), "eFX_LightFlickerFX", NanoFX_Config.eFX_LightFlickerFX)
    pExplosionFX.AddChild(pExplosionFXFlickerLight)

    pExplosionFXFixBright = CreateOnOffButton(App.TGString("Fix Bright Glows Bug: "), "eFX_FixBrightGlows", NanoFX_Config.eFX_FixBrightGlows)
    pExplosionFX.AddChild(pExplosionFXFixBright)

    pExplosionFXExpSpkLvl = CreateStateButton(App.TGString("Explosion Spark Level: "), "eFX_ExpSparkFXLevel", [App.TGString("Low"), App.TGString("Medium"), App.TGString("High"), App.TGString("Ultra")], NanoFX_Config.eFX_ExpSparkFXLevel-1)
    pExplosionFX.AddChild(pExplosionFXExpSpkLvl)

    pExplosionFXDamSpkLvl = CreateStateButton(App.TGString("Damage Spark Level: "), "eFX_DamageSparkFXLevel", [App.TGString("Low"), App.TGString("Medium"), App.TGString("High"), App.TGString("Ultra")], NanoFX_Config.eFX_DamageSparkFXLevel-1)
    pExplosionFX.AddChild(pExplosionFXDamSpkLvl)

    pExplosionFXDamSpkDur = CreateTextField(App.TGString("Damage Spark Duration: "), "eFX_DamageSparkFXDuration")
    pExplosionFX.AddChild(pExplosionFXDamSpkDur)

    pExplosionFXDebLvl = CreateStateButton(App.TGString("DebrisFX Level: "), "eFX_DebrisFXLevel", [App.TGString("Low"), App.TGString("Medium"), App.TGString("High"), App.TGString("Ultra")], NanoFX_Config.eFX_DebrisFXLevel-1)
    pExplosionFX.AddChild(pExplosionFXDebLvl)

    pExplosionFXDebDur = CreateTextField(App.TGString("DebrisFX Duration: "), "eFX_DebrisFXDuration")
    pExplosionFX.AddChild(pExplosionFXDebDur)

    pExplosionFXParContr  = CreateTextField(App.TGString("Particle Control: "), "eFX_ParticleControl")
    pExplosionFX.AddChild(pExplosionFXParContr)

    pExplosionFXRotationFX = CreateOnOffButton(App.TGString("RotationFX: "), "eFX_RotationFX", NanoFX_Config.eFX_RotationFX)
    pExplosionFX.AddChild(pExplosionFXRotationFX)

    pExplosionFXSplashRad  = CreateTextField(App.TGString("Splash Radius: "), "eFX_SplashRadius")
    pExplosionFX.AddChild(pExplosionFXSplashRad)


    pSpecialFX = App.STCharacterMenu_Create("SpecialFX")
    pContentPanel.AddChild(pSpecialFX)

    pSpecialFXEnabled = CreateMenuYesNoButton(App.TGString("Enable SpecialFX"), "sFX_Enabled", NanoFX_Config.sFX_Enabled)
    pSpecialFX.AddChild(pSpecialFXEnabled)

    pSpecialFXAtmos = CreateOnOffButton(App.TGString("AtmosphereFX: "), "sFX_AtmosphereGlowFX", NanoFX_Config.sFX_AtmosphereGlowFX)
    pSpecialFX.AddChild(pSpecialFXAtmos)

    pSpecialFXPlasma = CreateOnOffButton(App.TGString("PlasmaFX: "), "sFX_PlasmaFX", NanoFX_Config.sFX_PlasmaFX)
    pSpecialFX.AddChild(pSpecialFXPlasma)


    pWarpFX = App.STCharacterMenu_Create("WarpFX")
    pContentPanel.AddChild(pWarpFX)

    pWarpFXEnabled = CreateMenuYesNoButton(App.TGString("Enable WarpFX"), "wFX_Enabled", NanoFX_Config.wFX_Enabled)
    pWarpFX.AddChild(pWarpFXEnabled)

    pWarpFXMaxRandDist  = CreateTextField(App.TGString("Maximum Random Distance: "), "wFX_MaxRandomDistance")
    pWarpFX.AddChild(pWarpFXMaxRandDist)

    return App.TGPane_Create(0,0)

def SaveConfig():
    TRUE = 1
    FALSE = 0
    ###[BridgeFX Settings]###
    bFX_Enabled = NanoFX_Config.bFX_Enabled
    ###
    bFX_ExpSparkFXLevel = NanoFX_Config.bFX_ExpSparkFXLevel
    bFX_DamageSparkFXLevel = NanoFX_Config.bFX_DamageSparkFXLevel
    bFX_DamageSparkFXDuration = NanoFX_Config.bFX_DamageSparkFXDuration
    bFX_ParticleControl = NanoFX_Config.bFX_ParticleControl
    ###
    ###[CameraFX Settings]###
    cFX_Enabled = NanoFX_Config.cFX_Enabled
    ###
    cFX_ViewScreenDefault = NanoFX_Config.cFX_ViewScreenDefault
    cFX_ViewScreenMax = NanoFX_Config.cFX_ViewScreenMax
    cFX_AwayDistance = NanoFX_Config.cFX_AwayDistance
    cFX_ForwardDistance = NanoFX_Config.cFX_ForwardDistance
    ###
    ###[ExplosionFX Settings]###
    eFX_Enabled = NanoFX_Config.eFX_Enabled
    ###
    eFX_LightFlickerFX = NanoFX_Config.eFX_LightFlickerFX
    eFX_FixBrightGlows = NanoFX_Config.eFX_FixBrightGlows
    eFX_ExpSparkFXLevel = NanoFX_Config.eFX_ExpSparkFXLevel
    eFX_DamageSparkFXLevel = NanoFX_Config.eFX_DamageSparkFXLevel
    eFX_DamageSparkFXDuration = NanoFX_Config.eFX_DamageSparkFXDuration
    eFX_DebrisFXLevel = NanoFX_Config.eFX_DebrisFXLevel
    eFX_DebrisFXDuration = NanoFX_Config.eFX_DebrisFXDuration
    eFX_ParticleControl = NanoFX_Config.eFX_ParticleControl
    eFX_RotationFX = NanoFX_Config.eFX_RotationFX
    eFX_SplashRadius = NanoFX_Config.eFX_SplashRadius
    ###
    ###[SpecialFX Settings]###
    sFX_Enabled = NanoFX_Config.sFX_Enabled
    ###
    sFX_AtmosphereGlowFX = NanoFX_Config.sFX_AtmosphereGlowFX
    sFX_PlasmaFX = NanoFX_Config.sFX_PlasmaFX
    ###
    ###[WarpFX Settings]###
    wFX_Enabled = NanoFX_Config.wFX_Enabled
    ###
    wFX_MaxRandomDistance = NanoFX_Config.wFX_MaxRandomDistance
    ###

    import nt
    file = nt.open(ConfigPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
    # Write header...
    nt.write(file, "TRUE = 1\nFALSE = 0\n")
    # Write bridge stuff
    nt.write(file, "###[BridgeFX Settings]###\nbFX_Enabled = " + str(bFX_Enabled) +
             "\n###\nbFX_ExpSparkFXLevel = " + str(bFX_ExpSparkFXLevel) +
             "\nbFX_DamageSparkFXLevel = " + str(bFX_DamageSparkFXLevel) +
             "\nbFX_DamageSparkFXDuration = " + str(bFX_DamageSparkFXDuration) +
             "\nbFX_ParticleControl = " + str(bFX_ParticleControl) + "\n###\n")
    # Write camera stuff
    nt.write(file, "###[CameraFX Settings]###\ncFX_Enabled = " + str(cFX_Enabled) +
             "\n###\ncFX_ViewScreenDefault = " + str(cFX_ViewScreenDefault) +
             "\ncFX_ViewScreenMax = " + str(cFX_ViewScreenMax) +
             "\ncFX_AwayDistance = " + str(cFX_AwayDistance) +
             "\ncFX_ForwardDistance = " + str(cFX_ForwardDistance) + "\n###\n")
    # Write explosion stuff
    nt.write(file, "###[ExplosionFX Settings]###\neFX_Enabled = " + str(eFX_Enabled) +
             "\n###\neFX_LightFlickerFX = \"" + str(eFX_LightFlickerFX) + "\"" +
             "\neFX_FixBrightGlows = \"" + str(eFX_FixBrightGlows) + "\"" +
             "\neFX_ExpSparkFXLevel = " + str(eFX_ExpSparkFXLevel) +
             "\neFX_DamageSparkFXLevel = " + str(eFX_DamageSparkFXLevel) +
             "\neFX_DamageSparkFXDuration = " + str(eFX_DamageSparkFXDuration) +
             "\neFX_DebrisFXLevel = " + str(eFX_DebrisFXLevel) +
             "\neFX_DebrisFXDuration = " + str(eFX_DebrisFXDuration) +
             "\neFX_ParticleControl = " + str(eFX_ParticleControl) +
             "\neFX_RotationFX = \"" + str(eFX_RotationFX) + "\"" +
             "\neFX_SplashRadius = " + str(eFX_SplashRadius) + "\n###\n")
    # Write special stuff
    nt.write(file, "###[SpecialFX Settings]###\nsFX_Enabled = " + str(sFX_Enabled) +
             "\n###\nsFX_AtmosphereGlowFX = \"" + str(sFX_AtmosphereGlowFX) + "\"" +
             "\nsFX_PlasmaFX = \"" + str(sFX_PlasmaFX) + "\"\n###\n")
    # Write warp stuff
    nt.write(file, "###[WarpFX Settings]###\nwFX_Enabled = " + str(wFX_Enabled) +
             "\n###\nwFX_MaxRandomDistance = " + str(wFX_MaxRandomDistance) + "\n###\n")
    nt.close(file)

    reload(NanoFX_Config)

def CreateMenuYesNoButton(pName, sVar, iState):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_TOGGLE_BUTTON)
    pEvent.SetString(sVar)
    pEvent.SetDestination(pOptionsWindow)

    pMenuButton = App.STButton_CreateW(pName, pEvent)
    pEvent.SetSource (pMenuButton)

    pMenuButton.SetChoosable (1)
    pMenuButton.SetAutoChoose (1)
    if (iState):
    	pMenuButton.SetChosen (1)
    else:
    	pMenuButton.SetChosen (0)

    return pMenuButton

def CreateStateButton(pName, sVar, lStates, iState):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    kArgs = [pName, iState]
    kEvents=[]
    for kStateName in lStates:
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_STATE_BUTTON)
        pEvent.SetDestination(pOptionsWindow)
        pEvent.SetString(sVar)

        kArgs.append(kStateName)
        kArgs.append(pEvent)
        kEvents.append(pEvent)
    kMenuButton = apply(App.STToggle_CreateW, kArgs)
    for pEvent in kEvents:
        pEvent.SetSource(kMenuButton)

    return kMenuButton

def CreateOnOffButton(pName, sVar, iState):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOffEvent = App.TGStringEvent_Create()
    pOnEvent  = App.TGStringEvent_Create()
    pOffEvent.SetString(sVar)
    pOnEvent.SetString(sVar)
    pOffEvent.SetEventType(ET_ONOFF_BUTTON)
    pOnEvent.SetEventType(ET_ONOFF_BUTTON)
    pOffEvent.SetDestination(pOptionsWindow)
    pOnEvent.SetDestination(pOptionsWindow)

    if iState == "On":
        iState = 0
    else:
        iState = 1

    pMenuButton = App.STToggle_CreateW(pName, iState, App.TGString("On"), pOnEvent, App.TGString("Off"), pOffEvent)
    pOffEvent.SetSource(pMenuButton)
    pOnEvent.SetSource(pMenuButton)
    return pMenuButton

def CreateTextField(pName, sVar):
    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
    LCARS = __import__(pGraphicsMode.GetLcarsModule())
    fMaxWidth = LCARS.MAIN_MENU_CONFIGURE_CONTENT_WIDTH-0.03
    pPane = App.TGPane_Create (fMaxWidth, 1.0)

    # Create the text tag
    pText = App.TGParagraph_CreateW(pName)
    fWidth = pText.GetWidth ()+0.01
    pTText = App.STButton_CreateW(pName, None)
    del pText

    pPane.AddChild(pTText,0,0)
    pTText.SetUseEndCaps(0)
    pTText.SetJustification(App.STButton.LEFT)
    pTText.SetDisabled(1)
    pTText.SetDisabledColor(App.g_kMainMenuBorderMainColor)
    pTText.SetColorBasedOnFlags()
    pTText.SetVisible()

    pcLCARS = pGraphicsMode.GetLcarsString()

    pTextEntry = App.TGParagraph_Create (str(NanoFX_Config.__dict__[sVar]))
    pTextEntry.SetIgnoreString("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*?\t\\/,<>\"|:;\'\n-+()&^%$#@!`~")

    pTextEntry.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
    pTextEntry.SetReadOnly(0)
    pTextEntry.SetColor(App.NiColorA(0,0,0,1))

    pTextEntry.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".HandleKeyboardGoBetween")

    pSubEntry = App.TGParagraph_Create(str(sVar))
    pSubEntry.SetNotVisible(1)

    pPane.AddChild (pTextEntry, fWidth + 0.02, 0.002)
    pPane.AddChild(pSubEntry)

    pPane.Resize (fMaxWidth, pTText.GetHeight(), 0)

    return pPane

def HandleToggleButton(pObject, pEvent):
    NanoFX_Config.__dict__[pEvent.GetCString()] = App.STButton_Cast(pEvent.GetSource()).IsChosen()
    SaveConfig()
    pObject.CallNextHandler(pEvent)

def HandleStateButton(pObject, pEvent):
    NanoFX_Config.__dict__[pEvent.GetCString()] = App.STToggle_Cast(pEvent.GetSource()).GetState()+1
    SaveConfig()
    pObject.CallNextHandler(pEvent)

def HandleOnOffButton(pObject, pEvent):
    iState = "Off"
    if not App.STToggle_Cast(pEvent.GetSource()).GetState():
        iState = "On"
    NanoFX_Config.__dict__[pEvent.GetCString()] = iState
    SaveConfig()
    pObject.CallNextHandler(pEvent)

def HandleKeyboardGoBetween(pObject, pEvent):
    pPara = App.TGParagraph_Cast(pEvent.GetDestination())
    pParent = App.TGPane_Cast(pPara.GetParent())
    pSubPara = App.TGParagraph_Cast(pParent.GetNthChild(2))
    pString = App.TGString()
    pSubPara.GetString(pString)
    pNewVal = App.TGString()
    pPara.GetString(pNewVal)
    sNewVal = pNewVal.GetCString()
    import string
    if string.count(sNewVal, ".") > 1:
        lList = string.split(sNewVal, ".")
        sNewVal = lList[0] + "." + string.join(lList[1:-1], "")
        pPara.SetString(sNewVal)
    NanoFX_Config.__dict__[pString.GetCString()] = pNewVal.GetCString()
    
    SaveConfig()
    pObject.CallNextHandler(pEvent)