# This will fake an ET_SET_COURSE event thus fixing incompatibility with DS9FX's Custom Course Setting

# by Sov

import App

def SetCourseEvent():
    pBridge = App.g_kSetManager.GetSet('bridge')
    if not pBridge:
        return
    
    pKiska = App.CharacterClass_GetObject(pBridge, 'Helm')
    if not pKiska:
        return
    
    pEvent = App.TGIntEvent_Create()
    pEvent.SetEventType(App.ET_SET_COURSE)
    pEvent.SetDestination(pKiska)
    pEvent.SetInt(0)
    App.g_kEventManager.AddEvent(pEvent)
