from bcdebug import debug
import App
import FoundationTech
import traceback
import MissionLib
from DisablerYields import DisablerTorpDef, oImpulseDisable, oWarpDisable

# Impact flash effect - same pattern as ZZShieldDrain.py
try:
	import Tactical.Projectiles.impactEffects.ImpactTexture
	ImpactTexture = Tactical.Projectiles.impactEffects.ImpactTexture
except:
	ImpactTexture = None
	traceback.print_exc()

# ZZEngineDisable.py
# October 2026 - v1.023
# by Alex Marques aka Zambie Zan (alexmarques400@hotmail.com)
# small changes by CharaToLoki
#
# Torpedo yield that disables both Impulse and Warp engines for 10 seconds.
# Auto-restore is handled internally by pInstance.DisableSubSys() - no timer needed.
#
# Place this file in: scripts/ftb/Tech/

NonSerializedObjects = (
	"oZZEngineDisable",
)

DISABLE_DURATION = 10


class ZZEngineDisableDef(FoundationTech.TechDef):

	def __init__(self, name):
		FoundationTech.TechDef.__init__(self, name)
		self.dSettings = {}

	def IsTorpYield(self):
		debug(__name__ + ", IsTorpYield")
		return 1

	def IsPhaseYield(self):
		debug(__name__ + ", IsPhaseYield")
		return 0

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 0

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")

		if not pShip or (pShip.IsDead() or pShip.IsDying()) or not pInstance:
			return

		if not pEvent:
			return

		# Get custom settings if registered, else use defaults
		fDuration = DISABLE_DURATION

		# --- Impact flash effect - variables come from AddTorpedo() registration ---
		sTexture = "data/Textures/Effects/ExplosionA.tga"
		kColor   = [0.4, 0.8, 1.0]
		iFrameW  = 8
		iFrameH  = 2
		iAmount  = 2
		fSizeMult = 2.0
		fLife    = 1.5

		if pTorp:
			sMod = pTorp.GetModuleName()
			if self.dSettings.has_key(sMod):
				kData    = self.dSettings[sMod]
				sTexture = kData.get('sTexture',  sTexture)
				kColor   = kData.get('kColor',    kColor)
				iFrameW  = kData.get('iFrameW',   iFrameW)
				iFrameH  = kData.get('iFrameH',   iFrameH)
				iAmount  = kData.get('iAmount',   iAmount)
				fSizeMult = kData.get('fSizeMult', fSizeMult)
				fLife    = kData.get('fLife',     fLife)
				fDuration = kData.get('fDuration', fDuration)

		# --- Disable ship glows for the duration ---
		iShipID = pShip.GetObjID()
		if iShipID != None and iShipID != App.NULL_ID and not (pShip.IsDead() or pShip.IsDying()):
			# Disable impulse engines
			pImpulse = pShip.GetImpulseEngineSubsystem()
			if pImpulse:
				try:
					pInstance.DisableSubSys(pShip, pImpulse, fDuration)
				except:
					traceback.print_exc()

			# Disable warp engines
			pWarp = pShip.GetWarpEngineSubsystem()
			if pWarp:
				try:
					pInstance.DisableSubSys(pShip, pWarp, fDuration)
				except:
					traceback.print_exc()

			try:
				pShip.DisableGlowAlphaMaps()
			except:
				traceback.print_exc()

			# Schedule glow restore after fDuration seconds
			# Uses NanoFX TGSequence pattern from NanoFX_Lib.CreateFlickerSeq()
			try:
				pSeq = App.TGSequence_Create()
				pSeq.AddAction(
					App.TGScriptAction_Create(__name__, "RestoreGlow", iShipID),
					App.TGAction_CreateNull(),
					fDuration
				)
				pSeq.Play()
			except:
				traceback.print_exc()

			if ImpactTexture and pShip and sTexture:
				try:
					ImpactTexture.DriveEnterFlash(
						None,
						pShip.GetObjID(),
						None,
						amount      = iAmount,
						sparkSize   = 1.0,
						sFile       = sTexture,
						sFileFrameW = iFrameW,
						sFileFrameH = iFrameH,
						colorKey    = kColor,
						pAttachTo   = pShip.GetNode(),
						pEmitFrom   = pShip,
						fSize       = pShip.GetRadius() * fSizeMult,
						fFrequency  = 0.05,
						fEmitLife   = 0.75,
						fSpeed      = 0.0,
						fLife       = fLife
					)
				except:
					traceback.print_exc()

	def AddTorpedo(self, path, fDuration=10, sTexture="data/Textures/Effects/ExplosionA.tga", kColor=[0.4, 0.8, 1.0], iFrameW=8, iFrameH=2, iAmount=2, fSizeMult=2.0, fLife=1.5):
		FoundationTech.dYields[path] = self
		self.dSettings[path] = {
			'fDuration'  : fDuration,
			'sTexture'   : sTexture,
			'kColor'     : kColor,
			'iFrameW'    : iFrameW,
			'iFrameH'    : iFrameH,
			'iAmount'    : iAmount,
			'fSizeMult'  : fSizeMult,
			'fLife'      : fLife,
		}


def RestoreGlow(pAction, iShipID):
	debug(__name__ + ", RestoreGlow")
	try:
		# Restore glows - same method as NanoFX_ScriptActions.TurnOnLights()
		if App.g_kLODModelManager.AreGlowMapsEnabled() == 1:
			App.g_kLODModelManager.SetGlowMapsEnabled(0)
			if App.g_kLODModelManager.GetDropLODLevel() == 0:
				App.g_kLODModelManager.SetGlowMapsEnabled(1)
	except:
		traceback.print_exc()

	# Reassign the ship's AI so movement resumes after engine restore
	# Pattern from QuickBattle.py line 2629: __import__(pcWhichAI) -> SetAI()
	# TARDIS changes: since you are not really modifying the AI, you can just pick it up again - this is really useful for when 
	# you had changed the AI from the original (i.e. given them a fleet command). Pattern from scripts.Custom.QBautostart.FleetUtils
	try:
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if pShip and not (pShip.IsDead() or pShip.IsDying()):
			pOldAI = pShip.GetAI()
			if pOldAI:
				pShip.ClearAI(0, pOldAI)
				pShip.SetAI(pOldAI)
		"""
		import Foundation
		import string
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if pShip and not pShip.IsDead():
			# Get the ship's ShipDef to find its AI module name
			pShipScript = string.split(pShip.GetScript(), ".")
			sShipKey = pShipScript[-1]
			if Foundation.shipList._keyList.has_key(sShipKey):
				pShipDef = Foundation.shipList[sShipKey]
				# Determine if this ship is on the friendly or enemy side
				pMission = MissionLib.GetMission()
				if pMission:
					sShipName = pShip.GetName()
					pFriendlies = pMission.GetFriendlyGroup()
					if pFriendlies and pFriendlies.IsNameInGroup(sShipName):
						pcWhichAI = pShipDef.StrFriendlyAI()
					else:
						pcWhichAI = pShipDef.StrEnemyAI()
					if pcWhichAI:
						pAIModule = __import__(pcWhichAI)
						pShip.SetAI(pAIModule.CreateAI(pShip), 0, 0)
		"""
	except:
		traceback.print_exc()
	return 0


oZZEngineDisable = ZZEngineDisableDef('Engine Disable Torpedo')
