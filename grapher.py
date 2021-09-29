from Utility import Database as db

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import numpy as np

# Epochs till migration graph
df = pd.DataFrame(columns=['Algorithm', 'Epoch', 'Migration Rate', 'Fitness'])

configs = db.con.execute('''
    select * 
    from config 
    where 
        name="TSP" and 
        population_size=320 
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
            'Epoch': c.epochs_till_migration,
            'Migration Rate': c.migration_rate,
            'Fitness': r.fitness
        }, ignore_index=True)


df_full = df[df['Algorithm'] == 'Island GA Ring Lattice']

X, Y = np.meshgrid(df_full['Epoch'], df_full['Migration Rate'])
# X = [1,2,3,4,5]
# Y = [1,3,5,7,9]
# Z = [1,4,9,25,36]
# X,Y = np.meshgrid(X, Y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# surf = ax.plot_wireframe(X, Y, np.array([[x] for x in df_full['Fitness']]))
# surf = ax.plot_wireframe(X, Y, np.array([[x] for x in df_full['Fitness']]))
# ax.scatter(df_full['Epoch'], df_full['Migration Rate'], np.array([[x] for x in df_full['Fitness']]))
ax.plot_trisurf(df_full['Epoch'], df_full['Migration Rate'], df_full['Fitness'])
plt.show()

# sns.set_theme(style="darkgrid")

# sns.lineplot(data=df, x='Fitness Calculations', y='Fitness', hue='Algorithm')
# plt.show()