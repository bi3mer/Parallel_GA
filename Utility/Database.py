# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS config
#     (
#         config_id INT PRIMARY KEY,
#         problem_name TEXT NOT NULL,
#         runs INT NOT NULL,
#         time REAL NOT NULL,
#         population_size INT NOT NULL,
#         strands_per_cell INT NOT NULL,
#         epochs_till_migration INT NOT NULL,
#         crossover_rate REAL NOT NULL,
#         migration_rate REAL NOT NULL,
#         mutation_rate REAL NOT NULL,
#         network_run_percentage REAL NOT NULL,
#         num_elites_ga INT NOT NULL,
#         num_elites_network INT NOT NULL
#     );
#     '''
# )
# sqllite3 doesn't have foreign keys in the version for pypy3. So, I need to make a custom DB :/