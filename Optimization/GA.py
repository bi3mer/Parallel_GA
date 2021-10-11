from itertools import repeat
from random import seed

from Utility.PriorityQueue import insert_tup
from Utility.Stochastic import weighted_sample_tup
from .Algorithm import Algorithm

class GA(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, population=None, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        if population == None:
            population = []
            for _ in repeat(None, self.config.population_size):
                strand = self.config.create_strand()
                fitness = self.fitness(strand)
                insert_tup(population, strand, fitness, self.config.population_size)

        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            new_population = []
            # maintain some number of elites between epochs
            for i in range(self.config.num_elites_network):
                new_population.append(population[i])

            # crossover and mutation for the rest
            while len(new_population) < self.config.population_size:
                for strand in self.config.crossover(*weighted_sample_tup(population, 2)):
                    strand = self.config.mutate(strand[1])
                    fitness = self.fitness(strand)
                    insert_tup(new_population, strand, fitness, self.config.population_size)

            population = new_population

        return population[0]
