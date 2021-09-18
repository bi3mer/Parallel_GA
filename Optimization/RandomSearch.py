from random import seed
from .Algorithm import Algorithm
from Utility import Timer

class RandomSearch(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, population=None, run_time=None, rng_seed=None):
        if rng_seed:
            seed(rng_seed)

        timer = Timer()
        if run_time == None:
            timer.start(self.config.run_time)
        else:
            timer.start(run_time)

        best_strand = self.config.create_strand()
        best_fitness = self.fitness(best_strand)

        while not timer.is_done():
            strand = self.config.create_strand()
            fitness = self.fitness(strand)

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness

        return fitness, strand
        
