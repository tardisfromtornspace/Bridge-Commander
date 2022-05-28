from bcdebug import debug
"""
Rotate(pPlanet, fPlanetRotationTime, fPlanetCirculationPeriod, pSun):
        Rotate Objects around another

CreateObjectsAroundAsCircle2D(pObject, sShipType, r, deltaphi, iTargetable=0):
        e.g. to create Asteroids around a Planet
"""

import App
import loadspacehelper
from math import sqrt, pi, sin, cos
from Custom.QBautostart.Libs.LibQBautostart import *


class UpdatePlanets:
	def __init__(self, iPlanetID, fPlanetRotationTime, fPlanetCirculationPeriod, pSun):
                debug(__name__ + ", __init__")
                self.iPlanetID = iPlanetID
                self.pSun = pSun
                self.fRadius = Distance(self.GetPlanetObject(), self.pSun)
                # start with a Random Rotation
                self.fcurRot = App.g_kSystemWrapper.GetRandomNumber(2*pi*100) / 100.0
		self.fPlanetRotInc = 2.0*pi / float(fPlanetRotationTime)
                self.fThetaTransInc = 2.0*pi / float(fPlanetCirculationPeriod)
                self.fPhiTransInc = 0
                self.fTheta = pi / 2.0
		self.fphi = pi / 2.0
                
		self.pTimerProcess = None
		self.SetupTimer()
		
		
        def GetPlanetObject(self):
                debug(__name__ + ", GetPlanetObject")
                try:
                        return App.ObjectClass_GetObjectByID(None, self.iPlanetID)
                except:
                        return None
        
        
	def SetupTimer(self):
		debug(__name__ + ", SetupTimer")
		if self.pTimerProcess:
			# We already have a timer.
			return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(1.0)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)
	
	
	def Update(self, dTimeAvailable):
                # check if the Planet doesn't exist anymore
                debug(__name__ + ", Update")
                if not self.GetPlanetObject():
                        # delete our timer
                        self.pTimerProcess = None
                
                # else update
		if App: # don't ask why
			self.RotateAroundSun()
                	self.RotatePlanet()


        def RotateAroundSun(self):
                debug(__name__ + ", RotateAroundSun")
                kLocation = App.TGPoint3()
                x = self.fRadius * sin(self.fTheta) * cos(self.fphi) + self.pSun.GetWorldLocation().GetX()
                y = self.fRadius * sin(self.fTheta) * sin(self.fphi) + self.pSun.GetWorldLocation().GetY()
                z = self.fRadius * cos(self.fTheta) + self.pSun.GetWorldLocation().GetZ()
                kLocation.SetXYZ(x, y, z)
                self.GetPlanetObject().SetTranslate(kLocation)

                self.fTheta = self.fTheta + self.fThetaTransInc
                if self.fTheta > 2.0 * pi:
                        self.fTheta = 0.0
                self.fphi = self.fphi + self.fPhiTransInc
                if self.fphi > 2.0 * pi:
                        self.fphi = 0.0
        
        
        def RotatePlanet(self):
                debug(__name__ + ", RotatePlanet")
                self.GetPlanetObject().SetAngleAxisRotation(self.fcurRot, 0, 0, 1)
                self.fcurRot = self.fcurRot - self.fPlanetRotInc
                if self.fcurRot < -2.0 * pi:
                        self.fcurRot = 0.0


def Rotate(pPlanet, fPlanetRotationTime, fPlanetCirculationPeriod, pSun):        
        debug(__name__ + ", Rotate")
        u = UpdatePlanets(pPlanet.GetObjID(), fPlanetRotationTime, fPlanetCirculationPeriod, pSun)
        return u


def CreateObjectsAroundAsCircle2D(pObject, sShipType, r, deltaphi, iTargetable=0):
        debug(__name__ + ", CreateObjectsAroundAsCircle2D")
        pSet = pObject.GetContainingSet()
        kObjectlocation = pObject.GetWorldLocation()
        phi = 0
        iShipNum = 0
        
        while phi < 2*pi:
                # calculate the coordinates
                x = r * sin(phi) + kObjectlocation.GetX()
                y = r * cos(phi) + kObjectlocation.GetY()
                z = kObjectlocation.GetZ()
                phi = phi + deltaphi
                
                # get a free shipname
                pcName = sShipType + " " + str(iShipNum)
                while(MissionLib.GetShip(pcName)):
                        iShipNum = iShipNum + 1
                        pcName = sShipType + " " + str(iShipNum)
                
                # create the ship and set its position
                pShip = loadspacehelper.CreateShip(sShipType, pSet, pcName, "", 0)
                kLocation = App.TGPoint3()
                kLocation.SetXYZ(x, y, z)
                pShip.SetTranslate(kLocation)
                pShip.SetTargetable(iTargetable)
                pShip.UpdateNodeOnly()
