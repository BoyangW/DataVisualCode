### Seaborn 2 #################################################################
plt.figure(figsize=(30,20))
stats_df = df_pk.drop(['Total', 'Generation', 'Legendary'], axis=1)
melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], 
                    var_name="Stat")
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
sns.swarmplot(x='Stat', 
              y='value', 
              data=melted_df, 
              hue='Type 1', 
              split=True,
              palette=pkmn_type_colors)
 
plt.ylim(0, 260)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.title("Swarm Plot of Pokemon Stats by Type", fontsize=60)
plt.savefig('seaborn_2.png')
###############################################################################