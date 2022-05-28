# Foundation Triggers Extension 20030305 for Bridge Commander
# Written March 5, 2003 by Daniel B. Rollings AKA Dasher42, all rights reserved.


import Foundation

if int(Foundation.version[0:8]) < 20030305:

	import FoundationTriggers
	import App
	import Registry

	print 'Outdated Foundation, updating functions'


	class ListenerDef:
		def __init__(self, funcs):
			self.funcs = funcs

		def __call__(self, pObject, pEvent):
			for i in self.funcs:
				i(pObject, pEvent)


	class TriggerDef(Foundation.OverrideDef):
		def __init__(self, name, eventKey, dict = {}):
			self.eventKey = eventKey

			self.sourceMask = long(0)
			self.destMask = long(0)
			self.fireMask = long(0)
			self.targetMask = long(0)

			Foundation.OverrideDef.__init__(self, name, None, None, dict)

		def _SwapInModules(self, pre, post):				pass
		def _SwapOutModules(self, pre, post):				pass

		def __call__(self, pObject, pEvent, dict = {}):
			pass

		def MakeListener(self):
			return Foundation.ListenerDef([ self ])

		def Activate(self):
			key = str(self.eventKey)
			#print 'Registering listener', self.name, 'FoundationTriggers.' + key
			if not FoundationTriggers.__dict__.has_key(key):
				FoundationTriggers.__dict__[key] = self.MakeListener()
				pTopWindow = App.TopWindow_GetTopWindow()
				pWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
				if pWindow:
					App.g_kEventManager.AddBroadcastPythonFuncHandler(self.eventKey, pWindow, 'FoundationTriggers.' + str(key))
			else:
				FoundationTriggers.__dict__[key].funcs.append(self)

			#print FoundationTriggers.__dict__.keys()

		def Deactivate(self):
			key = str(self.eventKey)

			#print FoundationTriggers.__dict__.keys()

			#print 'Removing listener', self.name
			try:
				FoundationTriggers.__dict__[key].funcs.remove(self)
				if not len(FoundationTriggers.__dict__[key].funcs):
					pTopWindow = App.TopWindow_GetTopWindow()
					pWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
					App.g_kEventManager.RemoveBroadcastHandler(self.eventKey, pWindow, 'FoundationTriggers.' + str(key))
					del FoundationTriggers.__dict__[key]
			except:
				pass

	# WeaponHit
	# 	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	#	pTorp = App.Torpedo_Cast(pEvent.GetSource())
	# 	pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())

	#		kVectNiWorldHitPoint=pEvent.GetWorldHitPoint()		#Determine where the torpedo struck the shields

	# 	fDamage=pEvent.GetDamage()*0.9	#The power to reflect the weapon causes damage, 10% of the original damage

	# pTargetShip = App.ShipClass_Cast(pEvent.GetTargetObject())

	# sneakSize = pEvent.GetRadius()

	# pModuleName=pTorp.GetModuleName()

	sList = Foundation.shipList._keyList

	class MaskListenerDef:
		def __init__(self, funcs):
			self.funcs = funcs

		def __call__(self, pObject, pEvent):
			pShip = App.ShipClass_Cast(pEvent.GetDestination())
			pTorp = App.Torpedo_Cast(pEvent.GetSource())
			pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())

			iAttackerMask = 0

			iShipMask = sList[pShip.GetName()]._pMask
			iTorpMask = pTorp.GetModuleName()
			if pAttacker:	iAttackerMask = sList[pAttacker.GetName()]._pMask

			for i in self.funcs:
				if i.destMask and not iShipMask & i.destMask:		continue
				if i.sourceMask and not iTorpMask & i.sourceMask:	continue
				if i.fireMask and not iAttackerMask & i.fireMask:	continue

				i(pObject, pEvent)




	Foundation.propertyList = Registry.Registry()
	pList = Foundation.propertyList		# We're going to be looking this up a lot, so let's
										# not do lots of namespace lookups


	class PropertyDef:
		def __init__(self, name, triggers, dict = {}):
			self.name = name
			self.triggers = triggers
			self.mask = long(1 << pList.Register(self, name))

		def Add(self, target):
			if not target.__dict__.has_key('_pList'):
				target._pList = [ self ]
				target._pMask = self.mask
			else:
				target._pList.append(self)
				target._pMask = target._pMask | self.mask

		def Remove(self, target):
			target._pList.remove(self)
			target._pMask = target._pMask ^ self.mask





	Foundation.TriggerDef = TriggerDef
	Foundation.ListenerDef = ListenerDef
	Foundation.PropertyDef = PropertyDef

	Foundation.version = '20030221p'

