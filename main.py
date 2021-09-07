from Optimization import * 
from Problems import *
from Networks import *

seed = 0

ga = GA(TSP, rng_seed=seed)
for res in ga.run()[:10]:
    print(res)

# ring_lattice = IslandGA(TSP, ring_lattice)
# for res in ring_lattice.run()[:5]:
#     print(res)
