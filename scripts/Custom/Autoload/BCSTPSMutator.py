#################################################
#   TPSMutator by USS Sovereign
#
#   This is Targetable Plasma autoload file
#   which when activated loads main TPS file
#   and nanofx overrides.
#
#   Do not modify unless you know what you are
#   doing.
#       - LJ overrides <-- I know what
#           i am doing! or at least thats what i
#           you to think! Mwahahahaah
#
#   Property of BCS: TNG
#
################################################

# import the files we need
import App
import Foundation
import Custom.QBautostart.TargetablePlasmaStreams
import Custom.Qbautostart.TPSDATA.BCSTNGPlasmaFXoverride
import Custom.Qbautostart.TPSDATA.BCSTNGExpFXoverride

# make a mutator button
mode = Foundation.MutatorDef("BCS:TB: Targetable Plasma Streams")

# override of plasmafx.py
Foundation.OverrideDef('BCSTNGPlasmaFXoverride', 'Custom.NanoFXv2.SpecialFX.PlasmaFX.CreatePlasmaFX', 'Custom.Qbautostart.TPSDATA.BCSTNGPlasmaFXoverride.BCSTNGPlasmaFXoverride', dict = { "modes": [ mode ] } )

# Fix for CreateNanoExpSmallSeq
#Foundation.OverrideDef('BCSTNGCreateNanoExpSmallSeqFix', 'Custom.NanoFXv2.ExplosionFX.ExpFX.CreateNanoExpSmallSeq', 'Custom.Qbautostart.TPSDATA.BCSTNGExpFXoverride.CreateNanoExpSmallSeqFix', dict = { "modes": [ mode ] } )
# Fix for CreateNanoWeaponExpSeq
#Foundation.OverrideDef('BCSTNGCreateNanoWeaponExpSeqFix', 'Custom.NanoFXv2.ExplosionFX.ExpFX.CreateNanoWeaponExpSeq', 'Custom.Qbautostart.TPSDATA.BCSTNGExpFXoverride.CreateNanoWeaponExpSeqFix', dict = { "modes": [ mode ] } )
# Fix for CreateNanoExpLargeSeq
#Foundation.OverrideDef('BCSTNGCreateNanoExpLargeSeqFix', 'Custom.NanoFXv2.ExplosionFX.ExpFX.CreateNanoExpLargeSeq', 'Custom.Qbautostart.TPSDATA.BCSTNGExpFXoverride.CreateNanoExpLargeSeqFix', dict = { "modes": [ mode ] } )


# THE END! And there you go. It was fairly simple for me to make all of this!

# Credits are: Defiant for qbautostart, Dasher for foundation, NanoByte for NanoFX and us BCS: TNG for this small mod ;)

# Ask for a permission to modify any of our files or well, let's just say wowbagger has a gun :)
