from collections import namedtuple

import sqlite3
import json

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
        epochs_till_migration INT NOT NULL,
        strand_size INT NOT NULL,
        fitness_calculations FLOAT NOT NULL,
        runs INT NOT NULL,
        algorithm TEXT NOT NULL
    );
''')

con.execute('''
    CREATE TABLE IF NOT EXISTS result (
        result_id INTEGER PRIMARY KEY AUTOINCREMENT,
        config_id INT NOT NULL,
        time FLOAT NOT NULL,
        strand TEXT NOT NULL,
        fitness FLOAT NOT NULL,
        order_index INT NOT NULL
    );
''')

Config = namedtuple('Config', [
    'config_id',
    'name',
    'population_size',
    'num_elites_ga',
    'num_elites_network',
    'strands_per_cell',
    'crossover_rate',
    'mutation_rate',
    'migration_rate',
    'epochs_till_migration',
    'strand_size',
    'fitness_calculations',
    'runs',
    'algorithm'
])

Result = namedtuple('Result', [
    'result_id',
    'config_id',
    'time',
    'strand',
    'fitness',
    'order_index'
])

def insert_config_slash_exists(config, runs, alg_name):
    sql_config = con.execute(f'''
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
            epochs_till_migration = {config.epochs_till_migration} AND
            strand_size = {config.strand_size} AND
            fitness_calculations = {config.FITNESS_CALCULATIONS} AND 
            runs = {runs} AND
            algorithm = "{alg_name}"
    ''')
    rows = sql_config.fetchall()

    if len(rows) == 0:
        # add config to db if it does not already exists
        con.execute(f'''
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
                    epochs_till_migration,
                    strand_size ,
                    fitness_calculations,
                    runs,
                    algorithm
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
                    {config.epochs_till_migration},
                    {config.strand_size},
                    {config.FITNESS_CALCULATIONS},
                    {runs},
                    "{alg_name}"
                )
        ''')

        con.commit()
        return False
    else:
        return True
    
def store(config, runs, alg_name, strands, times, fitnesses):
    assert len(strands) == len(times)
    assert len(strands) == len(fitnesses)

    # get config_id
    sql_config = con.execute(f'''
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
            epochs_till_migration = {config.epochs_till_migration} AND
            strand_size = {config.strand_size} AND
            fitness_calculations = {config.FITNESS_CALCULATIONS} AND
            runs = {runs} AND
            algorithm = "{alg_name}"
    ''')
    rows = sql_config.fetchall()

    assert len(rows) == 1
    config_id = rows[0][0]

    # store results
    for i in range(len(times)):
        con.execute(f'''
            INSERT INTO result 
                (
                    config_id,
                    time,
                    strand,
                    fitness,
                    order_index
                )
            VALUES
                (
                    {config_id},
                    {times[i]},
                    "{json.dumps(strands[i])}",
                    {fitnesses[i]},
                    {i}
                )
        ''')

    con.commit()

def save_and_quit():
    con.commit()
    con.close()