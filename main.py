from Optimization.StochasticBeamSearch import StochasticBeamSearch
from Optimization import * 
from Problems import *
from Networks import *

from time import time

hc = []
rrhc = []
lbs = []
sbs = []
sa = []
ga = []
rl_sa = []

for seed in range(5):
    print(f'seed={seed}')

    hc_strand = TSP.create_strand()
    hc_fitness = TSP.fitness(hc_strand)
    start = time()
    hc_fitness, hc_strand = hill_climb(hc_fitness, hc_strand, TSP, start + TSP.run_time, greedy=True)
    end = time()
    hc.append(hc_fitness)
    print(f'Hill Climb took {end - start} seconds.')

    rrhc_alg = RandomRestartHillClimbing(TSP, rng_seed=seed)
    start = time()
    rrhc_fitness, rrhc_strand = rrhc_alg.run()
    end = time()
    rrhc.append(rrhc_fitness)
    print(f'RandomRestartHillClimbing took {end - start} seconds.')

    beam = LocalBeamSearch(TSP, rng_seed=seed)
    start = time()
    beam_fitness, beam_strand = beam.run()
    end = time()
    lbs.append(beam_fitness)
    print(f'Local Beam Search took {end - start} seconds.')

    sbeam = StochasticBeamSearch(TSP, rng_seed=seed)
    start = time()
    sbeam_fitness, sbeam_strand = sbeam.run()
    end = time()
    sbs.append(sbeam_fitness)
    print(f'Stochastic Beam Search took {end - start} seconds.')

    sa_alg = SimulatedAnnealing(TSP, rng_seed=seed)
    start = time()
    sa_fitness, sa_strand = sa_alg.run()
    end = time()
    sa.append(sa_fitness)
    print(f'Simulated Annealing took {end - start} seconds.')

    ga_alg = GA(TSP, rng_seed=seed)
    start = time()
    ga_solutions = ga_alg.run()
    end = time()
    ga.append(ga_solutions[0][0])
    print(f'Genetic Algorithm took {end - start} seconds.')

    rl_sa_alg = IslandGA(TSP, ring_lattice)
    start = time()
    rl_solutions = rl_sa_alg.run(lambda population, time: SimulatedAnnealing(TSP).run(solution=population[0], run_time=time))
    end = time()
    rl_sa.append(rl_solutions[0])
    print(f'Ring Lattice + SA took {end - start} seconds.')

    print()

def mean(l):
    return sum(l) / len(l)

print()
print()
print(f'Hill Climbing:                {min(hc)}\t{mean(hc)}')
print(f'Random Restart Hill Climbing: {min(rrhc)}\t{mean(rrhc)}')
print(f'Local Beam Search:            {min(lbs)}\t{mean(lbs)}')
print(f'Stochastic Beam Search:       {min(sbs)}\t{mean(sbs)}')
print(f'Simulated Annealing:          {min(sa)}\t{mean(sa)}')
print(f'GA:                           {min(ga)}\t{mean(ga)}')
print(f'Ring Lattice + SA:            {min(rl_sa)}\t{mean(rl_sa)}')
