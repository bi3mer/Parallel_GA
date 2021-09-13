from Utility.PriorityQueue import insert_tup
from math import ceil, floor, sqrt

def __initialize_vertice_population(config):
    vertices = []
    for _ in range(config.population_size // config.strands_per_cell):
        population = []
        for __ in range(config.strands_per_cell):
            strand = config.create_strand()
            population.append((config.fitness(strand), strand))
            insert_tup(population, strand, config.fitness(strand), config.strands_per_cell)

        vertices.append(population)

    return vertices

def ring_lattice(config):
    vertices = __initialize_vertice_population(config)

    edges = {}
    for v in range(len(vertices)):
        edges[v] = ((v-1) % len(vertices), (v+1) % len(vertices))

    return vertices, edges

def cell(config):
    vertices = __initialize_vertice_population(config)

    '''
    Cell structure is a grid where cells connect in the four cardinal directions
    (north, east, south, and west). We need to upscale the 1 dimensional vertices
    array to a matrix. We don't do this literally but we do create a mapping so 
    that we can build the edges. 

    First, we can find the most compact matrix representation. This is accomplished
    by taking the ceiling of the square root of the length of the vertices array. 
    This tells us the largest square matrix. It doesn't mean we will use all the
    space. 
    '''
    DIR = ((0,1), (0,-1), (1,0), (-1,0))
    num_vertices = len(vertices)
    row_size = ceil(sqrt(num_vertices)) # row size and col size would be the same

    def index_to_coordinate(index):
        row = floor(index / row_size)
        col = index % row_size

        return row, col

    def coordinate_to_index(row, col):
        return row * row_size + col
    
    edges = {}
    for v in range(num_vertices):
        edges[v] = []
        v_row, v_col = index_to_coordinate(v)
        for direction in DIR:
            new_row, new_col = v_row + direction[0], v_col + direction[1]
            new_index = coordinate_to_index(new_row, new_col)
            if new_index < num_vertices:
                edges[v].append(new_index)

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
