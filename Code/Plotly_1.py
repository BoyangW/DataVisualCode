### Plotly Visual 1 ###########################################################
###############################################################################
df_A_1 = pd.read_csv('suicide_data.csv',usecols=['age','suicides_no'])
df_A_2 = pd.read_csv('suicide_data.csv',usecols=['age','population'])

df_age = df_A_1.groupby('age').sum()
df_age_p = df_A_2.groupby('age').sum()
df_age['age'] = df_age.index
df_age_p['age'] = df_age_p.index
df_age_whole = pd.merge(df_age, df_age_p, on='age')

df_age_whole = df_age_whole.sort_values(by = ['suicides_no'])

trace0 = go.Bar(x = df_age_whole['population'],
                y = df_age_whole['age'],
                marker = dict(color = '#BF5959', 
                              line = dict(
                                  color = '#FFFEA6', width = 1) 
                             ),
               name = "Population Size",
               orientation = "h"
               )
                              
trace1 = go.Scatter(x = df_age_whole['suicides_no'],
                    y = df_age_whole['age'],
                    mode='lines+markers',
                    line=dict(
                        color='#5079DC'),
                    name='Suicides Number')

fig = tools.make_subplots(rows=1, cols=2)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig['layout'].update(title='Population and Suicide Number by Age Groups')

py.plot(fig, filename = 'ployly_sub_bar_scatter', auto_open = True)
plotly.offline.plot(fig, filename = "testt.html")
###############################################################################