import App


ET_LAST_EVENT_NUMBER = App.UtopiaModule_GetNextEventType()
ET_LAST_KNOWN_EVENT_NUMBER = App.g_kConfigMapping.GetIntValue("General Options", "KM Last Known Event Number")

test = ET_LAST_EVENT_NUMBER == ET_LAST_KNOWN_EVENT_NUMBER
if not test:
	# Clear old Keyboard Config
	print "Detected new mod, restoring Keyboard Binding.."
	App.g_kKeyboardBinding.RebuildMappingFromFile("DefaultKeyboardBinding")
	App.g_kKeyboardBinding.GenerateMappingFile()
	App.g_kConfigMapping.SetIntValue("General Options", "KM Last Known Event Number", ET_LAST_EVENT_NUMBER)
	App.g_kConfigMapping.SaveConfigFile("Options.cfg")

