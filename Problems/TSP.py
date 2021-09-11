from Library import TSPLib

from random import randrange, random, randint
from os.path import join, expanduser
from random import shuffle

cities = TSPLib.load(join(expanduser('~'), 'data', 'TSPLib', 'berlin52.tsp'))
strand_size = len(list(cities.get_nodes()))

max_distance = 1000000
population_size = 160
num_elites_ga = 5
num_elites_network = 1

strands_per_cell = 8
epochs_till_migration = 10

crossover_rate = 0.95
migration_rate = 0.9
mutation_rate = 0.02

network_run_percentage = 0.9

run_time = 0.5

alpha = 0.9 # simulated annealing
k = 10 # beam search

def create_strand():
    strand = [i + 1 for i in range(strand_size)]
    shuffle(strand)
    return strand

def fitness(strand):
    assert len(strand) == strand_size

    result = 0
    for current in range(1, len(strand)):
        result += cities.get_weight(strand[current-1], strand[current])

    result += cities.get_weight(strand[-1], strand[0])

    return result

def mutate(strand):
    if random() < mutation_rate:
        p_1 = randrange(0, strand_size)
        p_2 = randrange(0, strand_size)
        strand[p_1], strand[p_2] = strand[p_2], strand[p_1]
        
    return strand

def crossover(p_1, p_2):
    if random() < crossover_rate:
        cross_over_point = randrange(0, strand_size)
        cross_over_strand_p1 = p_1[:cross_over_point]
        cross_over_strand_p2 = p_2[cross_over_point:]
        
        return cross_over_strand_p1 + [val for val in p_2 if val not in cross_over_strand_p1], \
               cross_over_strand_p2 + [val for val in p_1 if val not in cross_over_strand_p2],

    return p_1, p_2

def get_neighbors(strand):
    for i in range(len(strand)):
        for j in range(i+1, len(strand)):
            n = strand.copy()
            n[i] = strand[j]
            n[j] = strand[i]

            yield n

def get_random_neighbor(strand):
    index_1 = randint(0, len(strand) - 1)
    index_2 = randint(0, len(strand) - 1)

    n = strand.copy()
    n[index_1] = strand[index_2]
    n[index_2] = strand[index_1]

    return n

'''
Useful Stuff
-------------------------------------------------------------------------------

Shortest paths can be found here: 
    http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html
    
    ulysses16 : 6859
    ulysses22 : 7013
    berlin52  : 7542
    pr76      : 108159
    brd14051  : 469385
    dsj1000   : 18659688

max_distance is so large because it is used for the weighted random selection
for crossover.
'''