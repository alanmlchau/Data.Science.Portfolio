#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.dates as mdates


weather = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
weather['Data_Value']=weather['Data_Value']/10 #to convert tmeperature as degree celcius 
weather['D_T'] = pd.to_datetime(weather['Date'])


weather_to_year_2014 = weather[weather['D_T'].dt.year != 2015]
weather_to_year_2014['Day'] = weather_to_year_2014['Date'].str[5:]
weather_to_year_2014.sort_values('Day', inplace=True)
weather_to_year_2014 = weather_to_year_2014.groupby(['Day']).Data_Value.agg([('Min','min'),('Max','max')]).add_prefix('Historic Daily ')

weather_year_2015 = weather[weather['D_T'].dt.year == 2015]
weather_year_2015.sort_values('D_T', inplace=True)
weather_year_2015['Day'] = weather_year_2015['Date'].str[5:]
weather_year_2015 = weather_year_2015.groupby(['Day']).Data_Value.agg([('Min','min'),('Max','max')]).add_prefix('2015 Daily ')


weather_combined = pd.merge(weather_year_2015, weather_to_year_2014, left_index=True, right_index=True)
weather_combined.reset_index(inplace=True)
weather_combined['Day'] = weather_combined['Day']+'-2015'
weather_combined['Day'] = pd.to_datetime(weather_combined['Day'])
weather_combined.set_index('Day', inplace=True)


daily_max = weather_combined['Historic Daily Max']
daily_min = weather_combined['Historic Daily Min']
break_record_2015_max = weather_combined['2015 Daily Max'].loc[combined['2015 Daily Max']>combined['HistMax']]
break_record_2015_min = weather_combined['2015 Daily Min'].loc[combined['2015 Daily Min']<combined['HistMin']]
Base = weather_combined.index




plt.gca().fill_between(x=Base, y1=daily_max, y2=daily_min, facecolor='violet', alpha=0.25)
plt.scatter(break_record_2015_max.index, break_record_2015_max, s=10, c='red', label= 'Record Daily Max Broken in 2015')
plt.scatter(break_record_2015_min.index, break_record_2015_min, s=10, c='blue', label= 'Record Daily Min Broken in 2015')
plt.margins(x=0)

locator = mdates.MonthLocator()
fmt = mdates.DateFormatter('%b')
X = plt.gca().xaxis
plt.ylabel('Degree Celsius')
X.set_major_locator(locator)
X.set_major_formatter(fmt)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)



plt.title('Record Daily Max and Min Termperature 10 Years Prior to 2015 \n and Reocrd Broke in 2015 ')

plt.legend()
plt.legend(loc=4, frameon=False)

plt.show()



# In[ ]:




