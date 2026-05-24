# File: Z (Python 1.5)

import App

def DefaultColorKeyFunc(pEffect, fSize):
    pEffect.AddColorKey(0.0, 255.0, 0.0, 0.0)
    pEffect.AddColorKey(0.5, 255.0, 255.0, 0.0)
    pEffect.AddColorKey(1.0, 0.0, 255.0, 0.0)
    pEffect.AddAlphaKey(0.0, 0.5)
    pEffect.AddSizeKey(0.0, 1.0 * fSize)
    pEffect.AddSizeKey(0.5, 1.5 * fSize)
    pEffect.AddSizeKey(1.0, 2.0 * fSize)

