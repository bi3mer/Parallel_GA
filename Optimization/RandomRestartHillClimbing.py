from random import seed
from math import inf

from .HillClimber import HillClimber
from Utility import Timer

class RandomRestartHillClimbing:
    def __init__(self, config):
        self.config = config

    def run(self, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        timer = Timer()
        timer.start(self.config.run_time)

        best_strand = None
        best_fitness = inf

        hc = HillClimber(self.config)

        while not timer.is_done():
            strand = self.config.create_strand()
            fitness = self.config.fitness(strand)

            fitness, strand = hc.run(population=[(fitness, strand)], run_time=timer.time_left())

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness

        return best_fitness, best_strand
