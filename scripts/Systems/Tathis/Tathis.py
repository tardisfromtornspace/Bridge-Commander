from bcdebug import debug
import App

def CreateMenus():
	debug(__name__ + ", CreateMenus")
	import Systems.Utils
	return Systems.Utils.CreateSystemMenu("Tathis", "Systems.Tathis.Tathis1",
					                 "Systems.Tathis.Tathis1")
