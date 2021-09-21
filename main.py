from Utility.ProgressBar import update_progress
from Utility import Database as db
from Utility import Tabulate
from Optimization import * 
from Networks import *
import Problems

from time import time
from gc import collect as gc_collect

RUNS = 3
CONFIG = Problems.Rastrigin

simulated_annealing_fine_tuner = lambda population, time: SimulatedAnnealing(CONFIG).run(solution=population[0], stop_time=time)
hill_climb_fine_tuner = lambda population, time: HillClimber(CONFIG).run(population=population, stop_time=time)
beam_search_fine_tuner = lambda population, time: HillClimber(CONFIG).run(population=population, stop_time=time)
genetic_algorithm_fine_tuner = lambda population, time: GA(CONFIG).run(population=population, stop_time=time)

algorithms = {
    'Hill Climber': HillClimber(CONFIG),
    'Random Restart Hill Climbing': RandomRestartHillClimbing(CONFIG),
    'Local Beam Search': LocalBeamSearch(CONFIG),
    'Stochastic Beam Search': StochasticBeamSearch(CONFIG),
    'Simulated Annealing': SimulatedAnnealing(CONFIG),
    'Random Search': RandomSearch(CONFIG),
    'Genetic Algorithm': GA(CONFIG),
    'Island GA Ring Lattice': IslandGA(CONFIG, ring_lattice),
    'Island GA Cell': IslandGA(CONFIG, cell),
    'Island GA Hierarchy': IslandGA(CONFIG, hier),
    'Island GA Caveman': IslandGA(CONFIG, caveman,),
    'Island GA Rewired Caveman': IslandGA(CONFIG, rewired_caveman),
    'Island GA Watts Strogatz': IslandGA(CONFIG, watts_strogatz),
    'Island GA Empty': IslandGA(CONFIG, empty),
}

results = {}
time_taken = {}
for alg_name in algorithms:
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

    db.store(CONFIG, alg_name, alg_strands, alg_times, alg_fitness)
db.save_and_quit()

def mean(l):
    return sum(l) / len(l)


print_data = []
for title in algorithms:
    print_data.append((title, mean(results[title]), mean(time_taken[title])))

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