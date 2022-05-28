# Probes an event and returns a matching event type

import App

def GetMatchingEventType(pEvent):
    pNewEvent = None
    if hasattr(pEvent, "GetBool"):
        pNewEvent = App.TGBoolEvent_Create()
    elif hasattr(pEvent, "GetChar"):
        pNewEvent = App.TGCharEvent_Create()
    elif hasattr(pEvent, "GetShort"):
        pNewEvent = App.TGShortEvent_Create()
    elif hasattr(pEvent, "GetInt"):
        pNewEvent = App.TGIntEvent_Create()
    elif hasattr(pEvent, "GetFloat"):
        pNewEvent = App.TGFloatEvent_Create()
    elif hasattr(pEvent, "GetString"):
        pNewEvent = App.TGStringEvent_Create()
    elif hasattr(pEvent, "GetVoidPtr"):
        pNewEvent = App.TGVoidPtrEvent_Create()
    else:
        pNewEvent = App.TGEvent_Create()
    return pNewEvent