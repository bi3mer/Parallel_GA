from Library import TSPLib

from random import randrange, random
from os.path import join, expanduser
from random import shuffle

cities = TSPLib.load(join(expanduser('~'), 'data', 'TSPLib', 'pr76.tsp'))


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

run_time = 45

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

test = [0, 22, 21, 20, 24, 23, 45, 44, 43, 47, 46, 68, 67, 69, 66, 49, 48, 52, 26, 25, 19, 18, 30, 29, 28, 31, 32, 27, 42, 41, 53, 51, 50, 65, 64, 55, 54, 57, 56, 70, 71, 72, 63, 62, 61, 60, 58, 59, 40, 39, 33, 34, 38, 37, 35, 36, 17, 16, 15, 14, 73, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 74, 75]
test = [i + 1 for i in test]
print(fitness(test))
import sys
sys.exit(-1)

'''
Useful Stuff
-------------------------------------------------------------------------------

Shortest paths can be found here: 
    http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html
    
    ulysses16 : 6859
    ulysses22 : 7013
    brd14051  : 469385
    pr76      : 108159

max_distance is so large because it is used for the weighted random selection
for crossover.
'''