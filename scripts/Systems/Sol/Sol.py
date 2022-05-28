from bcdebug import debug
import App

def CreateMenus():
	debug(__name__ + ", CreateMenus")
	import Systems.Utils
	return Systems.Utils.CreateSystemMenu("Sol", "Systems.Sol.Sol9",
										  "Systems.Sol.Sol1",
										  "Systems.Sol.Sol2",
										  "Systems.Sol.Sol3",
										  "Systems.Sol.Sol4",
										  "Systems.Sol.Sol5",
										  "Systems.Sol.Sol6",
										  "Systems.Sol.Sol7",
										  "Systems.Sol.Sol8",
										  "Systems.Sol.Sol9")
