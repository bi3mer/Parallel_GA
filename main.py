from Optimization import * 
from Problems import *
from Networks import *

seed = 1

print('GA')
ga = GA(TSP, rng_seed=seed)
for res in ga.run()[:5]:
    print(res[0])

print('Ring Lattice')
ring_lattice = IslandGA(TSP, ring_lattice)
for res in ring_lattice.run()[:5]:
    print(res[0])
