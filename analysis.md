
# DELHI AIR QUALITY ANALYSIS 

##### BY:- YAJUSH MISHRA
###### 02-03-2018

<ol type="1">
    <li> Data preparation, NA values
    <ul>
        <li>Importing Data </li>
        <li>Calculating Aqi </li>
        <li>Merging Data </li>
    </ul>
    <li> Data Visualisation</li>
    <li> Creating Models
    <ul>
        <li>Predictions</li>
        <li>Model Evaluation</li>
    </ul>
    <li>Conclusions
</ol>


```python
###load packages and csv file
import pandas as pd
import aqi
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


```

## 1. Data Preparation
     

####             1.1 Importing and processing air quality data
* Importing 


```python
## data is now processed and is ready for further estimation
df1=pd.read_json('https://data.gov.in/node/1144121/datastore/export/json')
df2=pd.read_json('https://data.gov.in/node/1144101/datastore/export/json')
df3=pd.read_json('https://data.gov.in/node/2927501/datastore/export/json')
df=pd.concat([df2,df1])
df=df[[2,4,1,7,8,9,10]]
df.columns=df3.iloc[0]
df=df.iloc[1:]
df3.columns=df3.iloc[0]
df3=df3.iloc[1:]
df3.head()
df=pd.concat([df,df3])
df.to_csv('air_processed_data.csv', sep=',', encoding='utf-8')
df.head()
## data is now processed and is ready for further estimation
##saving data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State/City</th>
      <th>Location</th>
      <th>DATE</th>
      <th>SO2</th>
      <th>NO2</th>
      <th>PM10</th>
      <th>PM2.5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>01-01-14</td>
      <td>4</td>
      <td>40</td>
      <td>154</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>01-06-14</td>
      <td>4</td>
      <td>41</td>
      <td>232</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>01-09-14</td>
      <td>4</td>
      <td>44</td>
      <td>402</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>15-01-14</td>
      <td>4</td>
      <td>46</td>
      <td>291</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>20-01-14</td>
      <td>4</td>
      <td>41</td>
      <td>289</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>
</div>



The data used for analysis is of year 2014-2016,this data is taken from data.gov.in website

#### 1.2 Calculating aqi index values using alogrithm by EPA


```python
#now importing processed data file
df=pd.read_csv('air_processed_data_new.csv')
```

###### Calculating aqi


```python
#print([i for i in df[['SO2','NO2','PM10']].values])
df['DATE'] =pd.to_datetime(df.DATE)
aqi_values=[int(aqi.to_aqi([(aqi.POLLUTANT_PM10,int(i[2])),(aqi.POLLUTANT_NO2_1H,int(i[1])),(aqi.POLLUTANT_SO2_1H,int(i[0])),(aqi.POLLUTANT_PM25,int(i[3]))],algo=aqi.ALGO_EPA )) for i in df[['SO2','NO2','PM10','PM2.5']].values]
df['aqi']=aqi_values
df.sort_values('DATE')
df.head()
#data after calculating aqi
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State/City</th>
      <th>Location</th>
      <th>DATE</th>
      <th>SO2</th>
      <th>NO2</th>
      <th>PM10</th>
      <th>PM2.5</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-01</td>
      <td>4</td>
      <td>40</td>
      <td>154</td>
      <td>0</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-06</td>
      <td>4</td>
      <td>41</td>
      <td>232</td>
      <td>0</td>
      <td>139</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-09</td>
      <td>4</td>
      <td>44</td>
      <td>402</td>
      <td>0</td>
      <td>268</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-15</td>
      <td>4</td>
      <td>46</td>
      <td>291</td>
      <td>0</td>
      <td>169</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-20</td>
      <td>4</td>
      <td>41</td>
      <td>289</td>
      <td>0</td>
      <td>168</td>
    </tr>
  </tbody>
</table>
</div>



#### Importing and processing weather data 


```python
wf=pd.read_csv('weather.csv')
wf['DATE'] =pd.to_datetime(wf.DATE).dt.date
wf.sort_values('DATE',ascending=True,inplace=True)
wf.reindex()
wf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATE</th>
      <th>T</th>
      <th>Po</th>
      <th>P</th>
      <th>Pa</th>
      <th>U</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8698</th>
      <td>2014-01-01</td>
      <td>13.6</td>
      <td>746.8</td>
      <td>765.8</td>
      <td>-0.3</td>
      <td>97</td>
    </tr>
    <tr>
      <th>8696</th>
      <td>2014-01-01</td>
      <td>11.8</td>
      <td>747.5</td>
      <td>766.6</td>
      <td>1.2</td>
      <td>100</td>
    </tr>
    <tr>
      <th>8695</th>
      <td>2014-01-01</td>
      <td>15.6</td>
      <td>748.2</td>
      <td>767.1</td>
      <td>0.7</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8694</th>
      <td>2014-01-01</td>
      <td>17.6</td>
      <td>746.4</td>
      <td>765.1</td>
      <td>-1.8</td>
      <td>78</td>
    </tr>
    <tr>
      <th>8693</th>
      <td>2014-01-01</td>
      <td>15.6</td>
      <td>745.8</td>
      <td>764.7</td>
      <td>-0.6</td>
      <td>87</td>
    </tr>
  </tbody>
</table>
</div>



### 1.3 Merging Data 
##### This python script merges the data and saves in a new file


```python
%run -i 'select_data_to_merge.py'
```


```python
df=pd.read_csv('data_merged.csv')
#df.set_index('DATE', inplace=True)
df.head()
## this is merged data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State/City</th>
      <th>Location</th>
      <th>DATE</th>
      <th>SO2</th>
      <th>NO2</th>
      <th>PM10</th>
      <th>PM2.5</th>
      <th>aqi</th>
      <th>T</th>
      <th>Po</th>
      <th>P</th>
      <th>Pa</th>
      <th>U</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-01</td>
      <td>4</td>
      <td>40</td>
      <td>154</td>
      <td>0</td>
      <td>100</td>
      <td>13.6</td>
      <td>746.8</td>
      <td>765.8</td>
      <td>-0.3</td>
      <td>97</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-01</td>
      <td>4</td>
      <td>40</td>
      <td>212</td>
      <td>0</td>
      <td>129</td>
      <td>13.6</td>
      <td>746.8</td>
      <td>765.8</td>
      <td>-0.3</td>
      <td>97</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-06</td>
      <td>4</td>
      <td>41</td>
      <td>232</td>
      <td>0</td>
      <td>139</td>
      <td>26.2</td>
      <td>735.2</td>
      <td>753.1</td>
      <td>2.6</td>
      <td>72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-06</td>
      <td>4</td>
      <td>40</td>
      <td>190</td>
      <td>0</td>
      <td>118</td>
      <td>26.2</td>
      <td>735.2</td>
      <td>753.1</td>
      <td>2.6</td>
      <td>72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-09</td>
      <td>4</td>
      <td>44</td>
      <td>402</td>
      <td>0</td>
      <td>268</td>
      <td>0.0</td>
      <td>744.0</td>
      <td>751.3</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



##  2. Data Visualization


```python
%matplotlib inline
def getMonth(s):
  return s.split("-")[1]
df['month']= df['DATE'].apply(lambda x: getMonth(x))
def getYear(s):
  return s.split("-")[0]
df['year']= df['DATE'].apply(lambda x: getYear(x))
kf=df.groupby(['month'])
kf=kf.mean()
listval=['january','february','march','april','may','june','july','august','september','october','november','december']
kf.index=listval
ax=kf['aqi'].plot(kind="bar",figsize=(15,7),grid=True,title="Average Air Quality Month Wise",use_index=True,legend=False)
ax.set_ylabel("Aqi")
ax.set_xlabel("Months")
```




    Text(0.5,0,'Months')




![png](output_16_1.png)


This graph shows that average aqi is higher in winter seasons of November and December.This rise in aqi can be attributed to crop residue burning and as well as low wind speed during these months. 


```python
lf=df.groupby(['year']).mean()
ax=lf['aqi'].plot(kind='bar',figsize=(14,6),grid=True,title="Average Air Quality Year Wise",use_index=True,legend=False)
ax.set_ylabel("Aqi")
```




    Text(0,0.5,'Aqi')




![png](output_18_1.png)


As shown in the above graph the average air quality of 2016 was very high as compared to previous years.


```python
jf=df.groupby(['year','month']).mean()
listval=['january','february','march','april','may','june','july','august','september','october','november','december','january','february','march','april','may','june','july','august','september','october','november','december','january','march','april','may','june','july','september','october']
jf.index=listval
ax=jf['aqi'].plot(x='year',kind='bar',figsize=(15,6),title='Average Aqi Month Wise')
ax.set_xlabel("year 2014                                                                          year 2015                                                                                year 2016")
ax.set_ylabel("Aqi")
```




    Text(0,0.5,'Aqi')




![png](output_20_1.png)


This graph shows average aqi month wise over years.


```python
df.plot(x='T',y='aqi',kind='scatter',figsize=(15,5),title="AQI vs TEMPERATURE",legend=True)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdbd53c8780>




![png](output_22_1.png)


Scatter graph of aqi versus the temprature let us visualize how much it aqi deviates.


```python
df['month'] = df['month'].apply(pd.to_numeric)
df.plot(x='month',y='aqi',figsize=(16,6),use_index=True,kind='scatter',legend=True,title="AQI plot over MOTH")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdbd63c0128>




![png](output_24_1.png)


Scatter graph of aqi over month 

## 3. Creating Model to predict air quality

 ###   Correlation Chart


```python
df.corr(method='pearson', min_periods=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SO2</th>
      <th>NO2</th>
      <th>PM10</th>
      <th>PM2.5</th>
      <th>aqi</th>
      <th>T</th>
      <th>Po</th>
      <th>P</th>
      <th>Pa</th>
      <th>U</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>SO2</th>
      <td>1.000000</td>
      <td>0.475103</td>
      <td>0.184400</td>
      <td>-0.126112</td>
      <td>0.135903</td>
      <td>-0.117442</td>
      <td>0.033768</td>
      <td>0.040119</td>
      <td>0.020958</td>
      <td>0.036105</td>
      <td>-0.016684</td>
    </tr>
    <tr>
      <th>NO2</th>
      <td>0.475103</td>
      <td>1.000000</td>
      <td>0.357908</td>
      <td>-0.268020</td>
      <td>0.290300</td>
      <td>-0.182320</td>
      <td>0.024129</td>
      <td>0.037788</td>
      <td>0.018222</td>
      <td>0.009554</td>
      <td>0.103767</td>
    </tr>
    <tr>
      <th>PM10</th>
      <td>0.184400</td>
      <td>0.357908</td>
      <td>1.000000</td>
      <td>0.120394</td>
      <td>0.898631</td>
      <td>-0.249425</td>
      <td>0.074569</td>
      <td>0.090393</td>
      <td>0.012017</td>
      <td>-0.013655</td>
      <td>0.106433</td>
    </tr>
    <tr>
      <th>PM2.5</th>
      <td>-0.126112</td>
      <td>-0.268020</td>
      <td>0.120394</td>
      <td>1.000000</td>
      <td>0.326136</td>
      <td>0.042689</td>
      <td>0.012926</td>
      <td>0.007516</td>
      <td>-0.027043</td>
      <td>-0.045059</td>
      <td>0.038708</td>
    </tr>
    <tr>
      <th>aqi</th>
      <td>0.135903</td>
      <td>0.290300</td>
      <td>0.898631</td>
      <td>0.326136</td>
      <td>1.000000</td>
      <td>-0.213258</td>
      <td>0.060212</td>
      <td>0.068750</td>
      <td>0.011573</td>
      <td>-0.025687</td>
      <td>0.110475</td>
    </tr>
    <tr>
      <th>T</th>
      <td>-0.117442</td>
      <td>-0.182320</td>
      <td>-0.249425</td>
      <td>0.042689</td>
      <td>-0.213258</td>
      <td>1.000000</td>
      <td>-0.087029</td>
      <td>-0.145159</td>
      <td>-0.215880</td>
      <td>-0.665794</td>
      <td>0.022948</td>
    </tr>
    <tr>
      <th>Po</th>
      <td>0.033768</td>
      <td>0.024129</td>
      <td>0.074569</td>
      <td>0.012926</td>
      <td>0.060212</td>
      <td>-0.087029</td>
      <td>1.000000</td>
      <td>0.894964</td>
      <td>0.023413</td>
      <td>0.034238</td>
      <td>-0.032088</td>
    </tr>
    <tr>
      <th>P</th>
      <td>0.040119</td>
      <td>0.037788</td>
      <td>0.090393</td>
      <td>0.007516</td>
      <td>0.068750</td>
      <td>-0.145159</td>
      <td>0.894964</td>
      <td>1.000000</td>
      <td>0.028188</td>
      <td>0.007997</td>
      <td>-0.051568</td>
    </tr>
    <tr>
      <th>Pa</th>
      <td>0.020958</td>
      <td>0.018222</td>
      <td>0.012017</td>
      <td>-0.027043</td>
      <td>0.011573</td>
      <td>-0.215880</td>
      <td>0.023413</td>
      <td>0.028188</td>
      <td>1.000000</td>
      <td>0.293983</td>
      <td>-0.015816</td>
    </tr>
    <tr>
      <th>U</th>
      <td>0.036105</td>
      <td>0.009554</td>
      <td>-0.013655</td>
      <td>-0.045059</td>
      <td>-0.025687</td>
      <td>-0.665794</td>
      <td>0.034238</td>
      <td>0.007997</td>
      <td>0.293983</td>
      <td>1.000000</td>
      <td>-0.035513</td>
    </tr>
    <tr>
      <th>month</th>
      <td>-0.016684</td>
      <td>0.103767</td>
      <td>0.106433</td>
      <td>0.038708</td>
      <td>0.110475</td>
      <td>0.022948</td>
      <td>-0.032088</td>
      <td>-0.051568</td>
      <td>-0.015816</td>
      <td>-0.035513</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



The correlation chart shows correlation coefficient between various features,Interestingly the coefficient of correlation between T and aqi is -ve showcasing that if temprature drops aqi increases and viceversa.


```python
def getSeason(x):
    if x in range(1,4):
        return 0
    elif x in range(4,6):
        return 1
    elif x in range(6,9):
        return 2
    else:
        return 3
df['season']=df['month'].apply(lambda x:getSeason(x))
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State/City</th>
      <th>Location</th>
      <th>DATE</th>
      <th>SO2</th>
      <th>NO2</th>
      <th>PM10</th>
      <th>PM2.5</th>
      <th>aqi</th>
      <th>T</th>
      <th>Po</th>
      <th>P</th>
      <th>Pa</th>
      <th>U</th>
      <th>month</th>
      <th>year</th>
      <th>season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-01</td>
      <td>4</td>
      <td>40</td>
      <td>154</td>
      <td>0</td>
      <td>100</td>
      <td>13.6</td>
      <td>746.8</td>
      <td>765.8</td>
      <td>-0.3</td>
      <td>97</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-01</td>
      <td>4</td>
      <td>40</td>
      <td>212</td>
      <td>0</td>
      <td>129</td>
      <td>13.6</td>
      <td>746.8</td>
      <td>765.8</td>
      <td>-0.3</td>
      <td>97</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-06</td>
      <td>4</td>
      <td>41</td>
      <td>232</td>
      <td>0</td>
      <td>139</td>
      <td>26.2</td>
      <td>735.2</td>
      <td>753.1</td>
      <td>2.6</td>
      <td>72</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-06</td>
      <td>4</td>
      <td>40</td>
      <td>190</td>
      <td>0</td>
      <td>118</td>
      <td>26.2</td>
      <td>735.2</td>
      <td>753.1</td>
      <td>2.6</td>
      <td>72</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-09</td>
      <td>4</td>
      <td>44</td>
      <td>402</td>
      <td>0</td>
      <td>268</td>
      <td>0.0</td>
      <td>744.0</td>
      <td>751.3</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-09</td>
      <td>4</td>
      <td>67</td>
      <td>379</td>
      <td>0</td>
      <td>235</td>
      <td>0.0</td>
      <td>744.0</td>
      <td>751.3</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Delhi</td>
      <td>Mayapuri Industrial Area, Delhi</td>
      <td>2014-01-09</td>
      <td>18</td>
      <td>100</td>
      <td>604</td>
      <td>0</td>
      <td>500</td>
      <td>0.0</td>
      <td>744.0</td>
      <td>751.3</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Delhi</td>
      <td>Town Hall, Ayurvedic Dispensary, Chandni Chowk...</td>
      <td>2014-01-09</td>
      <td>14</td>
      <td>106</td>
      <td>541</td>
      <td>0</td>
      <td>437</td>
      <td>0.0</td>
      <td>744.0</td>
      <td>751.3</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-15</td>
      <td>4</td>
      <td>46</td>
      <td>291</td>
      <td>0</td>
      <td>169</td>
      <td>11.4</td>
      <td>746.0</td>
      <td>765.1</td>
      <td>1.4</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-15</td>
      <td>5</td>
      <td>60</td>
      <td>380</td>
      <td>0</td>
      <td>237</td>
      <td>11.4</td>
      <td>746.0</td>
      <td>765.1</td>
      <td>1.4</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Delhi</td>
      <td>N-Y- SCHOOL, Sarojini Nagar, Delhi</td>
      <td>2014-01-15</td>
      <td>19</td>
      <td>113</td>
      <td>396</td>
      <td>0</td>
      <td>260</td>
      <td>11.4</td>
      <td>746.0</td>
      <td>765.1</td>
      <td>1.4</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Delhi</td>
      <td>Town Hall, Ayurvedic Dispensary, Chandni Chowk...</td>
      <td>2014-01-15</td>
      <td>10</td>
      <td>114</td>
      <td>499</td>
      <td>0</td>
      <td>394</td>
      <td>11.4</td>
      <td>746.0</td>
      <td>765.1</td>
      <td>1.4</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-20</td>
      <td>4</td>
      <td>41</td>
      <td>289</td>
      <td>0</td>
      <td>168</td>
      <td>21.6</td>
      <td>746.3</td>
      <td>764.8</td>
      <td>-2.0</td>
      <td>56</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-20</td>
      <td>4</td>
      <td>44</td>
      <td>222</td>
      <td>0</td>
      <td>134</td>
      <td>21.6</td>
      <td>746.3</td>
      <td>764.8</td>
      <td>-2.0</td>
      <td>56</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-23</td>
      <td>4</td>
      <td>41</td>
      <td>192</td>
      <td>0</td>
      <td>119</td>
      <td>12.6</td>
      <td>746.3</td>
      <td>765.4</td>
      <td>0.3</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-23</td>
      <td>4</td>
      <td>40</td>
      <td>106</td>
      <td>0</td>
      <td>76</td>
      <td>12.6</td>
      <td>746.3</td>
      <td>765.4</td>
      <td>0.3</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Delhi</td>
      <td>Mayapuri Industrial Area, Delhi</td>
      <td>2014-01-23</td>
      <td>4</td>
      <td>84</td>
      <td>250</td>
      <td>0</td>
      <td>148</td>
      <td>12.6</td>
      <td>746.3</td>
      <td>765.4</td>
      <td>0.3</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Delhi</td>
      <td>N-Y- SCHOOL, Sarojini Nagar, Delhi</td>
      <td>2014-01-23</td>
      <td>2</td>
      <td>63</td>
      <td>167</td>
      <td>0</td>
      <td>107</td>
      <td>12.6</td>
      <td>746.3</td>
      <td>765.4</td>
      <td>0.3</td>
      <td>100</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-01-28</td>
      <td>4</td>
      <td>37</td>
      <td>280</td>
      <td>0</td>
      <td>163</td>
      <td>23.4</td>
      <td>742.9</td>
      <td>761.2</td>
      <td>-2.5</td>
      <td>37</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-01-28</td>
      <td>4</td>
      <td>35</td>
      <td>219</td>
      <td>0</td>
      <td>133</td>
      <td>23.4</td>
      <td>742.9</td>
      <td>761.2</td>
      <td>-2.5</td>
      <td>37</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Delhi</td>
      <td>Town Hall, Ayurvedic Dispensary, Chandni Chowk...</td>
      <td>2014-01-28</td>
      <td>6</td>
      <td>60</td>
      <td>368</td>
      <td>0</td>
      <td>220</td>
      <td>23.4</td>
      <td>742.9</td>
      <td>761.2</td>
      <td>-2.5</td>
      <td>37</td>
      <td>1</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-02-03</td>
      <td>4</td>
      <td>37</td>
      <td>326</td>
      <td>0</td>
      <td>186</td>
      <td>12.6</td>
      <td>743.1</td>
      <td>762.1</td>
      <td>0.0</td>
      <td>100</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-02-03</td>
      <td>4</td>
      <td>54</td>
      <td>279</td>
      <td>0</td>
      <td>163</td>
      <td>12.6</td>
      <td>743.1</td>
      <td>762.1</td>
      <td>0.0</td>
      <td>100</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-02-06</td>
      <td>4</td>
      <td>49</td>
      <td>297</td>
      <td>0</td>
      <td>172</td>
      <td>31.4</td>
      <td>735.2</td>
      <td>752.8</td>
      <td>-0.4</td>
      <td>34</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-02-06</td>
      <td>5</td>
      <td>50</td>
      <td>192</td>
      <td>0</td>
      <td>119</td>
      <td>31.4</td>
      <td>735.2</td>
      <td>752.8</td>
      <td>-0.4</td>
      <td>34</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Delhi</td>
      <td>N-Y- SCHOOL, Sarojini Nagar, Delhi</td>
      <td>2014-02-06</td>
      <td>22</td>
      <td>90</td>
      <td>174</td>
      <td>0</td>
      <td>110</td>
      <td>31.4</td>
      <td>735.2</td>
      <td>752.8</td>
      <td>-0.4</td>
      <td>34</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Delhi</td>
      <td>Town Hall, Ayurvedic Dispensary, Chandni Chowk...</td>
      <td>2014-02-06</td>
      <td>18</td>
      <td>97</td>
      <td>143</td>
      <td>0</td>
      <td>97</td>
      <td>31.4</td>
      <td>735.2</td>
      <td>752.8</td>
      <td>-0.4</td>
      <td>34</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Delhi</td>
      <td>Pritampura, Delhi</td>
      <td>2014-02-11</td>
      <td>4</td>
      <td>38</td>
      <td>246</td>
      <td>0</td>
      <td>146</td>
      <td>30.4</td>
      <td>741.6</td>
      <td>759.4</td>
      <td>-2.1</td>
      <td>28</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Delhi</td>
      <td>Nizamuddin, Delhi</td>
      <td>2014-02-11</td>
      <td>4</td>
      <td>50</td>
      <td>312</td>
      <td>0</td>
      <td>179</td>
      <td>30.4</td>
      <td>741.6</td>
      <td>759.4</td>
      <td>-2.1</td>
      <td>28</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Delhi</td>
      <td>Mayapuri Industrial Area, Delhi</td>
      <td>2014-02-11</td>
      <td>9</td>
      <td>92</td>
      <td>273</td>
      <td>0</td>
      <td>160</td>
      <td>30.4</td>
      <td>741.6</td>
      <td>759.4</td>
      <td>-2.1</td>
      <td>28</td>
      <td>2</td>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1484</th>
      <td>Delhi</td>
      <td>Sirifort</td>
      <td>2016-06-10</td>
      <td>4</td>
      <td>40</td>
      <td>273</td>
      <td>61</td>
      <td>160</td>
      <td>26.8</td>
      <td>736.3</td>
      <td>754.2</td>
      <td>0.2</td>
      <td>86</td>
      <td>6</td>
      <td>2016</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1485</th>
      <td>Delhi</td>
      <td>ShahzadaBagh</td>
      <td>2016-06-10</td>
      <td>4</td>
      <td>38</td>
      <td>275</td>
      <td>61</td>
      <td>161</td>
      <td>26.8</td>
      <td>736.3</td>
      <td>754.2</td>
      <td>0.2</td>
      <td>86</td>
      <td>6</td>
      <td>2016</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1486</th>
      <td>Delhi</td>
      <td>Sirifort</td>
      <td>2016-09-10</td>
      <td>4</td>
      <td>35</td>
      <td>322</td>
      <td>102</td>
      <td>184</td>
      <td>33.4</td>
      <td>737.5</td>
      <td>755.0</td>
      <td>-0.2</td>
      <td>48</td>
      <td>9</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1487</th>
      <td>Delhi</td>
      <td>ShahzadaBagh</td>
      <td>2016-09-10</td>
      <td>4</td>
      <td>53</td>
      <td>347</td>
      <td>62</td>
      <td>197</td>
      <td>33.4</td>
      <td>737.5</td>
      <td>755.0</td>
      <td>-0.2</td>
      <td>48</td>
      <td>9</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1488</th>
      <td>Delhi</td>
      <td>Sirifort</td>
      <td>2016-10-14</td>
      <td>4</td>
      <td>40</td>
      <td>344</td>
      <td>160</td>
      <td>210</td>
      <td>24.8</td>
      <td>739.0</td>
      <td>757.1</td>
      <td>1.3</td>
      <td>74</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1489</th>
      <td>Delhi</td>
      <td>ShahzadaBagh</td>
      <td>2016-10-14</td>
      <td>4</td>
      <td>57</td>
      <td>317</td>
      <td>70</td>
      <td>182</td>
      <td>24.8</td>
      <td>739.0</td>
      <td>757.1</td>
      <td>1.3</td>
      <td>74</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1490</th>
      <td>Delhi</td>
      <td>Sirifort</td>
      <td>2016-10-18</td>
      <td>4</td>
      <td>33</td>
      <td>234</td>
      <td>120</td>
      <td>184</td>
      <td>31.0</td>
      <td>737.5</td>
      <td>755.2</td>
      <td>-0.6</td>
      <td>45</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1491</th>
      <td>Delhi</td>
      <td>ShahzadaBagh</td>
      <td>2016-10-18</td>
      <td>5</td>
      <td>59</td>
      <td>452</td>
      <td>140</td>
      <td>335</td>
      <td>31.0</td>
      <td>737.5</td>
      <td>755.2</td>
      <td>-0.6</td>
      <td>45</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1492</th>
      <td>Delhi</td>
      <td>Sirifort</td>
      <td>2016-10-21</td>
      <td>4</td>
      <td>45</td>
      <td>428</td>
      <td>102</td>
      <td>305</td>
      <td>24.8</td>
      <td>738.9</td>
      <td>757.0</td>
      <td>1.5</td>
      <td>54</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1493</th>
      <td>Delhi</td>
      <td>ShahzadaBagh</td>
      <td>2016-10-21</td>
      <td>5</td>
      <td>56</td>
      <td>589</td>
      <td>94</td>
      <td>485</td>
      <td>24.8</td>
      <td>738.9</td>
      <td>757.0</td>
      <td>1.5</td>
      <td>54</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1494</th>
      <td>Delhi</td>
      <td>Sirifort</td>
      <td>2016-10-27</td>
      <td>4</td>
      <td>56</td>
      <td>486</td>
      <td>0</td>
      <td>377</td>
      <td>29.2</td>
      <td>741.5</td>
      <td>759.4</td>
      <td>-0.5</td>
      <td>53</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1495</th>
      <td>Delhi</td>
      <td>ShahzadaBagh</td>
      <td>2016-10-27</td>
      <td>6</td>
      <td>58</td>
      <td>361</td>
      <td>195</td>
      <td>245</td>
      <td>29.2</td>
      <td>741.5</td>
      <td>759.4</td>
      <td>-0.5</td>
      <td>53</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1496</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-01-10</td>
      <td>5</td>
      <td>52</td>
      <td>280</td>
      <td>37</td>
      <td>163</td>
      <td>32.0</td>
      <td>737.5</td>
      <td>755.1</td>
      <td>1.7</td>
      <td>67</td>
      <td>1</td>
      <td>2016</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1497</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-01-10</td>
      <td>5</td>
      <td>53</td>
      <td>268</td>
      <td>73</td>
      <td>160</td>
      <td>32.0</td>
      <td>737.5</td>
      <td>755.1</td>
      <td>1.7</td>
      <td>67</td>
      <td>1</td>
      <td>2016</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1498</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-04-10</td>
      <td>4</td>
      <td>45</td>
      <td>265</td>
      <td>112</td>
      <td>180</td>
      <td>25.4</td>
      <td>736.3</td>
      <td>754.3</td>
      <td>2.1</td>
      <td>88</td>
      <td>4</td>
      <td>2016</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1499</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-04-10</td>
      <td>5</td>
      <td>42</td>
      <td>188</td>
      <td>99</td>
      <td>173</td>
      <td>25.4</td>
      <td>736.3</td>
      <td>754.3</td>
      <td>2.1</td>
      <td>88</td>
      <td>4</td>
      <td>2016</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1500</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-07-10</td>
      <td>4</td>
      <td>50</td>
      <td>320</td>
      <td>99</td>
      <td>183</td>
      <td>34.4</td>
      <td>736.1</td>
      <td>753.6</td>
      <td>-2.2</td>
      <td>44</td>
      <td>7</td>
      <td>2016</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1501</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-07-10</td>
      <td>4</td>
      <td>51</td>
      <td>196</td>
      <td>61</td>
      <td>154</td>
      <td>34.4</td>
      <td>736.1</td>
      <td>753.6</td>
      <td>-2.2</td>
      <td>44</td>
      <td>7</td>
      <td>2016</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1502</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-10-10</td>
      <td>4</td>
      <td>51</td>
      <td>334</td>
      <td>106</td>
      <td>190</td>
      <td>25.2</td>
      <td>735.6</td>
      <td>753.6</td>
      <td>-0.3</td>
      <td>82</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1503</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-10-10</td>
      <td>4</td>
      <td>42</td>
      <td>206</td>
      <td>94</td>
      <td>171</td>
      <td>25.2</td>
      <td>735.6</td>
      <td>753.6</td>
      <td>-0.3</td>
      <td>82</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1504</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-10-15</td>
      <td>4</td>
      <td>38</td>
      <td>293</td>
      <td>147</td>
      <td>198</td>
      <td>18.8</td>
      <td>739.1</td>
      <td>757.6</td>
      <td>0.3</td>
      <td>84</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1505</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-10-15</td>
      <td>5</td>
      <td>53</td>
      <td>279</td>
      <td>137</td>
      <td>193</td>
      <td>18.8</td>
      <td>739.1</td>
      <td>757.6</td>
      <td>0.3</td>
      <td>84</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1506</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-10-19</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>154</td>
      <td>204</td>
      <td>22.4</td>
      <td>739.3</td>
      <td>757.6</td>
      <td>1.7</td>
      <td>66</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1507</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-10-19</td>
      <td>4</td>
      <td>48</td>
      <td>353</td>
      <td>148</td>
      <td>200</td>
      <td>22.4</td>
      <td>739.3</td>
      <td>757.6</td>
      <td>1.7</td>
      <td>66</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1508</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-10-22</td>
      <td>4</td>
      <td>47</td>
      <td>307</td>
      <td>0</td>
      <td>177</td>
      <td>31.6</td>
      <td>737.6</td>
      <td>755.3</td>
      <td>-1.7</td>
      <td>45</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1509</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-10-22</td>
      <td>4</td>
      <td>52</td>
      <td>428</td>
      <td>105</td>
      <td>305</td>
      <td>31.6</td>
      <td>737.6</td>
      <td>755.3</td>
      <td>-1.7</td>
      <td>45</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1510</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-10-25</td>
      <td>4</td>
      <td>57</td>
      <td>372</td>
      <td>99</td>
      <td>225</td>
      <td>29.6</td>
      <td>737.2</td>
      <td>755.0</td>
      <td>-0.3</td>
      <td>50</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1511</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-10-25</td>
      <td>6</td>
      <td>59</td>
      <td>375</td>
      <td>176</td>
      <td>230</td>
      <td>29.6</td>
      <td>737.2</td>
      <td>755.0</td>
      <td>-0.3</td>
      <td>50</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1512</th>
      <td>Delhi</td>
      <td>Janakpuri</td>
      <td>2016-10-28</td>
      <td>4</td>
      <td>64</td>
      <td>516</td>
      <td>241</td>
      <td>412</td>
      <td>31.8</td>
      <td>739.9</td>
      <td>757.6</td>
      <td>-2.0</td>
      <td>41</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1513</th>
      <td>Delhi</td>
      <td>Shahdara</td>
      <td>2016-10-28</td>
      <td>5</td>
      <td>52</td>
      <td>327</td>
      <td>211</td>
      <td>261</td>
      <td>31.8</td>
      <td>739.9</td>
      <td>757.6</td>
      <td>-2.0</td>
      <td>41</td>
      <td>10</td>
      <td>2016</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>1514 rows × 16 columns</p>
</div>



### 3.1 Predictions and Model Evaluations
#### Using Machine learning to create Models



###### - KNN Model


```python
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
X_train,X_test,y_train,y_test=train_test_split(df[['T','season','year','P','U']].values,df['aqi'].values,random_state=0)
clf=KNeighborsClassifier(n_neighbors=2)
clf.fit(X_train, y_train)
#print("Test set predictions: {}".format(clf.predict(X_test)))
print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))
```

    Test set accuracy: 0.01


Accuracy for this model is relatively low as this is having about 1% accuracy rate which is very low.

######  - KNN Regression Model


```python
from sklearn.neighbors import KNeighborsRegressor
reg = KNeighborsRegressor(n_neighbors=1)
reg.fit(X_train, y_train)
print("Test set accuracy: {:.2f}".format(reg.score(X_test, y_test)))

```

    Test set accuracy: -0.30


Kneighbor regressor model also fails to fit the data and make accurate predictions.

###### -Linear Regression Model


```python
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(df[['T','month','P']].values,df['aqi'].values,random_state=42)
lr = LinearRegression().fit(X_train, y_train)
print("Test set score accuracy: {:.2f}".format(lr.score(X_train, y_train)))

```

    Test set score accuracy: 0.07


Linear regression model is having accuracy rate of 7% which is not sufficient enough.

###### -Ridge Model


```python
from sklearn.linear_model import Ridge
ridge = Ridge().fit(X_train, y_train)
print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))
```

    Training set score: 0.07
    Test set score: 0.03


Ridge regression model also fails.

## 4.Conclusion

##### The following conclusions are made after data analysis 

* This aqi has increased over the years,this means that the air quality has droped significantly in the year (2014-2016).
* The maximum aqi was in the month of november where aqi ranged between (200-300) average.
* No model was effective in predicting the aqi because of limited data,To effectively model we need more data. 
