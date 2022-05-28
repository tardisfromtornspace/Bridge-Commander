from bcdebug import debug
# 2009 by Defiant for KM, but should work on all installations
# see http://bckobayashimaru.de/phpBB3/viewtopic.php?f=30

import App
import sys
import cPickle
#import pickle
from bcdebug import debug

VERSION = "201109200000"


NonSerializedObjects = (
"DamageableObject_CastOrig",
"DisableGlowAlphaMapsOrig",
"GetRandomPointOnModelOrig",
"GetLocalRandomPointAndNormalOnModelOrig",
"GetRandomNumberOrig",
"AddDamageOrig",
"TurnOffOrig",
"TurnOnOrig",
"TurnOrig",
"SetGlowMapsEnabledOrig",
"AddActionOrig",
"SequenceAbortOrig",
"DeleteObjectFromSetOrig",
"CodeConditionSetStatusOrig",
"cPickle_PicklerOrig",
)


def init():
	debug(__name__ + ", init")
	sys._getframe = _getframe

	global DamageableObject_CastOrig
	DamageableObject_CastOrig = App.DamageableObject_Cast
	App.DamageableObject_Cast = DamageableObject_Cast

	global DisableGlowAlphaMapsOrig
	DisableGlowAlphaMapsOrig = App.DamageableObject.DisableGlowAlphaMaps
	App.DamageableObject.DisableGlowAlphaMaps = DisableGlowAlphaMaps
	
	global GetRandomPointOnModelOrig
	GetRandomPointOnModelOrig = App.ObjectClass.GetRandomPointOnModel
	App.ObjectClass.GetRandomPointOnModel = GetRandomPointOnModel
	
	global GetLocalRandomPointAndNormalOnModelOrig
	GetLocalRandomPointAndNormalOnModelOrig = App.ObjectClass.GetLocalRandomPointAndNormalOnModel
	App.ObjectClass.GetLocalRandomPointAndNormalOnModel = GetLocalRandomPointAndNormalOnModel
	
	global GetRandomNumberOrig
	GetRandomNumberOrig = App.g_kSystemWrapper.GetRandomNumber
	App.g_kSystemWrapper.GetRandomNumber = GetRandomNumber

	global AddDamageOrig
	AddDamageOrig = App.DamageableObject.AddDamage
	App.DamageableObject.AddDamage = AddDamage
	
	global TurnOffOrig
	TurnOffOrig = App.PoweredSubsystem.TurnOff
	App.PoweredSubsystem.TurnOff = TurnOff
	
	global TurnOnOrig
	TurnOnOrig = App.PoweredSubsystem.TurnOn
	App.PoweredSubsystem.TurnOn = TurnOn

	global TurnOrig
	TurnOrig = App.PoweredSubsystem.Turn
	App.PoweredSubsystem.Turn = Turn
	
	global SetGlowMapsEnabledOrig
	SetGlowMapsEnabledOrig = App.LODModelManager.SetGlowMapsEnabled
	App.LODModelManager.SetGlowMapsEnabled = SetGlowMapsEnabled
	
	global AddActionOrig
 	AddActionOrig = App.TGSequence.AddAction
	App.TGSequence.AddAction = AddAction
	
	global SequenceAbortOrig
 	SequenceAbortOrig = App.TGAction.Abort
	App.TGAction.Abort = SequenceAbort

	global DeleteObjectFromSetOrig
	DeleteObjectFromSetOrig = App.SetClass.DeleteObjectFromSet
	App.SetClass.DeleteObjectFromSet = DeleteObjectFromSet

	global CodeConditionSetStatusOrig
	CodeConditionSetStatusOrig = App.TGCondition.SetStatus
	App.TGCondition.SetStatus = CodeConditionSetStatus

	#global cPickle_PicklerOrig
	#cPickle_PicklerOrig = cPickle.Pickler
	#cPickle.Pickler = cPickle_Pickler


def DamageableObject_Cast(pObject):
	debug(__name__ + ", DamageableObject_Cast")
	pObject = App.ObjectClass_GetObjectByID(None, pObject.GetObjID())
	if pObject:
		return DamageableObject_CastOrig(pObject)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def DisableGlowAlphaMaps(pObject):
	debug(__name__ + ", DisableGlowAlphaMaps")
	pObject = App.DamageableObject_GetObjectByID(None, pObject.GetObjID())
	if pObject and not pObject.IsDead():
		return DisableGlowAlphaMapsOrig(pObject)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def GetRandomPointOnModel(pObject):
	# this is probably a ship
	debug(__name__ + ", GetRandomPointOnModel")
	pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
	if pShip:
		if pShip.IsDead():# or pShip.IsDying():
			#print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)
			return
		elif pShip.IsDying():
			debug(__name__ + ", GetRandomPointOnModel IsDying - Might result in crash!")
			#print(__name__ + ", GetRandomPointOnModel IsDying - Might result in crash!")
	# not a ship or not dead
	pObject = App.ObjectClass_GetObjectByID(None, pObject.GetObjID())
	if pObject:
		return GetRandomPointOnModelOrig(pObject)
	#print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def GetLocalRandomPointAndNormalOnModel(pObject):
	debug(__name__ + ", GetLocalRandomPointAndNormalOnModel")
	print "Broken function GetLocalRandomPointAndNormalOnModel: Don't use it!"
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)
	return


def GetRandomNumber(i):
	debug(__name__ + ", GetRandomNumber")
	if i > 0:
		return GetRandomNumberOrig(i)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)
	return 0


def AddDamage(pObject, vEmitPos, fRadius, fDamage):
	debug(__name__ + ", AddDamage")
	pObject = App.DamageableObject_GetObjectByID(None, pObject.GetObjID())
	if pObject and vEmitPos:
		return AddDamageOrig(pObject, vEmitPos, fRadius, fDamage)
	#print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def TurnOff(pSubsystem):
	debug(__name__ + ", TurnOff")
	pShip = pSubsystem.GetParentShip()
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShip.GetObjID())
	if pShip:
		return TurnOffOrig(pSubsystem)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def TurnOn(pSubsystem):
	debug(__name__ + ", TurnOn")
	pShip = pSubsystem.GetParentShip()
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShip.GetObjID())
	if pShip:
		return TurnOnOrig(pSubsystem)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def Turn(pSubsystem, bTurn):
	debug(__name__ + ", Turn")
	pShip = pSubsystem.GetParentShip()
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShip.GetObjID())
	if pShip:
		return TurnOrig(pSubsystem, bTurn)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def SetGlowMapsEnabled(self, bSet):
	debug(__name__ + ", SetGlowMapsEnabled")
	if App.g_kLODModelManager.GetDropLODLevel() == 0:
		return SetGlowMapsEnabledOrig(self, bSet)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def AddAction(self, pAction1, pAction2 = App.TGAction_CreateNull(), ftime=0.0):
	debug(__name__ + ", AddAction")
	if pAction1:
		return AddActionOrig(self, pAction1, pAction2, ftime)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def SequenceAbort(pSequence):
	debug(__name__ + ", SequenceAbort")
	if pSequence.IsPlaying():
		SequenceAbortOrig(pSequence)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


def DeleteObjectFromSet(pSet, sName):
	debug(__name__ + ", DeleteObjectFromSet")
	return pSet.RemoveObjectFromSet(sName)


def CodeConditionSetStatus(pCondition, bStatus):
	debug(__name__ + ", CodeConditionSetStatus")
	pCondition = App.ConditionScript_Cast(App.TGObject_GetTGObjectPtr(pCondition.GetObjID()))
	if pCondition:
		return CodeConditionSetStatusOrig(pCondition, bStatus)
	print "Crash avoided; Please fix %s"  % (sys._getframe(1).f_code.co_name)


#class cPickle_Pickler(pickle.Pickler):
#	def __init__(self, file, bin = 0):
#		debug(__name__ + ", __init__")
#		pickle.Pickler.__init__(self, 4, bin)
#
#	def dump(self, object):
#		debug(__name__ + ", dump")
#		try:
#			pickle.Pickler.dump(self, object)
#		except:
#			print "dump", object, type(object)
#			print "fail"
#			raise


# http://code.activestate.com/recipes/66062/
# http://code.activestate.com/recipes/52315/
def _getframe(level=0):
    debug(__name__ + ", _getframe")
    try:
        1/0
    except:
        tb = sys.exc_info()[-1]
    frame = tb.tb_frame
    while level >= 0:
        frame = frame.f_back
        level = level - 1
    return frame

init()
