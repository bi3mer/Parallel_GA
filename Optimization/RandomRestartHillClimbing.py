from random import seed
from time import time
from math import inf

from .HillClimber import hill_climb

class RandomRestartHillClimbing:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def run(self):
        best_strand = None
        best_fitness = inf

        stop_time = time() + self.config.run_time
        while stop_time > time():
            strand = self.config.create_strand()
            fitness = self.config.fitness(strand)

            fitness, strand = hill_climb(fitness, strand, self.config, stop_time, greedy=True)

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness

        return best_fitness, best_strand
