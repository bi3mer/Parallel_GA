from random import seed, random
from math import inf

from Utility.Stochastic import weighted_sample
from Utility.PriorityQueue import insert_tup
from Utility import Timer
from .Algorithm import Algorithm

class IslandGA(Algorithm):
    def __init__(self, config, network, fine_tuner):
        super().__init__(config)
        self.network = network
        self.fine_tuner = fine_tuner

    def run(self, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        timer = Timer()
        if self.fine_tuner == None:
            timer.start(self.config.run_time)
        else:
            timer.start(self.config.run_time * self.config.network_run_percentage)

        # Network
        v, edges = self.network(self.config)

        epoch = 1
        while not timer.is_done():
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
                        fitness = self.fitness(strand)
                        insert_tup(new_population, strand, fitness, self.config.strands_per_cell)
                
                v[v_index] = new_population
                

        # run an optimizer with the final set of strands
        if self.fine_tuner != None:
            return self.fine_tuner(
                [population[0] for population in v],
                time() + self.config.run_time * (1 - self.config.network_run_percentage))
        else:
            best_strand = None
            best_fitness = inf

            for population in v:
                if population[0][0] < best_fitness:
                    best_fitness = population[0][0]
                    best_strand = population[0][1]

            return best_fitness, best_strand
