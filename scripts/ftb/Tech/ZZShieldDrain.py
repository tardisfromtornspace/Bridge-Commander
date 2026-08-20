# August 20, 2026 - v1.0
#
# by Alex Marques aka Zambie Zan (alexmarques400@hotmail.com) with great pointers from Alex SL Gato/CharaToLoki (andromedavirgoa@gmail.com)
#
# Permission to redistribute or alter this code as part of any other packaging requires
# the explicit permission of the author in advance.
##############################################################################

from bcdebug import debug
import App
import FoundationTech
import traceback

# Clean Python 1.5.2 compatible import
try:
	import Tactical.Projectiles.impactEffects.ImpactTexture
	ImpactTexture = Tactical.Projectiles.impactEffects.ImpactTexture
except:
	ImpactTexture = None

NonSerializedObjects = (
"oZZShieldDrain",
)

class ZZShieldDrainDef(FoundationTech.TechDef):

	def __init__(self, name):
		FoundationTech.TechDef.__init__(self, name)
		# Dictionary mapping torpedo module paths to their custom settings dict
		self.dSettings = {}

	def IsTorpYield(self):
		debug(__name__ + ", IsTorpYield")
		return 1

	def IsPhaseYield(self):
		debug(__name__ + ", IsPhaseYield")
		return 0 # This tells others that this yield is NOT a Phased Torpedo yield, for some stock KM techs like Multivectral Shields, which do not verify if this function exists on the first place, either.

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 0 # This tells others that this yield is NOT a Breen Drainer yield, in case the Breen Drainer Defense gets on the way (it verified a torp has a yield, and then it verifies if "IsDrainYield" gives 1... issue is that the Breen Drainer does not check if the yield has that function on the same place) or for some techs like Multivectral Shields, which do not verify, either.

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")
		
		if not pEvent or pEvent.IsHullHit():
			return

		if not pShip:
			return

		pShields = pShip.GetShields()
		if not pShields:
			return

		# Fallback defaults
		fDrainPercent = 0.10
		sFlashTexture = "data/Textures/Effects/ExplosionA.tga"
		kElectricColor = [1.0, 0.2, 0.9]
		iFrameW = 8
		iFrameH = 1
		iAmount = 3
		fSparkSize = 1.0
		fSizeMult = 1.5
		fFreq = 0.05
		fEmitLife = 0.75
		fLife = 0.5

		# Pull custom variables directly from torpedo registration if provided
		if pTorp:
			sMod = pTorp.GetModuleName()
			if self.dSettings.has_key(sMod):
				kData = self.dSettings[sMod]
				fDrainPercent = kData.get('fDrainPercent', fDrainPercent)
				sFlashTexture = kData.get('sFlashTexture', sFlashTexture)
				kElectricColor = kData.get('kElectricColor', kElectricColor)
				iFrameW = kData.get('iFrameW', iFrameW)
				iFrameH = kData.get('iFrameH', iFrameH)
				iAmount = kData.get('iAmount', iAmount)
				fSparkSize = kData.get('fSparkSize', fSparkSize)
				fSizeMult = kData.get('fSizeMult', fSizeMult)
				fFreq = kData.get('fFreq', fFreq)
				fEmitLife = kData.get('fEmitLife', fEmitLife)
				fLife = kData.get('fLife', fLife)

		# Drain fDrainPercent from each shield facing's CURRENT capacity
		for iShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			fCurr = pShields.GetCurShields(iShieldDir)
			
			fDrainAmount = fCurr * fDrainPercent
			fNewShield = fCurr - fDrainAmount
			
			if fNewShield < 0.0:
				fNewShield = 0.0

			# Explicitly cast to float to satisfy Bridge Commander's C++ bindings
			pShields.SetCurShields(iShieldDir, float(fNewShield))

		# --- Trigger Electric Flash Effect on Shield Impact ---
		if ImpactTexture and pShip and sFlashTexture: # To consider, you might want to add a check so if a ship is dying, this effect does not happen.
			try:
				ImpactTexture.DriveEnterFlash(
					None,
					pShip.GetObjID(),
					None,
					amount=iAmount,
					sparkSize=fSparkSize,
					sFile=sFlashTexture,
					sFileFrameW=iFrameW,
					sFileFrameH=iFrameH,
					colorKey=kElectricColor,
					pAttachTo=pShip.GetNode(),
					pEmitFrom=pShip,
					fSize=pShip.GetRadius() * fSizeMult,
					fFrequency=fFreq,
					fEmitLife=fEmitLife,
					fSpeed=0.0,
					fLife=fLife
				)
			except:
				traceback.print_exc()

	def AddTorpedo(self, path, fPercent = 0.10, sTexture = "data/Textures/Effects/ExplosionA.tga", kColor = [1.0, 0.2, 0.9], iFrameW = 8, iFrameH = 1, iAmount = 3, fSizeMult = 1.5, fLife = 0.5):
		FoundationTech.dYields[path] = self
		# Store torpedo parameters directly in a configuration map
		self.dSettings[path] = {
			'fDrainPercent': float(fPercent),
			'sFlashTexture': sTexture,
			'kElectricColor': kColor,
			'iFrameW': iFrameW,
			'iFrameH': iFrameH,
			'iAmount': iAmount,
			'fSparkSize': 1.0,
			'fSizeMult': fSizeMult,
			'fFreq': 0.05,
			'fEmitLife': 0.75,
			'fLife': fLife
		}


oZZShieldDrain = ZZShieldDrainDef('Shield Drain Torpedo')