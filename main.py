from Utility.ProgressBar import update_progress
from Utility import Database as db
from Utility import Tabulate
from Optimization import * 
from Networks import *
import Problems

from time import time
from gc import collect as gc_collect

RUNS = 10
CONFIG = Problems.TSP

algorithms = {
    # 'Hill Climber': HillClimber(CONFIG),
    # 'Random Restart Hill Climbing': RandomRestartHillClimbing(CONFIG),
    # 'Local Beam Search': LocalBeamSearch(CONFIG),
    # 'Stochastic Beam Search': StochasticBeamSearch(CONFIG),
    'Simulated Annealing': SimulatedAnnealing(CONFIG),
    # 'Random Search': RandomSearch(CONFIG),
    'Genetic Algorithm': GA(CONFIG),
    'Island GA Ring Lattice': IslandGA(CONFIG, ring_lattice),
    'Island GA Cell': IslandGA(CONFIG, cell),
    'Island GA Hierarchy': IslandGA(CONFIG, hier),
    'Island GA Caveman': IslandGA(CONFIG, caveman,),
    'Island GA Rewired Caveman': IslandGA(CONFIG, rewired_caveman),
    'Island GA Watts Strogatz': IslandGA(CONFIG, watts_strogatz),
    'Island GA Empty': IslandGA(CONFIG, empty),
    'Island GA Full': IslandGA(CONFIG, fully_connected),
}

TOTAL = 50
for index in range(TOTAL):
    print(f'\n{index+1}/{TOTAL}')
    CONFIG.FITNESS_CALCULATIONS = 1000 * (index + 1)
    # CONFIG.epochs_till_migration = index + 2

    results = {}
    time_taken = {}
    for alg_name in algorithms:
        if db.insert_config_slash_exists(CONFIG, RUNS, alg_name):
            print(f'{alg_name} already calculated.')
            continue

        print(alg_name)

        alg_strands = []
        alg_times = []
        alg_fitness = []

        alg = algorithms[alg_name]
        for seed in range(RUNS):
            alg.fitness_calculations = 0
            gc_collect()
            start = time() 
            fitness, strand = alg.run(rng_seed=seed)
            alg_times.append(time() - start)
            alg_fitness.append(fitness)
            alg_strands.append(strand)
            update_progress((seed+1)/RUNS)
        
        results[alg_name] = alg_fitness
        time_taken[alg_name] = alg_times

        db.store(CONFIG, RUNS, alg_name, alg_strands, alg_times, alg_fitness)

    def mean(l):
        return sum(l) / len(l)


    print_data = []
    for title in algorithms:
        try:
            print_data.append((title, mean(results[title]), mean(time_taken[title])))
        except KeyError:
            pass

    print_data.sort(key=lambda t: t[1])

    print()
    print()
    Tabulate.print_markdown_table(
        ['Algorithm', 'Mean Fitness', 'Mean Time'],
        print_data
    )


    print()
    Tabulate.print_table(
        ['Algorithm', 'Mean Fitness', 'Mean Time'],
        print_data
    )

db.save_and_quit()
