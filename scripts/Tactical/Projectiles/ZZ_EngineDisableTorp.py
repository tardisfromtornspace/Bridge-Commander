# ZZ_EngineDisableTorp.py
# August 2026 - v1.0
# by Alex Marques aka Zambie Zan (alexmarques400@hotmail.com)
#
# Standalone torpedo that disables engines and warp on the hit ship for 10 seconds.
# Modeled on ZZ_QuDFMPA.py pattern.
#
# Place this file in: scripts/Tactical/Projectiles/
##############################################################################

import App
import traceback

trailsWork = 0
try:
	import trails.OriBeam
	trailsWork = 1
except:
	trailsWork = 0
	print(__name__, " will not load effects because dependencies are missing:")
	traceback.print_exc()


def Create(pTorp):
	# --- Torpedo visual: blue-white EMP pulse color ---
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.3, 0.6, 1.0, 1.0)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.92, 0.98, 1.0, 1.0)

	pTorp.CreateTorpedoModel(
		"data/Textures/Tactical/ZZEngineCore.tga",
		kCoreColor,
		0.2,
		7.0,
		"data/Textures/Tactical/ZZEngineGlow.tga",
		kGlowColor,
		15.0,
		0.3,
		0.9,
		"data/Textures/Tactical/ZZEngineCore.tga",
		kGlowColor,
		25,
		0.2,
		2.0
	)

	pTorp.SetDamage(GetDamage())
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
	pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
	pTorp.SetLifetime(GetLifetime())

	# Multiplayer type
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)

	# Register the engine-disable yield on this torpedo
	try:
		import FoundationTech
		import ftb.Tech.ZZEngineDisable
		ftb.Tech.ZZEngineDisable.oZZEngineDisable.AddTorpedo(
			__name__,
			fDuration = 15,
			sTexture  = "data/Textures/Effects/ZZEngine.tga",
			kColor    = [0.4, 0.8, 1.0],
			iFrameW   = 8,
			iFrameH   = 2,
			iAmount   = 1,
			fSizeMult = 2.0,
			fLife     = 1.0
		)
	except Exception, e:
		print "Failed to register ZZEngineDisable yield:", str(e)
		traceback.print_exc()

	return 0


# --- Standard torpedo parameters ---
def GetLaunchSpeed():       return 45.0
def GetLaunchSound():       return "photon"
def GetPowerCost():         return 1.0
def GetName():              return "Engine Disruptor"
def GetDamage():            return 0.0001      # near-zero kinetic damage; effect is the yield
def GetGuidanceLifetime():  return 10.0
def GetMaxAngularAccel():   return 0.2
def GetLifetime():          return 10.0
def GetDamageDistance():    return 40
