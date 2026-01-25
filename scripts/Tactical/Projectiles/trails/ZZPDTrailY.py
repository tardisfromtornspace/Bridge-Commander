# File: Z (Python 1.5)

import App

def DefaultColorKeyFunc(pEffect, fSize):
    if not pEffect:
        return None
    
    pEffect.AddColorKey(0.0, 1.0, 0.4, 0.0)
    pEffect.AddColorKey(0.3, 1.0, 0.7, 0.1)
    pEffect.AddColorKey(1.0, 1.0, 0.95, 0.3)
    pEffect.AddAlphaKey(0.0, 1.0)
    pEffect.AddAlphaKey(0.4, 0.8)
    pEffect.AddAlphaKey(1.0, 0.4)
    pEffect.AddSizeKey(0.0, 0.25 * fSize)
    pEffect.AddSizeKey(0.3, 1.2 * fSize)
    pEffect.AddSizeKey(1.0, 0.2 * fSize)

