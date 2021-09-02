from random import randrange, random

def mutate(strand, strand_size, mutation_rate):
    if random() < mutation_rate:
        p_1 = randrange(0, strand_size)
        p_2 = randrange(0, strand_size)
        strand[p_1], strand[p_2] = strand[p_2], strand[p_1]
        
    return strand

def crossover(p_1, p_2, strand_size, crossover_rate):
    if random() < crossover_rate:
        cross_over_point = randrange(0, strand_size)
        cross_over_strand_p1 = p_1[:cross_over_point]
        cross_over_strand_p2 = p_2[cross_over_point:]
        
        return cross_over_strand_p1 + [val for val in p_2 if val not in cross_over_strand_p1], \
               cross_over_strand_p2 + [val for val in p_1 if val not in cross_over_strand_p2],

    return p_1, p_2