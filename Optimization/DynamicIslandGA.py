from random import randint, seed
from itertools import repeat
from math import inf

from Utility.Stochastic import weighted_sample_tup
from Utility.PriorityQueue import insert_tup
from Utility.Math import get_slope_and_intercept
from .Algorithm import Algorithm


STRANDS_PER_CELL = 8

class DynamicIslandGA(Algorithm):
    def __init__(self, config):
        super().__init__(config)

    def __create_population(self):
        population = []
        for _ in repeat(None, STRANDS_PER_CELL):
            strand = self.config.create_strand()
            insert_tup(population, strand, self.fitness(strand), STRANDS_PER_CELL)

        return population

    def __average_percent_change(self, strand_fitness, strand, num_tested=100):
        '''
        Modified version of:
        https://github.com/fillipe-gsm/python-tsp/blob/master/python_tsp/heuristics/simulated_annealing.py
        '''
        fitness_change_sum = 0
        for _ in repeat(None, num_tested):
            new_strand = self.config.get_random_neighbor(strand, step_size=self.config.step_size)
            fitness_change_sum += abs(self.fitness(new_strand) / strand_fitness)

        return fitness_change_sum / num_tested

    def __run_ga(self, population, delta):
        update_made = False
        fitnesses = []
        x = []
        current_x = 0
        
        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            new_population = []

            # maintain one eliete between epochs
            new_population.append(population[0])

            # crossover and mutation for the rest
            while len(new_population) < STRANDS_PER_CELL:
                strands = map(lambda a: a[1], weighted_sample_tup(population, 2))
                for strand in self.config.crossover(*strands):
                    strand = self.config.mutate(strand)
                    fitness = self.fitness(strand)
                    insert_tup(new_population, strand, fitness, STRANDS_PER_CELL)

            population = new_population

            # break out if some level of convergence has occurred 
            if len(x) > 3:
                # slope, _ = get_slope_and_intercept(x[-2:], fitnesses[-2:])
                slope = abs(fitnesses[-1] / fitnesses[-2])
                if abs(slope) < delta:
                    update_made = True
                else:
                    break
            
            fitnesses.append(sum(a[0] for a in population) / STRANDS_PER_CELL)
            # fitnesses.append(population[0][0])
            # print([a[0] for a in population])
            x.append(current_x)
            current_x += 1

        return population, update_made

    def run(self, rng_seed=None):
        if seed != None:
            seed(rng_seed)

        # initialize population
        v = [self.__create_population()]

        # get delta percent change
        delta = self.__average_percent_change(*v[0][0])

        # begin run
        v_update_made = [True]
        while self.fitness_calculations <= self.config.FITNESS_CALCULATIONS:
            for v_index, v_update in enumerate(v_update_made):
                if not v_update:
                    continue

                # migrate if possible
                if len(v) > 1:
                    # random number that is not self. So we generate for [0, n-2] and 
                    # if we get the same as tgt_index than turn into n-1.
                    src_index = randint(0, len(v) - 2)
                    if v_index == src_index:
                        src_index = len(v) - 1

                    insert_tup(v[v_index], v[src_index][0][1].copy(), v[src_index][0][0], STRANDS_PER_CELL + 2)

                population, update_made = self.__run_ga(v[v_index], delta)
                v_update_made[v_index] = update_made
                v[v_index] = population

            # Only add new population when improvement is stagnant
            if not all(v_update_made):
                population = self.__create_population()
                population, _ = self.__run_ga(population, delta)

                # migrate elites to rest of the population to force spread of new population
                for tgt_index in range(len(v)):
                    insert_tup(v[tgt_index], population[0][1].copy(), population[0][0], STRANDS_PER_CELL + 2)
                    v_update_made[tgt_index] = True

                v.append(population)
                v_update_made = [True for _ in range(len(v_update_made))]
                v_update_made.append(True)

        best_strand = None
        best_fitness = inf

        for population in v:
            if population[0][0] < best_fitness:
                best_fitness = population[0][0]
                best_strand = population[0][1]

        return best_fitness, best_strand
