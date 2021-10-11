from random import randrange, random, randint, shuffle, uniform
from math import sin

NAME = 'Alpine'

population_size = 1280
num_elites_ga = 5
num_elites_network = 3

strands_per_cell = 8
epochs_till_migration = 2

crossover_rate = 0.95
migration_rate = 0.01
mutation_rate = 0.2

FITNESS_CALCULATIONS = 10_000

alpha = 0.9 # simulated annealing
k = 10 # beam search

strand_size = 50
bits = 16 # 16 is actually 32 bits (16*2)

bounds = [-10, 10]


step_size = 1
step_size_alpha = 0.9

def decode(strand):
    # https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
    largest = 2**bits
    start, end = 0, bits
    substring = strand[start:end]
    chars = ''.join([str(s) for s in substring])
    integer = int(chars, 2)
    return bounds[0] + (integer/largest) * (bounds[1] - bounds[0])

def create_strand():
    return [[randint(0,1) for __ in range(16)] for _ in range(strand_size)]

def fitness(strand):
    assert len(strand) == strand_size
    return sum(abs(x*sin(x) + 0.1*x) for x in map(lambda binary: decode(binary), strand))

def mutate(strand):
    for i in range(strand_size):
        for j in range(bits):
            if random() < mutation_rate:
                strand[i][j] = 1 - strand[i][j]
        
    return strand

def crossover(p_1, p_2):
    if random() < crossover_rate:
        cross_over_point = randrange(0, strand_size)
        
        return p_1[:cross_over_point] + p_2[cross_over_point:],\
               p_2[:cross_over_point] + p_1[cross_over_point:],

    return p_1, p_2

def get_neighbors(strand, step_size=None):
    for i in range(strand_size):
        for j in range(bits):
            new = strand.copy()
            new[i][j] = 1 - new[i][j]
            yield new

def get_random_neighbor(strand, step_size=None):
    new = strand.copy()
    i = randint(0, strand_size - 1)
    j = randint(0, bits - 1)
    new[i][j] = 1 - new[i][j]

    return new

