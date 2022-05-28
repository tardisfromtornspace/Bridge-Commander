# This makes sure nobody gets fussy because they just downgraded. ;)
import Foundation

def BridgeSetLocation(locationName, kAM, pSequence, pAnimNode):
	if Foundation.pCurrentBridge:
		return Foundation.pCurrentBridge.SetLocation(locationName, kAM, pSequence, pAnimNode)
	return None


#########################################################
# Bridge-related definitions

class BridgeDef(Foundation.MutatorElementDef):

	def __init__(self, name, bridgeString, dict = {}):
		self.bridgeString = bridgeString
		self.num = Foundation.bridgeList.Register(self, name)

		# This is a touch risky but I foresee no problem - Dasher42
		Foundation.bridgeList._keyList[bridgeString] = self

		self.locations = None
		if dict.has_key('locations'):
			self.locations = dict['locations']
			# print 'Updating locations', name, self, self.locations, dict.keys()
		Foundation.MutatorElementDef.__init__(self, name, dict)

	def AddToMutator(self, toMode):
		toMode.bridgeList.Register(self, self.name)
		toMode.elements.append(self)

	def SetLocation(self, locationName, kAM, pSequence, pAnimNode):
		try:
			loc = self.locations[locationName]
			import App
			kAM.LoadAnimation(loc[0], loc[1])
			pSequence.AppendAction(App.TGAnimPosition_Create(pAnimNode, loc[1]))
			for i in range(2, len(loc)):
				try:
					exec(loc[i])
				except SyntaxError:
					raise SyntaxError, evalStr
			return 1
		except:
			pass
		return None


def Initialize(bTestFlag = 0):
	if not Foundation.bInitialized:

		import StaticDefs

		if bTestFlag != 0:
			bTesting = 1

		Foundation.LoadExtraShips()
		Foundation.LoadExtraPlugins()

# print int(Foundation.version)

#if int(Foundation.version[0:8]) < 20030221:
	# print 'Outdated Foundation, updating functions'
Foundation.BridgeSetLocation = BridgeSetLocation

Foundation.Initialize = Initialize
Foundation.bInitialized = 0


Foundation.pCurrentBridge = None
Foundation.version = '20030221'
Foundation.BridgeDef = BridgeDef

mode = Foundation.MutatorDef.QuickBattle

import Registry

tempList = Foundation.bridgeList
Foundation.bridgeList = Registry.Registry()
for i in tempList._keyList.values():
        # print i.name
        BridgeDef(i.name, i.bridgeString, dict = { 'modes': [ mode  ] } )

Foundation.OverrideDef('FixSetPosition', 'Bridge.Characters.CommonAnimations.SetPosition', 'Fixes20030217.SetPosition', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef('FixLoadBridge', 'LoadBridge.Load', 'Fixes20030217.LoadBridge_Load', dict = { 'modes': [ mode ] } )
#else:
#	del Initialize
#	del BridgeDef
#	del BridgeSetLocation
