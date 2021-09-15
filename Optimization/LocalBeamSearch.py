from random import seed
from time import time

from Utility.PriorityQueue import insert_tup

class LocalBeamSearch:
    def __init__(self, config):
        self.config = config

    def run(self, population=None, stop_time=None, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        if population == None:
            population = []
            for _ in range(self.config.k):
                strand = self.config.create_strand()
                insert_tup(population, strand, self.config.fitness(strand), self.config.k)

        if stop_time == None:
            stop_time = time() + self.config.run_time

        start_time = time()
        total_time = stop_time - start_time

        step_size = self.config.step_size
        while stop_time > time():
            new_population = []
            for strand in population:
                for n_strand in self.config.get_neighbors(strand[1], step_size=step_size):
                    insert_tup(new_population, n_strand, self.config.fitness(n_strand), self.config.k)

                    if stop_time < time():
                        population = new_population
                        break
            
            if step_size != None:
                step_size = self.config.step_size * (1 - ((time() - start_time) / total_time))
                
            population = new_population

        return population[0]
