# by USS Sovereign

# We need to make sure before initiating high speeds that we are aiming towards empty space


# Imports
import App
import MissionLib

# Vars
vBetterDirection = None
sGoodAim = 'FALSE'
fDirectionTimeThreshold = 0.2


# Position the player towards empty space
def GoodAim():
            global sGoodAim
            global vBetterDirection
            global fDirectionTimeThreshold
            
            # Reset good aim string
            sGoodAim = 'FALSE'
            
            # Check to see if there's something in front of the ship
            pPlayer = MissionLib.GetPlayer()
	    fRayLength = 8000.0
	    vOrigin = pPlayer.GetWorldLocation()
	    vEnd = pPlayer.GetWorldForwardTG()
	    vEnd.Scale(fRayLength)
	    vEnd.Add(vOrigin)

	    sObstacles = GrabObstacles(vOrigin, vEnd, pPlayer)
	    
            # No obstacles?! Cool!!!
	    if len(sObstacles) == 0:
		    vZero = App.TGPoint3()
		    vZero.SetXYZ(0, 0, 0)
		    pPlayer.SetTargetAngularVelocityDirect(vZero)
		    sGoodAim = 'TRUE'
		    # print 'Slipstream: No obstacles, free to jump.'
		    return 1

	    if not vBetterDirection:
                    # Search for a good direction
		    for iRayCount in range(8):
                        vRay = App.TGPoint3_GetRandomUnitVector()

                        vRay.Scale(1.5)
                        vRay.Add(pPlayer.GetWorldForwardTG())

                        vRay.Unitize()

                        vEnd = App.TGPoint3()
                        vEnd.Set(vRay)
                        vEnd.Scale(fRayLength)

                        vEnd.Add(vOrigin)
                        
                        # Grab obstacles
                        sObstacles = GrabObstacles(vOrigin, vEnd, pPlayer)
                        
                        if not sObstacles:
                                # Good direction? Break away
                                vBetterDirection = vRay
                                # print 'Slipstream: Bit of a situation here... Not ready to jump yet!'
                                break

            # Adjust the position so we all can have a happy life
            if vBetterDirection:
			fTime = pPlayer.TurnTowardDirection(vBetterDirection)
			# Not quite there yet?
			if fTime < fDirectionTimeThreshold:
				vBetterDirection = None
                                # print 'Slipstream: We are getting close...'
                        # Sweet!!!
                        else:
                                sGoodAim = 'TRUE'
                                # print 'Slipstream: Ready to jump!'


# Returns warp obstacles
def GrabObstacles(vStart, vEnd, pPlayer):
	    return MissionLib.GrabWarpObstaclesFromSet(vStart, vEnd, pPlayer.GetContainingSet(), pPlayer.GetRadius(), 1, pPlayer.GetObjID())


# Checks the stats of Aim
def CheckGoodAim():
            global sGoodAim
            return sGoodAim
