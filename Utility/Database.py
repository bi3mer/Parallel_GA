import sqlite3

con = sqlite3.connect('my_db.db')

con.execute('''
    CREATE TABLE IF NOT EXISTS config (
        config_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        population_size INT NOT NULL,
        num_elites_ga INT NOT NULL,
        num_elites_network INT NOT NULL,
        strands_per_cell INT NOT NULL,
        crossover_rate FLOAT NOT NULL,
        mutation_rate FLOAT NOT NULL,
        migration_rate FLOAT NOT NULL,
        strand_size INT NOT NULL,
        fitness_calculations FLOAT NOT NULL
    );
''')

con.execute('''
    CREATE TABLE IF NOT EXISTS result (
        result_id INTEGER PRIMARY KEY AUTOINCREMENT,
        config_id INT NOT NULL,
        time FLOAT NOT NULL,
        strand TEXT NOT NULL,
        fitness FLOAT NOT NULL,
        algorithm TEXT NOT NULL,
        order_index INT NOT NULL
    );
''')

def store(config, alg_name, strands, times, fitnesses):
    config_exists_query = f'''
        SELECT * 
        FROM config 
        WHERE
            name = "{config.NAME}" AND
            population_size = {config.population_size} AND
            num_elites_ga  = {config.num_elites_ga} AND
            num_elites_network = {config.num_elites_network} AND
            strands_per_cell= {config.strands_per_cell} AND
            crossover_rate= {config.crossover_rate} AND
            mutation_rate = {config.mutation_rate} AND
            migration_rate = {config.migration_rate} AND
            strand_size = {config.strand_size} AND
            fitness_calculations = {config.FITNESS_CALCULATIONS}
    '''
    sql_config = con.execute(config_exists_query)
    rows = sql_config.fetchall()

    if len(rows) == 0:
        a = f'''
            INSERT INTO config 
                (
                    name,
                    population_size,
                    num_elites_ga,
                    num_elites_network,
                    strands_per_cell,
                    crossover_rate,
                    mutation_rate,
                    migration_rate,
                    strand_size ,
                    fitness_calculations
                )
            VALUES
                (
                    "{config.NAME}",
                    {config.population_size},
                    {config.num_elites_ga} ,
                    {config.num_elites_network},
                    {config.strands_per_cell},
                    {config.crossover_rate},
                    {config.mutation_rate},
                    {config.migration_rate},
                    {config.strand_size},
                    {config.FITNESS_CALCULATIONS}
                )
        '''
        print(a)
        print()
        con.execute(a)

    con.commit()

def save_and_quit():
    con.commit()
    con.close()