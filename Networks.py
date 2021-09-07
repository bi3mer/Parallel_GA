def ring_lattice(config):
    vertices = []
    for _ in range(config.population_size // config.strands_per_cell):
        population = []
        for __ in range(config.strands_per_cell):
            strand = config.create_strand()
            population.append((config.fitness(strand), strand))

        vertices.append(population)

    vertices = [[config.create_strand() for _ in range(config.strands_per_cell)] for __ in range(config.population_size // config.strands_per_cell)]
    edges = [(i-1, i) for i in range(len(vertices))] + [(i, i-1) for i in range(len(vertices))]
    edges.append((0, len(vertices)))
    edges.append((len(vertices), 0))

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
