from Utility import Timer
from .Algorithm import Algorithm

class HillClimber(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, population=None, run_time=None, rng_seed=None):
        timer = Timer()
        if run_time == None:
            timer.start(self.config.run_time)
        else:
            timer.start(run_time)

        if population == None:
            strand = self.config.create_strand()
            fitness = self.fitness(strand)
        else:
            fitness, strand = population[0]

        step_size = self.config.step_size

        update_made = True
        while update_made and not timer.is_done():
            update_made = False
            for new_strand in self.config.get_neighbors(strand, step_size=step_size):
                new_fitness = self.fitness(new_strand)
                if new_fitness < fitness:
                    update_made = True
                    strand = new_strand
                    fitness = new_fitness
                    break # greedy implementation

            if step_size != None and not update_made and step_size > 1e-6:
                step_size = self.config.step_size * (1 - timer.percent_done())
                update_made = True

        return fitness, strand
