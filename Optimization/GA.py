from random import choices, seed, shuffle
from itertools import repeat

from Utility.ProgressBar import update_progress
from Utility.PriorityQueue import insert

class GA:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def run(self, epochs):
        '''
        Two arrays are used instead of generating a new one on each epoch to 
        avoid the GC. 
        '''
        strand_size = self.config.strand_size
        population_fitness = []
        population = []

        for _ in repeat(None, self.population_size):
            strand = [i for i in range(strand_size)]
            shuffle(strand)
            strand_fitness = self.config.fitness(strand)

            insert(population, population_fitness, strand, strand_fitness, self.population_size)

        for e in range(epochs):
            update_progress(e / epochs)

            new_population = []
            new_fitness = []
            
            weights = [self.max_distance - fit for fit in population_fitness]

            # add previous elites to population
            for i in range(self.num_elites):
                new_population.append(population[i])
                new_fitness.append(population_fitness[i])

            # build rest of population based on old one
            while len(new_population) < self.population_size:
                strands = self.config.crossover(choices(population, weights=weights, k=2))
                for strand in strands:
                    strand = self.config.mutate(strand)
                    fitness = self.config.fitness(strand)
                    insert(new_population, new_fitness, strand, fitness, self.config.population_size)

            population_fitness = new_fitness
            population = new_population

        update_progress(1)

        return [(self.fitness_function(self.city_list, val), val) for _, val in sorted(zip(population_fitness, population))]