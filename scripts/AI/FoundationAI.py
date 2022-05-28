import App


# Support functions for Foundation-related ship AI

speedBoost = 5000
accelBoost = 8


# Special thanks to jwatts_jr for helping to figure out the proper syntax
# for accessing the SetMax methods. -Dasher42

def EnableInterceptSpeed(pShip):
	pProp = pShip.GetImpulseEngineSubsystem().GetProperty()
	maxSpeed = pProp.GetMaxSpeed()

	if maxSpeed and maxSpeed < speedBoost:
		pProp.SetMaxSpeed(maxSpeed + speedBoost)
		maxAccel = pProp.GetMaxAccel()
		pProp.SetMaxAccel(maxAccel * accelBoost)


def DisableInterceptSpeed(pShip):
	pProp = pShip.GetImpulseEngineSubsystem().GetProperty()
	maxSpeed = pProp.GetMaxSpeed()

	if maxSpeed and maxSpeed >= speedBoost:
		maxSpeed = maxSpeed - speedBoost
		pProp.SetMaxSpeed(maxSpeed)
		maxAccel = pProp.GetMaxAccel()
		pProp.SetMaxAccel(maxAccel / accelBoost)

		currentSpeed = pShip.GetVelocityTG().Length()
		if currentSpeed > maxSpeed:
			pShip.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )
			pShip.SetVelocity(App.TGPoint3_GetModelForward())


# Standard motion formula variables
# u = initial velocity
# s = distance
# v = final velocity
# t = time
# a = acceleration

# Of course, because the ships don't slam on the brakes in Intercept_Dasher, these
# aren't used to their full potential. -Dasher42

def AccelerationDistance(u, a):
	t = u / a
	return u * t + 0.5 * a * (t * t)

def DecelerationDistance(u, a):
	t = u / a
	return u * t - (0.5 * a * (t * t))
