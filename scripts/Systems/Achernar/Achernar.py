from bcdebug import debug
import App

def CreateMenus():
	debug(__name__ + ", CreateMenus")
	import Systems.Utils
	return Systems.Utils.CreateSystemMenu("Achernar", "Systems.Achernar.Achernar1",
					                 "Systems.Achernar.Achernar1")
