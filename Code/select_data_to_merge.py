import pandas as pd 
df=pd.read_csv('air_processed_data_after_aqi.csv')
wf=pd.read_csv('weather_final.csv')


k=0
jndex=[i for i in range(0,1088)]
kf=pd.DataFrame(columns=['DATE','T', 'Po', 'P', 'Pa','U'],index=jndex)
#kf.head()

#kf.append(wf.iloc[1])
#kf.append(wf.iloc[12])

for i in range(0,8699,8):
    kf.iloc[k]=pd.Series({'DATE':wf['DATE'].iloc[i],'T':wf['T'].iloc[i],'Po':wf['Po'].iloc[i],'P':wf['P'].iloc[i],'Pa':wf['Pa'].iloc[i],'U':wf['U'].iloc[i]})
    k+=1
result = pd.merge(df,kf, on='DATE')
result.to_csv('data_merged.csv',sep=',')