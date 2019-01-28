### Plotly Visual 5 ###########################################################
###############################################################################
df_pk = pd.read_csv('Pokemon.csv')
df_pk_1 = df_pk[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']]
group_labels = list(df_pk_1.columns)
pk_list = []
for i in group_labels:
    pk_list.append(df_pk_1[i].tolist())

fig = ff.create_distplot(pk_list, group_labels, bin_size=5)
fig['layout'].update(title='Distribution of All Pokemon Stats')
py.iplot(fig, filename='distplot', validate = False)
plotly.offline.plot(fig, filename = "plotly_5.html")
###############################################################################

### Plotly Visual 6 ###########################################################
###############################################################################
from bubbly.bubbly import bubbleplot 
df_bb = pd.read_csv('suicide_data.csv')
df_bb = df_bb.sort_values(by = ['year'])
df_bb['rate'] = df_bb['suicides_no'] / df_bb['population']

figure = bubbleplot(dataset=df_bb, x_column='population', y_column='suicides_no', 
    bubble_column='country', time_column='year', size_column='suicides_no', 
    color_column='age', x_title="Population", 
    y_title="Suicides Number", 
    title='Suicides/Population Bubble Plot by Age Groups 1979-2016',
    x_logscale=True, scale_bubble=3, height=650)

py.iplot(figure, filename='nbplot', validate = False)
plotly.offline.plot(figure, filename = "plotly_6.html")
###############################################################################