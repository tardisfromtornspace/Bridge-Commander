# Fix Jaggies
# 3rd Era
#
import App
import Custom.UnifiedMainMenu.UMM

bRunOnce = 0

if not Custom.UnifiedMainMenu.UMM.__dict__.get("bNamelessPluginsAllowed", 0):
   def GetName():
      return "3rd Era Jaggie Fix"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
   return None

OriginalFinishOpeningMovie = None

def StartUp():
	import MainMenu.mainmenu
	global OriginalFinishOpeningMovie
	OriginalFinishOpeningMovie = MainMenu.mainmenu.FinishOpeningMovie
	MainMenu.mainmenu.FinishOpeningMovie = AdditionalFinishOpeningMovie

def AdditionalFinishOpeningMovie(pAction):
	global OriginalPlayOpeningMovies
	if OriginalFinishOpeningMovie:
		OriginalFinishOpeningMovie(pAction)
	FixJaggies()
	return 0

def FixJaggies():
	global bRunOnce
	if bRunOnce:
		return
	bRunOnce = 1
	print "Fixing Jaggies"
	## This should be called to fix the Jaggies
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Options.tgl")
	pGraphicsMenu = App.GraphicsMenu_CreateW(pDatabase.GetString("Graphics"))
	pGraphicsMenu.SetNotVisible()
	pGraphicsMenu.SetDisabled()
	pGraphicsMenu.ResetToggles()
	pGraphicsMenu.ChangeDisplayMode()
	del pGraphicsMenu
	App.g_kLocalizationManager.Unload(pDatabase)

	## Switch back to 'New Game'
	from MainMenu.mainmenu import SwitchMiddlePane
	SwitchMiddlePane("New Game")
	return 0

