### Plotly Visual 3 ###########################################################
###############################################################################
df_3 = pd.read_csv('suicide_data.csv',usecols=['country','suicides_no'])
df_3 = df_3.groupby('country').sum()
df_3['country'] = df_3.index
df_3 = df_3.sort_values(by = ['suicides_no'], ascending = False)
df_3 = df_3.reset_index(drop=True)
df_3['rank'] = df_3.index + 1

df_3['text'] = df_3['country'] + '<br>' +\
    'Suicides Number: ' + df_3['suicides_no'].astype(str) + '<br>'+\
    'Rank in the world: ' + df_3['rank'].astype(str)


data = [dict(
            type = 'choropleth',
            locationmode = 'country names',
            locations = df_3['country'],
            z = df_3['suicides_no'],
            text = df_3['text'],
            colorscale = 'Greens',
            autocolorscale = False,
            reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 0.01
                    ) 
                ),
            colorbar = dict(
                title = 'Number'
                ),
            ) 
        ]
        
layout = dict(
    title = 'Suicides Number World Map',
    geo = dict(
        showframe = False,
        showcoastlines = False
    )
)
        
fig = dict(data = data, layout = layout)
py.iplot(fig, filename='map', validate = False)
plotly.offline.plot(fig, filename = "plotly_3.html")
###############################################################################