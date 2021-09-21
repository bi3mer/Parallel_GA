from random import seed

from Utility.PriorityQueue import insert_tup
from .Algorithm import Algorithm

class LocalBeamSearch(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, population=None, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        if population == None:
            population = []
            for _ in range(self.config.k):
                strand = self.config.create_strand()
                insert_tup(population, strand, self.fitness(strand), self.config.k)

        step_size = self.config.step_size
        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            new_population = []
            for strand in population:
                for n_strand in self.config.get_neighbors(strand[1], step_size=step_size):
                    insert_tup(new_population, n_strand, self.fitness(n_strand), self.config.k)

                    if self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
                        population = new_population
                        break
            
            if step_size != None:
                step_size = self.config.step_size * (1 - (self.fitness_calculations / self.config.FITNESS_CALCULATIONS))
                
            population = new_population

        return population[0]
