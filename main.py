from Utility.ProgressBar import update_progress
from Utility.Iterator import float_range
from Utility import Database as db
from Utility import Tabulate
from Optimization import * 
from Networks import *
import Problems

from itertools import product
from time import time
from gc import collect as gc_collect
import argparse


parser = argparse.ArgumentParser(description='GA Benchmarker')
parser.add_argument('--store', action='store_true', help='store results to database')
args = parser.parse_args()

if args.store:
    print('Results will be stored from this run.')
else:
    print('Results not stored for this run.')
db.should_store = args.store

RUNS = 5
CONFIG = Problems.Sphere

algorithms = {
    # 'Hill Climber': HillClimber(CONFIG),
    # 'Random Restart Hill Climbing': RandomRestartHillClimbing(CONFIG),
    # 'Local Beam Search': LocalBeamSearch(CONFIG),
    # 'Stochastic Beam Search': StochasticBeamSearch(CONFIG),
    # 'Simulated Annealing': SimulatedAnnealing(CONFIG),
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
    'Dynamic Island GA': DynamicIslandGA(CONFIG),
}

migration_rates = list(float_range(0.01,1.01,0.02))
epochs_till_migration = list(range(2,15))

# for m_rate, e_rate in product(migration_rates, epochs_till_migration):
for index in range(1):
    # print(f'\n{index+1}/{50}')
    # CONFIG.FITNESS_CALCULATIONS = 2_500 * index
    # CONFIG.epochs_till_migration = index + 2

    # print(f'{m_rate}, {e_rate}')

    # CONFIG.migration_rate = m_rate
    # CONFIG.epochs_till_migration = e_rate

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
