from Optimization import * 
from Problems import *
from Networks import *

from time import time

seed = 1

rrhc = RandomRestartHillClimbing(TSP, rng_seed=seed)
start = time()
rrhc_fitness, rrhc_strand = rrhc.run()
end = time()
print(f'RandomRestartHillClimbing took {end - start} seconds.')

beam = LocalBeamSearch(TSP, rng_seed=seed)
start = time()
beam_fitness, beam_strand = beam.run()
end = time()
print(f'Local Beam Search took {end - start} seconds.')

sa = SimulatedAnnealing(TSP, rng_seed=seed)
start = time()
sa_fitness, sa_strand = sa.run()
end = time()
print(f'Simulated Annealing took {end - start} seconds.')

ga = GA(TSP, rng_seed=seed)
start = time()
ga_solutions = ga.run()
end = time()
print(f'Genetic Algorithm took {end - start} seconds.')

ring_lattice = IslandGA(TSP, ring_lattice)
start = time()
rl_solutions = ring_lattice.run()
end = time()
print(f'Ring Lattice took {end - start} seconds.')


print()
print()
print(f'Random Restart Hill Climbing: {rrhc_fitness}')
print(f'Local Beam Search:            {beam_fitness}')
print(f'Simulated Annealing:          {sa_fitness}')
print(f'GA:                           {ga_solutions[0][0]}')
print(f'Ring Lattice:                 {rl_solutions[0][0]}')
