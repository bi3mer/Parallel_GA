from random import seed

from Utility.PriorityQueue import insert_tup
from Utility import Timer

class LocalBeamSearch:
    def __init__(self, config):
        self.config = config

    def run(self, population=None, run_time=None, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        timer = Timer()
        if run_time == None:
            timer.start(self.config.run_time)
        else:
            timer.start(run_time)

        if population == None:
            population = []
            for _ in range(self.config.k):
                strand = self.config.create_strand()
                insert_tup(population, strand, self.config.fitness(strand), self.config.k)

        step_size = self.config.step_size
        while not timer.is_done():
            new_population = []
            for strand in population:
                for n_strand in self.config.get_neighbors(strand[1], step_size=step_size):
                    insert_tup(new_population, n_strand, self.config.fitness(n_strand), self.config.k)

                    if timer.is_done():
                        population = new_population
                        break
            
            if step_size != None:
                step_size = self.config.step_size * (1 - timer.percent_done())
                
            population = new_population

        return population[0]
