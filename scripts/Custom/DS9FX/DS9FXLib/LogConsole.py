# This file outputs console errors in a text file

# by Sov & Mleo (I used a part of his code so give credit where due)

# Imports
import App
import nt

# Vars
sPath = 'scripts\\Custom\\DS9FX\\ExitGameLog.txt'

# Functions
def Output():
    pTop = App.TopWindow_GetTopWindow()
    pCon = pTop.FindMainWindow(App.MWT_CONSOLE)
    pConsole = App.TGConsole_Cast(pCon.GetFirstChild())
    App.TopWindow_GetTopWindow().ToggleConsole()
    pConsole.AddConsoleString("# DS9FX has...")
    pConsole.EvalString("# taken a console dump")
    App.TopWindow_GetTopWindow().ToggleConsole()
	
    from time import time, localtime, strftime
    sTime = strftime("%d %b %Y %H:%M:%S", localtime(time()))
    sFirstLine = "##### Bridge Commander Exit Log: " + sTime + "#####\n"
    sEndLine = "##### End Of The Log #####\n"
    pString = App.TGString()
    
    file = nt.open(sPath, nt.O_WRONLY | nt.O_APPEND | nt.O_CREAT)
    nt.write(file, str(sFirstLine))
    for i in range(0, pConsole.GetNumChildren(), 1):
	pPara = App.TGParagraph_Cast(pConsole.GetNthChild(i))
	pPara.GetString(pString)
	nt.write(file, pString.GetCString() + "\n")
    nt.write(file, str(sEndLine))
    nt.close(file)

