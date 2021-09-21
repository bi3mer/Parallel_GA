from random import seed, random
from itertools import repeat
from math import exp, log

from Utility import Timer
from .Algorithm import Algorithm

class SimulatedAnnealing(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def __initial_temp(self, strand_fitness):
        '''
        Modified version of:
        https://github.com/fillipe-gsm/python-tsp/blob/master/python_tsp/heuristics/simulated_annealing.py
        '''
        dfx_list = []
        for _ in repeat(None, 1000):
            strand = self.config.get_random_neighbor(self.config.create_strand(), step_size=self.config.step_size)
            dfx_list.append(self.fitness(strand) - strand_fitness)

        dfx_mean = abs(sum(dfx_list) / len(dfx_list))

        return -dfx_mean / log(0.5)

    def run(self,  rng_seed=None):
        if seed != None:
            seed(rng_seed)


        strand = self.config.create_strand()
        fitness = self.fitness(strand)

        best_strand = strand
        best_fitness = fitness

        initial_temp = self.__initial_temp(fitness)
        T = initial_temp
        step_size = self.config.step_size
        
        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            # print(step_size)
            if step_size != None:
                step_size = self.config.step_size * (1 - (self.fitness_calculations / self.config.FITNESS_CALCULATIONS))

            new_strand = self.config.get_random_neighbor(strand, step_size=step_size)
            new_fitness = self.fitness(new_strand)

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
