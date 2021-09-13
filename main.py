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
rl_hc = []
rl_bs = []
rl_ga = []

c_sa = []
c_hc = []
c_bs = []
c_ga = []

for seed in range(5):
    print(f'seed={seed}')

    hc_alg = HillClimber(TSP)
    start = time()
    hc_fitness, hc_strand = hc_alg.run()
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
    rl_solutions = rl_sa_alg.run(lambda population, time: SimulatedAnnealing(TSP).run(solution=population[0], stop_time=time))
    end = time()
    rl_sa.append(rl_solutions[0])
    print(f'Ring Lattice + SA took {end - start} seconds.')

    rl_hc_alg = IslandGA(TSP, ring_lattice)
    start = time()
    rl_solutions = rl_hc_alg.run(lambda population, time: HillClimber(TSP).run(population=population, stop_time=time))
    end = time()
    rl_hc.append(rl_solutions[0])
    print(f'Ring Lattice + HC took {end - start} seconds.')

    rl_bs_alg = IslandGA(TSP, ring_lattice)
    start = time()
    rl_solutions = rl_hc_alg.run(lambda population, time: LocalBeamSearch(TSP).run(population=population, stop_time=time))
    end = time()
    rl_bs.append(rl_solutions[0])
    print(f'Ring Lattice + BS took {end - start} seconds.')

    rl_ga_alg = IslandGA(TSP, ring_lattice)
    start = time()
    rl_solutions = rl_hc_alg.run(lambda population, time: GA(TSP).run(population=population, stop_time=time))
    end = time()
    rl_ga.append(rl_solutions[0][0])
    print(f'Ring Lattice + GA took {end - start} seconds.')

    rl_sa_alg = IslandGA(TSP, cell)
    start = time()
    rl_solutions = rl_sa_alg.run(lambda population, time: SimulatedAnnealing(TSP).run(solution=population[0], stop_time=time))
    end = time()
    c_sa.append(rl_solutions[0])
    print(f'Cell + SA took {end - start} seconds.')

    rl_hc_alg = IslandGA(TSP, cell)
    start = time()
    rl_solutions = rl_hc_alg.run(lambda population, time: HillClimber(TSP).run(population=population, stop_time=time))
    end = time()
    c_hc.append(rl_solutions[0])
    print(f'Cell + HC took {end - start} seconds.')

    rl_bs_alg = IslandGA(TSP, cell)
    start = time()
    rl_solutions = rl_hc_alg.run(lambda population, time: LocalBeamSearch(TSP).run(population=population, stop_time=time))
    end = time()
    c_bs.append(rl_solutions[0])
    print(f'Cell + BS took {end - start} seconds.')

    rl_ga_alg = IslandGA(TSP, cell)
    start = time()
    rl_solutions = rl_hc_alg.run(lambda population, time: GA(TSP).run(population=population, stop_time=time))
    end = time()
    c_ga.append(rl_solutions[0][0])
    print(f'Cell + GA took {end - start} seconds.')

    print()

def mean(l):
    return sum(l) / len(l)

def print_res(title, l):
    print(f'{title}\t{min(l)}\t{int(mean(l))}\t{max(l)}')

print()
print()
print('Algorithm\t\t\tMin\tMean\tMax')
print_res(f'Hill Climbing               ', hc)
print_res(f'Random Restart Hill Climbing', rrhc)
print_res(f'Local Beam Search           ', lbs)
print_res(f'Stochastic Beam Search      ', sbs)
print_res(f'Simulated Annealing         ', sa)
print_res(f'Genetic Algorithm           ', ga)
print_res(f'Ring Lattice + SA           ', rl_sa)
print_res(f'Ring Lattice + HC           ', rl_hc)
print_res(f'Ring Lattice + BS           ', rl_bs)
print_res(f'Ring Lattice + GA           ', rl_ga)
print_res(f'Cell + SA                   ', c_sa)
print_res(f'Cell + HC                   ', c_hc)
print_res(f'Cell + BS                   ', c_bs)
print_res(f'Cell + GA                   ', c_ga)