from Library import TSPLib
from random import randrange, random
from os.path import join, expanduser

cities = TSPLib.load(join(expanduser('~'), 'data', 'TSPLib', 'ulysses22.tsp'))

strand_size = len(list(cities.get_nodes()))

max_distance = 1000000
population_size = 100
num_elites = 5

crossover_rate = 0.95
mutation_rate = 0.02

run_time = 30

def fitness(strand):
    assert len(strand) == strand_size

    result = 0
    for current in range(0, len(strand)):
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


'''
Useful Stuff
-------------------------------------------------------------------------------

Shortest paths can be found here: 
    http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html
    
    ulysses16 : 6859
    ulysses22 : 7013

max_distance is so large because it is used for the weighted random selection
for crossover.
'''