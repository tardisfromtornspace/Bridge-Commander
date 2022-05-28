#
# Based off Dasher42's LoadExtraShips(), as based off Banbury's GetShipList() snippet
#
pluginsLoaded = {}

def ImportTechs(dir = "scripts\\Custom\\Tech"):
    import nt
    import string
    global pluginsLoaded

    list = nt.listdir(dir)

    for tech in list:
        s = string.split(tech, ".")

        if len(s) <= 1:
            continue

        extension = s[-1]
        techFile = string.join(s[:-1], ".")

        if ((extension == "pyc" or extension == "py") and not pluginsLoaded.has_key(techFile)):
            pluginsLoaded[techFile] = 1 # save, so we don't load twice.
            pModule = __import__("Custom.Tech." + techFile)
            if hasattr(pModule, 'Setup'):
                pModule.Setup()
