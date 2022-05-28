from bcdebug import debug
###############################################################################
##	Filename:	PlasmaFX.py
##	
##	Original Effect by Sneaker98, Module for NanoFX's SpecialFX
##	
##	Created:	09/24/2003 - NanoByte a.k.a Michael T. Braams
##
##      All credit goes to this man NanoByte and lost_jedi for his modification
##      I only did minor adjustments to the file, USS Sovereign
###############################################################################
import App
import Custom.NanoFXv2.NanoFX_ScriptActions

#global variable for emitting the plasma streamer
g_sneakerPlasmaCheck = 2
g_sneakerPlasmaConstant = 0

###############################################################################
## PlasmaFX
###############################################################################
def BCSTNGPlasmaFXoverride(pShip, pEvent):
	
	debug(__name__ + ", BCSTNGPlasmaFXoverride")
	if pShip:
		### Setup ###
		pSequence = App.TGSequence_Create()
		###
		### Setup Attachment ###
		pTargetObject = pEvent.GetTargetObject()
		if not pTargetObject:
			return pSequence
		vEmitPos      = pEvent.GetObjectHitPoint()
		vEmitDir      = pEvent.GetObjectHitNormal()
		pSet 	      = pShip.GetContainingSet()
		pAttachTo     = pSet.GetEffectRoot()
		pEmitFrom     = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
		fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "PlasmaFX")
		if (fPlasmaColor == None):
			sRace	      = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
			fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)
		sFile         = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga"
		###
		pWarpSys = pShip.GetWarpEngineSubsystem()
		if pWarpSys:
			# determine how many warp subsystems
			iNumWarp = pWarpSys.GetNumChildSubsystems()
			# go through every one of em.. make em smoke if they are damaged enough
			for iEng in range(iNumWarp):
				pWarpChild = pWarpSys.GetChildSubsystem(iEng)
				if pWarpChild:
                                        # Insert IgnitePlasmaFX addin here

                                        # Carry on ...
					pWarpChildPos = pWarpChild.GetPosition()
					pWarpChildCondition = pWarpChild.GetCondition()
					pWarpChildMaxCondition = pWarpChild.GetMaxCondition()
					if (pWarpChildCondition <= pWarpChildMaxCondition / 2):
						global g_sneakerPlasmaCheck
						sneakerPlasmaRandom = App.g_kSystemWrapper.GetRandomNumber(4)
						if (g_sneakerPlasmaCheck == sneakerPlasmaRandom):
							global g_sneakerPlasmaConstant
							if g_sneakerPlasmaConstant == 0:
								fVentTime = App.g_kSystemWrapper.GetRandomNumber(25) + 60.0 
								try:
									if App.g_kUtopiaModule.IsMultiplayer():
										from Multiplayer.Episode.Mission4.Mission4 import MPSendCreatePlasma
										MPSendCreatePlasma(pShip, vEmitDir, iEng, fVentTime)
								except:
									pass
								### Generate Gfx Sequence ###
								fVentTime = App.g_kSystemWrapper.GetRandomNumber(25) + 60.0
								sFile         = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga"
								pPlasma = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, 
																pEmitFrom, 
																pAttachTo, 
																pShip.GetRadius() * 0.10, 
																pWarpChildPos, 
																vEmitDir,
																bInheritVel = 0,
																fFrequency = 0.03, 
																fLifeTime = fVentTime,
																fEmitVel = 0.1,
																fVariance = 150.0,
																iTiming = 72,
																sType = "Plasma",
																fRed = fPlasmaColor[0], 
																fGreen = fPlasmaColor[1], 
																fBlue = fPlasmaColor[2],
																fBrightness = 0.10)
								pSequence.AddAction(pPlasma)
								
								pPlasma = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, 
																pEmitFrom, 
																pAttachTo, 
																pShip.GetRadius() * 0.05, 
																pWarpChildPos, 
																vEmitDir,
																bInheritVel = 0,
																fFrequency = 0.03, 
																fLifeTime = fVentTime,
																fEmitVel = 0.1,
																fVariance = 150.0,
																iTiming = 72,
																sType = "Plasma",
																fRed = fPlasmaColor[0], 
																fGreen = fPlasmaColor[1], 
																fBlue = fPlasmaColor[2],
																fBrightness = 0.60)
								pSequence.AddAction(pPlasma)
								###
								### Create Plasma Event SFX
								sSound = "Plasma"
								###
								### Add an action to play the sound. ###
								if pShip.GetName() == "Player" or pShip.GetName() == "player":
									### Vent Sounds ###
									pSound = App.TGSoundAction_Create("Player_Burst.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound)
									pSound = App.TGSoundAction_Create("Player_Vent.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound)
									pSound = App.TGSoundAction_Create("Player_Seal.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound, App.TGAction_CreateNull(), fVentTime)
									###
									### Computer Alerts ###
									pSound = App.TGSoundAction_Create("Comp_Burst.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound)
									pSound = App.TGSoundAction_Create("Comp_Seal.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound, App.TGAction_CreateNull(), fVentTime)
									###									
								else:
									### Vent Sounds ###
									pSound = App.TGSoundAction_Create("AI_Burst.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound)
									pSound = App.TGSoundAction_Create("AI_Vent.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound)
									pSound = App.TGSoundAction_Create("AI_Seal.wav", 0, pSet.GetName())
									pSound.SetNode(pShip.GetNode())
									pSequence.AddAction(pSound, App.TGAction_CreateNull(), fVentTime)
									###
								g_sneakerPlasmaConstant = 8
								### Return our SpecialFX Sequence ###
								
								###################################################################################
								### BCS:TNG Targetable Plasma Streams Insert                                    ###
								if not App.g_kUtopiaModule.IsMultiplayer():
                                                                    # Multiplayer game so we don't want to start up TPS
                                                                    print "PlasmaFX Communicating with Targetable Plasma Streams..."            ###
                                                                    #try:                                                                       ###
                                                                    from Custom.QBautostart.TargetablePlasmaStreams import AppendPlasmaTracker  ###
                                                                    AppendPlasmaTracker(pWarpChild,fVentTime,pShip,pSequence)                   ###
                                                                    print "...Sucess"                                                           ###
                                                                    #except:                                                                    ###
                                                                    #print "...Failed"                                                          ###
                                                                ### END INSERT                                                                  ###
                                                                ###################################################################################

								return pSequence
							else:
								g_sneakerPlasmaConstant = g_sneakerPlasmaConstant - 1
		
		###
	return pSequence
