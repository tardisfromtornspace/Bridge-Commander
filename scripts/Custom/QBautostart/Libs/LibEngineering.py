from bcdebug import debug
# Engineering Lib
# Functions:
#  - CreateMenuButton(ButtonName, Person, Function, EventInt = 0)
#       ButtonName is a String, like "Goto Engineering"
#       Person maybe Engineer, XO, Helm, Tactical and Science.
#       Function, set it like __name__ + ".myFunc"
#  - CreateFriendlyAI(pShip)
#  - CreateEnemyAI(pShip)
#  - CreateStarbaseFriendlyAI(pShip)
#  - CreateStarbaseEnemyAI(pShip)
#  - GetEngineeringNextEventType() - hopefully returns a clean event type
#  - CreateInfoBox(String) - Creates a little popup window with String
#  - GetButton(ButtonName, pMenu) - Find a Button in a Menu

import App
import MissionLib
import nt
import Foundation
import Custom.Autoload.LoadEngineeringExtension


# The stuff here will create a Button
def CreateMenuButton(ButtonName, Person, Function, EventInt = 0, ToButton = None, Method = "prepend"):
        debug(__name__ + ", CreateMenuButton")
        pMenu = GetBridgeMenu(Person)
        ET_EVENT = App.Mission_GetNextEventType()

        #pMission = MissionLib.GetMission()
        #App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_EVENT, pMission, Function)
        pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pMenu)
        pEvent.SetInt(EventInt)
        pButton = App.STButton_CreateW(App.TGString(ButtonName), pEvent)
    
        if ToButton:
                pAddToMenu = ToButton
        else:
                pAddToMenu = pMenu
        
        if Method == "append":
                pAddToMenu.AddChild(pButton)
        else:
                pAddToMenu.PrependChild(pButton)

        return pButton


def GetBridgeMenu(Person):
        debug(__name__ + ", GetBridgeMenu")
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	if not pTacticalControlWindow:
		print "Error: No Tactical Control Window"
		return None
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString(Person))
        App.g_kLocalizationManager.Unload(pDatabase)
        return pMenu


# Support for mldaalders key foundation
# valid Types for Group: General, Menu, Ship, Camera
# valid Types for eType: App.KeyboardBinding.GET_EVENT, App.KeyboardBinding.GET_INT_EVENT,
#                       App.KeyboardBinding.GET_BOOL_EVENT, App.KeyboardBinding.GET_FLOAT_EVENT
def AddKeyBind(KeyName, Function, EventInt = 0, Group = "General", eType = App.KeyboardBinding.GET_INT_EVENT):
	debug(__name__ + ", AddKeyBind")
	if not hasattr(Foundation, "g_kKeyBucket"):
		return
        mode = Custom.Autoload.LoadEngineeringExtension.mode
        pMission = MissionLib.GetMission()
        #ET_KEY_EVENT = App.Mission_GetNextEventType()
        ET_KEY_EVENT = GetEngineeringNextEventType()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_KEY_EVENT, pMission, Function)
        Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig(KeyName, KeyName, ET_KEY_EVENT, eType, EventInt, Group, dict = {"modes": [mode]}))
        

def CheckActiveMutator(MutatorName):
        debug(__name__ + ", CheckActiveMutator")
        Foundation.LoadConfig()
	for i in Foundation.mutatorList._arrayList:
		fdtnMode = Foundation.mutatorList._keyList[i]
		if fdtnMode.IsEnabled() and (fdtnMode.name == MutatorName):
			return 1
	return 0


# Find a Button in Menu
def GetButton(ButtonName, pMenu):
    debug(__name__ + ", GetButton")
    kString = App.TGString()

    # cycle all Buttons
    curButton = pMenu.GetFirstChild()
    while (curButton != None):
        if curButton:
            curButtonattr = App.STButton_Cast(curButton)
            if not curButtonattr:
                curButtonattr = App.STMenu_Cast(curButton)
            if curButtonattr:
                curButtonattr.GetName(kString)
                if (kString.GetCString() == ButtonName):
                    return curButtonattr
        curButton = pMenu.GetNextChild(curButton)


# broken in Bridge Commander? Looks like the game gives the same event type away several times.
# Fix arround that
def GetEngineeringNextEventType():
    debug(__name__ + ", GetEngineeringNextEventType")
    return App.Mission_GetNextEventType() #+ 333
    #return App.UtopiaModule_GetNextEventType()


# Create an Info Box, Basics from mainmenu.py
def CreateInfoBox(String):
    debug(__name__ + ", CreateInfoBox")
    ET_BOX_OKAY = GetEngineeringNextEventType()
    
    pTopWindow = App.TopWindow_GetTopWindow()
    pDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))
    
    if (pDialogWindow):
        # Create a okay and cancel events
        pOkayEvent = App.TGIntEvent_Create()
        pOkayEvent.SetEventType(ET_BOX_OKAY)
        pOkayEvent.SetDestination(pDialogWindow)
        
        pTitle = App.TGString("Engineering Extension Info Box")		
        pOkay = App.TGString("OK")
        pText = App.TGString(String)

        pDialogWindow.Run(pTitle, pText, pOkay, pOkayEvent, None, None)


# Set Friendly AI
def CreateFriendlyAI(pShip):
        debug(__name__ + ", CreateFriendlyAI")
        pEnemies        = MissionLib.GetEnemyGroup()
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (194, 57)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pEnemies, Difficulty = 1, FollowTargetThroughWarp=1, UseCloaking=1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 1, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (41, 304)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWait)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles


def CreateEnemyAI(pShip):
        debug(__name__ + ", CreateEnemyAI")
        pFriendlies     = MissionLib.GetFriendlyGroup()
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pFriendlies, Difficulty = 1, FollowTargetThroughWarp = 1, UseCloaking = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PlainAI Turn at (237, 47)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (353, 55)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (429, 103)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (448, 147)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (198, 181)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (309, 185)
	pFlyPointlessly.AddAI(pTurn)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating SequenceAI RepeatForever at (195, 224)
	pRepeatForever = App.SequenceAI_Create(pShip, "RepeatForever")
	pRepeatForever.SetInterruptable(1)
	pRepeatForever.SetLoopCount(-1)
	pRepeatForever.SetResetIfInterrupted(1)
	pRepeatForever.SetDoubleCheckAllDone(1)
	pRepeatForever.SetSkipDormant(0)
	# SeqBlock is at (295, 228)
	pRepeatForever.AddAI(pFlyPointlessly)
	# Done creating SequenceAI RepeatForever
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (30, 228)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 235)
	pPriorityList.AddAI(pAttack, 1)
	pPriorityList.AddAI(pRepeatForever, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (29, 285)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 1, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAvoidObstacles)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def CreateStarbaseFriendlyAI(pShip):
        debug(__name__ + ", CreateStarbaseFriendlyAI")
        pEnemies        = MissionLib.GetEnemyGroup()
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 1, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def CreateStarbaseEnemyAI(pShip):
        debug(__name__ + ", CreateStarbaseEnemyAI")
        pFriendlies     = MissionLib.GetFriendlyGroup()
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pFriendlies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 1, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def GetMd5(filename):
        debug(__name__ + ", GetMd5")
        file = nt.open(filename, nt.O_CREAT)
        mdsum = MD5new()
        readBytes = 1024
        while(readBytes):
                readString = nt.read(file, 1024)
                mdsum.update(readString)
                readBytes = len(readString)
        nt.close(file)
        return mdsum.hexdigest()


"""A sample implementation of MD5 in pure Python.

This is an implementation of the MD5 hash function, as specified by
RFC 1321, in pure Python. It was implemented using Bruce Schneier's
excellent book "Applied Cryptography", 2nd ed., 1996.

Surely this is not meant to compete with the existing implementation
of the Python standard library (written in C). Rather, it should be
seen as a Python complement that is more readable than C and can be
used more conveniently for learning and experimenting purposes in
the field of cryptography.

This module tries very hard to follow the API of the existing Python
standard library's "md5" module, but although it seems to work fine,
it has not been extensively tested! (But note that there is a test
module, test_md5py.py, that compares this Python implementation with
the C one of the Python standard library.

BEWARE: this comes with no guarantee whatsoever about fitness and/or
other properties! Specifically, do not use this in any production
code! License is Python License!

Special thanks to Aurelian Coman who fixed some nasty bugs!

Dinu C. Gherman
"""


__date__    = '2001-10-1'
__version__ = 0.9


#import struct, string, copy
import struct, string

# ======================================================================
# Bit-Manipulation helpers
#
#   _long2bytes() was contributed by Barry Warsaw
#   and is reused here with tiny modifications.
# ======================================================================

def _long2bytes(n, blocksize=0):
    """Convert a long integer to a byte string.

    If optional blocksize is given and greater than zero, pad the front
    of the byte string with binary zeros so that the length is a multiple
    of blocksize.
    """

    # After much testing, this algorithm was deemed to be the fastest.
    s = ''
    pack = struct.pack
    while n > 0:
        ### CHANGED FROM '>I' TO '<I'. (DCG)
        s = pack('<I', n & 0xffffffffL) + s
        ### --------------------------
        n = n >> 32

    # Strip off leading zeros.
    for i in range(len(s)):
        if s[i] <> '\000':
            break
    else:
        # Only happens when n == 0.
        s = '\000'
        i = 0

    s = s[i:]

    # Add back some pad bytes. This could be done more efficiently
    # w.r.t. the de-padding being done above, but sigh...
    if blocksize > 0 and len(s) % blocksize:
        s = (blocksize - len(s) % blocksize) * '\000' + s

    return s


def _bytelist2long(list):
    "Transform a list of characters into a list of longs."

    imax = len(list)/4
    hl = [0L] * imax

    j = 0
    i = 0
    while i < imax:
        b0 = long(ord(list[j]))
        b1 = (long(ord(list[j+1]))) << 8
        b2 = (long(ord(list[j+2]))) << 16
        b3 = (long(ord(list[j+3]))) << 24
        hl[i] = b0 | b1 |b2 | b3
        i = i+1
        j = j+4

    return hl


def _rotateLeft(x, n):
    "Rotate x (32 bit) left n bits circularly."

    return (x << n) | (x >> (32-n))


# ======================================================================
# The real MD5 meat...
#
#   Implemented after "Applied Cryptography", 2nd ed., 1996,
#   pp. 436-441 by Bruce Schneier.
# ======================================================================

# F, G, H and I are basic MD5 functions.

def F(x, y, z):
    return (x & y) | ((~x) & z)

def G(x, y, z):
    return (x & z) | (y & (~z))

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | (~z))


def XX(func, a, b, c, d, x, s, ac):
    """Wrapper for call distribution to functions F, G, H and I.

    This replaces functions FF, GG, HH and II from "Appl. Crypto.
    Rotation is separate from addition to prevent recomputation
    (now summed-up in one function).
    """

    res = 0L
    res = res + a + func(b, c, d)
    res = res + x 
    res = res + ac
    res = res & 0xffffffffL
    res = _rotateLeft(res, s)
    res = res & 0xffffffffL
    res = res + b

    return res & 0xffffffffL


class MD5:
    "An implementation of the MD5 hash function in pure Python."

    def __init__(self):
        debug(__name__ + ", __init__")
        "Initialisation."
        
        # Initial 128 bit message digest (4 times 32 bit).
        self.A = 0L
        self.B = 0L
        self.C = 0L
        self.D = 0L
        
        # Initial message length in bits(!).
        self.length = 0L
        self.count = [0, 0]

        # Initial empty message as a sequence of bytes (8 bit characters).
        self.input = []

        # Length of the final hash (in bytes).
        self.HASH_LENGTH = 16
         
        # Length of a block (the number of bytes hashed in every transform).
        self.DATA_LENGTH = 64

        # Call a separate init function, that can be used repeatedly
        # to start from scratch on the same object.
        self.init()


    def init(self):
        debug(__name__ + ", init")
        "Initialize the message-digest and set all fields to zero."

        self.length = 0L
        self.input = []

        # Load magic initialization constants.
        self.A = 0x67452301L
        self.B = 0xefcdab89L
        self.C = 0x98badcfeL
        self.D = 0x10325476L


    def _transform(self, inp):
        """Basic MD5 step transforming the digest based on the input.

        Note that if the Mysterious Constants are arranged backwards
        in little-endian order and decrypted with the DES they produce
        OCCULT MESSAGES!
        """

        a, b, c, d = A, B, C, D = self.A, self.B, self.C, self.D

        # Round 1.

        S11, S12, S13, S14 = 7, 12, 17, 22

        a = XX(F, a, b, c, d, inp[ 0], S11, 0xD76AA478L) # 1 
        d = XX(F, d, a, b, c, inp[ 1], S12, 0xE8C7B756L) # 2 
        c = XX(F, c, d, a, b, inp[ 2], S13, 0x242070DBL) # 3 
        b = XX(F, b, c, d, a, inp[ 3], S14, 0xC1BDCEEEL) # 4 
        a = XX(F, a, b, c, d, inp[ 4], S11, 0xF57C0FAFL) # 5 
        d = XX(F, d, a, b, c, inp[ 5], S12, 0x4787C62AL) # 6 
        c = XX(F, c, d, a, b, inp[ 6], S13, 0xA8304613L) # 7 
        b = XX(F, b, c, d, a, inp[ 7], S14, 0xFD469501L) # 8 
        a = XX(F, a, b, c, d, inp[ 8], S11, 0x698098D8L) # 9 
        d = XX(F, d, a, b, c, inp[ 9], S12, 0x8B44F7AFL) # 10 
        c = XX(F, c, d, a, b, inp[10], S13, 0xFFFF5BB1L) # 11 
        b = XX(F, b, c, d, a, inp[11], S14, 0x895CD7BEL) # 12 
        a = XX(F, a, b, c, d, inp[12], S11, 0x6B901122L) # 13 
        d = XX(F, d, a, b, c, inp[13], S12, 0xFD987193L) # 14 
        c = XX(F, c, d, a, b, inp[14], S13, 0xA679438EL) # 15 
        b = XX(F, b, c, d, a, inp[15], S14, 0x49B40821L) # 16 

        # Round 2.

        S21, S22, S23, S24 = 5, 9, 14, 20

        a = XX(G, a, b, c, d, inp[ 1], S21, 0xF61E2562L) # 17 
        d = XX(G, d, a, b, c, inp[ 6], S22, 0xC040B340L) # 18 
        c = XX(G, c, d, a, b, inp[11], S23, 0x265E5A51L) # 19 
        b = XX(G, b, c, d, a, inp[ 0], S24, 0xE9B6C7AAL) # 20 
        a = XX(G, a, b, c, d, inp[ 5], S21, 0xD62F105DL) # 21 
        d = XX(G, d, a, b, c, inp[10], S22, 0x02441453L) # 22 
        c = XX(G, c, d, a, b, inp[15], S23, 0xD8A1E681L) # 23 
        b = XX(G, b, c, d, a, inp[ 4], S24, 0xE7D3FBC8L) # 24 
        a = XX(G, a, b, c, d, inp[ 9], S21, 0x21E1CDE6L) # 25 
        d = XX(G, d, a, b, c, inp[14], S22, 0xC33707D6L) # 26 
        c = XX(G, c, d, a, b, inp[ 3], S23, 0xF4D50D87L) # 27 
        b = XX(G, b, c, d, a, inp[ 8], S24, 0x455A14EDL) # 28 
        a = XX(G, a, b, c, d, inp[13], S21, 0xA9E3E905L) # 29 
        d = XX(G, d, a, b, c, inp[ 2], S22, 0xFCEFA3F8L) # 30 
        c = XX(G, c, d, a, b, inp[ 7], S23, 0x676F02D9L) # 31 
        b = XX(G, b, c, d, a, inp[12], S24, 0x8D2A4C8AL) # 32 

        # Round 3.

        S31, S32, S33, S34 = 4, 11, 16, 23

        a = XX(H, a, b, c, d, inp[ 5], S31, 0xFFFA3942L) # 33 
        d = XX(H, d, a, b, c, inp[ 8], S32, 0x8771F681L) # 34 
        c = XX(H, c, d, a, b, inp[11], S33, 0x6D9D6122L) # 35 
        b = XX(H, b, c, d, a, inp[14], S34, 0xFDE5380CL) # 36 
        a = XX(H, a, b, c, d, inp[ 1], S31, 0xA4BEEA44L) # 37 
        d = XX(H, d, a, b, c, inp[ 4], S32, 0x4BDECFA9L) # 38 
        c = XX(H, c, d, a, b, inp[ 7], S33, 0xF6BB4B60L) # 39 
        b = XX(H, b, c, d, a, inp[10], S34, 0xBEBFBC70L) # 40 
        a = XX(H, a, b, c, d, inp[13], S31, 0x289B7EC6L) # 41 
        d = XX(H, d, a, b, c, inp[ 0], S32, 0xEAA127FAL) # 42 
        c = XX(H, c, d, a, b, inp[ 3], S33, 0xD4EF3085L) # 43 
        b = XX(H, b, c, d, a, inp[ 6], S34, 0x04881D05L) # 44 
        a = XX(H, a, b, c, d, inp[ 9], S31, 0xD9D4D039L) # 45 
        d = XX(H, d, a, b, c, inp[12], S32, 0xE6DB99E5L) # 46 
        c = XX(H, c, d, a, b, inp[15], S33, 0x1FA27CF8L) # 47 
        b = XX(H, b, c, d, a, inp[ 2], S34, 0xC4AC5665L) # 48 

        # Round 4.

        S41, S42, S43, S44 = 6, 10, 15, 21

        a = XX(I, a, b, c, d, inp[ 0], S41, 0xF4292244L) # 49 
        d = XX(I, d, a, b, c, inp[ 7], S42, 0x432AFF97L) # 50 
        c = XX(I, c, d, a, b, inp[14], S43, 0xAB9423A7L) # 51 
        b = XX(I, b, c, d, a, inp[ 5], S44, 0xFC93A039L) # 52 
        a = XX(I, a, b, c, d, inp[12], S41, 0x655B59C3L) # 53 
        d = XX(I, d, a, b, c, inp[ 3], S42, 0x8F0CCC92L) # 54 
        c = XX(I, c, d, a, b, inp[10], S43, 0xFFEFF47DL) # 55 
        b = XX(I, b, c, d, a, inp[ 1], S44, 0x85845DD1L) # 56 
        a = XX(I, a, b, c, d, inp[ 8], S41, 0x6FA87E4FL) # 57 
        d = XX(I, d, a, b, c, inp[15], S42, 0xFE2CE6E0L) # 58 
        c = XX(I, c, d, a, b, inp[ 6], S43, 0xA3014314L) # 59 
        b = XX(I, b, c, d, a, inp[13], S44, 0x4E0811A1L) # 60 
        a = XX(I, a, b, c, d, inp[ 4], S41, 0xF7537E82L) # 61 
        d = XX(I, d, a, b, c, inp[11], S42, 0xBD3AF235L) # 62 
        c = XX(I, c, d, a, b, inp[ 2], S43, 0x2AD7D2BBL) # 63 
        b = XX(I, b, c, d, a, inp[ 9], S44, 0xEB86D391L) # 64 

        A = (A + a) & 0xffffffffL
        B = (B + b) & 0xffffffffL
        C = (C + c) & 0xffffffffL
        D = (D + d) & 0xffffffffL

        self.A, self.B, self.C, self.D = A, B, C, D


    # Down from here all methods follow the Python Standard Library
    # API of the md5 module.

    def update(self, inBuf):
        """Add to the current message.

        Update the md5 object with the string arg. Repeated calls
        are equivalent to a single call with the concatenation of all
        the arguments, i.e. m.update(a); m.update(b) is equivalent
        to m.update(a+b).
        """
        leninBuf = long(len(inBuf))

        # Compute number of bytes mod 64.
        index = (self.count[0] >> 3) & 0x3FL

        # Update number of bits.
        self.count[0] = self.count[0] + (leninBuf << 3)
        if self.count[0] < (leninBuf << 3):
            self.count[1] = self.count[1] + 1
        self.count[1] = self.count[1] + (leninBuf >> 29)

        partLen = 64 - index

        if leninBuf >= partLen:
            index = int(index)
            partLen = int(partLen)
            self.input[index:] = map(None, inBuf[:partLen])
            self._transform(_bytelist2long(self.input))
            i = partLen
            while i + 63 < leninBuf:
                self._transform(_bytelist2long(map(None, inBuf[i:i+64])))
                i = i + 64
            else:
                leninBuf = int(leninBuf)
                self.input = map(None, inBuf[i:leninBuf])
        else:
            i = 0
            self.input = self.input + map(None, inBuf)


    def digest(self):
        """Terminate the message-digest computation and return digest.

        Return the digest of the strings passed to the update()
        method so far. This is a 16-byte string which may contain
        non-ASCII characters, including null bytes.
        """

        A = self.A
        B = self.B
        C = self.C
        D = self.D
        input = [] + self.input
        count = [] + self.count

        index = (self.count[0] >> 3) & 0x3fL

        if index < 56:
                padLen = 56 - index
        else:
                padLen = 120 - index

        padding = ['\200'] + ['\000'] * 63
        self.update(padding[:int(padLen)])

        # Append length (before padding).
        bits = _bytelist2long(self.input[:56]) + count

        self._transform(bits)

        # Store state in digest.
        digest = _long2bytes(self.A << 96, 16)[:4] + \
                 _long2bytes(self.B << 64, 16)[4:8] + \
                 _long2bytes(self.C << 32, 16)[8:12] + \
                 _long2bytes(self.D, 16)[12:]

        self.A = A 
        self.B = B
        self.C = C
        self.D = D
        self.input = input 
        self.count = count 

        return digest


    def hexdigest(self):
        """Terminate and return digest in HEX form.

        Like digest() except the digest is returned as a string of
        length 32, containing only hexadecimal digits. This may be
        used to exchange the value safely in email or other non-
        binary environments.
        """

        d = map(None, self.digest())
        d = map(ord, d)
        d = map(lambda x:"%02x" % x, d)
        d = string.join(d, '')

        return d


#    def copy(self):
        """Return a clone object.

        Return a copy ('clone') of the md5 object. This can be used
        to efficiently compute the digests of strings that share
        a common initial substring.
        """

#        return copy.deepcopy(self)


# ======================================================================
# Mimick Python top-level functions from standard library API
# for consistency with the md5 module of the standard library.
# ======================================================================

def MD5new(arg=None):
    debug(__name__ + ", MD5new")
    """Return a new md5 object.

    If arg is present, the method call update(arg) is made.
    """

    md5 = MD5()
    if arg:
        md5.update(arg)

    return md5

