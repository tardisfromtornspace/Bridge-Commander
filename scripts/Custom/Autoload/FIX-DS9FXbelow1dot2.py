import App
ds9fx = 0
try:
    from Custom.DS9FX import DS9FXVersionSignature, DS9FXMutatorFunctions
    if hasattr(DS9FXVersionSignature,"DS9FXVersionNumber"): # Newer versions of DS9FX
            if DS9FXVersionSignature.DS9FXVersionNumber == "1.0" or DS9FXVersionSignature.DS9FXVersionNumber == "1.1":
                    ds9fx = 1
                    print "Fixing DS9FX version"
            else :
                    ds9fx = 0
                    print "Congrats! Your DS9FX version doesn't require of any phased fix we are aware of"
        
    else: # The older versions of DS9FX f.ex. 1.0 may not have a version number
        if hasattr(DS9FXVersionSignature, "DS9FXVersion"):
                ds9fx = 1
                print "Fixing your old DS9FX version"
        else :
                ds9fx = 0 # I don't know what kind of script you have, but it's probably not any DS9FX we know of
                print "idk what kind of DS9FX script you have"

except:
    print "Unable to find DS9FX signature"
    pass

if ds9fx:
    original = DS9FXMutatorFunctions.HandleNoDamageThroughShields

    def ReplacementHandleNoDamageThroughShields(param, pObject, pEvent):
        if param == "WeaponHit":
            isthisPhased = 0  # Alex SL Gato: Taking into account phased weaponry
            pWeaponType = pEvent.GetWeaponType()
            if pWeaponType == pEvent.TORPEDO:  # Fixing how this mod conflicts with PhasedTorp and any kind of similar stock and modded technologies
                try:
                    pTorp = App.Torpedo_Cast(pEvent.GetSource())
                    # pTorp.GetNetType() == Multiplayer.SpeciesToTorp.PHASEDPLASMA
                    if pTorp.GetNetType() == 12:
                        isthisPhased = 1
                except:
                    isthisPhased = 0
            if isthisPhased == 0:
                original(param, pObject, pEvent)
        else:
            original(param, pObject, pEvent)

    DS9FXMutatorFunctions.HandleNoDamageThroughShields = ReplacementHandleNoDamageThroughShields