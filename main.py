from random import Random
from Optimization import * 
from Problems import *
from Networks import *

from time import time

seed = 1

rrhc = RandomRestartHillClimbing(TSP)
start = time()
rrhc_fitness, rrhc_strand = rrhc.run()
end = time()

print(f'Random Restart Hill Climbing ({end - start})')
print(rrhc_fitness)

ga = GA(TSP, rng_seed=seed)
start = time()
ga_solutions = ga.run()
end = time()

print()
print(f'GA ({end - start})')
for res in ga_solutions[:5]:
    print(res[0])

ring_lattice = IslandGA(TSP, ring_lattice)
start = time()
rl_solutions = ring_lattice.run()
end = time()

print()
print(f'Ring Lattice ({end - start})')
for res in rl_solutions[:5]:
    print(res[0])
