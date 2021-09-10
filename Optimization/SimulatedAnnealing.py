from random import seed, random
from itertools import repeat
from time import time
from math import exp, log

class SimulatedAnnealing:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def __initial_temp(self, strand_fitness):
        '''
        Modified version of:
        https://github.com/fillipe-gsm/python-tsp/blob/master/python_tsp/heuristics/simulated_annealing.py
        '''
        dfx_list = []
        for _ in repeat(None, 1000):
            strand = self.config.get_random_neighbor(self.config.create_strand())
            dfx_list.append(self.config.fitness(strand) - strand_fitness)

        dfx_mean = abs(sum(dfx_list) / len(dfx_list))

        return -dfx_mean / log(0.5)

    def run(self):
        strand = self.config.create_strand()
        fitness = self.config.fitness(strand)

        best_strand = strand
        best_fitness = fitness

        initial_temp = self.__initial_temp(fitness)
        T = initial_temp
        
        start_time = time()
        run_time = start_time + self.config.run_time
        while run_time > time():
            new_strand = self.config.get_random_neighbor(strand)
            new_fitness = self.config.fitness(new_strand)

            # Always hill climb if valid
            delta_f = new_fitness - fitness 
            if delta_f < 0:
                strand = new_strand
                fitness = new_fitness
                T *= self.config.alpha

                if fitness < best_fitness:
                    best_strand = strand
                    best_fitness = fitness
                continue
            
            # Anneal if we can
            if random() < exp(-delta_f / T):
                strand = new_strand
                fitness = new_fitness
                T *= self.config.alpha


        return best_fitness, best_strand
