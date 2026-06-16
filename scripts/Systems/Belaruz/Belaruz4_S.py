import App
import loadspacehelper







# Tethys code, modified by CharaToLoki
# TO-DO move this to another file
###############################################################################
##	Filename:	AtmoshpereALT.py
##	
##	Creates an Atmosphere around a planet, using nif files instead
##	Creates a random rotation for the planet and atmosphere
##	
##	Created:	05/17/2003 - NanoByte a.k.a Michael T. Braams
##	Modified:	06/04/2026 - Tethys
###############################################################################
from bcdebug import debug
import traceback

import App
#import Foundation
import MissionLib
#import Custom.NanoFXv2.NanoFX_Config
#import Custom.NanoFXv2.NanoFX_ScriptActions


class TethysRotationChecks:
	def __init__(self, name):
		self.name = name
		self.g_lRotatingBodies = {}
		self.g_bRotationTimerRunning = None
		self.g_Belaruz4SRotTimer = None

	def AddRotatingBody(self, pObject, fSpeed):
		if (pObject and hasattr(pObject, "GetObjID")):
			pObjectID = pObject.GetObjID()
			if pObjectID != None and pObjectID != App.NULL_ID:	
				self.AddRotatingBodyForID(pObjectID, fSpeed)

	def AddRotatingBodyForID(self, pObjectID, fSpeed):
		self.g_lRotatingBodies[pObjectID] = [pObjectID, 0.0, fSpeed]

		self.StartRotationTimer()

	def RemoveRotatingBody(self, pObject):
		if (pObject and hasattr(pObject, "GetObjID")):
			pObjectID = pObject.GetObjID()
			if pObjectID != None and pObjectID != App.NULL_ID:	
				self.RemoveRotatingBodyForID(pObjectID)

	def RemoveRotatingBodyForID(self, pObjectID):
		if self.g_lRotatingBodies.has_key(pObjectID):
			del self.g_lRotatingBodies[pObjectID]

	def StartRotationTimer(self):
		if self.g_bRotationTimerRunning != None:
			return

		self.g_bRotationTimerRunning = App.Game_GetNextEventType()
		self.CreateCleanRotationTimer(self.g_bRotationTimerRunning, future=0.1)

	def CreateCleanRotationTimer(self, evtType, future=0.1):
		if self.g_Belaruz4SRotTimer != None and hasattr(self.g_Belaruz4SRotTimer, "GetObjID"):
			timerID = self.g_Belaruz4SRotTimer.GetObjID()
			if timerID != None:
				App.g_kTimerManager.DeleteTimer(timerID)
			self.g_Belaruz4SRotTimer = None

		# Setup the handler function.
		pGame = App.Game_GetCurrentGame()
		if (pGame == None):
			return None
		pEpisode = pGame.GetCurrentEpisode()
		if (pEpisode == None):
			return None
		pMission = pEpisode.GetCurrentMission()
		if (pMission == None):
			return None

		pMission.RemoveHandlerForInstance(evtType, __name__ + ".RotateTimer")
		self.CreateRotationTimer(evtType, future)

	def CreateRotationTimer(self, evtType, future=0.1):

		myTimer = MissionLib.CreateTimer(evtType, __name__ + ".RotateTimer", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)

		self.g_Belaruz4SRotTimer = myTimer

	def RotateTimer(self, pObject, pEvent):
		rotatingBodyKeys = self.g_lRotatingBodies.keys()

		for keys in rotatingBodyKeys:
			lBody = self.g_lRotatingBodies[keys]
			iID = lBody[0]
			fRot = lBody[1]
			fSpeed = lBody[2]
			failure = 0
			pBody = App.ObjectClass_GetObjectByID(None, iID)

			if pBody:
				try:
					fRot = fRot + fSpeed

					pBody.SetAngleAxisRotation(fRot, 0, 0, 1)
					pBody.UpdateNodeOnly()

					lBody[1] = fRot
				except:
					failure = 1
					print __name__ + ".RotateTimer ERROR: "
					traceback.print_exc()
			else:
				failure = 1

			if failure:
				self.RemoveRotatingBodyForID(iID)

		if self.g_bRotationTimerRunning != None:
			self.CreateCleanRotationTimer(self.g_bRotationTimerRunning, future=0.01)

		if pObject:
			pObject.CallNextHandler(pEvent)
		return 0

tethysTimer = TethysRotationChecks("System Rotation Check")

def RotateTimer(pObject, pEvent, timerS=tethysTimer):
	return timerS.RotateTimer(pObject, pEvent)


###############################################################################
## AtmosphereFX 
###############################################################################
def CreateAtmosphereALT(pPlanet, sNifPath, sTexturePath, sCloudPath, timerS=tethysTimer):
	
	### Setup for Effect
	debug(__name__ + ", CreateAtmosphereALT")
	pSet          = pPlanet.GetContainingSet()
	fSize         = pPlanet.GetRadius()
	sName         = pPlanet.GetName()
	###
	# pPlanet.SetAtmosphereRadius ((fSize * 1.15) - fSize)
	pPlanet.UpdateNodeOnly()
	timerS.AddRotatingBody(pPlanet, (App.g_kSystemWrapper.GetRandomNumber(5) + 3) / 10000.0)
	###
	# lennie notes:  these layers are render-order specific!

	#0.15 1.15 1.15
	pAtmosphere1 = App.Sun_Create(fSize * 0.1, fSize * 1.11, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/" + sTexturePath + "/GlowColor.tga", None)
	pSet.AddObjectToSet(pAtmosphere1, sName + " Air")
	pAtmosphere1.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere1)
	timerS.AddRotatingBody(pAtmosphere1, 0.025)

	pAtmosphere3 = App.Sun_Create(fSize * 0.1, fSize * 1.11, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/" + sTexturePath + "/Clouds.tga", None)
	pSet.AddObjectToSet(pAtmosphere3, sName + " Air")
	pAtmosphere3.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere3)
	timerS.AddRotatingBody(pAtmosphere3, 0.0125)

	### Create Sphere Model Around Planet for Clouds ###
	pAtmosphere = App.Planet_Create(fSize * 1.1, sNifPath)
	pSet.AddObjectToSet(pAtmosphere, sNifPath + " Planet")
	pAtmosphere.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere)
	timerS.AddRotatingBody(pAtmosphere, (App.g_kSystemWrapper.GetRandomNumber(5) + 3) / 10000.0) # Can also be used (pAtmosphere, 0.0004) for all planets same rotation

	pAtmosphere2 = App.Planet_Create(fSize * 1.12, sCloudPath)
	pSet.AddObjectToSet(pAtmosphere2, sNifPath + " Clouds for Planet") # Actually it's Clouds
	pAtmosphere2.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere2)
	timerS.AddRotatingBody(pAtmosphere2, (App.g_kSystemWrapper.GetRandomNumber(5) + 5) / 10000.0) # Can also be used (pAtmosphere, 0.0004) for all planets same rotation
	"""
	# 0.1 1.11 0.0
	pAtmosphere2 = App.Planet_Create(fSize * 1.12, sCloudPath)
	pSet.AddObjectToSet(pAtmosphere2, sName + " Clouds")
	pAtmosphere2.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere2)
	timerS.AddRotatingBody(pAtmosphere2, (App.g_kSystemWrapper.GetRandomNumber(10) + 5) / 10000.0) # Can also be used (pAtmosphere, 0.0010) for all clouds same rotation
	"""

"""
# TO-DO THOSE ARE A TON OF OVERRIDES
def OverrideStockPlanets(mode):
	
	debug(__name__ + ", OverrideStockPlanets")
	Foundation.OverrideDef('Initialize', 'Systems.Albirea.Albirea1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Albirea.Albirea1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Albirea.Albirea2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Albirea.Albirea2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Albirea.Albirea3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Albirea.Albirea3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth5_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth6_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth6_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth7_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth7_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth8_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Alioth.Alioth8_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Artrus.Artrus1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Artrus.Artrus1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Artrus.Artrus2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Artrus.Artrus2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Artrus.Artrus3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Artrus.Artrus3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ascella.Ascella1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ascella.Ascella2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ascella.Ascella3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ascella.Ascella4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ascella.Ascella5_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Belaruz.Belaruz2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Belaruz.Belaruz2_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Belaruz.Belaruz3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Belaruz.Belaruz3_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Belaruz.Belaruz4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Belaruz.Belaruz4_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Beol.Beol1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Beol.Beol2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Beol.Beol3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Beol.Beol4_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Biranu.Biranu1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Biranu.Biranu1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Biranu.Biranu2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Biranu.Biranu2_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Cebalrai.Cebalrai1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Cebalrai.Cebalrai1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Cebalrai.Cebalrai2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Cebalrai.Cebalrai2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Cebalrai.Cebalrai3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Cebalrai.Cebalrai3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Chambana.Chambana1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Chambana.Chambana1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Chambana.Chambana2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Chambana.Chambana2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Geble.Geble1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Geble.Geble2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Geble.Geble3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Geble.Geble4_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari5_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari6_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari6_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari7_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari7_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari8_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Itari.Itari8_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Nepenthe.Nepenthe1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Nepenthe.Nepenthe1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Nepenthe.Nepenthe2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Nepenthe.Nepenthe2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Nepenthe.Nepenthe3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Nepenthe.Nepenthe3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.OmegaDraconis.OmegaDraconis1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.OmegaDraconis.OmegaDraconis2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.OmegaDraconis.OmegaDraconis3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.OmegaDraconis.OmegaDraconis4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.OmegaDraconis.OmegaDraconis5_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Ona.Ona1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ona.Ona1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ona.Ona2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ona.Ona2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Ona.Ona3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Ona.Ona3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Poseidon.Poseidon1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Poseidon.Poseidon1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Poseidon.Poseidon2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Poseidon.Poseidon2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Prendel.Prendel1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Prendel.Prendel2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Prendel.Prendel3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Prendel.Prendel4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Prendel.Prendel5_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Riha.Riha1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Riha.Riha1_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Savoy.Savoy1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Savoy.Savoy1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Savoy.Savoy2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Savoy.Savoy2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Savoy.Savoy3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Savoy.Savoy3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Serris.Serris1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Serris.Serris1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Serris.Serris2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Serris.Serris2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Serris.Serris3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Serris.Serris3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	#Foundation.OverrideDef('Initialize', 'Systems.Starbase12.Starbase12_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Starbase12.Starbase12_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Tevron.Tevron1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Tevron.Tevron1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Tevron.Tevron2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Tevron.Tevron2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Tezle.Tezle1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Tezle.Tezle1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Tezle.Tezle2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Tezle.Tezle2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Vesuvi.Vesuvi5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Vesuvi.Vesuvi5_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Vesuvi.Vesuvi6_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Vesuvi.Vesuvi6_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Voltair.Voltair1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Voltair.Voltair1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Voltair.Voltair2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Voltair.Voltair2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.XiEntrades.XiEntrades1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.XiEntrades.XiEntrades2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.XiEntrades.XiEntrades3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.XiEntrades.XiEntrades4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.XiEntrades.XiEntrades5_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Yiles.Yiles1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Yiles.Yiles2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Yiles.Yiles3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.SystemsAlt.Yiles.Yiles4_S.Initialize', dict = { 'modes': [ mode ] } )

"""

# TO-DO REGULAR BELARUZ4 CODE, MODIFIED 


def Initialize(pSet):

	import Systems.Belaruz.Belaruz4
	pBelaruz4 = Systems.Belaruz.Belaruz4.GetSet()

	################
	# Create the Planet
	################
#	print ("Putting in the planet.\n")
	pBelaruzPlanet = App.Planet_Create(180.0, "data/models/environment/AquaPlanet.nif")
	pSet.AddObjectToSet(pBelaruzPlanet, "Belaruz 4")

	#Place the object at the specified location.
	#pBelaruzPlanet.PlaceObjectByName( "Belaruz4" )
	#pBelaruzPlanet.UpdateNodeOnly()

	pKClassPlanet = App.Planet_Create(180.0, "data/Models/Environment/K-Class.nif")
	pSet.AddObjectToSet(pKClassPlanet, "Tethys K-Class")
	#Place the object at the specified location.
	pKClassPlanet.PlaceObjectByName( "Tethys K-Class" )
	pKClassPlanet.UpdateNodeOnly()
	# TO-DO MAKE THIS AN IMPORT
	#try:
	#	CreateAtmosphereALT(pKClassPlanet, "data/Models/Environment/K-Class.nif", "K-Class", "data/Models/Environment/K-Class.nif")
	#except:
	#	print "TO-DO ERROR"
	#	traceback.print_exc()

	#########
	# Create the asteroids and make them rotate randomly
	#########

	#Get the asteroid model
#	print ("Putting in the asteroid.\n")
	
	import ships.Asteroid
	ships.Asteroid.LoadModel ()

#	App.g_kModelManager.LoadModel('data/models/misc/Asteroids/asteroid.nif', None)

	# Only create system stuff if not multiplayer or is the host in multiplayer
	if (App.g_kUtopiaModule.IsMultiplayer () == 0 or App.g_kUtopiaModule.IsHost () == 1):
#		print ("Placing asteroids.\n")
		#Create the asteroids for Belaruz4
		for sAsteroidName, sPlacementName in ( 
			("Asteroid 1", "Asteroid1"),
			("Asteroid 2", "Asteroid2"),
			("Asteroid 3", "Asteroid3"),
			("Asteroid 4", "Asteroid4"),
			("Asteroid 5", "Asteroid5"),
			("Asteroid 6", "Asteroid6"),
			("Asteroid 7", "Asteroid7")):
	#		pModel = App.g_kModelManager.CloneModel('data/models/misc/Asteroids/asteroid.nif' )
	#		pModel.SetScale(0.1) 
	#		if (pModel == None):
	#			print("Unable to create asteroid; couldn't load model.")
	#		else:

			pAsteroid = loadspacehelper.CreateShip("Asteroid", pBelaruz4, sAsteroidName, sPlacementName)

			if (pAsteroid):
				pAsteroid.SetHailable(0)
				pAsteroid.SetTargetable(0)
				pAsteroid.SetScannable(0)

				#Rotate the asteroid
				vVelocity = App.TGPoint3_GetModelForward()	# Get the vector to rotate around
				vVelocity.Scale( 10.0 * App.PI / 180.0 )		# Scale it to 10 degrees/second (converted to radians)
				pAsteroid.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)