from bcdebug import debug
import App
import Foundation
import MissionLib
import nt
import string
import sys
import Custom.QBautostart.Libs.LibEngineering

MODINFO = { "Author": "\"Defiant\" erik@vontaene.de",
            "Download": "http://defiant.homedns.org/~erik/STBC/Engineering/",
            "Version": "1.0",
            "License": "GPL",
            "Description": "This is to load the files in scripts/Custom/QBautostart/"
            }

mode = Foundation.MutatorDef("QBautostart Extension V1.0")
ASK_FOR_VALID_QBAUTOSTART_SCRIPTS = 189
UseTryCatch = 1

class EngineeringExtension:
        def __init__(self):
                debug(__name__ + ", __init__")
                self.EngineeringInit = 0
                self.PlayerShip = None
                self.ShowWarningWindow = 1
                self.__MultAllowedScriptsMd5s = []

	def SetEngineeringInit(self, Value):
		debug(__name__ + ", SetEngineeringInit")
		self.EngineeringInit = Value
	
	def SetPlayerShip(self, Value):
		debug(__name__ + ", SetPlayerShip")
		self.PlayerShip = Value

        def SendMultiPlayerMessage(self, myMessage):
                debug(__name__ + ", SendMultiPlayerMessage")
                global ASK_FOR_VALID_QBAUTOSTART_SCRIPTS
                # Setup the stream.
                # Allocate a local buffer stream.
                kStream = App.TGBufferStream()
                # Open the buffer stream with a 256 byte buffer.
                kStream.OpenBuffer(256)
                # Write relevant data to the stream.
                # First write message type.
                kStream.WriteChar(chr(ASK_FOR_VALID_QBAUTOSTART_SCRIPTS))
                # send Message
                iCount = 0
                for ichar in range(len(myMessage)):
                        kStream.WriteChar(myMessage[iCount])
                        iCount = iCount + 1
                # set the last char:
                kStream.WriteChar('\0')
                pMessage = App.TGMessage_Create()
                # Yes, this is a guaranteed packet
                pMessage.SetGuaranteed(1)
                # Okay, now set the data from the buffer stream to the message
                pMessage.SetDataFromStream(kStream)
                # Send the message to everybody but me.  Use the NoMe group, which
                # is set up by the multiplayer game.
                # TODO: Send it to asking client only
                pNetwork = App.g_kUtopiaModule.GetNetwork()
                if not App.IsNull(pNetwork):
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                        else:
                                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
                # We're done.  Close the buffer.
                kStream.CloseBuffer()

        def DemandValidScripts(self):
                debug(__name__ + ", DemandValidScripts")
                self.SendMultiPlayerMessage("ASK")

        def ProcessMessageHandler(self, pObject, pEvent):
                debug(__name__ + ", ProcessMessageHandler")
                global ASK_FOR_VALID_QBAUTOSTART_SCRIPTS
                
                pMessage = pEvent.GetMessage()
                if App.IsNull(pMessage):
                        return
                # Get the data from the message
                # Open a buffer stream to read the data
                kStream = pMessage.GetBufferStream();
                cType = kStream.ReadChar();
                cType = ord(cType)
                if (cType == ASK_FOR_VALID_QBAUTOSTART_SCRIPTS):
                        iName = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                iName = iName + iChar
                        if App.g_kUtopiaModule.IsHost() and iName == "ASK":
                                self.SendMultiPlayerMessage("LISTBEGIN")
                                for md5sum in self.__MultAllowedScriptsMd5s:
                                        self.SendMultiPlayerMessage(md5sum)
                                self.SendMultiPlayerMessage("LISTEND")
                        elif App.g_kUtopiaModule.IsClient() and iName == "LISTBEGIN":
                                # nothing here todo?
                                pass
                        elif App.g_kUtopiaModule.IsClient() and iName == "LISTEND":
                                self.ImportQBautostart(0)
                                self.EngineeringInit = 1
                        elif App.g_kUtopiaModule.IsClient():
                                self.__MultAllowedScriptsMd5s.append(iName)

		kStream.Close()

        def MultImportQBautostart(self, QBrestart=0):
                debug(__name__ + ", MultImportQBautostart")
                if App.g_kUtopiaModule.IsHost():
                        self.ImportQBautostart(QBrestart)
                        self.EngineeringInit = 1
                elif App.g_kUtopiaModule.IsClient():
                        # ok lets ask the server which md5s are valid
                        #self.DemandValidScripts()
                        # not used, just load them for now:
                        self.ImportQBautostart(QBrestart)
                pMission = MissionLib.GetMission()
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, pMission, __name__ + ".ProcessMessageHandler")

        def __IsKnownScript(self, md5sum):
                debug(__name__ + ", __IsKnownScript")
                i = self.__MultAllowedScriptsMd5s.count(md5sum)
                if i == 0:
                        return 0
                return 1

	def ImportQBautostart(self, QBrestart=0):
                debug(__name__ + ", ImportQBautostart")
                global UseTryCatch
		dir = "scripts\\Custom\\QBautostart"
		
		if (self.EngineeringInit == 1 and QBrestart == 0):
			return
		
		pluginsLoaded = {}
		list = nt.listdir(dir)
		list.sort()

		dotPrefix = string.join(string.split(dir, '\\')[1:], '.') + '.'

		#print("Loading QBautostart")
        
		for plugin in list:
                        needBridge = 1
			s = string.split(plugin, '.')
			if len(s) <= 1:
				continue
			# Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
			extension = s[-1]
			fileName = string.join(s[:-1], '.')

                        if (fileName == "__init__"):
                                continue

                        # We don't want to accidentally load the wrong ship.
                        if (extension == 'py' and not pluginsLoaded.has_key(fileName)):
                                pluginsLoaded[fileName] = 1 # save, so we don't load twice.
                                if UseTryCatch == 0:
                                        pModule = __import__(dotPrefix + fileName)
                                else:
                                        try:
                                                pModule = __import__(dotPrefix + fileName)
                                        except:
                                                errtype, errinfo, errtrace = sys.exc_info()
                                                print("Error: was unable to load %s - %s: %s") % (fileName, errtype, errinfo)
                                                import traceback
                                                fulltrace = traceback.print_exc(errtrace)
                                                if fulltrace:
                                                        print("Traceback: %s") % (fulltrace)
                                                continue
                                ModVersion = ""
                                ModAuthor = "."
                                ModHP = ""
                                # TODO: Refuse to load files that are causing this trouble.
                                # We will do this later, when most people got the chance to upgrade to this Version
                                if hasattr(pModule, "MODINFO"):
                                        MODINFO = pModule.MODINFO
                                        if MODINFO.has_key("Author"):
                                                ModAuthor = ": " + str(MODINFO["Author"])
                                        if MODINFO.has_key("Version"):
                                                ModVersion = " - Version" + str(MODINFO["Version"]) + " -"
                                        if MODINFO.has_key("Download"):
                                                ModHP = " from " + str(MODINFO["Download"])
                                        if MODINFO.has_key("needBridge"):
                                                needBridge = MODINFO["needBridge"]
                                if needBridge == 1 and not App.g_kSetManager.GetSet("bridge"):
                                        #print("no Bridge, so we don't load %s") % (fileName)
                                        continue
        			if (QBrestart == 0) and not hasattr(pModule, "init"):
				        if (self.ShowWarningWindow == 1):
        					Custom.QBautostart.Libs.LibEngineering.CreateInfoBox("file scripts/Custom/QBautostart/" + str(fileName) + "." + str(extension) + ModVersion + " has no init attribute.\nPlease update this Mod" + ModHP + " or contact the Author" + ModAuthor + "\nElse you should delete or disable this file.")
				        else:
        					print("file scripts/Custom/QBautostart/" + str(fileName) + "." + str(extension) + ModVersion + " has no init attribute.\nPlease update this Mod" + ModHP + " or contact the Author" + ModAuthor + "\nElse you should delete or disable this file.")
			        if (QBrestart == 1):
        				if hasattr(pModule , "Restart"):
					        pModule.Restart() # just restart
			        elif (QBrestart == 2):
        				if hasattr(pModule , "NewPlayerShip"):
					        pModule.NewPlayerShip() # New Player Ship
			        elif (QBrestart == 3):
        				if hasattr(pModule , "exit"):
						# seems to be a bad idea in SP - exit is called on save/load
						pGame = App.Game_GetCurrentGame()
						if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
							return
					        pModule.exit() # if something to kill
			        elif (hasattr(pModule , "init")):
                                        if App.g_kUtopiaModule.IsHost() or App.g_kUtopiaModule.IsClient():
                                                # save all valid md5sums in a list
                                                md5sum = Custom.QBautostart.Libs.LibEngineering.GetMd5(dir + "\\" + fileName + "." + extension)
                                        if App.g_kUtopiaModule.IsHost():
                                                self.__MultAllowedScriptsMd5s.append(md5sum)
                                        #elif App.g_kUtopiaModule.IsClient() and not self.__IsKnownScript(md5sum):
                                        #        del pluginsLoaded[fileName]
                                        #        continue
                                        if App.g_kUtopiaModule.IsHost() and not App.g_kUtopiaModule.IsClient():
                                                continue
                                        pModule.init() # init the file


LoadQBautostart = EngineeringExtension()

def ProcessMessageHandler(pObject, pEvent):
        debug(__name__ + ", ProcessMessageHandler")
        LoadQBautostart.ProcessMessageHandler(pObject, pEvent)

class EngineeringExtensionTrigger_init(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		self.name = name
		self.eventKey = eventKey
		self.dict = dict
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)
                LoadQBautostart.SetEngineeringInit(0)

        def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
                if App.g_kUtopiaModule.IsMultiplayer():
                        return
                LoadQBautostart.ImportQBautostart()
                if not LoadQBautostart.PlayerShip:
                        LoadQBautostart.SetPlayerShip(str(MissionLib.GetShip("Player")))
                LoadQBautostart.SetEngineeringInit(1)
        def Deactivate(self):
                debug(__name__ + ", Deactivate")
                LoadQBautostart.ImportQBautostart(3) # Exit
                LoadQBautostart.SetEngineeringInit(0)
		#Foundation.TriggerDef.__init__(self, self.name, self.eventKey, self.dict) # I don't know why, but we have to reactivate here


class EngineeringExtensionTrigger_Restart(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                debug(__name__ + ", __init__")
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
                if LoadQBautostart.EngineeringInit:
                        if (MissionLib.GetPlayer().GetName() == "Player") and (str(MissionLib.GetPlayer()) != LoadQBautostart.PlayerShip):
                                LoadQBautostart.ImportQBautostart(1) # Restart
                                LoadQBautostart.SetPlayerShip(str(MissionLib.GetShip("Player")))
                        else:
                                LoadQBautostart.ImportQBautostart(2) # New ship

EngineeringExtensionTrigger_init('Engineering Extension Trigger init', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )
EngineeringExtensionTrigger_Restart('Engineering Extension Trigger Restart', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )
