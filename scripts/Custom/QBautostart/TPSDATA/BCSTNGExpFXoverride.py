 ###############################################################################
##	Filename:	ExpFX.py
##
##	Nano's Explosion Effects Enhancements Version 2.0
##
##	Created:	03/11/2003 - NanoByte a.k.a Michael T. Braams
##
##      Modified by USS Sovereign, thanks to Nanobyte for permission :)
##      This is an override file actually so if people decide to uninstall
##      TPS they don't have to reinstall NanoFX.
##
##      -------------------------------------------------------------------------
##      I found the following fix needed to be applied in these functions
##          -CreateNanoExpSmallSeq
##          -CreateNanoWeaponExpSeq
##          -CreateNanoExpLargeSeq
##      Changed how the override works, so the functionaility is still with
##      the NanoFX code, (so that any updates too it are not affected by this
##      mod)Plus its less code ;) - Viva la 56K!
##      -- Lost_Jedi
###############################################################################
import App

# Fix for CreateNanoExpSmallSeq
def CreateNanoExpSmallSeqFix(pShip, fTime):
    pSequence = App.TGSequence_Create()
    if pShip:
        if pShip.GetRadius() < 0.1:                     # Check to see if the event will start a game crash
            return pSequence                            # don't run if it will
        
    # OK, no need to worry about crashing! yay! so lets carry on with the function
    from Custom.NanoFXv2.ExplosionFX.ExpFX import CreateNanoExpSmallSeq
    pSequence.AddAction(CreateNanoExpSmallSeq(pShip, fTime))
    return pSequence


# Fix for CreateNanoWeaponExpSeq
def CreateNanoWeaponExpSeqFix(pEvent, sType):
    pSequence = App.TGSequence_Create()
    pShip = App.ShipClass_Cast(pEvent.GetTargetObject())
    if pShip:
        if pShip.GetRadius() < 0.1:                     # Check to see if the event will start a game crash
            return pSequence                            # don't run if it will
    # OK, no need to worry about crashing! yay! so lets carry on with the function        
    from Custom.NanoFXv2.ExplosionFX.ExpFX import CreateNanoWeaponExpSeq
    pSequence.AddAction(CreateNanoWeaponExpSeq(pEvent, sType))
    return pSequence

# Fix for CreateNanoExpLargeSeq
def CreateNanoExpLargeSeqFix(pShip, iNumPlume):
    pSequence = App.TGSequence_Create()
    if pShip:
        if pShip.GetRadius() < 0.1:                     # Check to see if the event will start a game crash
            return pSequence                            # don't run if it will

    # OK, no need to worry about crashing! yay! so lets carry on with the function
    from Custom.NanoFXv2.ExplosionFX.ExpFX import CreateNanoExpLargeSeq
    pSequence.AddAction(CreateNanoExpLargeSeq(pShip, iNumPlume))
    return pSequence
