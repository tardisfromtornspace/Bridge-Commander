import App

sProfileFile = "KobMaruProfile.txt"

def init():
	App.TGProfilingInfo_EnableProfiling()
	App.TGProfilingInfo_StartTiming(sProfileFile)

def save():
	App.TGProfilingInfo_SaveRawData(sProfileFile)
