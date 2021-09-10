from time import time

def hill_climb(fitness, strand, config, stop_time, greedy=False):
    update_made = True

    while update_made and stop_time > time():
        update_made = False
        neighbors = config.get_neighbors(strand)
        for new_strand in neighbors:
            new_fitness = config.fitness(new_strand)
            if new_fitness < fitness:
                update_made = True
                strand = new_strand
                fitness = new_fitness

                if greedy:
                    break

    return fitness, strand
