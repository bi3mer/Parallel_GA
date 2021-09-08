from random import choices, seed
from itertools import repeat

from Utility.PriorityQueue import insert

from time import time

class IslandGA:
    def __init__(self, config, network, rng_seed=None):
        self.config = config
        self.network = network

        if seed != None:
            seed(rng_seed)

    def run(self):
        strand_size = self.config.strand_size
        v, e = self.network(self.config)

        start_time = time()
        i = 0
        while start_time + self.config.run_time > time():
            # migration
            if i % self.config.epochs_till_migration == 0:
                raise NotImplementedError('Migration not yet implemented')

                continue
                
            # regular GA for each population
            for population in v:
                new_population = []
                weights = [self.config.max_distance - tup[0] for tup in population]

                # maintain some number of elites between epochs
                for i in range(self.config.num_elites_network):
                    new_population.append(v[i])

                # crossover and mutation for the rest
                while len(new_population) < self.config.population_size:
                    break
                

        # TODO: There should be a final step where the populations are combined and
        # a GA is run on the whole population as a refinement step. This also means 
        # that the time needs to be like at 80% of time used, switch to the single
        # GA. And, make sure to compare to make sure that this stands experimentally.

        return [(self.config.fitness(val), val) for _, val in sorted(zip(population_fitness, population))]