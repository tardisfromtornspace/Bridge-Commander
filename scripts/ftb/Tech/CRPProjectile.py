###############################################################################################################
#          Chain Reaction Pulsar v2.0
#                                           by USS Frontier
###############################################################################################################
# The Chain Reaction Pulsar is a torpedo tech that lets a torpedo bounce off the target that he hitted, with a
# boost in damage and proceed to a new target, and so on, until a limit of bounces is reached or if there is 
# no targets in range.
###############################################################################################################
# To add the Chain Reaction Pulsar tech to a torpedo, add the following code at the end of the script:
# And remove the "#" symbols

#try:
#	import FoundationTech
#	import ftb.Tech.CRPProjectile
#
#	oFire = ftb.Tech.CRPProjectile.CRPProjectileDef('CRP Projectile', {
#	'MaxHits':			25,
#	'InDmgFac':			0.05,
#})
#	FoundationTech.dYields[__name__] = oFire
#except:
#	import sys
#	et = sys.exc_info()
#	error = str(et[0])+": "+str(et[1])
#	print "ERROR at script: " + __name__ +", details -> "+error

# You can change that 'CRP Projectile' string to the name that you want.
# You can change the Maximum Number of Hits (MaxHits) value from 25 to what you want.
# You can change the Increase Damage Factor (InDmgFac) value from 0.05 to what you want.

#########################################################################################################################


import App
import FoundationTech
import MissionLib
import string
from ATPFunctions import *

try:
	from bcdebug import debug
except:
	def debug(s):
		pass

class CRPProjectileDef(FoundationTech.TechDef):

	def __init__(self, name, dict):
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.MaxHits = 50
		self.InDmgFac = 0.05
		self.__dict__.update(dict)
		self.dCRPs = {}
		self.lOldIDs = []

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		pCRP = None
		iOldID = pTorp.GetObjID()
		sFullName = str(pTorp.GetName())
		if sFullName == "None" or sFullName == "":
			pCRP = ChainReactionPulsar(pTorp, self.MaxHits, self.InDmgFac)
			self.dCRPs[pCRP.Name] = pCRP
			#print "created CRP for ID", iOldID
		else:
			lStrs = string.split(sFullName, "-")
			sName = lStrs[0]
			iHits = int(lStrs[1])
			if self.dCRPs.has_key(sName):
				pCRP = self.dCRPs[sName]
				#print "got old CRP for ID", sName
				if pCRP.NumHits == iHits:
					#print "Hit number matching - ok to proceed"
					pass
				else:
					#print "CRP Hit Number not matching, cancelling..."
					return
			else:
				#print "no CRP for this ID....", sName
				return

		if pCRP != None:
			pCRP.OnYield(pShip, pInstance, pEvent, pTorp)
		return


class ChainReactionPulsar:
	def __init__(self, torp, fMaxHits, fInDmgFac):
		self.ID = torp.GetObjID()
		self.Name = "CRP"+str(self.ID)
		self.MaxHits = fMaxHits
		self.InDmgFac = fInDmgFac
		self.NumHits = 0
		self.LastTorp = None
	def GetID(self):
		return self.ID
	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		pOldTorp = pTorp
		#print "beggining CRP Projectile yield"
		iNewID = 0
		if pShip != None:
			pSet = pShip.GetContainingSet()
	
			#print "Old Torp =", pOldTorp, " || ID=", pOldTorp.GetObjID(), " || Name=", pOldTorp.GetName()
			pNextTarget = GetNextEnemyInSet(pShip)

			if self.NumHits > self.MaxHits:
				#print "CRP ID", self.ID, " reached max hits"
				self.LastTorp = None
				return -1
			self.NumHits = self.NumHits + 1

			if pOldTorp != None and pNextTarget != None:	
				#print "Next Target =", pNextTarget.GetName()

				VecsXY = VectorMath(pNextTarget.GetWorldLocation(), pEvent.GetWorldHitPoint(), pEvent.GetWorldHitNormal())
				X = VecsXY[0]
				Y = VecsXY[1]
							
				#The torp stuff
				sCRPTorp = pOldTorp.GetModuleName()
				#print "Old Torp Dmg =", pOldTorp.GetDamage()
				pTorpScript = __import__(sCRPTorp)

				sTorpName = self.Name+"-"+str(self.NumHits)

				pNewTorp = CRPFireTorpedo(sTorpName,Y,X,sCRPTorp,pNextTarget.GetObjID(),pShip.GetObjID(),pTorpScript.GetLaunchSpeed())
				iNewID = pNewTorp.GetObjID()
				TorpDmg = pOldTorp.GetDamage()+(pOldTorp.GetDamage()*self.InDmgFac)
	
				#print "NewTorpDefaultDmg=", pNewTorp.GetDamage(), "TorpNewDmg=", round(TorpDmg), "Hits=", self.NumHits

				pNewTorp.SetDamage(round(TorpDmg))

				#print "New Torp ID=", iNewID, " ||| Actual Torp Dmg=", pNewTorp.GetDamage()

				PlayTorpLaunchSound(pNewTorp, pSet)			

				self.LastTorp = pNewTorp
				#self.CreateTrail()
		if iNewID == 0:
			self.LastTorp = None
		return iNewID

	def CreateTrail(self):
		if self.LastTorp == None:
			return
		debug(__name__ + ", creating trail")
		sTexture = "data/sphere.tga"  ###"scripts/Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga"
		pSeq = App.TGSequence_Create()
		pAction = None
		lColor = [255.0, 255.0, 255.0, 255.0]  # ARGB
		fSize = self.LastTorp.GetRadius() * 601.02
		fLength = 300.0
		fVelocity = 10.0
		fAngleVariance = 1.0
		fEffectLifeTime = 60.0
		fFrequency = 0.01
		vPosOffset = App.TGPoint3()
		vPosOffset.SetXYZ(0.0, 0.0, 0.0)
		vDirection = App.TGPoint3()
		vDirection.SetXYZ(0.0, 1.0, 0.0)
		debug(__name__ + ", going to create particle stream")
		pAction = createParticleStream(self.LastTorp, sTexture, fSize, fLength, fVelocity, fAngleVariance, fEffectLifeTime, fFrequency, vPosOffset, vDirection, lColor)
		debug(__name__ + ", created particle stream")
		pSeq.AddAction(pAction)
		pFinalAction = App.TGScriptAction_Create(__name__, "CRP_CreateTrailAction", self)
		pSeq.AddAction(pFinalAction, pAction)
		debug(__name__ + ", going to play to play sequence")
		pSeq.Play()
		debug(__name__ + ", played trail sequence")
		return

def CRP_CreateTrailAction(pAction, pCRP):
	pCRP.CreateTrail()
	return 0


#Credit for this goes to Mleo, from his Foundation Tech.
#This is for some vector calculation that are needed before using the FireTorpFromPointWithVector, ive made a func to return 
#the values needed because, well, its much more simpler than copying 19 lines of code before each time the FireTorp func woulda be used
def VectorMath(GotoCOOR, GoFromCOOR, GoFromNormal):
	X = GotoCOOR
	kVectNiWorldHitPoint = GoFromCOOR
	Y = App.TGPoint3()
	Y.SetX(kVectNiWorldHitPoint.x)
	Y.SetY(kVectNiWorldHitPoint.y)
	Y.SetZ(kVectNiWorldHitPoint.z)
	kVectNiWorldHitNormal = GoFromNormal
	N = App.TGPoint3()
	N.SetX(kVectNiWorldHitNormal.x)
	N.SetY(kVectNiWorldHitNormal.y)
	N.SetZ(kVectNiWorldHitNormal.z)
		
	X.Subtract(Y)
	X.Unitize()
	U = X.Cross(N)
	V = N.Cross(U)
	V.Unitize()
	V.Scale(-2.0*X.Dot(V))
	X.Add(V)
	
	return [X, Y]

#Mleo's FireTorpFromPointWithVector didn't played the launch sound of the torpedo, so i've made this
#out of the FireTorpFromPoint in MissionLib
def PlayTorpLaunchSound(TorpedoProp, SetProp):
	pcLaunchSound = TorpedoProp.GetLaunchSound()
	if pcLaunchSound != None:
		pSound = App.g_kSoundManager.GetSound(pcLaunchSound)
		if pSound != None:
			pSound.AttachToNode(TorpedoProp.GetNode())
			pSoundRegion = App.TGSoundRegion_GetRegion(SetProp.GetName())
			if pSoundRegion != None:
				pSoundRegion.AddSound(pSound)

			pSound.Play()

#Mleo's FireTorpFromPointWithVector function from FTech (ATPFunctions.py)
#This is here because this is a slightly modified version, most importantly because I need to set a name for the torpedo.
def CRPFireTorpedo(sTorpName, kPoint, kVector, pcTorpScriptName, idTarget, pShipID, fSpeed, TGOffset = None):

	# This is an slightly altered version of the original definition (MissionLib.py), to suit specific needs

	pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
	pSet = pTarget.GetContainingSet()
	if not pSet:
		return None

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)
	if not TGOffset and pShip:
		pTorp.SetTargetOffset(pShip.GetHull().GetPosition())
	else:
		pTorp.SetTargetOffset(TGOffset)
	pTorp.SetParent(pShipID)

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, sTorpName)
	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	kTorpLocation = pTorp.GetWorldLocation()
	kTargetLocation = pTarget.GetWorldLocation()

	kTargetLocation.Subtract(kTorpLocation)
	kFwd = kTargetLocation
	kFwd.Unitize()
	kPerp = kFwd.Perpendicular()
	kPerp2 = App.TGPoint3()
	kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)
	pTorp.AlignToVectors(kFwd, kPerp2)
	pTorp.UpdateNodeOnly()

	# Give the torpedo an appropriate speed.
	kSpeed = CopyVector(kVector)
	kSpeed.Unitize()
	kSpeed.Scale(fSpeed)
	pTorp.SetVelocity(kSpeed)

	return pTorp

#slightly modified MakeEnemyShipList from Mleo's FoundationTech
def MakeEnemyShipObjectList(pShip):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies = pMission.GetFriendlyGroup()
	pNeutrals = pMission.GetNeutralGroup()
	if pFriendlies.IsNameInGroup(pShip.GetName()):
		pEnemyGroup = pFriendlies
	elif pEnemies.IsNameInGroup(pShip.GetName()):
		pEnemyGroup = pEnemies
	elif pNeutrals.IsNameInGroup(pShip.GetName()):
		pEnemyGroup = pNeutrals
	else:
		pEnemyGroup = None

	pPlayer = MissionLib.GetPlayer ()
	pPlayerID = pPlayer.GetObjID()
	lEnemyShips = []
	if pEnemyGroup != None:
		ObjTuple = pEnemyGroup.GetActiveObjectTupleInSet(pPlayer.GetContainingSet())
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:			
					lEnemyShips.append(pObj)

	return lEnemyShips

def GetNextEnemyInSet(pFirstTarget, IsShip=1):
	if IsShip == 1:
		pOldTarget = App.ShipClass_Cast(pFirstTarget)
	else:
		pOldTarget = pFirstTarget
	pEnemyList = MakeEnemyShipObjectList(pOldTarget)
	
	#this might be useless too, but leave it here anyway...
	try:
		if pEnemyList[pEnemyList.index(pOldTarget)]:
			pEnemyList.remove(pOldTarget)
	except:
		pass
	
	#now to the real deal
	EnemyDistDict = {}
	for pShip in pEnemyList:
		#Define the distance and check it after checking if pShip is cloaked
		lDistance = DistanceCheck(pOldTarget, pShip)
		if not pShip.IsCloaked():
			if 0 < lDistance <= 600:
				#To make sure the CRP won't target a ship that is exploding, and then fuck everything up
				pHull = pShip.GetHull()
				if pHull.GetCondition() > 0 and not pShip.IsDying() and not pShip.IsDead():
					#and finally create the {Distance(from pFirstTarget): Enemy} dictionary
					EnemyDistDict[lDistance] = pShip
	#and then check if the dict isn't none
	if EnemyDistDict:
		#took me a while to discover this, but finally it is here and working perfectly!
		pNewTarget = App.ShipClass_Cast(EnemyDistDict[min(EnemyDistDict.keys())])
	else:
		pNewTarget = None
	return pNewTarget

#a distance check, tah dah!!
def DistanceCheck(pObject1, pObject2):
	vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()

# thanks to L_J  ;)
def createParticleStream(pSpaceObject, sTextureFile, fSize, fLength, fVelocity, fAngleVariance = 1.0, fEffectLifeTime = 20.0, fFrequency = 0.01, pLocalPositionOffset = None, pLocalDirection = None, tColourARGB = (255.0, 255.0, 255.0, 255.0)):
	""" 
		args:
			pSpaceObject	- The object in space to attach the stream to.
			sTextureFile	- The texture to display.
			fSize		- The width of the texture as to be shown on screen.
			fLength		- The length of the particle stream. To be more accurate this is the lifetime of each particle.
			fVelocity	- The speed at which to emit.
			fAngleVariance   - This controls how varied the emit stream is (it's in degrees).
			fEffectLifeTime	- The lifetime of the effect.
			fFrequency	- How oftern to emit a new particle.
			pLocalPositionOffset	- A modelspace (local to the ship) offset of where to emit the stream from.
			pLocalDirection		- A modelspace (local to the ship) direction vector for where to "point" the stream.
			tColourARGB	- A tuple or list which contains 4 floats in the format ARGB. These components are between 0 and 1.
		returns:
			A partical stream object.
		
		example:
			One may use the function as below:
			pSequence = App.TGSequence_Create()
			sTexture = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga"
			fShipRadius = pShip.GetRadius()
			pAction = createParticleStream(pShip, sTexture, fShipRadius / 20.0, fShipRadius * 1.5, 10.0, 20.0, 0.01, App.NiPoint3(0.0, 0.0, 0.0),  App.NiPoint3(0.0, -1.0, 0.0), (128.0, 10.0, 255.0, 70.0)
			pSequence.AddAction(pAction)
			pSequence.Play()
	"""
	
	# Parse Arguments.
	if (pLocalPositionOffset is None):
		pLocalPositionOffset = App.TGPoint3()	# these may need to be NIPoint3's.. i can't remember..
	if (pLocalDirection is None):
		pLocalDirection = App.TGPoint3()
	
	# Create a particle stream object.
	pParticleStream = App.AnimTSParticleController_Create()
	
	# Setup Colour maskes on the object. (Brightness, Red, Green, Blue) These components are between 0 and 1.
	# They control the colour of the particle over it's lifetime.
	pParticleStream.AddColorKey(0.1, 1.0, 1.0, 1.0)
	pParticleStream.AddColorKey(tColourARGB[0] / 255.0, tColourARGB[1] / 255.0, tColourARGB[2] / 255.0, tColourARGB[3] / 255.0)
	pParticleStream.AddColorKey(1.0, 0.0, 0.0, 0.0)
	
	# Setup alpha masks.  These are pretty standard and should work pretty nice with your streams.
	pParticleStream.AddAlphaKey(0.0, 1.0)
	pParticleStream.AddAlphaKey(0.7, 0.5)
	pParticleStream.AddAlphaKey(1.0, 0.0)

	# Frontier add: setup size keys? dunno if this will work
	fRandSize = App.g_kSystemWrapper.GetRandomNumber(10) * 0.01
	pParticleStream.AddSizeKey(0.0, 1.0 * fSize + fRandSize)
	pParticleStream.AddSizeKey(1.0, 1.0 * fSize + fRandSize)
	#####	

	# Set Physics Properties.
	pParticleStream.SetEmitVelocity(fVelocity)
	pParticleStream.SetAngleVariance(fAngleVariance) # This controls how varied the emit stream is (it's in degrees).  Try playing with the values. #60.0
	# Frontier add: maybe this is important :P
	pParticleStream.SetEmitRadius(fSize / 4.0)	

	# The life of a particle in the stream.
	pParticleStream.SetEmitLife(fLength)
	
	# How oftern to emit the next particle.
	pParticleStream.SetEmitFrequency(fFrequency)
	
	# How long should the whole effect last.
	pParticleStream.SetEffectLifeTime(fEffectLifeTime)
	
	# Texture File.
	pParticleStream.CreateTarget(sTextureFile)
	
	# These next lines are important because they 
	pParticleStream.SetEmitFromObject(pSpaceObject.GetNiObject())
	pParticleStream.AttachEffect(pSpaceObject.GetContainingSet().GetEffectRoot())
	pParticleStream.SetEmitPositionAndDirection(pLocalPositionOffset, pLocalDirection)
	
	# Make it blend closer to white than black. (for transparency reasons)
	pParticleStream.SetTargetAlphaBlendModes(0, 0)

	# Frontier add: whit this will inherit velocity of parent obj?
	pParticleStream.SetInheritsVelocity(1)	

	return App.EffectAction_Create(pParticleStream)