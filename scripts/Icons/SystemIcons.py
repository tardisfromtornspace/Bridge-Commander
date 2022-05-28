from bcdebug import debug
import App

# Load the System Icons icon group.
def LoadSystemIcons(kIcons = None):
	
	# Setup
	debug(__name__ + ", LoadSystemIcons")
	if kIcons is None:
		kIcons = App.g_kIconManager.CreateIconGroup("System")
		# Add group to manager.
		App.g_kIconManager.AddIconGroup(kIcons)
	
	# Mouse cursor
	kTextureHandle = kIcons.LoadIconTexture('Data/Icons/MarksCursor.tga')
	kIcons.SetIconLocation(0, kTextureHandle, 34,  0, 16, 20)
	kIcons.SetIconLocation(1, kTextureHandle,  0, 34, 20, 24)
	kIcons.SetIconLocation(2, kTextureHandle,  0,  0, 26, 32)
	kIcons.SetIconLocation(3, kTextureHandle, 32, 24, 32, 40)
	kIcons.SetIconLocation(4, kTextureHandle, 74, 7, 38, 48)

	# Target cursor
	kTextureHandle = kIcons.LoadIconTexture("Data/Icons/MarksTargetCursors2.tga")
	kIcons.SetIconLocation(10, kTextureHandle, 47, 1, 15, 15)
	kIcons.SetIconLocation(11, kTextureHandle, 0, 0, 19, 19)
	kTextureHandle = kIcons.LoadIconTexture("Data/Icons/MarksTargetCursors1.tga")
	kIcons.SetIconLocation(12, kTextureHandle, 7,  38, 26, 26)
	kIcons.SetIconLocation(13, kTextureHandle, 96, 0, 32, 32)
	kIcons.SetIconLocation(14, kTextureHandle,  0,  0, 38, 38) 

	# Circle cursor
	kTextureHandle = kIcons.LoadIconTexture("Data/Icons/MarksTargetCursors2.tga")
	kIcons.SetIconLocation(20, kTextureHandle, 47,  16, 15, 15)
	kIcons.SetIconLocation(21, kTextureHandle, 19, 0, 19, 19)
	kTextureHandle = kIcons.LoadIconTexture("Data/Icons/MarksTargetCursors1.tga")
	kIcons.SetIconLocation(22, kTextureHandle, 55,  38, 26, 26)
	kIcons.SetIconLocation(23, kTextureHandle, 96, 32, 32, 32)
	kIcons.SetIconLocation(24, kTextureHandle,  48,  0, 38, 38) 
	
	# Slider for numeric bar controls.
	kTextureHandle = kIcons.LoadIconTexture("Data/Icons/BarSlider.tga")
	kIcons.SetIconLocation(100, kTextureHandle, 0, 0, 10, 18)

	# Noise icons (static)
	kTextureHandle = kIcons.LoadIconTexture("Data/Textures/Effects/Noise1.tga")
	kIcons.SetIconLocation(200, kTextureHandle, 0, 0, 200, 200)
	kTextureHandle = kIcons.LoadIconTexture("Data/Textures/Effects/Noise2.tga")
	kIcons.SetIconLocation(201, kTextureHandle, 0, 0, 200, 200)
	kTextureHandle = kIcons.LoadIconTexture("Data/Textures/Effects/Noise3.tga")
	kIcons.SetIconLocation(202, kTextureHandle, 0, 0, 200, 200)

#
# GetScreenResWidth()
#
def GetScreenResWidth():
	debug(__name__ + ", GetScreenResWidth")
	if (App.g_kIconManager.GetScreenWidth() == 640):
		return 0
	if (App.g_kIconManager.GetScreenWidth() == 800):
		return 1
	elif (App.g_kIconManager.GetScreenWidth() == 1024):
		return 2
	elif (App.g_kIconManager.GetScreenWidth() == 1280):
		return 3
	elif (App.g_kIconManager.GetScreenWidth() == 1600):
		return 4
	elif (App.g_kIconManager.GetScreenWidth() > 1500):
		return 4
	elif (App.g_kIconManager.GetScreenWidth() > 1150):
		return 3
	return 2	# default to 1024

#
# SetTrekCursor()
#
def SetTrekCursor():
	debug(__name__ + ", SetTrekCursor")
	iCentering = App.TGRootPane.MCPP_HORIZONTAL_CENTER + App.TGRootPane.MCPP_VERTICAL_TOP
	iResWidth = GetScreenResWidth()
	fScale = 1.0
	App.g_kRootWindow.SetMouseCursor("System", 0 + iResWidth, iCentering, fScale)

def PushTrekCursor():							
	debug(__name__ + ", PushTrekCursor")
	iCentering = App.TGRootPane.MCPP_HORIZONTAL_CENTER + App.TGRootPane.MCPP_VERTICAL_TOP
	iResWidth = GetScreenResWidth()
	fScale = 1.0
	App.g_kRootWindow.PushCursor("System", 0 + iResWidth, iCentering, fScale)

#
# SetTargetCursor()
#
g_kTargetCursorScales = [1.0, 1.0, 1.0, 1.0, 1.0]
def SetTargetCursor():
	debug(__name__ + ", SetTargetCursor")
	iCentering = App.TGRootPane.MCPP_HORIZONTAL_CENTER + App.TGRootPane.MCPP_VERTICAL_CENTER
	iResWidth = GetScreenResWidth()
	fScale = g_kTargetCursorScales[iResWidth]
	App.g_kRootWindow.SetMouseCursor("System", 10 + iResWidth, iCentering, fScale)

#
# SetCircleCursor()
#
g_kCircleCursorScales = [1.0, 1.0, 1.0, 1.0, 1.0]
def SetCircleCursor():
	debug(__name__ + ", SetCircleCursor")
	iCentering = App.TGRootPane.MCPP_HORIZONTAL_CENTER + App.TGRootPane.MCPP_VERTICAL_CENTER
	iResWidth = GetScreenResWidth()
	fScale = g_kCircleCursorScales[iResWidth]
	App.g_kRootWindow.SetMouseCursor("System", 20 + iResWidth, iCentering, fScale)
