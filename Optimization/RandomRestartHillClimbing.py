from random import seed
from math import inf

from .HillClimber import HillClimber
from .Algorithm import Algorithm

class RandomRestartHillClimbing(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, rng_seed=None):
        if rng_seed != None:
            seed(rng_seed)
            
        best_strand = None
        best_fitness = inf

        hc = HillClimber(self.config)

        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            strand = self.config.create_strand()
            fitness = self.fitness(strand)

            fitness, strand = hc.run(
                population=[(fitness, strand)], 
                calculations=self.config.FITNESS_CALCULATIONS - self.fitness_calculations)

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness

        return best_fitness, best_strand
