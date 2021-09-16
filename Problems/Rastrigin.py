from random import randrange, random, randint, shuffle, uniform
from math import cos, pi as PI

max_distance = 1000000
# population_size = 160
# population_size = 320
# population_size = 640
population_size = 1280
num_elites_ga = 5
num_elites_network = 1

strands_per_cell = 8
epochs_till_migration = 10

crossover_rate = 0.95
migration_rate = 0.9
mutation_rate = 0.2

network_run_percentage = 0.9

run_time = 0.1
run_time = 0.5
run_time = 1
run_time = 5

alpha = 0.9 # simulated annealing
k = 10 # beam search

strand_size = 10

step_size = 1
step_size_alpha = 0.9

two_pi = 2 * PI

def create_strand():
    strand = [uniform(-5.12, 5.12) for _ in range(strand_size)]
    return strand

def fitness(strand):
    assert len(strand) == strand_size

    fit = 10 * strand_size
    for val in strand:
        fit += val**2 - (10 * cos(two_pi * val))

    return fit

def mutate(strand):
    for i in range(strand_size):
        if random() < mutation_rate:
            strand[i] = uniform(-5.12, 5.12)
        
    return strand

def crossover(p_1, p_2):
    if random() < crossover_rate:
        cross_over_point = randrange(0, strand_size)
        
        return p_1[:cross_over_point] + p_2[cross_over_point:],\
               p_2[:cross_over_point] + p_1[cross_over_point:],

    return p_1, p_2

def get_neighbors(strand, step_size=None):
    for i in range(strand_size):
        new = strand.copy()
        new[i] = max(5.12, new[i] + step_size)
        yield new

        new = strand.copy()
        new[i] = min(-5.12, new[i] - step_size)
        yield new

def get_random_neighbor(strand, step_size=None):
    new = strand.copy()
    index = randint(0, strand_size - 1)
    
    if random() < 0.5:
        new[index] = max(5.12, new[index] + step_size)
    else:
        new[index] = min(-5.12, new[index] - step_size)

    return new

