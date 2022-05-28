# Prints out text onto screen. MissionLib has one but that one also is used for logging

# by Sov

import App

pPaneID = App.NULL_ID

def PrintText(sText, iPos, iFont, iDur, iDelay):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime(1)
        pSequence.AppendAction(TextSequence(pPane, sText, iPos, iFont, iDur, iDelay))
        pPaneID = pPane.GetObjID()
        pSequence.Play()
        
def TextSequence(pPane, sText, iPos, iFont, iDur, iDelay):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime(1)

        pAction = LineAction(sText, pPane, iPos, iDur, iFont)
        pSequence.AddAction(pAction, None, iDelay)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()
        
def LineAction(sLine, pPane, fPos, duration, fontSize):
        fHeight = fPos * 0.0375
        App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
        pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
        return pAction

def KillPane(pAction):
        global pPaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        pPaneID = App.NULL_ID

        return 0