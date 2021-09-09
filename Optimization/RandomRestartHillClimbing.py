from random import seed
from time import time

class RandomRestartHillClimbing:
    def __init__(self, config, rng_seed=None):
        self.config = config

        if seed != None:
            seed(rng_seed)

    def run(self):
        best_strand = None
        best_fitness = 1000000

        start_time = time()
        run_time = start_time + self.config.run_time
        while run_time > time():
            strand = self.config.create_strand()
            fitness = self.config.fitness(strand)

            update_made = True

            while update_made and run_time > time():
                update_made = False
                neighbors = self.config.get_neighbors(strand)
                for new_strand in neighbors:
                    new_fitness = self.config.fitness(new_strand)
                    if new_fitness < fitness:
                        update_made = True
                        strand = new_strand
                        fitness = new_fitness

            if fitness < best_fitness:
                best_strand = strand
                best_fitness = fitness

        return best_fitness, best_strand
