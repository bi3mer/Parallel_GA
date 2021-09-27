from Utility import Database as db

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

## Epochs till migration graph
df = pd.DataFrame(columns=['Algorithm', 'Fitness Calculations', 'Fitness'])

configs = db.con.execute('''
    select * 
    from config 
    where 
        name="TSP" and 
        population_size=320 and
        epochs_till_migration = 2
    order by 
        fitness_calculations
''').fetchall()

for unnamed_tuple in configs:
    c = db.Config(*unnamed_tuple)

    results = db.con.execute(f'''
        select *
        from result
        where
            config_id={c.config_id}
        order by
            order_index
    ''').fetchall()

    for unnamed_result in results:
        r = db.Result(*unnamed_result)
        
        df = df.append({
            'Algorithm': c.algorithm,
            'Fitness Calculations': c.fitness_calculations,
            'Fitness': r.fitness
        }, ignore_index=True)


sns.set_theme(style="darkgrid")

sns.lineplot(data=df, x='Fitness Calculations', y='Fitness', hue='Algorithm')
plt.show()