from Utility.ProgressBar import update_progress
from Optimization.StochasticBeamSearch import StochasticBeamSearch
from Optimization import * 
from Problems import *
from Networks import *

from time import time

RUNS = 20
CONFIG = TSP


simulated_annealing_fine_tuner = lambda population, time: SimulatedAnnealing(TSP).run(solution=population[0], stop_time=time)
hill_climb_fine_tuner = lambda population, time: HillClimber(TSP).run(population=population, stop_time=time)
beam_search_fine_tuner = lambda population, time: HillClimber(TSP).run(population=population, stop_time=time)
genetic_algorithm_fine_tuner = lambda population, time: GA(TSP).run(population=population, stop_time=time)

algorithms = {
    'Hill Climber                 ': HillClimber(CONFIG),
    'Random Restart Hill Climbing ': RandomRestartHillClimbing(CONFIG),
    'Local Beam Search            ': LocalBeamSearch(CONFIG),
    'Stochastic Beam Search       ': StochasticBeamSearch(CONFIG),
    'Simulated Annealing          ': SimulatedAnnealing(CONFIG),
    'Genetic Algorithm            ': GA(CONFIG),
    'Ring Lattice + SA            ': IslandGA(CONFIG, ring_lattice, simulated_annealing_fine_tuner),
    'Ring Lattice + HC            ': IslandGA(CONFIG, ring_lattice, hill_climb_fine_tuner),
    'Ring Lattice + BS            ': IslandGA(CONFIG, ring_lattice, beam_search_fine_tuner),
    'Ring Lattice + GA            ': IslandGA(CONFIG, ring_lattice, beam_search_fine_tuner),
    'Cell + SA                    ': IslandGA(CONFIG, cell, simulated_annealing_fine_tuner),
    'Cell + HC                    ': IslandGA(CONFIG, cell, hill_climb_fine_tuner),
    'Cell + BS                    ': IslandGA(CONFIG, cell, beam_search_fine_tuner),
    'Cell + GA                    ': IslandGA(CONFIG, cell, genetic_algorithm_fine_tuner),
    'Hierarchy + SA               ': IslandGA(CONFIG, hier, simulated_annealing_fine_tuner),
    'Hierarchy + HC               ': IslandGA(CONFIG, hier, hill_climb_fine_tuner),
    'Hierarchy + BS               ': IslandGA(CONFIG, hier, beam_search_fine_tuner),
    'Hierarchy + GA               ': IslandGA(CONFIG, hier, genetic_algorithm_fine_tuner),
    'Caveman + SA                 ': IslandGA(CONFIG, caveman, simulated_annealing_fine_tuner),
    'Caveman + HC                 ': IslandGA(CONFIG, caveman, hill_climb_fine_tuner),
    'Caveman + BS                 ': IslandGA(CONFIG, caveman, beam_search_fine_tuner),
    'Caveman + GA                 ': IslandGA(CONFIG, caveman, genetic_algorithm_fine_tuner),
    'Rewired Caveman + SA         ': IslandGA(CONFIG, rewired_caveman, simulated_annealing_fine_tuner),
    'Rewired Caveman + HC         ': IslandGA(CONFIG, rewired_caveman, hill_climb_fine_tuner),
    'Rewired Caveman + BS         ': IslandGA(CONFIG, rewired_caveman, beam_search_fine_tuner),
    'Rewired Caveman + GA         ': IslandGA(CONFIG, rewired_caveman, genetic_algorithm_fine_tuner),
    'Watts Strogatz Caveman + SA  ': IslandGA(CONFIG, watts_strogatz, simulated_annealing_fine_tuner),
    'Watts Strogatz Caveman + HC  ': IslandGA(CONFIG, watts_strogatz, hill_climb_fine_tuner),
    'Watts Strogatz Caveman + BS  ': IslandGA(CONFIG, watts_strogatz, beam_search_fine_tuner),
    'Watts Strogatz Caveman + GA  ': IslandGA(CONFIG, watts_strogatz, genetic_algorithm_fine_tuner),
}

results = {}
for alg_name in algorithms:
    print(alg_name)

    res = []
    alg = algorithms[alg_name]
    for seed in range(RUNS):
        res.append(alg.run(rng_seed=seed)[0])
        update_progress((seed+1)/RUNS)
    
    results[alg_name] = res

def mean(l):
    return sum(l) / len(l)

def print_res(title, l):
    print(f'{title}\t{int(mean(l))}\t{min(l)}\t{max(l)}')

print()
print()
print('Algorithm\t\t\tMean\tMin\tMax')

for title in algorithms:
    print_res(title, results[title])
