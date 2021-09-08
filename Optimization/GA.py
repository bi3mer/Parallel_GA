from random import choices, seed, shuffle
from itertools import repeat

from Utility.PriorityQueue import insert
from Utility.Stochastic import weighted_sample
from time import time

class GA:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def run(self):
        '''
        Two arrays are used instead of generating a new one on each epoch to 
        avoid the GC. 
        '''
        strand_size = self.config.strand_size
        population_fitness = []
        population = []

        for _ in repeat(None, self.config.population_size):
            strand = [i + 1 for i in range(strand_size)]
            shuffle(strand)
            strand_fitness = self.config.fitness(strand)

            insert(population, population_fitness, strand, strand_fitness, self.config.population_size)

        start_time = time()
        while start_time + self.config.run_time > time():
            new_population = []
            new_fitness = []
            
            weights = [self.config.max_distance - fit for fit in population_fitness]

            # add previous elites to population
            for i in range(self.config.num_elites_ga):
                new_population.append(population[i])
                new_fitness.append(population_fitness[i])

            # build rest of population based on old one
            while len(new_population) < self.config.population_size:
                strands = self.config.crossover(*weighted_sample(population, weights, k=2))
                for strand in strands:
                    strand = self.config.mutate(strand)
                    fitness = self.config.fitness(strand)
                    insert(new_population, new_fitness, strand, fitness, self.config.population_size)

            population_fitness = new_fitness
            population = new_population

        return [(self.config.fitness(val), val) for _, val in sorted(zip(population_fitness, population))]