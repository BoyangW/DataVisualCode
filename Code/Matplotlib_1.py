### Matplotlib Visual 1 #######################################################
###############################################################################
df_C_S = pd.read_csv('suicide_data.csv',usecols=['country','suicides_no']).fillna(0)
dfcountry = df_C_S.groupby('country')
pdConcatOverall=pd.DataFrame()
for each,value in dfcountry:
    k= pd.DataFrame(pd.Series(int(np.sum(value['suicides_no']))),columns=['Total_Suicide_Num'])
    country = pd.DataFrame(pd.Series(str(each)),columns=['Country'])
    pdConcat= pd.concat([country,k],axis=1)
    pdConcatOverall =pd.concat([pdConcatOverall,pdConcat],ignore_index=True)

# Sort the results descendingly
pdConcatOverall.sort_values(by=['Total_Suicide_Num'],ascending=False,inplace=True)

# Draw the visual in donut chart
plt.figure(figsize=(20,15))
plt.pie(x=pdConcatOverall['Total_Suicide_Num'][0:10],
        labels=pdConcatOverall['Country'][0:10],autopct='%.1f')
inCircle = plt.Circle((0,0),0.65,fc='white',linewidth=2.5,color='black')
x=plt.gcf()
x.gca().add_artist(inCircle)
plt.legend()
plt.axis('equal')
plt.title('Top 10 Country having Suicide rates\' percentage',fontsize=20)

plt.savefig('plt_1.png') # Save into png
plt.show()
###############################################################################