from bcdebug import debug
from Custom.QBautostart.Libs.Races import Races
from Multiplayer.SpeciesToSystem import *

# add all systems to be constructed at start here
lStartingSets = [VESUVI, SOL]

# race specific sets
if App.g_kUtopiaModule.IsHost():
	Races["Federation"].iStartingSet = SOL
	
iDefaultStartingSet = VESUVI

pModule = __import__(__name__)

# all other sets
def CreateSystemMenuEntrys():
			debug(__name__ + ", CreateSystemMenuEntrys")
			import Systems.Starbase12.Starbase
			Systems.Starbase12.Starbase.CreateMenus()

			import Systems.Belaruz.Belaruz
			Systems.Belaruz.Belaruz.CreateMenus()

			import Systems.Vesuvi.Vesuvi
			Systems.Vesuvi.Vesuvi.CreateMenus()

			import Systems.Albirea.Albirea
			Systems.Albirea.Albirea.CreateMenus()

			import Systems.Alioth.Alioth
			Systems.Alioth.Alioth.CreateMenus()

			import Systems.Artrus.Artrus
			Systems.Artrus.Artrus.CreateMenus()

			import Systems.Ascella.Ascella
			Systems.Ascella.Ascella.CreateMenus()

			import Systems.Beol.Beol
			Systems.Beol.Beol.CreateMenus()

			import Systems.Biranu.Biranu
			Systems.Biranu.Biranu.CreateMenus()

			import Systems.Chambana.Chambana
			Systems.Chambana.Chambana.CreateMenus()

			import Systems.Geble.Geble
			Systems.Geble.Geble.CreateMenus()

			import Systems.Itari.Itari
			Systems.Itari.Itari.CreateMenus()

			import Systems.OmegaDraconis.OmegaDraconis
			Systems.OmegaDraconis.OmegaDraconis.CreateMenus()

			import Systems.Ona.Ona
			Systems.Ona.Ona.CreateMenus()

			import Systems.Poseidon.Poseidon
			Systems.Poseidon.Poseidon.CreateMenus()

			import Systems.Prendel.Prendel
			Systems.Prendel.Prendel.CreateMenus()

			import Systems.Savoy.Savoy
			Systems.Savoy.Savoy.CreateMenus()

			import Systems.Serris.Serris
			Systems.Serris.Serris.CreateMenus()

			import Systems.Tevron.Tevron
			Systems.Tevron.Tevron.CreateMenus()

			import Systems.Tezle.Tezle
			Systems.Tezle.Tezle.CreateMenus()

			import Systems.Vesuvi.Vesuvi
			Systems.Vesuvi.Vesuvi.CreateMenus()

			import Systems.Voltair.Voltair
			Systems.Voltair.Voltair.CreateMenus()

			import Systems.XiEntrades.XiEntrades
			Systems.XiEntrades.XiEntrades.CreateMenus()

			import Systems.Yiles.Yiles
			Systems.Yiles.Yiles.CreateMenus()

			import Systems.Badlands.Badlands
			Systems.Badlands.Badlands.CreateMenus()

			import Systems.Cebalrai.Cebalrai
			Systems.Cebalrai.Cebalrai.CreateMenus()

			import Systems.KavisAlpha.KavisAlpha
			Systems.KavisAlpha.KavisAlpha.CreateMenus()

			import Systems.Obstacles.Obstacles
			Systems.Obstacles.Obstacles.CreateMenus()

			import Systems.Procyon.Procyon
			Systems.Obstacles.Obstacles.CreateMenus()
			
			import Systems.Ross_128.Ross_128
			Systems.Ross_128.Ross_128.CreateMenus()

			import Systems.String.String
			Systems.String.String.CreateMenus()
			
			import Systems.Banzai.Banzai
			Systems.Banzai.Banzai.CreateMenus()

			import Systems.Fluid.Fluid
			Systems.Fluid.Fluid.CreateMenus()

			import Systems.Hekaras.Hekaras
			Systems.Hekaras.Hekaras.CreateMenus()

			import Systems.Khan.Khan
			Systems.Khan.Khan.CreateMenus()

			import Systems.SystemJ25.SystemJ25
			Systems.SystemJ25.SystemJ25.CreateMenus()
			
			import Systems.Arcturus.Arcturus
			Systems.Arcturus.Arcturus.CreateMenus()

			import Systems.Baqis.Baqis
			Systems.Baqis.Baqis.CreateMenus()

			import Systems.Borealis.Borealis
			Systems.Borealis.Borealis.CreateMenus()

			import Systems.CJones.CJones
			Systems.CJones.CJones.CreateMenus()

			import Systems.Kronos.Kronos
			Systems.Kronos.Kronos.CreateMenus()

			import Systems.Rainbow.Rainbow
			Systems.Rainbow.Rainbow.CreateMenus()

			import Systems.Tathis.Tathis
			Systems.Tathis.Tathis.CreateMenus()

			import Systems.Vulcan.Vulcan
			Systems.Vulcan.Vulcan.CreateMenus()

			import Systems.ArenaA.ArenaA
			Systems.ArenaA.ArenaA.CreateMenus()

			import Systems.BriarPatch.BriarPatch
			Systems.BriarPatch.BriarPatch.CreateMenus()

			import Systems.Comet.Comet
			Systems.Comet.Comet.CreateMenus()

			import Systems.Pleides.Pleides
			Systems.Pleides.Pleides.CreateMenus()

			import Systems.RedGiant.RedGiant
			Systems.RedGiant.RedGiant.CreateMenus()

			import Systems.Sirius_B.Sirius_B
			Systems.Sirius_B.Sirius_B.CreateMenus()

			import Systems.Vatris.Vatris
			Systems.Vatris.Vatris.CreateMenus()

			import Systems.Wolf359.Wolf359
			Systems.Wolf359.Wolf359.CreateMenus()

			import Systems.Calufrax.Calufrax
			Systems.Calufrax.Calufrax.CreateMenus()

			import Systems.Junkyard.Junkyard
			Systems.Junkyard.Junkyard.CreateMenus()

			import Systems.Nepenthe.Nepenthe
			Systems.Nepenthe.Nepenthe.CreateMenus()

			import Systems.Riha.Riha
			Systems.Riha.Riha.CreateMenus()

			import Systems.SmokeRing.SmokeRing
			Systems.SmokeRing.SmokeRing.CreateMenus()

			import Systems.Betelgeuse.Betelgeuse
			Systems.Betelgeuse.Betelgeuse.CreateMenus()

			import Systems.Canopus.Canopus
			Systems.Canopus.Canopus.CreateMenus()

			import Systems.DryDock.DryDockSystem
			Systems.DryDock.DryDockSystem.CreateMenus()

			import Systems.GasGiant.GasGiant
			Systems.GasGiant.GasGiant.CreateMenus()

			import Systems.Kastra.Kastra
			Systems.Kastra.Kastra.CreateMenus()

			import Systems.Nursery.Nursery
			Systems.Nursery.Nursery.CreateMenus()

			import Systems.Romulus.Romulus
			Systems.Romulus.Romulus.CreateMenus()

			import Systems.Vger.Vger
			Systems.Vger.Vger.CreateMenus()
