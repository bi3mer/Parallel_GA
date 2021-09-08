from Utility.PriorityQueue import insert_tup

def ring_lattice(config):
    vertices = []
    for _ in range(config.population_size // config.strands_per_cell):
        population = []
        for __ in range(config.strands_per_cell):
            strand = config.create_strand()
            population.append((config.fitness(strand), strand))
            insert_tup(population, strand, config.fitness(strand), config.strands_per_cell)

        vertices.append(population)

    edges = {}
    for v in range(len(vertices)):
        edges[v] = ((v-1) % len(vertices), (v+1) % len(vertices))

    return vertices, edges

def cell(config):
    raise NotImplementedError()
    vertices = [[strand_initializer() for _ in range(strands_per_cell)] for __ in range(population_size / strands_per_cell)]
    edges = []
    
    return vertices, edges

def hier(config):
    raise NotImplementedError()
    vertices = [[strand_initializer() for _ in range(strands_per_cell)] for __ in range(population_size / strands_per_cell)]
    edges = []
    
    return vertices, edges

def rcave(config):
    raise NotImplementedError()
    vertices = [[strand_initializer() for _ in range(strands_per_cell)] for __ in range(population_size / strands_per_cell)]
    edges = []
    
    return vertices, edges
