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

h_sa = []
h_hc = []
h_bs = []
h_ga = []

s_sa = []
s_hc = []
s_bs = []
s_ga = []

def run_networks(title, network, seed):
    # simulated annealing
    sa_alg = IslandGA(TSP, network, rng_seed=seed)
    start = time()
    sa_solutions = sa_alg.run(lambda population, time: SimulatedAnnealing(TSP).run(solution=population[0], stop_time=time))
    end = time()
    print(f'{title} + SA took {end - start} seconds.')

    # hill climber
    hc_alg = IslandGA(TSP, network, rng_seed=seed)
    start = time()
    hc_solutions = hc_alg.run(lambda population, time: HillClimber(TSP).run(population=population, stop_time=time))
    end = time()
    print(f'{title} + Hill Climbing took {end - start} seconds.')

    # beam search
    bs_alg = IslandGA(TSP, network, rng_seed=seed)
    start = time()
    bs_solutions = bs_alg.run(lambda population, time: HillClimber(TSP).run(population=population, stop_time=time))
    end = time()
    print(f'{title} + beam search took {end - start} seconds.')

    # genetic algorithm
    ga_alg = IslandGA(TSP, network, rng_seed=seed)
    start = time()
    ga_solutions = ga_alg.run(lambda population, time: GA(TSP).run(population=population, stop_time=time))
    end = time()
    print(f'{title} + Genetic Algorithm took {end - start} seconds.')

    # Return the fitness values. GA is the only one that returns the entire population.
    # It is ordered so the first solution is the best solution.
    return sa_solutions[0], hc_solutions[0], bs_solutions[0], ga_solutions[0][0]

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

    sa_res, hc_res, bs_res, ga_res = run_networks('Ring Lattice', ring_lattice, seed)
    rl_sa.append(sa_res)
    rl_hc.append(hc_res)
    rl_bs.append(bs_res)
    rl_ga.append(ga_res)

    sa_res, hc_res, bs_res, ga_res = run_networks('CELL', cell, seed)
    c_sa.append(sa_res)
    c_hc.append(hc_res)
    c_bs.append(bs_res)
    c_ga.append(ga_res)

    sa_res, hc_res, bs_res, ga_res = run_networks('Small World Network', small_world_network, seed)
    s_sa.append(sa_res)
    s_hc.append(hc_res)
    s_bs.append(bs_res)
    s_ga.append(ga_res)

    sa_res, hc_res, bs_res, ga_res = run_networks('HIER', hier, seed)
    h_sa.append(sa_res)
    h_hc.append(hc_res)
    h_bs.append(bs_res)
    h_ga.append(ga_res)

    print()

def mean(l):
    return sum(l) / len(l)

def print_res(title, l):
    print(f'{title}\t{int(mean(l))}\t{min(l)}\t{max(l)}')

print()
print()
print('Algorithm\t\t\tMean\tMin\tMax')
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
print_res(f'Small World Network + SA    ', s_sa)
print_res(f'Small World Network + HC    ', s_hc)
print_res(f'Small World Network + BS    ', s_bs)
print_res(f'Small World Network + GA    ', s_ga)
print_res(f'HIER + SA                   ', h_sa)
print_res(f'HIER + HC                   ', h_hc)
print_res(f'HIER + BS                   ', h_bs)
print_res(f'HIER + GA                   ', h_ga)