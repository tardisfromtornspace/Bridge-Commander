# If you are reading this script, fine by me... but you must discover a way to trigger it...

# by Sov

import App

ET_YES = App.UtopiaModule_GetNextEventType()
ET_NO = App.UtopiaModule_GetNextEventType()

def Prompt():
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_YES, __name__ + ".yes")
        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_NO, __name__ + ".no")

        StartWindow()

def StartWindow():
        # Lots of text, switch to small font
        import MainMenu.mainmenu
        App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
        pModalDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))

        pYesEvent = App.TGStringEvent_Create()
        pYesEvent.SetEventType(ET_YES)
        pYesEvent.SetString("EasterYes")
        pYesEvent.SetDestination(pOptionsWindow)

        pNoEvent = App.TGStringEvent_Create()
        pNoEvent.SetEventType(ET_NO)
        pNoEvent.SetString("EasterNo")
        pNoEvent.SetDestination(pOptionsWindow)

        pDatabase = App.g_kLocalizationManager.Load("data/TGL/DS9FXPromptDatabase.tgl")

        pTitle = pDatabase.GetString("EasterEggTitle")
        pText = pDatabase.GetString("EasterEgg")
        pYes = pDatabase.GetString("Yes")
        pNo = pDatabase.GetString("No")

        App.g_kLocalizationManager.Unload(pDatabase)

        pModalDialogWindow.Run(pTitle, pText, pYes, pYesEvent, pNo, pNoEvent)

def yes(pObject, pEvent):
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.RemoveHandlerForInstance(ET_YES, __name__ + ".yes")
        pOptionsWindow.RemoveHandlerForInstance(ET_NO, __name__ + ".no")

        from Custom.UnifiedMainMenu.ConfigModules.Options import DS9FXConfig
        DS9FXConfig.SetEasterEggs(1)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)        

def no(pObject, pEvent):
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.RemoveHandlerForInstance(ET_YES, __name__ + ".yes")
        pOptionsWindow.RemoveHandlerForInstance(ET_NO, __name__ + ".no")

        from Custom.UnifiedMainMenu.ConfigModules.Options import DS9FXConfig
        DS9FXConfig.SetEasterEggs(0)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)   