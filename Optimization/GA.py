from itertools import repeat
from random import seed

from Utility.PriorityQueue import insert_tup
from Utility.Stochastic import weighted_sample
from time import time

class GA:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def run(self):
        population = []
        for _ in repeat(None, self.config.population_size):
            strand = self.config.create_strand()
            fitness = self.config.fitness(strand)
            insert_tup(population, strand, fitness, self.config.population_size)

        start_time = time()
        run_time = start_time + self.config.run_time
        while run_time > time():
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
                    fitness = self.config.fitness(strand)
                    insert_tup(new_population, strand, fitness, self.config.population_size)

            population = new_population

        return population
