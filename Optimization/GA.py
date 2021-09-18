from itertools import repeat
from random import seed

from Utility.PriorityQueue import insert_tup
from Utility.Stochastic import weighted_sample
from Utility import Timer

from .Algorithm import Algorithm

class GA(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, population=None, run_time=None, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        timer = Timer()
        if run_time == None:
            timer.start(self.config.run_time)
        else:
            timer.start(run_time)

        if population == None:
            population = []
            for _ in repeat(None, self.config.population_size):
                strand = self.config.create_strand()
                fitness = self.fitness(strand)
                insert_tup(population, strand, fitness, self.config.population_size)
        while not timer.is_done():
            new_population = []
            weights = [self.config.max_distance - tup[0] for tup in population]

            # maintain some number of elites between epochs
            for i in range(self.config.num_elites_network):
                new_population.append(population[i])

            # crossover and mutation for the rest
            population = [strand[1] for strand in population]
            while len(new_population) < self.config.population_size:
                for strand in self.config.crossover(*weighted_sample(population, weights, k=2)):
                    strand = self.config.mutate(strand)
                    fitness = self.fitness(strand)
                    insert_tup(new_population, strand, fitness, self.config.population_size)

            population = new_population

        return population[0]
