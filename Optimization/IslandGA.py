from random import seed, random
from math import inf

from Utility.Stochastic import weighted_sample_tup
from Utility.PriorityQueue import insert_tup
from .Algorithm import Algorithm

class IslandGA(Algorithm):
    def __init__(self, config, network):
        super().__init__(config)
        self.network = network

    def run(self, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        # Network
        v, edges = self.network(self.config)

        epoch = 1
        # while not timer.is_done():
        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            epoch += 1

            # migration
            # print(epoch % self.config.epochs_till_migration)
            if epoch % self.config.epochs_till_migration == 0:
                for v_index, population in enumerate(v):
                    if v_index in edges and random() < self.config.migration_rate:
                        population.sort(key=lambda x: x[0]) # I don't think that this is necessary
                        for destination_index in edges[v_index]:
                            for tup in weighted_sample_tup(population, self.config.num_elites_network):
                                insert_tup(v[destination_index], tup[1].copy(), tup[0], self.config.strands_per_cell)
                                # v[destination_index].append((tup[0], tup[1].copy()))

                continue
                
            # regular GA for each population
            for v_index, population in enumerate(v):
                new_population = []

                # maintain some number of elites between epochs
                for i in range(self.config.num_elites_network):
                    new_population.append(population[i])

                # crossover and mutation for the rest
                while len(new_population) < self.config.strands_per_cell:
                    strands = map(lambda a: a[1], weighted_sample_tup(population, 2))
                    for strand in self.config.crossover(*strands):
                        strand = self.config.mutate(strand)
                        fitness = self.fitness(strand)
                        # new_population.append((fitness, strand))
                        insert_tup(new_population, strand, fitness, self.config.strands_per_cell)
                
                v[v_index] = new_population

        best_strand = None
        best_fitness = inf

        for population in v:
            if population[0][0] < best_fitness:
                best_fitness = population[0][0]
                best_strand = population[0][1]

        return best_fitness, best_strand
