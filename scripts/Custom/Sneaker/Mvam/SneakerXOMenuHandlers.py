import App
import nt
import string
import Bridge.BridgeUtils

def SneakerCreateMenu(strPlayerScript):
	#grab the database of strings
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")

	#grab the player menu
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pXOMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Commander"))

	#grab the MVAM submenu
	pMvamMenuName = pDatabase.GetString("Red Alert")
	pMvamMenuName.SetString("MVAM Menu")
	pMvamMenu = pXOMenu.GetSubmenuW(pMvamMenuName)
	if not pMvamMenu:
		return
	pMvamMenu.SetDisabled()
	pMvamMenu.KillChildren()
	pMvamMenuName.SetString("Red Alert")

	#go through every new Mvam item in the Custom/Autoload/Mvam folder. Create new icons in the mvam menu
	straMvamList = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

	#okay, we need a mock go through.. just so it'll spawn a pyc
	snkMockModule = []
	for t in range(len(straMvamList)):
		#mock mock mock mock
		straTempName = string.split(straMvamList[t], ".")
		snkMockModule.append(__import__ ("Custom.Autoload.Mvam." + straTempName[0]))

	#save some memory
	del snkMockModule

	#reload the list after the mock. Create new icons in the mvam menu
	straMvamList = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

	#trigger and a counter
	ET_MVAM_TRIGGER = []
	intMvamTriggerCounter = 0

	#time to go through every mvam item. set up an int so i can modify it
	intListNum = len(straMvamList)

	#now that all pyc's are in place, lets do the real deal
	for i in range(intListNum):
		#okayyyy, make sure it's a pyc file, and make sure its not the init
		straTempName = string.split(straMvamList[i], ".")
		if ((straMvamList[i] == "__init__.pyc") or (straTempName[-1] == "py")):
			#bad file alert. redo the for loop and lower the counter
			i = i - 1
			intListNum = intListNum - 1

		# we succeeded! good file, so lets go
		else:
			straTempName = string.split(straMvamList[i], ".pyc")
			snkMvamModule = __import__ ("Custom.Autoload.Mvam." + straTempName[0])

			for a in range (len(snkMvamModule.ReturnMvamShips())):
				if (("ships." + snkMvamModule.ReturnMvamShips()[a]) == strPlayerScript):
					#reenable the mvam menu
					pMvamMenu.SetEnabled()

#TEMP!!!!!!				#setup the player listener for damage. call it so that it's created
					#pPlayer = App.Game_GetCurrentGame().GetPlayer()
					#pPlayer.AddPythonFuncHandlerForInstance(App.ET_WEAPON_HIT, "Custom.Sneaker.Mvam.DamageTransfer.DamageTransfer")

					#lets do the buttons. remember to reset the string
					straMvamChildNames = snkMvamModule.ReturnIconNames()
					for j in range (len(straMvamChildNames)):
						#set up the trigger...
						ET_MVAM_TRIGGER.append(App.Game_GetNextEventType())

						#okay, we need to grab the name and split it, to make sure it isnt for reintegration
						straButtonName = string.split(straMvamChildNames[j], "$")

						#do the buttons as normal
						pMvamButtonName = pDatabase.GetString("Red Alert")
						pMvamButtonName.SetString(straButtonName[0])
						pMvamButton = Bridge.BridgeUtils.CreateBridgeMenuButton(pMvamButtonName, ET_MVAM_TRIGGER[intMvamTriggerCounter], 1, pXOMenu)
						pMvamMenu.AddChild(pMvamButton)
						pMvamButtonName.SetString("Red Alert")
						if (straButtonName[-1] != "Rein"):
							pXOMenu.AddPythonFuncHandlerForInstance(ET_MVAM_TRIGGER[intMvamTriggerCounter], "Custom.Autoload.Mvam." + straTempName[0] + "." + snkMvamModule.ReturnMvamShips()[j + 1])
						else:
							pXOMenu.AddPythonFuncHandlerForInstance(ET_MVAM_TRIGGER[intMvamTriggerCounter], "Custom.Autoload.Mvam." + straTempName[0] + ".Reintegrate")

						intMvamTriggerCounter = intMvamTriggerCounter + 1

					#unload and exit. we dont need to do anymore
					App.g_kLocalizationManager.Unload(pDatabase)
					return

	App.g_kLocalizationManager.Unload(pDatabase)
	return