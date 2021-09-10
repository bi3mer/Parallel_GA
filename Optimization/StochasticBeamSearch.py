from random import seed
from time import time
from math import inf

from Utility.Stochastic import weighted_sample_tup

class StochasticBeamSearch:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def run(self):
        population = []
        best_strand = None
        best_fitness = inf

        for _ in range(self.config.k):
            strand = self.config.create_strand()
            fitness = self.config.fitness(strand)
            population.append((fitness, strand))

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness
            
        stop_time = time() + self.config.run_time
        while stop_time > time():
            new_population = []
            for strand in population:
                for n_strand in self.config.get_neighbors(strand[1]):
                    fitness = self.config.fitness(n_strand)
                    new_population.append((fitness, n_strand))

                    if fitness < best_fitness:
                        best_strand = n_strand
                        best_fitness = fitness

                    if stop_time < time():
                        break
            
            population = weighted_sample_tup(new_population, self.config.k, reverse=True)

        return best_fitness, best_strand
