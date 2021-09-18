from random import seed
from math import inf

from Utility.Stochastic import weighted_sample_tup
from Utility import Timer
from .Algorithm import Algorithm

class StochasticBeamSearch(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        timer = Timer()
        timer.start(self.config.run_time)
            
        population = []
        best_strand = None
        best_fitness = inf

        for _ in range(self.config.k):
            strand = self.config.create_strand()
            fitness = self.fitness(strand)
            population.append((fitness, strand))

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness
            
        step_size = self.config.step_size
        
        while not timer.is_done():
            new_population = []
            for strand in population:
                for n_strand in self.config.get_neighbors(strand[1], step_size=step_size):
                    fitness = self.fitness(n_strand)
                    new_population.append((fitness, n_strand))

                    if fitness < best_fitness:
                        best_strand = n_strand
                        best_fitness = fitness

                    if timer.is_done():
                        break
            
            population = weighted_sample_tup(new_population, self.config.k, reverse=True)
            if step_size != None:
                step_size = self.config.step_size * (1 - timer.percent_done())

        return best_fitness, best_strand
