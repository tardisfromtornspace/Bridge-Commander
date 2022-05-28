import App

# Set the game speed.  1.0 is normal, >1 is fast, <1 is slow.
def Speed(fSpeed):
	if fSpeed > 0:
		App.g_kUtopiaModule.SetTimeScale(fSpeed)

def Save(pcFilename = "Quick.sav"):
	App.g_kUtopiaModule.SaveToFile("Saves/" + pcFilename)

# Enable/disable edit mode.
def Edit():
	pTop = App.TopWindow_GetTopWindow()
	pTop.ToggleEditMode()
	pTop.ToggleConsole()
	if (pTop.IsEditModeEnabled()):
		pTop.ForceTacticalVisible()
		pTop.ToggleBridgeAndTactical()

# Quit
def quit():
    import sys
    sys.exit()

def Quit():
    quit()

###############################################################################
#	TestFont()
#	
#	Font test code that displays every character
#	
#	Args:	iSize	- font size to display
#			sFont	- font name
#	
#	Return:	none
###############################################################################
def TestFont(iSize = 15, sFont = "Crillee"):
	pTop = App.TopWindow_GetTopWindow()
	pCon = pTop.FindMainWindow(App.MWT_CONSOLE)
	pConsole = App.TGConsole_Cast(pCon.GetFirstChild())
	pConsole.SetConsoleFont(sFont, iSize)
	pConsole.AddConsoleString("! \" # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < >")
	pConsole.AddConsoleString("? @ A B C D E F G H I J K L M N O P Q R S T U V W")
	pConsole.AddConsoleString("X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r")
	pConsole.AddConsoleString("s t u v w x y z { | } ~ \x84 � � � � � � � � � � � � �")
	pConsole.AddConsoleString("� � � � � � � � � � � � � � � � � � � � � � � �")
	pConsole.AddConsoleString("� � � � � � � � � � � � � � � � � � � � � � � � � � �")
