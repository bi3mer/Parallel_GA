from .Algorithm import Algorithm

class HillClimber(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def run(self, population=None, calculations=None, rng_seed=None):
        if population == None:
            strand = self.config.create_strand()
            fitness = self.fitness(strand)
        else:
            fitness, strand = population[0]

        if calculations == None:
            calculations = self.config.FITNESS_CALCULATIONS

        step_size = self.config.step_size

        update_made = True
        while update_made and self.fitness_calculations <= calculations:
            update_made = False
            for new_strand in self.config.get_neighbors(strand, step_size=step_size):
                new_fitness = self.fitness(new_strand)
                if new_fitness < fitness:
                    update_made = True
                    strand = new_strand
                    fitness = new_fitness
                    break # greedy implementation

            if step_size != None and not update_made and step_size > 1e-6:
                step_size = self.config.step_size * (1 - (self.fitness_calculations / self.config.FITNESS_CALCULATIONS))
                update_made = True

        return fitness, strand
