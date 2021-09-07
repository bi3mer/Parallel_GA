from Optimization import *
from Problems import *

seed = 0

ga = GA(TSP, rng_seed=seed)
for res in ga.run()[:5]:
    print(res)