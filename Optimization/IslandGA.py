from random import seed, random, choice
from time import time

from Utility.Stochastic import weighted_sample
from Utility.PriorityQueue import insert_tup

class IslandGA:
    def __init__(self, config, network, rng_seed=None):
        self.config = config
        self.network = network

        if seed != None:
            seed(rng_seed)

    def run(self):
        # Network
        v, edges = self.network(self.config)

        start_time = time()
        network_run_time = start_time + (self.config.run_time * self.config.network_run_percentage)
        epoch = 1
        while network_run_time > time():
            epoch += 1

            # migration
            if epoch % self.config.epochs_till_migration == 0:
                if random() > self.config.migration_rate:
                    continue

                for v_index, population in enumerate(v):
                    weights = [self.config.max_distance - tup[0] for tup in population]
                    for destination_index in edges[v_index]:
                        for tup in weighted_sample(population, weights, k=self.config.num_elites_network):
                            insert_tup(v[destination_index], tup[1], tup[0], self.config.strands_per_cell)

                continue
                
            # regular GA for each population
            for v_index, population in enumerate(v):
                new_population = []
                weights = [self.config.max_distance - tup[0] for tup in population]

                # maintain some number of elites between epochs
                for i in range(self.config.num_elites_ga):
                    new_population.append(population[i])

                # crossover and mutation for the rest
                population = [strand[1] for strand in population]
                while len(new_population) < self.config.strands_per_cell:
                    for strand in self.config.crossover(*weighted_sample(population, weights, k=2)):
                        strand = self.config.mutate(strand)
                        fitness = self.config.fitness(strand)
                        insert_tup(new_population, strand, fitness, self.config.strands_per_cell)
                
                v[v_index] = new_population
                

        # GA
        population = [population[0] for population in v]
        population_size = len(population)

        start_time = time()
        network_run_time = start_time + (self.config.run_time * (1 - self.config.network_run_percentage))
        while network_run_time > time():
            new_population = []
            weights = [self.config.max_distance - tup[0] for tup in population]

            # maintain some number of elites between epochs
            for i in range(self.config.num_elites_network):
                new_population.append(population[i])

            # crossover and mutation for the rest
            population = [strand[1] for strand in population]
            while len(new_population) < population_size:
                for strand in self.config.crossover(*weighted_sample(population, weights, k=2)):
                    strand = self.config.mutate(strand)
                    fitness = self.config.fitness(strand)
                    insert_tup(new_population, strand, fitness, population_size)

            population = new_population

        return population