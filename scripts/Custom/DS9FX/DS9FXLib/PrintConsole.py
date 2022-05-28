# Made by Mleo. All Rights Reserved.

# Changed output paths - USS Sovereign.
# Thx for the permission Mleo BTW :)

import App
import nt

def Print(sFile = "ConsoleDump.txt"):
	pTop = App.TopWindow_GetTopWindow()
	pCon = pTop.FindMainWindow(App.MWT_CONSOLE)
	pConsole = App.TGConsole_Cast(pCon.GetFirstChild())
	file = nt.open("scripts\\Custom\\DS9FX\\" + sFile, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
	pString = App.TGString()
	for i in range(0, pConsole.GetNumChildren(), 1):
		pPara = App.TGParagraph_Cast(pConsole.GetNthChild(i))
		pPara.GetString(pString)
		nt.write(file, pString.GetCString() + "\n###\n")

	nt.close(file)

def CreateScrollableConsole():
	pTop = App.TopWindow_GetTopWindow()
	pCon = pTop.FindMainWindow(App.MWT_CONSOLE)
	pConsole = App.TGConsole_Cast(pCon.GetFirstChild())
	
	pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Console"), 0.0, 0.0, None, 1, 1, 0.45)
	pWindow.AddChild(pConsole)
	pCon.AddChild(pWindow)
	pWindow.SetUseScrolling(1)
	pWindow.Layout()
	pWindow.InteriorChangedSize()

	
