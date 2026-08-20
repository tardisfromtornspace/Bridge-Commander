# File: Z (Python 1.5)

import App

def DefaultColorKeyFunc(pEffect, fSize):
    '''
    Light red \xe2\x86\x92 fiery orange-red \xe2\x86\x92 dark ember red
    Small \xe2\x86\x92 large \xe2\x86\x92 thin
    Slow fade for long-lasting glow
    '''
    if not pEffect:
        return None
    
    pEffect.AddColorKey(0.0, 1.0, 0.4, 0.3)
    pEffect.AddColorKey(0.35, 1.0, 0.5, 0.0)
    pEffect.AddColorKey(0.7, 0.9, 0.3, 0.0)
    pEffect.AddColorKey(1.0, 0.3, 0.0, 0.0)
    pEffect.AddAlphaKey(0.0, 0.2)
    pEffect.AddAlphaKey(0.2, 0.6)
    pEffect.AddAlphaKey(0.6, 0.4)
    pEffect.AddAlphaKey(0.85, 0.25)
    pEffect.AddAlphaKey(1.0, 0.1)
    pEffect.AddSizeKey(0.0, 0.2 * fSize)
    pEffect.AddSizeKey(0.3, 0.7 * fSize)
    pEffect.AddSizeKey(0.8, 0.4 * fSize)
    pEffect.AddSizeKey(1.0, 0.1 * fSize)

