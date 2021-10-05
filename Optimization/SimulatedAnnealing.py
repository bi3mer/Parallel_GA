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

        T = self.__initial_temp(fitness)
        step_size = self.config.step_size
        
        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            new_strand = self.config.get_random_neighbor(strand, step_size=step_size)
            new_fitness = self.fitness(new_strand)

            # Always hill climb if valid
            if  new_fitness <= fitness:
                strand = new_strand
                fitness = new_fitness

                if fitness < best_fitness:
                    best_strand = strand
                    best_fitness = fitness
            elif random() < exp(-(new_fitness - fitness) / T):
                    strand = new_strand
                    fitness = new_fitness
                    T *= self.config.alpha
            else:
                step_size *= 0.9 # TODO: improve this

        return best_fitness, best_strand
