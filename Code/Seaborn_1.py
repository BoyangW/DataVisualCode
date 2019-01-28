### Seaborn 1 #################################################################
df_pk_1 = df_pk[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']]

# Calculate correlations
corr = df_pk_1.corr()
 
# Heatmap
sns.set(rc={'figure.figsize':(30,18)}, font_scale=2.8)
sns.heatmap(corr, robust = True, annot=True, cmap="YlGnBu")
plt.title("Correlation Map of Pokemon Stats", fontsize=60)
plt.savefig('seaborn_1.png')
###############################################################################