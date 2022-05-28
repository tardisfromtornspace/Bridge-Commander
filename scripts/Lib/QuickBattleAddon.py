from bcdebug import debug
import App

#######################################################################################################
#	In order to recognize whether a ship has a certain technology we introduce a code, based on the
#	affilliation number (ShipProperty -> Affiliation in the Model Property Editor)
#
#
#	Structure of the AffilationNumber 	
#	YYYYYYYYYYXX are diffent control numbers assigned for various assets as multivectral shielding,
#	ablative armour, breen drain weapon ...
#
#	current reference: AffilationNumber = ...JIHGFEDCBAXX
#	
#	XX: Species number
#		00: Spacial Objects
#		01: Federation
#		02: Romulan
#		03: Klingon
#		04: Cardassian
#		05: Dominion
#		06: Borg
#		07: Kessok
#		08: Coalition
#		09: Breen
#		>09: Open for expansian
#
#	
#	09: (Breen) Drainerweapon
#
#	A: Multivectral Shielding (Type 1 -> positionSelectorShip(pObject,1))
#		0: Off
#		1-9: On
#
#	B:Immune to Drainerweapon
#		0: No
#		1-9: Yes
#	
#	C:Ablative Armour
#		0: No
#		1-9: Yes + A Hull subsystem called "Ablative Armour"
#
#	D: Phase Cloak
#		0: No
#		1-9: Yes
#
#	E:Corbinite Reflector
#		0: No
#		1-9: Yes
#
#   Example: the Coalition Star Destroyer has multivectral shielding, phase cloaking and is immune to the drain weapon:
#		-->(0) (1) (0) (1) (1) (08) = 01001108
#	
#		
########################################################################################################	


#########################################################################################################
#	{Main(pObject, pEvent)}
#
#	Calls the different Utilities
#
#	Args:	pObject -> a ship
#		PEvent  -> triggering Event
#
#
#	Return:	none
#########################################################################################################

def QuickBattleAddonMain(pObject, pEvent , pSet):
	# Called when a weapon hits a target
	debug(__name__ + ", QuickBattleAddonMain")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	multiVectralShields(pShip)
	drainerWeapon(pEvent)
	ablativeArmour(pShip)
	corboniteReflector(pEvent)
	
def QuickBattleAddonMain2(pObject, pEvent):
	# Called when a ship cloaks
	debug(__name__ + ", QuickBattleAddonMain2")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	phaseCloakOn(pShip)

def QuickBattleAddonMain3(pObject, pEvent):
	# Called when a ship decloaks
	debug(__name__ + ", QuickBattleAddonMain3")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	phaseCloakOff(pShip)
	
	

###############################################################################
#	{Utility}
#	
#	The explicit codes for the Utilites
#
#	Return:	none
###############################################################################

	
def multiVectralShields(pShip):
	debug(__name__ + ", multiVectralShields")
	if(positionSelectorShip(pShip,1)>=1.0):   #Check if the ship is scripted to have multivectral shields
		pShields = pShip.GetShields()		
		if (pShields != None):
			pShieldTotal=0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
				pShieldTotal=pShieldTotal+pShields.GetCurShields(ShieldDir)
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShields.SetCurShields(ShieldDir,pShieldTotal/6.0)  		#Redistribute shields equally

def drainerWeapon(pEvent):
	debug(__name__ + ", drainerWeapon")
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())
	
	if(getSpeciesNumber(pAttacker)>=9.0 and getSpeciesNumber(pAttacker)<10.0):		#Check if the attacker is Breen
		if(pEvent.GetDamage()<=5.0):  							#The drainerweapontorpedo is a dummy torpedo with low attack -> recognizable (I tried GetWeaponId() but that didn't work)
			if(positionSelectorShip(pShip,2)<1.0):					#Check if the tartget is immune to the drainerweapon (Klingon, Breen, Coalition (new shipline))
				pPower = pShip.GetPowerSubsystem()
				pProp = pPower.GetProperty()
				pProp.SetPowerOutput(0.0)					#Warp Core doesn't produce a single Watt anymore
												#Only the batteries hold for a short time
				
				pShields = pShip.GetShields()					#Bye, shields
				for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
					pShields.SetCurShields(ShieldDir,0.0)

def ablativeArmour(pShip):
	debug(__name__ + ", ablativeArmour")
	if(positionSelectorShip(pShip,3)>=1.0): 						#Check if the ship is scripted to have Ablative Armour
			repair=0		
			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			while (pSubsystem != None):
				if(pSubsystem.GetName()=="Ablative Armour"):			#The ship needs to have a Hull property with the name "Ablative Armour", which isn't destroyed !!!
					if(pSubsystem.GetCondition()>0.0):
						repair=1
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			pShip.EndGetSubsystemMatch(pIterator)
	
			if(repair==1):
				# Repair everything instantly except the ablative armour property

				pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				while (pSubsystem != None):
					if(pSubsystem.GetName() != "Ablative Armour"):
						if(pSubsystem.GetCondition()>0.0):
							pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
							iChildren = pSubsystem.GetNumChildSubsystems()
							if (iChildren > 0):
								for iIndex in range(iChildren):
									pChild = pSubsystem.GetChildSubsystem(iIndex)
									pChild.SetCondition(pChild.GetMaxCondition())
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				pShip.EndGetSubsystemMatch(pIterator)
			
			

def phaseCloakOn(pShip):						#Check if the ship is scripted to have Phase Cloak
	# work around crash in DamageableObject_Cast
	pShip = App.ObjectClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return
	if(positionSelectorShip(pShip,4)>=1.0):
		debug(__name__ + ", phaseCloakOn")
		App.DamageableObject_Cast(pShip).SetCollisionsOn(0)	#Set collisions off, so simple !!!

def phaseCloakOff(pShip):
	# work around crash in DamageableObject_Cast
	pShip = App.ObjectClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return
	debug(__name__ + ", phaseCloakOff")
	App.DamageableObject_Cast(pShip).SetCollisionsOn(1)		#Set collisions on, so simple !!!


def corboniteReflector(pEvent):
	debug(__name__ + ", corboniteReflector")
	pShip=App.ShipClass_Cast(pEvent.GetDestination())	
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())

	powerTest(pAttacker,0.15)

	if(positionSelectorShip(pShip,5)>=1.0):				#Check if the ship is scripted to have the Reflector
		if(pEvent.GetWeaponType()==App.WeaponHitEvent.TORPEDO):	#Check if the weapon is a torpedo
			if(pEvent.IsHullHit()==1):			#If the hull is hit, the shields are failing, so they cannot reflect
				return (0)
				
			else:
				powerTest(pAttacker,0.95)

				pSet=pAttacker.GetContainingSet()			
						
				kVect0=pAttacker.GetWorldLocation()
			
				kVectNiWorldHitPoint=pEvent.GetWorldHitPoint()		#Determine where the torpedo struck the shields
				kVectNiWorldHitNormal=pEvent.GetWorldHitNormal()
								
				kVectWorldHitPoint=App.TGPoint3()			#The "above "crap functions" give some more basic form of a vector that needed be to converted (costed me a lot of time to figure out)
				kVectWorldHitPoint.SetX(kVectNiWorldHitPoint.x)
				kVectWorldHitPoint.SetY(kVectNiWorldHitPoint.y)
				kVectWorldHitPoint.SetZ(kVectNiWorldHitPoint.z)

				kVectWorldHitNormal=App.TGPoint3()
				kVectWorldHitNormal.SetX(kVectNiWorldHitNormal.x)
				kVectWorldHitNormal.SetY(kVectNiWorldHitNormal.y)
				kVectWorldHitNormal.SetZ(kVectNiWorldHitNormal.z)
				n=kVectWorldHitNormal
				n.Unitize()

				powerTest(pAttacker,0.9)

				#Not for novices in mathematics, the following part:
				# u= vector of approach
				# n= normal vector on the shieldgrid
				#
				#(1) 	The reflected vector r is parallel the plane alpha(u,n)
				#	r // alpha(u,n)
				#(2)	The reflected vector r is must form the same angle with n as u does
				#	(u^n) = (n^r)
				#
				#(S1)	In alpha(u,n) choose a vector m perpendular on n
				#	m =(u X n) X n	(property of the double cross product)
				#
				#(S2)	If the reflected vector r must form the same angle with n as u does,
				#	then it needs to have the same n-component in its (n,m) decomposition (still following?) as r,
				#	while the m-component in its (n,m) decomposition must be the negative.
				#	
				#	u = a * n + b * m	-->	r = a * n - b * m	(a,b) the (n,m) decompositionfactors of u
				#
				#(S3)	a and b are determinated by the projections on n and m of u
				#	a = (u.n) 
				#	b = (u.m) 
				#
				#	-> r = (u.n) n - (u.m) m

					
				u=kVect0				
				u.Subtract(kVectWorldHitPoint)
				u.Unitize()

				a=u.Dot(n)
				m0=u.Cross(n)
				m=m0.Cross(n)
				b=u.Dot(m)
			
				n.Scale(a)
				m.Scale(b)
				n.Subtract(m)

				r=n

				# From this point on it goes wrong, to get the path of the fired torpedo/disruptor (eg tactical.projectiles.DomCannon2)
				# I need to get/cast the fired weapon from the WeaponHitEvent,
				# once this is achieved I can get the path ( with  GetModuleName() ) from the torpedo.
				# Getting the exact weapon from the WeaponHitEvent using both GetWeaponInstanceID() or GetWeaponType()
				# failed	
	
				pTorpID=pEvent.GetWeaponInstanceID()
			
				pTorpPath="Void"

				try:
					pTorp=App.Torpedo_Cast(App.Torpedo_GetObjectByID(pTorpID))
					pTorpPath=pTorp.GetModuleName()
				except:
					try:
						pTorp=App.PulseWeapon_Cast(App.Torpedo_GetObjectByID(pTorpID))
						pTorpPath=pTorp.GetModuleName()
					except:
						pTorpPath="Tactical.Projectiles.PhotonTorpedo2"

				# Luckily I found this definition in MissionLib.py
			
				FireTorpFromPoint(kVectWorldHitPoint,r,pTorpPath,pAttacker.GetObjID(),pShip)

				
				

##############################################################################
#	{Tools}
#	
#	The explicit codes for the the Tools used by {Utilities}
#	
#	Return:	various
###############################################################################

def positionSelectorShip(pShip,p):	
	#Selects a single number from ....JIHGFEDCBA(XX)  with A,1 B,2 C,3 ... J,10 ...
	debug(__name__ + ", positionSelectorShip")
	a=pShip.GetAffiliation()
	n=0.0
	if(a>99):
		n=positionSelector(a,p+2)
	return n

def getSpeciesNumber(pShip):
	debug(__name__ + ", getSpeciesNumber")
	a=pShip.GetAffiliation()
	if(a>99):
		a =10.0*positionSelector(a,2)
	return a

def positionSelector(a,p):
	#A tricky algorithm that requires some insights in mathematics,
	#
	# (1) 	We do a integer division (with a rest) of a=...JIHGFEDCBAXX with ten^(p) to drop the (p) less significant decimals
	#	eg.	...JIHGFEDCBAXX --->	...JIHGFEDC,BAXX - ...JIHGFEDC,0000   ----> ...000,BAXX
	#
	# (2)	We get the disired number (in the example = B) by multiplying the previous number with then
	#	eg.	...000,BAXX * 10-> ...000B,AXX
	# (3)	In the comparisons we must work with < and > instead of ==
	

	debug(__name__ + ", positionSelector")
	n=(((a*1.0)/(pow(10,p)*1.0))-(a/pow(10,p)))*10.0
	
	return n

def pow(x,y):	
	#BC Python lacks the pow so I need to declare it explicitely
	debug(__name__ + ", pow")
	n=x
	i=1
	if(y<0):
		n=0
	if(y==0):
		n=1
	while((y-i)>0):
		n=n*x
		i=i+1
	return n


def powerTest(pShip,a):
	#Just for debugging, to see how far a def goes without errors
	debug(__name__ + ", powerTest")
	if(a<0 or a>1):
		a=0.5
	pPower = pShip.GetPowerSubsystem()
	if (pPower != None):
		pPower.SetMainBatteryPower(a*pPower.GetMainBatteryLimit())
		pPower.SetBackupBatteryPower(a*pPower.GetBackupBatteryLimit())


def FireTorpFromPoint(kPoint,kNormal,pcTorpScriptName, idTarget ,pShip,idTargetSubsystem = App.NULL_ID,fSpeed = 0.0,pcSetName = None):

	# This is an slightly altered version of the original definition (MissionLib.py) , to suit specific needs

	debug(__name__ + ", FireTorpFromPoint")
	pTarget = App.ObjectClass_GetObjectByID(App.SetClass_GetNull(), idTarget)

	if (pcSetName != None):
		pSet = App.g_kSetManager.GetSet(pcSetName)
	elif (pTarget != None):
		pSet = pTarget.GetContainingSet()
	else:
		# No idea what set this is supposed to be in.
		return 0

	if (pSet == None):
		# No set.
		return 0

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)

	if (idTargetSubsystem != App.NULL_ID):
		pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(idTargetSubsystem))
		if (pSubsystem != None):
			pTorp.SetTargetOffset(pSubsystem.GetPosition())
		else:
			pTorp.SetTargetOffset(kPoint)
	else:
		pTorp.SetTargetOffset(kPoint)

	
	pTorp.SetParent(pShip.GetObjID())

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)

	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	if (pTarget != None):
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kFwd = kNormal
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()

	# Give the torpedo an appropriate speed.
	kVelocity = pTorp.GetWorldForwardTG()
	kVelocity.Unitize()
	if (fSpeed == 0.0):
		kVelocity.Scale(pTorp.GetLaunchSpeed())
	else:
		kVelocity.Scale(fSpeed)

	pTorp.SetVelocity(kVelocity)

	return 0



