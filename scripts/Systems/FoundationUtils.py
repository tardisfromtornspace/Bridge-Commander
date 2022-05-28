import App
import math

class SystemPlacer:
	def __init__(self, fPlanetDiameter, distX = 3, distZ = 5):
		self.fPlanetDiameter = fPlanetDiameter
		self.fPlanetRadius = fPlanetDiameter / 2
		extraX = fPlanetDiameter * distX
		extraZ = fPlanetDiameter * distZ
		fDiameterRoot = math.sqrt(fPlanetDiameter)

		self.fCenterX = fDiameterRoot * self.RandPercent()
		self.fCenterX = self.fCenterX * self.fCenterX + extraX

		self.fCenterY = fPlanetDiameter * 3

		# self.fCenterZ = (fPlanetDiameter * self.RandPercent()) - (fPlanetDiameter * 0.5)
		self.fCenterZ = fPlanetDiameter - self.fCenterX + extraZ

		if self.RandPercent() > 0.5:
			self.fCenterX = self.fCenterX * -1.0

		# print self.fCenterX, self.fCenterY, self.fCenterZ

	def SetOnOrbit(self, fOrbitDistance = 0):
		if fOrbitDistance:
			fHypotenuse = fOrbitDistance + self.fPlanetDiameter
			fHypotenuseSqr = fHypotenuse * fHypotenuse
			# Randomly determine the opposite and adjacent lengths to fit the hypotenuse
			# of orbit distance + planet radius
			X = fHypotenuseSqr * self.RandPercent()
			Y = fHypotenuseSqr - X
			X = math.sqrt(X)
			Y = math.sqrt(Y)

			# Now randomize the quadrants along the X and Z axes
			if self.RandPercent() > 0.5:	X = X * -1.0
			if self.RandPercent() > 0.5:	Y = Y * -1.0

			Z = self.fCenterZ - (self.fCenterZ * self.RandPercent() * 2)

			# Now shift the center onto the planet.
			X = X + self.fCenterX
			Y = Y + self.fCenterY

			return (X, Y, Z)
		else:
			return (self.fCenterX, self.fCenterY, self.fCenterZ)

	def SetFacing(self):
		X = self.RandPercent() * 180.0
		Y = 180.0 - X
		Z = 180.0 - X
		return (X, Y, Z)

	def RandPercent(self):
		return App.g_kSystemWrapper.GetRandomNumber(100) / 100.0
