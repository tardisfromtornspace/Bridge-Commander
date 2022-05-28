# Rotates a ship

# by Sov

import App

def Rotate(pShip):
        fSpeed = int(App.g_kSystemWrapper.GetRandomNumber(15)) + 1
        
	vVelocity = App.TGPoint3()
	vVelocity.SetXYZ( (App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 10000.0, (App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 10000.0, (App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 10000.0)
	vVelocity.Unitize()
	vVelocity.Scale( fSpeed * App.HALF_PI / 180.0 )
	
	pShip.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
