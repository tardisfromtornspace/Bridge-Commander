# File: Z (Python 1.5)

import App

def DefaultColorKeyFunc(pEffect, fSize):
    pEffect.AddColorKey(0.0, 1.0, 0.2, 0.9)
    pEffect.AddColorKey(0.025, 1.0, 0.1, 0.8)
    pEffect.AddColorKey(0.05, 0.8, 0.0, 0.6)
    pEffect.AddAlphaKey(0.0, 1.0)
    pEffect.AddSizeKey(0.0, 1.0 * fSize)
    pEffect.AddSizeKey(0.0125, 2.0 * fSize)
    pEffect.AddSizeKey(0.025, 3.0 * fSize)
    pEffect.AddSizeKey(0.0375, 3.0 * fSize)

