from random import randrange, random, randint, shuffle, uniform
from math import cos, pi as PI

NAME = 'Binary Sphere'

population_size = 640
num_elites_ga = 5
num_elites_network = 3

strands_per_cell = 8
epochs_till_migration = 2

crossover_rate = 0.95
migration_rate = 0.01
mutation_rate = 0.2

FITNESS_CALCULATIONS = 100_000

alpha = 0.9 # simulated annealing
k = 10 # beam search

strand_size = 100
bits = 16 # 16 is actually 32 bits (16*2)

bounds = [-10, 10]

step_size = 1
step_size_alpha = 0.9

two_pi = 2 * PI

def decode(strand):
    # https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
    largest = 2**bits
    start, end = 0, bits
    substring = strand[start:end]
    chars = ''.join([str(s) for s in substring])
    integer = int(chars, 2)
    return bounds[0] + (integer/largest) * (bounds[1] - bounds[0])

def create_strand():
    return [randint(0,1) for _ in range(strand_size*bits)]

def fitness(strand):
    fit = 10 * strand_size
    for i in range(strand_size):
        val = decode(strand[i*bits:(i+1)*bits])
        fit += val**2 - (10 * cos(two_pi * val))

    return fit

def crossover(p_1, p_2):
    if random() < crossover_rate:
        cross_over_point = randrange(0, len(p_1))
        
        return p_1[:cross_over_point] + p_2[cross_over_point:],\
               p_2[:cross_over_point] + p_1[cross_over_point:],

    return p_1, p_2

def get_neighbors(strand, step_size=None):
    indexes = list(range(len(strand)))
    shuffle(indexes)

    for i in indexes:
        new = strand.copy()
        new[i] = 1 - new[i]
        yield new

def get_random_neighbor(strand, step_size=None):
    new = strand.copy()
    i = randint(0, len(strand) - 1)
    new[i] = 1 - new[i]

    return new

def mutate(strand):
    if random() < mutation_rate:
        return get_random_neighbor(strand)
    return strand