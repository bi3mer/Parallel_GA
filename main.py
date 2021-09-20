from Utility.ProgressBar import update_progress
from Optimization import * 
from Networks import *
import Problems

import gc

RUNS = 3
CONFIG = Problems.TSP

simulated_annealing_fine_tuner = lambda population, time: SimulatedAnnealing(CONFIG).run(solution=population[0], stop_time=time)
hill_climb_fine_tuner = lambda population, time: HillClimber(CONFIG).run(population=population, stop_time=time)
beam_search_fine_tuner = lambda population, time: HillClimber(CONFIG).run(population=population, stop_time=time)
genetic_algorithm_fine_tuner = lambda population, time: GA(CONFIG).run(population=population, stop_time=time)

algorithms = {
    # 'Hill Climber                 ': HillClimber(CONFIG),
    # 'Random Restart Hill Climbing ': RandomRestartHillClimbing(CONFIG),
    # 'Local Beam Search            ': LocalBeamSearch(CONFIG),
    # 'Stochastic Beam Search       ': StochasticBeamSearch(CONFIG),
    # 'Simulated Annealing          ': SimulatedAnnealing(CONFIG),
    # 'Random Search                ': RandomSearch(CONFIG),
    'Genetic Algorithm            ': GA(CONFIG),
    'Island GA Ring Lattice       ': IslandGA(CONFIG, ring_lattice, None),
    # 'Ring Lattice + SA            ': IslandGA(CONFIG, ring_lattice, simulated_annealing_fine_tuner),
    # 'Ring Lattice + HC            ': IslandGA(CONFIG, ring_lattice, hill_climb_fine_tuner),
    # 'Ring Lattice + BS            ': IslandGA(CONFIG, ring_lattice, beam_search_fine_tuner),
    # 'Ring Lattice + GA            ': IslandGA(CONFIG, ring_lattice, genetic_algorithm_fine_tuner),
    'Island GA Cell               ': IslandGA(CONFIG, cell, None),
    # 'Cell + SA                    ': IslandGA(CONFIG, cell, simulated_annealing_fine_tuner),
    # 'Cell + HC                    ': IslandGA(CONFIG, cell, hill_climb_fine_tuner),
    # 'Cell + BS                    ': IslandGA(CONFIG, cell, beam_search_fine_tuner),
    # 'Cell + GA                    ': IslandGA(CONFIG, cell, genetic_algorithm_fine_tuner),
    'Island GA Hierarchy          ': IslandGA(CONFIG, hier, None),
    # 'Hierarchy + SA               ': IslandGA(CONFIG, hier, simulated_annealing_fine_tuner),
    # 'Hierarchy + HC               ': IslandGA(CONFIG, hier, hill_climb_fine_tuner),
    # 'Hierarchy + BS               ': IslandGA(CONFIG, hier, beam_search_fine_tuner),
    # 'Hierarchy + GA               ': IslandGA(CONFIG, hier, genetic_algorithm_fine_tuner),
    'Island GA Caveman            ': IslandGA(CONFIG, caveman, None),
    # 'Caveman + SA                 ': IslandGA(CONFIG, caveman, simulated_annealing_fine_tuner),
    # 'Caveman + HC                 ': IslandGA(CONFIG, caveman, hill_climb_fine_tuner),
    # 'Caveman + BS                 ': IslandGA(CONFIG, caveman, beam_search_fine_tuner),
    # 'Caveman + GA                 ': IslandGA(CONFIG, caveman, genetic_algorithm_fine_tuner),
    'Island GA Rewired Caveman    ': IslandGA(CONFIG, rewired_caveman, None),
    # 'Rewired Caveman + SA         ': IslandGA(CONFIG, rewired_caveman, simulated_annealing_fine_tuner),
    # 'Rewired Caveman + HC         ': IslandGA(CONFIG, rewired_caveman, hill_climb_fine_tuner),
    # 'Rewired Caveman + BS         ': IslandGA(CONFIG, rewired_caveman, beam_search_fine_tuner),
    # 'Rewired Caveman + GA         ': IslandGA(CONFIG, rewired_caveman, genetic_algorithm_fine_tuner),
    'Island GA Watts Strogatz     ': IslandGA(CONFIG, watts_strogatz, None),
    # 'Watts Strogatz Caveman + SA  ': IslandGA(CONFIG, watts_strogatz, simulated_annealing_fine_tuner),
    # 'Watts Strogatz Caveman + HC  ': IslandGA(CONFIG, watts_strogatz, hill_climb_fine_tuner),
    # 'Watts Strogatz Caveman + BS  ': IslandGA(CONFIG, watts_strogatz, beam_search_fine_tuner),
    # 'Watts Strogatz Caveman + GA  ': IslandGA(CONFIG, watts_strogatz, genetic_algorithm_fine_tuner),
    'Island GA Empty              ': IslandGA(CONFIG, empty, None),
}

results = {}
fitness_calculations = {}
for alg_name in algorithms:
    print(alg_name)

    fitness_results = []
    fitness_num = []
    alg = algorithms[alg_name]
    for seed in range(RUNS):
        alg.fitness_calculations = 0
        gc.collect()
        fitness_results.append(alg.run(rng_seed=seed)[0])
        fitness_num.append(alg.fitness_calculations)
        update_progress((seed+1)/RUNS)
    
    results[alg_name] = fitness_results
    fitness_calculations[alg_name] = fitness_num

def mean(l):
    return sum(l) / len(l)

print()
print()
print('Algorithm\t\t\tMean Fitness\tMin Fitness\tMax Fitness\tMean # Calculations')

print_data = []
for title in algorithms:
    print_data.append((title, mean(results[title]), min(results[title]), max(results[title])))

print_data.sort(key=lambda t: t[1])

for r in print_data:
    print(f'{r[0]}\t{r[1]:.2f}\t\t{r[2]:.2f}\t\t{r[3]:.2f}\t\t{mean(fitness_calculations[r[0]]):.2f}')
