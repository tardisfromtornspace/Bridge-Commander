###############################################################################
##	Filename:	WeaponFlashFX.py
##	
##	Adds a Flash to Projectiles when fired
##	
##	Created:	09/24/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Custom.NanoFXv2.NanoFX_ScriptActions

def CreateWeaponFlashFX(pObject, pEvent):
	pWeapon = App.TorpedoTube_Cast(pEvent.GetSource())
	if pWeapon == None:
		### Its not a Torpedo, lets try a Pulse ##
		pWeapon = App.PulseWeapon_Cast(pEvent.GetSource())
		if pWeapon == None:
			return
		else:
			fSize  = pWeapon.GetRadius() + 0.05
			pShip = App.ShipClass_Cast(pWeapon.GetParentShip())
			pModuleName = pWeapon.GetProperty().GetModuleName()
			pModule = __import__(pModuleName)			
	else:
		fSize  = pWeapon.GetRadius() + 0.2
		pShip = App.ShipClass_Cast(pWeapon.GetParentShip())
		pModuleName = pShip.GetTorpedoSystem().GetCurrentAmmoType().GetTorpedoScript()
		pModule = __import__(pModuleName)	
	try:
		fColor = pModule.GetFlashColor()
	except:
		fColor = (255.0, 255.0, 255.0)

	pSequence = App.TGSequence_Create()
	sFile = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Weapon/WeaponFlash.tga"
	
	### Setup for Effect ###
	pAttachTo = pShip.GetNode()
	pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	vEmitPos = pWeapon.GetPosition()
	vEmitDir = App.NiPoint3(1, 1, 1)
	pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fFrequency  = 0.01, fLifeTime   = 0.05, iTiming = 3.0, fRed = fColor[0], fGreen = fColor[1], fBlue = fColor[2], fBrightness = 0.8)
	pSequence.AddAction(pFlash)
	pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
	pSequence.Play()