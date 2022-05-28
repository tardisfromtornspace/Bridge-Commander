from bcdebug import debug
import App

def CreateMenus():
	debug(__name__ + ", CreateMenus")
	import Systems.Utils
	return Systems.Utils.CreateSystemMenu("Psi\'s Blackhole", "Systems.PsiBlackhole.PsiBlackhole")
