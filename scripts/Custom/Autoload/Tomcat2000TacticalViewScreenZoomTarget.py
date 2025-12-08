# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE
# 8th December 2025
# VERSION 0.1
# Patch made by Alex SL Gato, based on TomCat2000's TacticalInterfaceHandlers updated script.
# The purpose of this patch is to adapt TomCat2000's script (which only adds "ViewscreenZoomTarget" to the next camera mode) without having to overwrite newer improved functions on TacticalInterfaceHandlers
# Changes: 
# - Provides "ViewscreenZoomTarget" view to the TacticalInterfaceHandlers.CycleCameraMode
#
# You can add more camera modes by importing this script, append stuff to the "extraModes" list, then call this module's
# CheckUpdate()
# ApplyUpdate()


from bcdebug import debug
import App
import traceback

necessaryToUpdate = 0
scriptToPatch = None
path = "TacticalInterfaceHandlers"
oldFunc = None
lsPrimaryModes = None
extraModes = ["Target", "Chase", "ViewscreenForward", "ViewscreenZoomTarget"] #<--- Append with extraModes.append("NewCameraModeName")
newModes = []

def CheckUpdate():
	global necessaryToUpdate, scriptToPatch, oldFunc, lsPrimaryModes, newModes
	try:
		try:
			scriptToPatch = __import__(path)
		except:
			scriptToPatch = None
			print __name__, "Could not find ", path ," to patch"
		if scriptToPatch != None:
			if hasattr(scriptToPatch, "CycleCameraMode"):
				oldFunc = scriptToPatch.CycleCameraMode
				hasAttrClass = hasattr(oldFunc, "lsPrimaryModes")
				hasAttrInnerF = ("lsPrimaryModes" in oldFunc.func_code.co_varnames)
				if hasAttrClass or hasAttrInnerF:
					if hasAttrClass:
						lsPrimaryModes = oldFunc.lsPrimaryModes
					else:
						lsPrimaryModes = []
						necessaryToUpdate = 2	
					for aMode in extraModes:
						if not aMode in lsPrimaryModes:
							newModes.append(aMode)
							if necessaryToUpdate == 0:
								necessaryToUpdate = 1
				else:
					print __name__, ": no lsPrimaryModes to patch. It is likely something's broken with ", path
					#dirFu = dir(oldFunc)
					#print dir(oldFunc)
					#print oldFunc.__doc__ # None
					#print oldFunc.__name__ # CycleCameraMode
					#print oldFunc.func_name # CycleCameraMode
					#print oldFunc.func_doc # None
					#print oldFunc.func_defaults # None
					#print oldFunc.func_globals
					#print oldFunc.func_code # Position in the code
					#dirCoFu = dir(oldFunc.func_code)
					#print dirCoFu
					#print oldFunc.func_code.co_argcount
					#print oldFunc.func_code.co_code
					#print oldFunc.func_code.co_consts # (None, 'Target', 'Chase', 'ViewscreenForward', 'ViewscreenZoomTarget', 0, 1, 'InvalidSpace' )
					#print oldFunc.func_code.co_filename
					#print oldFunc.func_code.co_firstlineno
					#print oldFunc.func_code.co_flags
					#print oldFunc.func_code.co_lnotab
					#print oldFunc.func_code.co_name
					#print oldFunc.func_code.co_names
					#print oldFunc.func_code.co_nlocals
					#print oldFunc.func_code.co_stacksize
					#print oldFunc.func_code.co_varnames
			else:
				print __name__, ": No CycleCameramode. It is likely something's broken with ", path
		else:
			necessaryToUpdate = 0
			print __name__, ": Unable to find ", path
	except:
		necessaryToUpdate = 0
		print __name__, " Error while handling update check:"
		traceback.print_exc()

	return necessaryToUpdate


def ApplyUpdate():
	global necessaryToUpdate, scriptToPatch, oldFunc, lsPrimaryModes, newModes
	if scriptToPatch != None:
		try:
			if necessaryToUpdate != 0:

				lsPrimaryModesL = []
				if necessaryToUpdate == 1:

					for iIndex in range( len(lsPrimaryModes) ):
						lsPrimaryModesL.append(lsPrimaryModes[iIndex])

					for aMode in newModes:
						lsPrimaryModesL.append(aMode) # <-- THIS IS THE CHANGE THAT THE OTHER SCRIPT MAKES, just add a "ViewscreenZoomTarget" at the end of lsPrimaryModes

				else:
					lsPrimaryModesL = newModes

				lsPrimaryModesT = tuple(lsPrimaryModesL)

				if necessaryToUpdate == 1:
					scriptToPatch.CycleCameraMode.lsPrimaryModes = currlsPrimaryModes
					print "Patched TacticalControlInterfaces.CycleCameraMode.lsPrimaryModes to add mode viewing modes"
				elif necessaryToUpdate == 2:
					OldCycleCameraMode = scriptToPatch.CycleCameraMode


					def NewCycleCameraMode(pObject, pEvent, lsPrimaryModes=lsPrimaryModesT):
						# Cycle primary camera modes.  If we're not in
						# one of the primary modes, switch to one of them.
						# If we are, loop through them.
						if lsPrimaryModes == None:
							lsPrimaryModes = ( "Target", "Chase", "ViewscreenForward" )

						pGame = App.Game_GetCurrentGame()
						if not pGame:
							return

						pPlayer = pGame.GetPlayer()
						pCamera = pGame.GetPlayerCamera()
						if not (pCamera and pPlayer):
							return
	
						pMode = pCamera.GetCurrentCameraMode()

						# Check the current camera mode against each of the primary modes..
						if pMode:
							pModeID = pMode.GetObjID()
							for iIndex in range( len(lsPrimaryModes) ):
								sPrimaryMode = lsPrimaryModes[iIndex]
								if sPrimaryMode != None:
									pPrimaryMode = pCamera.GetNamedCameraMode(sPrimaryMode)
									if pPrimaryMode != None and pModeID == pPrimaryMode.GetObjID():
										# The current camera mode is this primary mode.  Cycle
										# it to the next primary mode.
										break
						else:
							iIndex = -1

						for iAttemptCount in range( len(lsPrimaryModes) ):
							iIndex = (iIndex + 1) % len(lsPrimaryModes)
							sPrimaryMode = lsPrimaryModes[iIndex]
							if sPrimaryMode != None:
								pPrimaryMode = pCamera.GetNamedCameraMode( sPrimaryMode )
								if pPrimaryMode != None and pPrimaryMode.IsValid():
									# Set the space view to use this camera mode.
									pCamera.AddModeHierarchy("InvalidSpace", sPrimaryMode)
									pPrimaryMode.Reset()
									return

						#debug("No valid primary camera modes.  Can't switch camera mode.")

					scriptToPatch.CycleCameraMode = NewCycleCameraMode
					print "Patched TacticalControlInterfaces.CycleCameraMode to add mode viewing modes"

		except:
			print __name__, " Error while applying update:"
			traceback.print_exc()

CheckUpdate()
ApplyUpdate()