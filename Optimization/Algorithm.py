class Algorithm:
    def __init__(self, config):
        self.config = config
        self.fitness_calculations = 0

    def fitness(self, strand):
        self.fitness_calculations += 1
        return self.config.fitness(strand)