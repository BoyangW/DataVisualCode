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