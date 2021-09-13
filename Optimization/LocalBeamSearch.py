from random import seed
from time import time

from Utility.PriorityQueue import insert_tup

class LocalBeamSearch:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def run(self, population=None, stop_time=None):
        if population == None:
            population = []
            for _ in range(self.config.k):
                strand = self.config.create_strand()
                insert_tup(population, strand, self.config.fitness(strand), self.config.k)

        if stop_time == None:
            stop_time = time() + self.config.run_time

        while stop_time > time():
            new_population = []
            for strand in population:
                for n_strand in self.config.get_neighbors(strand[1]):
                    insert_tup(new_population, n_strand, self.config.fitness(n_strand), self.config.k)

                    if stop_time < time():
                        population = new_population
                        break

            population = new_population

        return population[0]
