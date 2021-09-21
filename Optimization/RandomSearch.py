from random import seed
from .Algorithm import Algorithm
from Utility import Timer

class RandomSearch(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, rng_seed=None):
        if rng_seed:
            seed(rng_seed)

        best_strand = self.config.create_strand()
        best_fitness = self.fitness(best_strand)

        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            strand = self.config.create_strand()
            fitness = self.fitness(strand)

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness

        return fitness, strand
        
