# This file contains DS9FX events

import App
from Custom.DS9FX.DS9FXEventManager import ProbeEventTypes

ET_FORCE_MISSION_PLAYING = App.UtopiaModule_GetNextEventType()
ET_STOP_FORCING_MISSION_PLAYING = App.UtopiaModule_GetNextEventType()
ET_INSIDE_WORMHOLE = App.UtopiaModule_GetNextEventType()
ET_OUTSIDE_WORMHOLE = App.UtopiaModule_GetNextEventType()
ET_STOP_MANUAL_ENTRY_TRIGGER = App.UtopiaModule_GetNextEventType()
ET_DS9FX_MISSION_START = App.UtopiaModule_GetNextEventType()
ET_DS9FX_MISSION_END = App.UtopiaModule_GetNextEventType()
ET_SHIP_RECREWED = App.UtopiaModule_GetNextEventType()
ET_SHIP_DEAD_IN_SPACE = App.UtopiaModule_GetNextEventType()
ET_SHIP_REACTIVATED = App.UtopiaModule_GetNextEventType()
ET_SHIP_TAKEN_OVER = App.UtopiaModule_GetNextEventType()
ET_COMBAT_EFFECTIVENESS = App.UtopiaModule_GetNextEventType()
ET_COMBAT_EFFECTIVENESS_ADJUSTED = App.UtopiaModule_GetNextEventType()
ET_CUSTOM_DAMAGE = App.UtopiaModule_GetNextEventType()
ET_REPAIR_SHIP = App.UtopiaModule_GetNextEventType()
ET_MVAM_SEP = App.UtopiaModule_GetNextEventType()
ET_MVAM_REIN = App.UtopiaModule_GetNextEventType()
# Redirect events below, they prevent prevent event overloads as seen on DS9FX and GC 2.0 game crash example
ET_APP_ENTERED_SET = App.UtopiaModule_GetNextEventType()
ET_APP_OBJECT_DESTROYED = App.UtopiaModule_GetNextEventType()
ET_APP_OBJECT_EXPLODING = App.UtopiaModule_GetNextEventType()
ET_APP_SUBSYSTEM_DESTROYED = App.UtopiaModule_GetNextEventType()
ET_APP_WEAPON_HIT = App.UtopiaModule_GetNextEventType()
ET_APP_SET_PLAYER = App.UtopiaModule_GetNextEventType()
ET_APP_MUSIC_DONE = App.UtopiaModule_GetNextEventType()
ET_APP_MUSIC_CONDITION_CHANGED = App.UtopiaModule_GetNextEventType()


def Trigger_Force_Mission_Playing(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_FORCE_MISSION_PLAYING)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)
    

def Trigger_Stop_Forcing_Mission_Playing(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_STOP_FORCING_MISSION_PLAYING)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)        


def Trigger_Inside_Wormhole(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_INSIDE_WORMHOLE)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)


def Trigger_Outside_Wormhole(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_OUTSIDE_WORMHOLE)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)  


def Trigger_Stop_Manual_Entry_Trigger(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_STOP_MANUAL_ENTRY_TRIGGER)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)  


def Trigger_DS9FX_Mission_Start(pObject, pName):
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_DS9FX_MISSION_START)
    pEvent.SetDestination(pObject)
    pEvent.SetString(pName)
    App.g_kEventManager.AddEvent(pEvent)
    

def Trigger_DS9FX_Mission_End(pObject, pName): 
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_DS9FX_MISSION_END)
    pEvent.SetDestination(pObject)
    pEvent.SetString(pName)
    App.g_kEventManager.AddEvent(pEvent)  


def Trigger_Ship_Recrewed(pSource, pDestination):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_SHIP_RECREWED)
    pEvent.SetSource(pSource)
    pEvent.SetDestination(pDestination)
    App.g_kEventManager.AddEvent(pEvent)


def Trigger_Ship_Dead_In_Space(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_SHIP_DEAD_IN_SPACE)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)


def Trigger_Ship_Reactivated(pSource, pDestination):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_SHIP_REACTIVATED)
    pEvent.SetSource(pSource)
    pEvent.SetDestination(pDestination)
    App.g_kEventManager.AddEvent(pEvent) 


def Trigger_Ship_Taken_Over(pSource, pDestination):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_SHIP_TAKEN_OVER)
    pEvent.SetSource(pSource)
    pEvent.SetDestination(pDestination)
    App.g_kEventManager.AddEvent(pEvent)


def Trigger_Combat_Effectiveness(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_COMBAT_EFFECTIVENESS)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)


def Trigger_Combat_Effectiveness_Adjusted(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_COMBAT_EFFECTIVENESS_ADJUSTED)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)


def Trigger_Custom_Damage(pObject, fDamage):
    pEvent = App.TGFloatEvent_Create() 
    pEvent.SetEventType(ET_CUSTOM_DAMAGE)
    pEvent.SetDestination(pObject)
    pEvent.SetFloat(fDamage) 
    App.g_kEventManager.AddEvent(pEvent)
    
    
def Trigger_Repair_Ship(pObject):
    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_REPAIR_SHIP)
    pEvent.SetDestination(pObject)
    App.g_kEventManager.AddEvent(pEvent)
    
    
def Trigger_MVAM_Sep(pSource, pDestination, iCount):
    pEvent = App.TGIntEvent_Create()
    pEvent.SetEventType(ET_MVAM_SEP)
    pEvent.SetSource(pSource)
    pEvent.SetDestination(pDestination)
    pEvent.SetInt(iCount)
    App.g_kEventManager.AddEvent(pEvent)
    
    
def Trigger_MVAM_Rein(pSource, pDestination, bReset):
    pEvent = App.TGBoolEvent_Create()
    pEvent.SetEventType(ET_MVAM_REIN)
    pEvent.SetSource(pSource)
    pEvent.SetDestination(pDestination)
    pEvent.SetBool(bReset)
    App.g_kEventManager.AddEvent(pEvent)
    

# Redirect events below, they prevent prevent event overloads as seen on DS9FX and GC 2.0 game crash example
def Trigger_App_Entered_Set(pEvent):
    pNewEvent = ProbeEventTypes.GetMatchingEventType(pEvent)
    if not pNewEvent:
        return 0    
    pNewEvent.Copy(pEvent)
    pNewEvent.SetEventType(ET_APP_ENTERED_SET)
    App.g_kEventManager.AddEvent(pNewEvent)
    
    
def Trigger_App_Object_Destroyed(pEvent):
    pNewEvent = ProbeEventTypes.GetMatchingEventType(pEvent)
    if not pNewEvent:
        return 0    
    pNewEvent.Copy(pEvent)
    pNewEvent.SetEventType(ET_APP_OBJECT_DESTROYED)
    App.g_kEventManager.AddEvent(pNewEvent)
    
    
def Trigger_App_Object_Exploding(pEvent):
    pNewEvent = ProbeEventTypes.GetMatchingEventType(pEvent)
    if not pNewEvent:
        return 0    
    pNewEvent.Copy(pEvent)
    pNewEvent.SetEventType(ET_APP_OBJECT_EXPLODING)
    App.g_kEventManager.AddEvent(pNewEvent)
    

def Trigger_App_Subsystem_Destroyed(pEvent):
    pNewEvent = ProbeEventTypes.GetMatchingEventType(pEvent)
    if not pNewEvent:
        return 0    
    pNewEvent.Copy(pEvent)
    pNewEvent.SetEventType(ET_APP_SUBSYSTEM_DESTROYED)
    App.g_kEventManager.AddEvent(pNewEvent)
    
    
def Trigger_App_Set_Player(pEvent):
    pNewEvent = ProbeEventTypes.GetMatchingEventType(pEvent)
    if not pNewEvent:
        return 0    
    pNewEvent.Copy(pEvent)
    pNewEvent.SetEventType(ET_APP_SET_PLAYER)
    App.g_kEventManager.AddEvent(pNewEvent)
    

def Trigger_App_Music_Done(pEvent):
    pNewEvent = ProbeEventTypes.GetMatchingEventType(pEvent)
    if not pNewEvent:
        return 0    
    pNewEvent.Copy(pEvent)
    pNewEvent.SetEventType(ET_APP_MUSIC_DONE)
    App.g_kEventManager.AddEvent(pNewEvent)
    
    
def Trigger_App_Music_Condition_Changed(pEvent):
    pNewEvent = ProbeEventTypes.GetMatchingEventType(pEvent)
    if not pNewEvent:
        return 0    
    pNewEvent.Copy(pEvent)
    pNewEvent.SetEventType(ET_APP_MUSIC_CONDITION_CHANGED)
    App.g_kEventManager.AddEvent(pNewEvent)