from time import time


class HillClimber:
    def __init__(self, config):
        self.config = config

    def run(self, population=None, stop_time=None, rng_seed=None):
        if population == None:
            strand = self.config.create_strand()
            fitness = self.config.fitness(strand)
        else:
            fitness, strand = population[0]
        
        if stop_time == None:
            stop_time = time() + self.config.run_time

        step_size = self.config.step_size
        start_time = time()
        total_time = stop_time - start_time

        update_made = True
        while update_made and stop_time > time():
            update_made = False
            for new_strand in self.config.get_neighbors(strand, step_size=step_size):
                new_fitness = self.config.fitness(new_strand)
                if new_fitness < fitness:
                    update_made = True
                    strand = new_strand
                    fitness = new_fitness
                    break # greedy implementation

            if step_size != None and not update_made and step_size > 1e-6:
                step_size = self.config.step_size * (1 - ((time() - start_time) / total_time))
                update_made = True

        return fitness, strand
