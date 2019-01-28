### Matplotlib Visual 2 #######################################################
###############################################################################
df_Y_S = pd.read_csv('suicide_data.csv',usecols=['year','suicides_no']).fillna(0)
df_Y_P = pd.read_csv('suicide_data.csv',usecols=['year','population']).fillna(0)
dfyear = df_Y_S.groupby('year').sum()
dfyear_p = df_Y_P.groupby('year').sum()
dfyear['year'] = dfyear.index
dfyear_p['year'] = dfyear_p.index

# Make masks for sucides number greater/less than the average for color changes
mean_s = dfyear['suicides_no'].mean()
mask1 = dfyear['suicides_no'] < mean_s
mask2 = dfyear['suicides_no'] >= mean_s

plt.figure(figsize=(20,15))
plt.subplot(211)
plt.bar(dfyear_p['year'][mask1], dfyear_p['population'][mask1], 
        label='Population (low suicide)', color = 'blue')
plt.bar(dfyear_p['year'][mask2], dfyear_p['population'][mask2], 
        label='Population (high suicide)', color = 'red')
plt.xlabel('Year')
plt.ylabel('Count of populaton')
plt.title('Population Number Through 1979 to 2016')
plt.legend()

plt.subplot(212)
plt.plot(dfyear['year'],dfyear['suicides_no'], label='Suicide Number')
plt.xlabel('Year')
plt.ylabel('Count of populaton')
plt.title('Suicides Number Through 1979 to 2016')
plt.legend()

plt.savefig('plt_2.png') # Save into png
plt.show()
###############################################################################