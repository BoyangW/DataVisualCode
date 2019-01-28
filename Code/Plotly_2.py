### Plotly Visual 2 ###########################################################
###############################################################################
df_A_S = pd.read_csv('suicide_data.csv',usecols=['year','suicides_no'])

# get rid of outliers
col_names =  ['year', 'suicides_no']
df_temp  = pd.DataFrame(columns = col_names)
yearList = df_A_S['year'].unique()
for i in yearList:
    noL = df_A_S.loc[df_A_S['year'] == i]['suicides_no']
    elements = np.array(noL)
    mean = np.mean(elements, axis=0)
    sd = np.std(elements, axis=0)
    final_list = [x for x in noL if (x > mean - 2 * sd)]
    final_list = [x for x in final_list if (x < mean + 2 * sd)]
    
    yearL = [i] * len(final_list)
    
    add_list = pd.DataFrame(
    {'year': yearL,
     'suicides_no': final_list
    })
    
    df_temp = df_temp.append(add_list)
    
df_A_S = df_temp

data = []
for i in range(0,len(pd.unique(df_A_S['year']))):
    trace = {
            "type": 'violin',
            "x": df_A_S['year'][df_A_S['year'] == pd.unique(df_A_S['year'])[i]],
            "y": df_A_S['suicides_no'][df_A_S['year'] == pd.unique(df_A_S['year'])[i]],
            "name": str(pd.unique(df_A_S['year'])[i]),
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            }
        }
    data.append(trace)

        
fig = {
    "data": data,
    "layout" : {
        "title": "",
        "yaxis": {
            "zeroline": False,
        }
    }
}


py.iplot(fig, filename='multiple', validate = False)
plotly.offline.plot(fig, filename = "plotly_2.html")