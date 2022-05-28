from bcdebug import debug
###########################################################################################################################
###########################################################################################################################
##    THE   ULTIMATE  GUI LIBRARY          (i think)             v1.0
##			by Fernando Aluani aka USS Frontier
## License:
## 	- You can't change this file, but you may distribute it with your mod if you use it on your mod,
##	  and credit must be given to me.
##	- And remember, this file need the GravityFXlib and ListLib, so you may need to include them too, with the above 
##	   mentioned restriction.
#####################################################################################
##  With the purpose of having a single class that woulda make creating GUI elements, icons, and buttons easily,
##  after extensive research, i created this GUI Library, in it you can find the GUICreator class, and the IconCreator
##  and the ButtonCreator class, now you say: "but there is 3 class?!?!", the awnser is:"yes there is, but you only need to
##  use the GUICreator, because she has a ButtonCreator and a IconCreator atribute".
#########
## And the big comments aren't here to increase file size, they are here to explain more easily the stuff contained here
## and they are used for organization purposes!
###########################################################################################################################
###########################################################################################################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#########################################################################
# imports and exports(that don't exist)
#############################################################################
import App
import MissionLib
import nt
import string
import MainMenu.mainmenu
import Custom.GravityFX.GravityFXlib
from Custom.GravityFX.ListLib import *

############################################################################################################
##class##     GUICreator
##################################
# This class involves everything you need to create a GUI, panes, subpanes, windows, paragraphs, message and dialog boxes,
# plus she also hold an instance of a IconCreator class, and a ButtonCreator class (which you can set your own when initializing this),
# these IconCreator and ButtonCreator classes have everything you need to create icons, icon groups, buttons, and showing text banners.
# All of these 3 classes have functions to find a particular element, delete a particular element, or delete all elements,
# that she created, because they keep track of what they created. To get more info on IconCreator and ButtonCreator, visit
# their explanatory comment (the big comment above class, explaining his stuff, like this comment you're reading now).
###############################################################################################
#@@@@@@ initializing/creating the GUICreator
######
# 	- initialize: GUICreator(buttoncreator) 
#     	       buttoncreator -> optional argument, to define the GUICreator object ButtonCreator, if you don't give this arg
#           	                  GUICreator will create her own ButtonCreator object
###############################################################################################
#@@@@@@ The IconCreator/ButtonCreator atributes
######
#	- GUICreatorObject.ButtonCreator -> the GUICreator object's ButtonCreator 
# 	- GUICreatorObject.IconCreator -> the GUICreator object's IconCreator 
#	- GUICreatorObject.CLASS -> a string representing the object class.
#	- GUICreatorObject -> the GUICreator object, it comes with her own unique ID
###############################################################################################
#@@@@@@@The following function is extremely important, required to create panes/subpanes/windows/paragraphs
######
#	-SetInfoForName(name, X = 0, Y = 0, WIDTH = 0.2, HEIGTH = 0.2, IsVisible = 1, Scroll = 0, WinStyle = "NoMinimize")
#		- VERY IMPORTANT function, it defines the name's attributes. the name will later on be used to create something,
#		  and then that function will get the values needed, like X and Y, from the info defined for that name. So yes,
#		  you can just create 1 thing with a single name.
#		- X and Y :  self explanatory, remember that it is between 0 and 1 each one.
#		- WIDTH and HEIGTH: self explanatory, remember that is is between 0 and 1 each one
#		- IsVisible: set to 1 or more if you want that the object to be created with this name will be visible upon creation.
#		- Scroll (ONLY FOR WINDOWS): set to 0 to window not be scrollable, set to 1 to window be scrollable
#		- WinStyle (ONLY FOR WINDOWS): the stylized window style, they can be: "RightBorder", "NoMinimize", "NormalStyle",
#		                   "LeftSeparator", "WeaponsDisplay" or "SolidGlass". defaults to "NoMinimize".
#################################################################################################################
#@@@@@@@The following function are to create a GUI element. they all use the top window as parent if the Parent arg is None*
#@@@@@@@and the Parent arg always defaults to None if it not given *
######
#	-CreatePane(name, Parent = None)
#	-CreateSubPane(name, Parent = None)
#	-CreateWindow(name, Parent = None, color = None)
#	-CreateParagraph(name, StringList, Parent = None)
#		- StringList: additional argument, must be a list of strings with at least one string, the paragraph will be created
#		  		  with these strings, with a newline between each one of them.
#	-UpdateParagraph(name, StringList)
#		- the same as above, but instead of creating the paragraph, just updates her string with the StringList given
####################################################################################################################
#@@@@@@the following functions don't require the SetInfoForName for them*
######
#	-CreateMessageBox(name, text):
#	-CreateDialogBox(name, text, Button1name, Button1event, Button2name, Button2event)
#################
#@@@@@@the following are the misc functions, to get/show/close/delete element or DeleteAllElements
######
#	-GetElement(name)
#	-ShowElement(name)
#	-CloseElement(name)
#	-DeleteElement(name)
#	-DeleteAllElements()
#	-MasterPurge()
#		-This functions deletes everything from the GUICreator and his IconCreator/ButtonCreator instances.
######################################################################################################################
class GUICreator:
	def __init__(self, buttoncreator=None):
		debug(__name__ + ", __init__")
		self.ID = Custom.GravityFX.GravityFXlib.GetUniqueID("GUICreator")
		self.CLASS = 'GUI Creator'
		if buttoncreator:
			if hasattr(buttoncreator, "CLASS"):
				if buttoncreator.CLASS == 'Button Creator':
					self.ButtonCreator = buttoncreator
		else:
			self.ButtonCreator = ButtonCreator()
		self.IconCreator = IconCreator()
		self.Dict = {}
		self.InfoDict = {}
		self.__genericMessageOKevent = GetNextEventType()

	def GetGenericOKEventType(self):
		debug(__name__ + ", GetGenericOKEventType")
		return self.__genericMessageOKevent
	def SetInfoForName(self, name, X = 0, Y = 0, WIDTH = 0.2, HEIGTH = 0.2, IsVisible = 1, Scroll = 0, WinStyle = "NoMinimize"):
		debug(__name__ + ", SetInfoForName")
		self.InfoDict[name] = {'X': X, 'Y': Y, 'WIDTH': WIDTH, 'HEIGTH': HEIGTH, 'Visible': IsVisible, 'Scroll': Scroll, 'Style': WinStyle}
		return self.InfoDict[name]

	def CreatePane(self, name, Parent = None):
		debug(__name__ + ", CreatePane")
		if self.Dict.has_key(name):
			raise NameError, "Can't create pane with name "+name+", there's already a GUI element with this name."
			return None
		if Parent == None:
			Parent = App.TopWindow_GetTopWindow()
		if self.InfoDict.has_key(name):
			pPane = App.TGPane_Create(self.InfoDict[name]['WIDTH'], self.InfoDict[name]['HEIGTH'])
			if self.InfoDict[name]['Visible'] >= 1:
				pPane.SetVisible()
			else:
				pPane.SetNotVisible()
			Parent.AddChild(pPane, self.InfoDict[name]['X'], self.InfoDict[name]['Y'])
			self.Dict[name] = pPane
		else:
			pPane = None
			raise KeyError, "Missing Info for name "+name+", can't create the pane. Before creating a pane, set his info with SetInfoForName()."
		return pPane

	def CreateSubPane(self, name, Parent = None):
		debug(__name__ + ", CreateSubPane")
		if self.Dict.has_key(name):
			raise NameError, "Can't create subpane with name "+name+", there's already a GUI element with this name."
			return None
		if Parent == None:
			Parent = App.TopWindow_GetTopWindow()
		if self.InfoDict.has_key(name):
			pSubPane = App.STSubPane_Create(self.InfoDict[name]['WIDTH'], self.InfoDict[name]['HEIGTH'])
			if self.InfoDict[name]['Visible'] >= 1:
				pSubPane.SetVisible()
			else:
				pSubPane.SetNotVisible()
			Parent.AddChild(pSubPane, self.InfoDict[name]['X'], self.InfoDict[name]['Y'])
			self.Dict[name] = pSubPane
		else:
			pSubPane = None
			raise KeyError, "Missing Info for name "+name+", can't create the subpane. Before creating a subpane, set his info with SetInfoForName()."
		return pSubPane

	def CreateWindow(self, name, Parent = None, color = None):
		debug(__name__ + ", CreateWindow")
		if self.Dict.has_key(name):
			raise NameError, "Can't create window with name "+name+", there's already a GUI element with this name."
			return None
		if Parent == None:
			Parent = App.TopWindow_GetTopWindow()
		if color == None:
			color = App.g_kMainMenuBorderMainColor
		if self.InfoDict.has_key(name):
			pWindow = App.STStylizedWindow_CreateW("StylizedWindow", self.InfoDict[name]['Style'], App.TGString(name), 0, 0, None, 1, self.InfoDict[name]['WIDTH'], self.InfoDict[name]['HEIGTH'], color)
			if self.InfoDict[name]['Visible'] >= 1:
				pWindow.SetVisible()
			else:
				pWindow.SetNotVisible()
			pWindow.SetUseScrolling(self.InfoDict[name]['Scroll'])
			Parent.AddChild(pWindow, self.InfoDict[name]['X'], self.InfoDict[name]['Y'])
			self.Dict[name] = pWindow
		else:
			pWindow = None
			raise KeyError, "Missing Info for name "+name+", can't create the window. Before creating a window, set his info with SetInfoForName()."
		return pWindow

	def CreateParagraph(self, name, StringList, Parent = None):
		debug(__name__ + ", CreateParagraph")
		if self.Dict.has_key(name):
			raise NameError, "Can't create paragraph with name "+name+", there's already a GUI element with this name."
			return None
		if Parent == None:
			Parent = App.TopWindow_GetTopWindow()
		if self.InfoDict.has_key(name):
			pText = App.TGParagraph_Create("", 0.5, None, "", 0.5, App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
			if self.InfoDict[name]['Visible'] >= 1:
				pText.SetVisible()
			else:
				pText.SetNotVisible()
			for string in StringList:
				pText.AppendStringW(App.TGString(string+"\n"))
			Parent.AddChild(pText, self.InfoDict[name]['X'], self.InfoDict[name]['Y'])
			self.Dict[name] = pText
		else:
			pText = None
			raise KeyError, "Missing Info for name "+name+", can't create the paragraph. Before creating a paragraph, set his info with SetInfoForName()."
		return pText
	
	def UpdateParagraph(self, name, StringList):
		debug(__name__ + ", UpdateParagraph")
		if not self.Dict.has_key(name):
			raise NameError, "Can't update paragraph with name "+name+", there's not a GUI element with this name."
			return None
		pPara = self.GetElement(name)
		if pPara:
			sFullString = ""
			pPara.SetString(sFullString)
			for string in StringList:
				sFullString = sFullString + string + "\n"
			pPara.SetString(sFullString)
		return pPara		

	def CreateMessageBox(self, name, text):
		#if self.Dict.has_key(name):
		#	raise NameError, "Can't create MessageBox with name "+name+", there's already a GUI element with this name."
		#	return None
		debug(__name__ + ", CreateMessageBox")
		pTopWindow = App.TopWindow_GetTopWindow()
		pMessageBox = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow (App.MWT_MODAL_DIALOG))
		okEvent = App.TGEvent_Create()
		okEvent.SetEventType(self.__genericMessageOKevent)
		okEvent.SetDestination(pTopWindow)
		pMessageBox.Run(App.TGString(name), App.TGString(text), App.TGString("OK"), okEvent, None, None)
		#self.Dict[name] = pMessageBox
		return pMessageBox

	def CreateDialogBox(self, name, text, Button1name, Button1event, Button2name, Button2event):
		#if self.Dict.has_key(name):
		#	raise NameError, "Can't create DialogBox with name "+name+", there's already a GUI element with this name."
		#	return None
		debug(__name__ + ", CreateDialogBox")
		pTopWindow = App.TopWindow_GetTopWindow()
		pDialogBox = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow (App.MWT_MODAL_DIALOG))
		pDialogBox.Run(App.TGString(name), App.TGString(text), App.TGString(Button1name), Button1event, App.TGString(Button2name), Button2event)
		#self.Dict[name] = pDialogBox
		return pDialogBox

	def GetElement(self, name):
		debug(__name__ + ", GetElement")
		if self.Dict.has_key(name):
			return self.Dict[name]
		else:
			return None

	def ShowElement(self, name):
		debug(__name__ + ", ShowElement")
		pElement = self.GetElement(name)
		if pElement == None:
			return
		if not pElement.IsVisible():
			pElement.SetVisible()
			pElement.SetEnabled()
			pParent = pElement.GetParent()
			pParent.MoveToFront(pElement)
			pParent.MoveTowardsBack(pElement)
			pElement.SetAlwaysHandleEvents()

	def CloseElement(self, name):
		debug(__name__ + ", CloseElement")
		pElement = self.GetElement(name)
		if pElement == None:
			return
		if pElement.IsVisible():
			pElement.SetNotVisible()
			pElement.SetDisabled()
			pParent = pElement.GetParent()
			pParent.MoveToBack(pElement)
			pElement.SetNotAlwaysHandleEvents()

	def DeleteElement(self, name):
		debug(__name__ + ", DeleteElement")
		pElement = self.GetElement(name)
		if pElement == None:
			return
		pParent = pElement.GetParent()
		pParent.DeleteChild(pElement)
		pElement.__del__()
		del self.Dict[name]     

	def DeleteAllElements(self):
  		debug(__name__ + ", DeleteAllElements")
  		for index in self.Dict.keys():
			pElement = self.Dict[index]
			App.g_kFocusManager.RemoveAllObjectsUnder(pElement)
			pTopWindow = App.TopWindow_GetTopWindow()
			pTopWindow.DeleteChild(pElement)
		self.Dict = {}
	def MasterPurge(self):
		debug(__name__ + ", MasterPurge")
		self.DeleteAllElements()
		self.IconCreator.DeleteAllIcons()
		self.ButtonCreator.DeleteAllButtons()
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.ID+">"

############################################################################################################
##class##     IconCreator
######################################
# This class involves everything you need to create icons. Most probably used from a GUICreator object.
###############################################################################################
#@@@@@@ initializing/creating the IconCreator
######
# 	- initialize: IconCreator() 
#     	       yes, simple like that...
###############################################################################################
#@@@@@@ The IconCreator atributes
######
#	- IconCreator.CLASS -> a string representing the object class.
#	- IconCreator -> the IconCreator object, it comes with her own unique ID
###############################################################################################
#@@@@@@@The following function is extremely important, required to create icon and stuff here
######
#	-SetInfoForIcon(name, icongroup, number, X = 0.5, Y = 0.5, WIDTH = 0.2, HEIGTH = 0.2, IsVisible = 1)
#		- VERY IMPORTANT function, it defines the name's attributes. the name will later on be used to create something,
#		  and then that function will get the values needed, like X and Y, from the info defined for that name. So yes,
#		  you can just create 1 thing with a single name.
#		- icongroup: the IconGroup's name that the icon "name" will be created from.
#		- number: number of the icon in the icongroup, the icon "name" will be from this type.
#		- X and Y :  self explanatory, remember that it is between 0 and 1 each one.
#		- WIDTH and HEIGTH: self explanatory, remember that is is between 0 and 1 each one
#		- IsVisible: set to 1 or more if you want that the object to be created with this name will be visible upon creation.
#################################################################################################################
#@@@@@@@The following functions are to create stuuf related to icons. they all use the top window as parent if the Parent arg is None*
#@@@@@@@and the Parent arg always defaults to None if it not given *
######
#	-CreateIconGroup(name, folder)
#		- folder: the path to the folder where the icons are. something like: 'scripts/Custom/MyMod/MyModIcons'
#	-CreateIcon(name, Parent = None)
#	-CreateGlass(name, Parent = None)
#		- This creates that "glass" that appears behind stylized windows and such.
####################################################################################################################
#@@@@@@the following functions don't require the SetInfoForName for them*
######
#	-ShowTextBanner(text, X, Y, fDuration = 3.0, iSize = 16, bHCentered = 1, bVCentered = 0)
#		- this shows on-screen one of those nice text banners, that if i remember correctly are the ones that form the
#		  credits screen, the "Loading..." screen, "ETA", "WARP SPEED", and "DESTINATION" from NanoFX WarpFX and so on.
#################
#@@@@@@the following are the misc functions, to get/show/close/delete element or DeleteAllElements
######
#	-GetIcon(name)
#	-ShowIcon(name)
#	-HideIcon(name)
#	-DeleteIcon(name)
#	-DeleteAllIcons()
######################################################################################################################
class IconCreator:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.ID = Custom.GravityFX.GravityFXlib.GetUniqueID("IconCreator")
		self.CLASS = 'Icon Creator'
		self.IconDict = {}
		self.Info = {}
		self.IconGroupList = []

	def SetInfoForIcon(self, name, icongroup, number, X = 0.5, Y = 0.5, WIDTH = 0.2, HEIGTH = 0.2, IsVisible = 1):
		debug(__name__ + ", SetInfoForIcon")
		self.Info[name] = {'Number': number, 'IconGroup': icongroup, 'X': X, 'Y': Y, 'WIDTH': WIDTH, 'HEIGTH': HEIGTH, 'Visible': IsVisible}

	def CreateIconGroup(self, name, folder):
		debug(__name__ + ", CreateIconGroup")
		if name in self.IconGroupList:
			raise NameError, "Can't create icon group with name "+name+", there's already an icon group created with this name."
			return
		IconGroup = App.g_kIconManager.CreateIconGroup(name)
		FileList = nt.listdir(folder)
		index = 0
		for File in FileList:
			sExt = string.split(File, ".")[-1]
			if sExt == "tga":
				Texture = IconGroup.LoadIconTexture(folder+"/"+File)
				IconGroup.SetIconLocation(index, Texture, 0, 0, 128, 128)
				index = index+1
		App.g_kIconManager.AddIconGroup(IconGroup)
		App.g_kIconManager.RegisterIconGroup(name, name, name)
		self.IconGroupList.append(name)

	def CreateIcon(self, name, Parent = None):
		debug(__name__ + ", CreateIcon")
		if self.IconDict.has_key(name):
			raise NameError, "Can't create icon with name "+name+", icon with this name already exists"
			return None
		if Parent == None:
			Parent = App.TopWindow_GetTopWindow()
		if self.Info.has_key(name):
			pIcon = App.TGIcon_Create(self.Info[name]['IconGroup'], App.SPECIES_UNKNOWN)
			if self.Info[name]['Visible'] >= 1:
				pIcon.SetVisible()
			else:
				pIcon.SetNotVisible()
			pIcon.Resize(self.Info[name]['WIDTH'], self.Info[name]['HEIGTH'])
			pIcon.SetIconNum(self.Info[name]['Number'])
			Parent.AddChild(pIcon, self.Info[name]['X'], self.Info[name]['Y'])
			self.IconDict[name] = pIcon
		else:
			pIcon = None
			raise KeyError, "Missing Info for icon "+name+", can't create the icon. Before creating a icon, set his info with SetInfoForIcon()."
		return pIcon
	
	def ShowTextBanner(self, text, X, Y, fDuration = 3.0, iSize = 16, bHCentered = 1, bVCentered = 0):
		debug(__name__ + ", ShowTextBanner")
		MissionLib.TextBanner(None, App.TGString(text), X, Y, fDuration, iSize, bHCentered, bVCentered)

	def CreateGlass(self, name, Parent = None):
		debug(__name__ + ", CreateGlass")
		if self.IconDict.has_key(name):
			raise NameError, "Can't create glass with name "+name+", there's already a glass icon with this name."
			return None
		if Parent == None:
			Parent = App.TopWindow_GetTopWindow()
		pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		LCARS = pGraphicsMode.GetLcarsString()
		ParentPOS = Parent.GetPosition()
		self.SetInfoForIcon(name, LCARS, 120, ParentPOS.x, ParentPOS.y, Parent.GetWidth(), Parent.GetHeight())
		pGlass = self.CreateIcon(name, Parent)
		return pGlass

	def GetIcon(self, name):
		#debug(__name__ + ", GetIcon")
		if self.IconDict.has_key(name):
			return self.IconDict[name]
		else:
			return None

	def ShowIcon(self, name):
		debug(__name__ + ", ShowIcon")
		pIcon = self.GetIcon(name)
		if pIcon == None:
			return
		pParent = pIcon.GetParent()
		pIcon.SetVisible()
		pParent.MoveToFront(pIcon)
		pParent.MoveTowardsBack(pIcon)

	def HideIcon(self, name):
		debug(__name__ + ", HideIcon")
		pIcon = self.GetIcon(name)
		if pIcon == None:
			return
		pParent = pIcon.GetParent()
		pIcon.SetNotVisible()
		pParent.MoveToBack(pIcon)
		
	def DeleteIcon(self, name):
		debug(__name__ + ", DeleteIcon")
		pIcon = self.GetIcon(name)
		if pIcon == None:
			return
		pIcon = self.IconDict[name]
		pParent = pIcon.GetParent()
		pParent.DeleteChild(self.GetIcon(name))
		del self.IconDict[name]     

	def DeleteAllIcons(self):
  		debug(__name__ + ", DeleteAllIcons")
  		for iconname in self.IconDict.keys():
			pIcon = self.IconDict[iconname]
			pParent = pIcon.GetParent()
			pParent.DeleteChild(pIcon)
		self.IconDict = {}

	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.ID+">"

#############################################################################################################
##class##   ButtonCreator 
################################################
## Used to create various types of buttons, and keep track of them, so if you need to delete them later, just use one
##  of the functions in this class to do so.
########################################################################
#@@@@@@ initializing/creating the ButtonCreator
######
# 	- initialize: ButtonCreato() 
#     	       yes, simple like that...
###############################################################################################
#@@@@@@ ButtonCreator atributes
#	- ButtonCreatorObject.CLASS -> a string representing the object class.
#	- ButtonCreatorObject-> the ButtonCreator object, it comes with her own unique ID
###############################################################################################
#@@@@@@ButtonCreator function to create buttons
######
#	- CreateTextInput(pName, pToMenu, pDefault, fMaxWidth, fLongestLen, pcConfigName, iMaxChars, bBackground = 1, pcIgnoreString = None, Coords = None)
#		^>- returns [TextInputPane obj, TextEntry obj (it's one of TextInputPane childs)]
#	- CreateBar(pName, eType, sFunc, fValue, nRange = [0.0, 0.1], nMarker = 0.0, nUseButton = 0, pToMenu = None, Coords = None, Size = None)
#		^>- return the bar obj
#	- CreateToggleButton(pName, kStateNameList, eEventTypeList, sFunc, iEventValueList, iDefault, pToMenu = None, Coords = None, Size = None)
#		^>- Yes, kStateNameList, eEventTypeList and iEventValueList must be lists with their values, it's difficult to explain, but if your're able to understand why, you're able use this
#		^>- return the button obj
#	- CreateButton(pName, eType, sFunc, iState, pToMenu = None, Coords = None, Size = None)
#		^>- return the button obj
#	- CreateYesNoButton(pName, eType, sFunc, iState, pToMenu = None, Coords = None, Size = None)
#		^>- return the button obj
#	- CreateStringButton(pName, eType, sFunc, sValue, pToMenu = None, Coords = None, Size = None)
#		^>- return the button obj
#####################################################################################################
#@@@@@ButtonCreator misc function, to get/getByID/find/add to button creator created buttons dict/delete/deleteByID
#@@@@@deleteAll 
######
#	- GetButtonByName(name)
#		^>- This gets a button created by ButtonCreator with given name
#		^>- return the button obj if it was found, none if it wasn't
#	- GetButtonByID(ID)
#		^>- This gets a button created by ButtonCreator with given ID
#		^>- return the button obj if it was found, none if it wasn't
#	- FindButtonInPane(pane, name)
#		^>- This finds a button created by ButtonCreator with given name in given pane
#		^>- return the button obj if it was found, none if it wasn't
#	- AddButtonToDict(pName, pButton)
#		^>- This adds the pButton obj with given name to the ButtonCreator created buttons dict. 
#		^>- NOTE: the given name SHOULD be the name of the button!
#	- DeleteButtonByName(name)
#		^>- This deletes the button with given name, if it was created by ButtonCreator
#	- DeleteButtonByID(ID)
#		^>- This deletes the button with given ID, if it was created by ButtonCreator
#	- DeleteAllButtons()
#		^>- This deletes all buttons created by ButtonCreator
#########################################################################################################
# - NOTE: All "Coords" arguments must be dictionarys with 'X' and 'Y' keys, their values are the X and Y posititon respectively
#	    All "Size" arguments must be dictionarys with 'WIDTH' and 'HEIGTH' keys, their values are the WIDTH and HEIGTH values respectively
#	    You could also make just one dict with the 4 above mentioned keys, and use it as the Coords and Size args.
#########################################################################################################
# RANT:
# 	If after this long but short explanation you can't still understand how to use this, then don't use it, because you're stupid
# 	 and i don't want stupid people using my work.
# RANT END.
#
# sorry, but i will not write a book here to explain everything of this class...
#############################################################################################################
class ButtonCreator:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.ID = Custom.GravityFX.GravityFXlib.GetUniqueID("ButtonCreator")
		self.CLASS = 'Button Creator'
		self.ButtonDict = {}
		self.ButtonIDdict = {}
	
	def CreateTextInput(self, pName, pToMenu, pDefault, fMaxWidth, fLongestLen, pcConfigName, iMaxChars, bBackground = 1, pcIgnoreString = None, Coords = None):
		debug(__name__ + ", CreateTextInput")
		lpTEI = CreateTextEntry(pName, pDefault, fMaxWidth, fLongestLen, pcConfigName, iMaxChars, bBackground, pcIgnoreString)
		pPane = lpTEI[0]
		pTextEntry = lpTEI[1]
		if Coords == None:
			pToMenu.AddChild(pPane)
		else:
			pToMenu.AddChild(pPane, Coords['X'], Coords['Y'])
		self.AddButtonToDict(pName, pTextEntry)
		return lpTEI

	def CreateBar(self, pName, eType, sFunc, fValue, nRange = [0.0, 0.1], nMarker = 0.0, nUseButton = 0, pToMenu = None, Coords = None, Size = None):
		debug(__name__ + ", CreateBar")
		if eType == None:
			eType = GetNextEventType()
		##############
		if pToMenu:
			pToMenu = pToMenu
		else:
			pTopWindow = App.TopWindow_GetTopWindow()
			pToMenu = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

		pBar = App.STNumericBar_Create ()
		pBar.SetRange(nRange[0], nRange[1])
		pBar.SetKeyInterval(0.1)
		pBar.SetMarkerValue(nMarker)
		pBar.SetValue(fValue)
		pBar.SetUseAlternateColor(0)
		pBar.SetUseButtons(nUseButton)
		kNormalColor = App.g_kSTMenu3NormalBase
		kEmptyColor	= App.g_kSTMenu3Disabled
		pBar.SetNormalColor(kNormalColor)
		pBar.SetEmptyColor(kEmptyColor)
		pText = pBar.GetText();
		pText.SetStringW(App.TGString(pName))
		if Size != None:
			pBar.Resize(Size['WIDTH'], Size['HEIGTH'], 0)
		pEvent = App.TGFloatEvent_Create ()
		pEvent.SetDestination(pToMenu)
		pEvent.SetFloat (fValue)
		pEvent.SetEventType(eType)
		pEvent.SetSource(pBar)
		pBar.SetUpdateEvent(pEvent)

		if Coords == None:
			pToMenu.AddChild(pBar)
		else:
			pToMenu.AddChild(pBar, Coords['X'], Coords['Y'])
		if sFunc == None:
			pToMenu.AddPythonFuncHandlerForInstance(eType, __name__+".Nothing")
		else:
			pToMenu.AddPythonFuncHandlerForInstance(eType, sFunc)
		self.AddButtonToDict(pName, pBar)
		return pBar

	def CreateToggleButton(self, pName, kStateNameList, eEventTypeList, sFunc, iEventValueList, iDefault, pToMenu = None, Coords = None, Size = None):
		debug(__name__ + ", CreateToggleButton")
		if eEventTypeList == None:
			eEventTypeList = [GetNextEventType()]
		kStates = []
		for i in range((len(kStateNameList)+len(eEventTypeList)+len(iEventValueList))/3):
			tuple = (kStateNameList[i], eEventTypeList[i], iEventValueList[i])
			kStates.append(tuple)
		pMTButton = CreateMenuToggleButton(pName, kStates, iDefault, pToMenu)
		if pToMenu:
			pToMenu = pToMenu
		else:
			pTopWindow = App.TopWindow_GetTopWindow()
			pToMenu = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
		if Coords == None:
			pToMenu.AddChild(pMTButton)
		else:
			pToMenu.AddChild(pMTButton, Coords['X'], Coords['Y'])
		if Size != None:
			pMTButton.Resize(Size['WIDTH'], Size['HEIGTH'])
		if sFunc == None:
			for ET in eEventTypeList:
				pToMenu.AddPythonFuncHandlerForInstance(ET, __name__+".Nothing")
		else:
			for ET in eEventTypeList:
				pToMenu.AddPythonFuncHandlerForInstance(ET, sFunc)
		self.AddButtonToDict(pName, pMTButton)
		return pMTButton

	def CreateButton(self, pName, eType, sFunc, iState, pToMenu = None, Coords = None, Size = None):
		debug(__name__ + ", CreateButton")
		if eType == None:
			eType = GetNextEventType()
		pMButton = CreateMenuButton(pName, eType, iState, pToMenu, Size)
		if pToMenu:
			pToMenu = pToMenu
		else:
			pTopWindow = App.TopWindow_GetTopWindow()
			pToMenu = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
		if Coords == None:
			pToMenu.AddChild(pMButton)
		else:
			pToMenu.AddChild(pMButton, Coords['X'], Coords['Y'])
		if sFunc == None:
			pToMenu.AddPythonFuncHandlerForInstance(eType, __name__+".Nothing")
		else:
			pToMenu.AddPythonFuncHandlerForInstance(eType, sFunc)
		self.AddButtonToDict(pName, pMButton)
		return pMButton

	def CreateYesNoButton(self, pName, eType, sFunc, iState, pToMenu = None, Coords = None, Size = None):
		debug(__name__ + ", CreateYesNoButton")
		if eType == None:
			eType = GetNextEventType()
		pYNButton = CreateMenuYesNoButton(pName, eType, iState, pToMenu, Size)
		if pToMenu:
			pToMenu = pToMenu
		else:
			pTopWindow = App.TopWindow_GetTopWindow()
			pToMenu = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
		if Coords == None:
			pToMenu.AddChild(pYNButton)
		else:
			pToMenu.AddChild(pYNButton, Coords['X'], Coords['Y'])
		if sFunc == None:
			pToMenu.AddPythonFuncHandlerForInstance(eType, __name__+".Nothing")
		else:
			pToMenu.AddPythonFuncHandlerForInstance(eType, sFunc)
		self.AddButtonToDict(pName, pYNButton)
		return pYNButton

	def CreateStringButton(self, pName, eType, sFunc, sValue, pToMenu = None, Coords = None, Size = None):
		debug(__name__ + ", CreateStringButton")
		if eType == None:
			eType = GetNextEventType()
		pStrButton = CreateMenuButtonString(pName, eType, sValue, pToMenu)
		if pToMenu:
			pToMenu = pToMenu
		else:
			pTopWindow = App.TopWindow_GetTopWindow()
			pToMenu = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
		if Coords == None:
			pToMenu.AddChild(pStrButton)
		else:
			pToMenu.AddChild(pStrButton, Coords['X'], Coords['Y'])
		if Size != None:
			pStrButton.Resize(Size['WIDTH'], Size['HEIGTH'])
		if sFunc == None:
			pToMenu.AddPythonFuncHandlerForInstance(eType, __name__+".Nothing")
		else:
			pToMenu.AddPythonFuncHandlerForInstance(eType, sFunc)
		self.AddButtonToDict(pName, pStrButton)
		return pStrButton

	def GetButtonByName(self, name):
		debug(__name__ + ", GetButtonByName")
		if self.ButtonDict.has_key(name):
			return self.ButtonDict[name]
		else:
			return None

	def GetButtonByID(self, ID):
		debug(__name__ + ", GetButtonByID")
		if self.ButtonIDdict.has_key(ID):
			name = self.ButtonIDdict[ID]
			return self.ButtonDict[name]
		else:
			return None	

	def FindButtonInPane(self, pane, name):
		debug(__name__ + ", FindButtonInPane")
		pButton = GetButton(pane, name)
		pBCbutton = self.GetButtonByID(pButton.GetObjID())
		return pBCbutton

	def AddButtonToDict(self, pName, pButton):
		debug(__name__ + ", AddButtonToDict")
		self.ButtonDict[pName] = pButton
		self.ButtonIDdict[pButton.GetObjID()] = pName

	def DeleteButtonByName(self, name):
		debug(__name__ + ", DeleteButtonByName")
		if self.ButtonDict.has_key(name):
			pButton = self.ButtonDict[name]
			del self.ButtonIDdict[pButton.GetObjID()]
			pParent = pButton.GetParent()
			pParent.DeleteChild(pButton)
			pButton.__del__()
			del self.ButtonDict[name]
			
	def DeleteButtonByID(self, ID):
		debug(__name__ + ", DeleteButtonByID")
		if self.ButtonIDdict.has_key(ID):
			pButton = self.ButtonDict[self.ButtonIDdict[ID]]
			try:
				pName = App.TGString()
				pButton.GetName(pName)
				del self.ButtonDict[pName.GetCString()]
			except:
				del self.ButtonDict[pButton.GetName()]
			pParent = pButton.GetParent()
			pParent.DeleteChild(pButton)
			pButton.__del__()
			del self.ButtonIDdict[ID]
	
	def DeleteAllButtons(self):
		debug(__name__ + ", DeleteAllButtons")
		for key in self.ButtonDict.keys():
			pButton = self.ButtonDict[key]
			pParent = pButton.GetParent()
			pParent.DeleteChild(pButton)
			pButton.__del__()
		self.ButtonDict = {}
		self.ButtonIDdict = {}

	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.ID+">"

####################################################################################################
####################################################################################################
## HELPER Functions
#################
#  GetNextEventType -->  returns a event type
#####
#  GetWindow(sName, ObjType) --> returns a window with sName in TacticalControlWindow
#      ^> ObjType is the type of window you're searching, it can be:
#		 ^>- "Stylized Window"    (default value)
#            ^>- "Menu"
#		 ^>- "Character Menu"
#####
#  Nothing(pObject, pEvent)  --> this makes nothing, returns nothing (that for python, probably is None)
#	 ^> use this for event handlers that are supossed to do nothing, or for anything that you want to do nothing... 
# 	 ^> oh and, pObject and pEvent defaults to None...
####################################################################################################
def CreateCharMenu(sName, pParent):
	debug(__name__ + ", CreateCharMenu")
	pMenu = App.STCharacterMenu_Create(sName)
	pParent.AddChild(pMenu)
	return pMenu

def GetNextEventType():
	debug(__name__ + ", GetNextEventType")
	return App.Mission_GetNextEventType()

def GetWindow(sName, ObjType = "Stylized Window"):
	debug(__name__ + ", GetWindow")
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	TCWChild = pTacticalControlWindow.GetFirstChild()
	while TCWChild:
		if ObjType == "Stylized Window":
			TCWWindow = App.STStylizedWindow_Cast(TCWChild)
		elif ObjType == "Menu" or ObjType == "Character Menu":
			TCWWindow = App.STMenu_Cast(TCWChild)
		if TCWWindow:
			sString = TCWWindow.GetName()
			if (sString.GetCString() == sName):
				return TCWWindow
		TCWChild = pTacticalControlWindow.GetNextChild(TCWChild)

def Nothing(pObject = None, pEvent = None):
	debug(__name__ + ", Nothing")
	return

###############################################################################################################
###############################################################################################################
########   These functions camed from mainmenu.py :
#################################
###### I taked them out of mainmenu because it's easier to use them from here, plus I changed a few things in
###### them to make'em able to be used somewhere else, besides the MainMenu, and to make them work like i wanted  =P
######
###### But these functions don't add the button to a pane/menu/window, nor it creates the PythonFuncHandler for the event
###### So to create the button entirely, use the above class, ButtonCreator
###############################################################################################################
###############################################################################################################
###############################################################################
#	CreateTextEntry(pName, pDefault, fMaxWidth
#
#	Creates a text entry thingie
#
#	Args:	pName - the name of the title tag
#			pDefault - the default string of the text entry
#			fMaxWidth - the max width of this thingie
#			fLongestLen - spacing for the name versus the text entry box
#	Return:	the newly-created thingie
###############################################################################
def CreateTextEntry(pName, pDefault, fMaxWidth, fLongestLen, pcConfigName, iMaxChars, bBackground = 1, pcIgnoreString = None):
	# First create a pane for this.
	debug(__name__ + ", CreateTextEntry")
	pPane = App.TGPane_Create (fMaxWidth, 1.0)

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	# Create the text tag
	if (pName == None):
		pText = App.TGPane_Create ()
		fWidth = pText.GetWidth ()
		pPane.AddChild (pText, fLongestLen - fWidth, 0)

		# Add some space between text tag and text entry box
		fLongestLen = 0

		# Get width for spacing the text entry box.
		fWidth = fLongestLen

		# Create the name entry button
		# Get LCARS string
		pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pGraphicsMode.GetLcarsString()

		if (pDefault == None):
			pTextEntry = App.TGParagraph_Create ("Default")
		else:
			pTextEntry = App.TGParagraph_CreateW (pDefault)
		pTextEntry.SetMaxChars (iMaxChars)
		pTextEntry.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
		pTextEntry.SetReadOnly (0)
		if (pcIgnoreString == None):
			pTextEntry.SetIgnoreString ("\n\r")
		else:
			pTextEntry.SetIgnoreString(pcIgnoreString + "\n\r");
#		pTextEntry.SetColor (App.g_kSTMenuTextColor)

		pPane.AddChild (pTextEntry, fWidth + 0.005, (LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT - pTextEntry.GetHeight ()) / 2.0)

		# Create a background for the text entry button
		if (bBackground):
			pBackground = App.TGIcon_Create(pcLCARS, 200, App.g_kTextEntryColor)
			pBackground.Resize (fMaxWidth - fWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT, 0)
			pPane.AddChild (pBackground, fWidth, 0)

		# Now resize the pane to be the height of text entry
		pPane.Resize (fMaxWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT, 0)

		if (pDefault == None):
			# Okay, now I have to blank out the string
			pTextEntry.SetString ("", 0)

	else:
		pText = App.TGParagraph_CreateW (App.TGString(pName))
		fWidth = pText.GetWidth ()
		pPane.AddChild (pText, fLongestLen - fWidth, 0)

		# Add some space between text tag and text entry box
		fLongestLen = fLongestLen + MainMenu.mainmenu.g_fHorizontalSpacing

		# Get width for spacing the text entry box.
		fWidth = fLongestLen

		# Create the name entry button
		# Get LCARS string
		pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pGraphicsMode.GetLcarsString()

		if (pDefault == None):
			pTextEntry = App.TGParagraph_Create ("Default")
		else:
			pTextEntry = App.TGParagraph_CreateW (pDefault)
		pTextEntry.SetMaxChars (iMaxChars)
		pTextEntry.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
		pTextEntry.SetReadOnly (0)
		pTextEntry.SetIgnoreString ("\n\r")
		pPane.AddChild (pTextEntry, fWidth + 0.005, 0)
#		pTextEntry.SetColor (App.g_kSTMenuTextColor)

		# Create a background for the text entry button
		if (bBackground):
			pBackground = App.TGIcon_Create(pcLCARS, 200, App.g_kTextEntryColor)
			pBackground.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
			pPane.AddChild (pBackground, fWidth, 0)

		# Now resize the pane to be the height of text entry
		pPane.Resize (fMaxWidth, pTextEntry.GetHeight (), 0)

		if (pDefault == None):
			# Okay, now I have to blank out the string
			pTextEntry.SetString ("", 0)

	# Add a hidden child that stores the name to use in the configuration file.
	pPara = App.TGParagraph_Create (pcConfigName)
	pPane.AddChild (pPara, 0, 0)
	pPara.SetNotVisible ()

	pPane.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".TextEntryMouseHandler")

	return [pPane, pTextEntry, pBackground ]

###############################################################################
#	HandleMouse()
#
#	Handles mouse events. This is registered as an event handler for
#	TacticalWindow.
#
#	Args:	TacticalWindow	pTactical	- the TacticalWindow object
#			TGMouseEvent	pEvent		- mouse event
#
#	Return:	none
###############################################################################
def TextEntryMouseHandler (pSelf, pEvent):
	debug(__name__ + ", TextEntryMouseHandler")
	"Handle mouse events for the command interface"

	if (pEvent.EventHandled () == 0):
		if (pEvent.GetButtonNum() & App.TGMouseEvent.MEF_BUTTON_LEFT):
			if (pEvent.GetFlags() & App.TGMouseEvent.MEF_BUTTON_DOWN):
				# Give focus to the pane.

				pPara = App.TGParagraph_Cast (pSelf.GetNthChild (1))
				pPara.Resize (pSelf.GetWidth (), pSelf.GetHeight ())

	# Pass event to next handler.
	pSelf.CallNextHandler(pEvent)

###############################################################################
#	CreateVolumeButton(pName, eType, fValue, fWidth)
#
#	Creates a volume button for the options menu.
#
#	Args:	pName - name of the button
#			eType - event type to send when the button is activated
#		??    fValue - Default bar value
#		??    fWidth - 
#
#	Return:	the newly-created button
###############################################################################
def CreateVolumeButton (pName, eType, fValue, fWidth, nRange = [0.0, 0.1], nMarker = 0.0, pToMenu = None):
	debug(__name__ + ", CreateVolumeButton")
	if pToMenu:
		pOptionsWindow = pToMenu
	else:
		pTopWindow = App.TopWindow_GetTopWindow()
		pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pBar = App.STNumericBar_Create ()

	pBar.SetRange(nRange[0], nRange[1])
	pBar.SetKeyInterval(0.1)
	pBar.SetMarkerValue(nMarker)
	pBar.SetValue(fValue)
	pBar.SetUseMarker(0)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	kNormalColor = App.g_kSTMenu3NormalBase
	kEmptyColor	= App.g_kSTMenu3Disabled

	pBar.SetNormalColor(kNormalColor)
	pBar.SetEmptyColor(kEmptyColor)
	pText = pBar.GetText();
	pText.SetStringW(App.TGString(pName))

	pBar.Resize (fWidth, MainMenu.mainmenu.g_fButtonHeight, 0)

	pEvent = App.TGFloatEvent_Create ()
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetFloat (fValue)
	pEvent.SetEventType(eType)
	pEvent.SetSource(pBar)

	pBar.SetUpdateEvent(pEvent)

	return pBar


###############################################################################
#	CreateMenuToggleButton(pName, kStates, iDefault)
#
#	Creates a toggle button for the options menu.
#
#	Args:	pName - name of the button
#			kStates - set of tuples containing name, event type, and event
#				value (for an int event)
#			iDefault - default button state
#
#	Return:	the newly-created button
###############################################################################
def CreateMenuToggleButton(pName, kStates, iDefault, pToMenu = None):
	debug(__name__ + ", CreateMenuToggleButton")
	if pToMenu:
		pOptionsWindow = pToMenu
	else:
		pTopWindow = App.TopWindow_GetTopWindow()
		pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	kArgs = [App.TGString(pName), iDefault]

	for kStateName, eEventType, iEventValue in kStates:
		pEvent = App.TGIntEvent_Create()
		pEvent.SetEventType(eEventType)
		pEvent.SetDestination(pOptionsWindow)
		pEvent.SetInt(iEventValue)

		kArgs.append(App.TGString(kStateName))
		kArgs.append(pEvent)

	kMenuButton = apply(App.STToggle_CreateW, kArgs)

	return kMenuButton

###############################################################################
#	CreateMenuButton(pName, eType, iState)
#
#	Creates a regular Star Trek button for the menu.
#
#	Args:	pName - the name of the button
#			eType - event type to send when the button is activated
#			iState - the state of the button?
#
#	Return:	the newly-created button
###############################################################################
def CreateMenuButton(pName, eType, iState, pToMenu = None, Size = None):
	debug(__name__ + ", CreateMenuButton")
	if pToMenu:
		pOptionsWindow = pToMenu
	else:
		pTopWindow = App.TopWindow_GetTopWindow()
		pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetInt(iState)
	if Size == None:
		MenuButton = App.STButton_CreateW(App.TGString(pName), pEvent)
	else:
		MenuButton = App.STRoundedButton_CreateW(App.TGString(pName), pEvent, Size['WIDTH'], Size['HEIGTH'])

	return MenuButton

###############################################################################
#	CreateMenuYesNoButton(pName, eType, iState)
#
#	Creates a regular Star Trek button for the menu.
#
#	Args:	pName - the name of the button
#			eType - event type to send when the button is activated
#			iState - the state of the button?
#
#	Return:	the newly-created button
###############################################################################
def CreateMenuYesNoButton(pName, eType, iState, pToMenu = None, Size = None):
	debug(__name__ + ", CreateMenuYesNoButton")
	if pToMenu:
		pOptionsWindow = pToMenu
	else:
		pTopWindow = App.TopWindow_GetTopWindow()
		pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetInt(iState)

	if Size == None:
		pMenuButton = App.STButton_CreateW(App.TGString(pName), pEvent)
	else:
		pMenuButton = App.STButton_CreateW(App.TGString(pName), pEvent, 0, Size['WIDTH'], Size['HEIGTH'])

	pEvent.SetSource (pMenuButton)

	pMenuButton.SetChoosable (1)
	pMenuButton.SetAutoChoose (1)
	if iState != 0:
		pMenuButton.SetChosen (1)
	else:
		pMenuButton.SetChosen (0)

	return pMenuButton

###############################################################################
#	CreateMenuButtonString(pName, eType, iState)
#
#	Creates a regular Star Trek button for the menu.  Have
#	it send a string event.
#
#	Args:	pName - the name of the button
#			eType - event type to send when the button is activated
#			sValue - The string value to give the event.
#
#	Return:	the newly-created button
###############################################################################
def CreateMenuButtonString(pName, eType, sValue, pToMenu = None):
	debug(__name__ + ", CreateMenuButtonString")
	if pToMenu:
		pOptionsWindow = pToMenu
	else:
		pTopWindow = App.TopWindow_GetTopWindow()
		pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetString(sValue)

	pMenuButton = App.STButton_CreateW(pName)

	pEvent.SetSource(pMenuButton)
	pMenuButton.SetActivationEvent(pEvent)

	return pMenuButton

###############################################################################
#	GetButton(pPane, pTargetName)
#
#	return a button object in the given pane with the given name.
#
#	Args:	??	pPane - the Pane object to look into
#		??	pTargetName - the name of the button to search for
#
#	Return:	the button if it was found, return None if didn't
###############################################################################
def GetButton(pPane, strName):
	debug(__name__ + ", GetButton")
	pTargetName = App.TGString(strName)
	pcTargetName = pTargetName.GetCString ()
	iLen = len (pcTargetName)

	for i in range (0, pPane.GetNumChildren ()):
		pButton = App.STButton_Cast (pPane.GetNthChild (i))
		if (pButton):
			pName = App.TGString ()
			pButton.GetName (pName)
			pcName = pName.GetCString ()
			if (pcName [:iLen] == pcTargetName):
				return pButton

	return None
