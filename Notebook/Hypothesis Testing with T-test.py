#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing with T-Test
# 
# Definitions:
# * A _quarter_ is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
# * A _recession_ is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
# * A _recession bottom_ is the quarter within a recession which had the lowest GDP.
# * A _university town_ is a city which has a high percentage of university students compared to the total population of the city.
# 
# **Hypothesis**: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (`price_ratio=quarter_before_recession/recession_bottom`)
# 
# Data files that will be used for the Project:
# * From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.
# * From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
# * From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file ```gdplev.xls```.we will only look at GDP data from the first quarter of 2000 onward.
# 

# ## Datapreprocessing 

# In[ ]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

pd.set_option('display.max_rows', 100)
      
university_towns = pd.read_csv('university_towns.txt', sep='delimiter', header=None)
university_towns_list = pd.DataFrame([], columns =['State', 'RegionName'])
state = ''
for items in university_towns[0]:
        
    if '[edit]' in items:
        state = items[:items.find('[')]
        continue
        
    region = ''
    if '(' in items:
            
        region = items[:items.find(' (')]
        
    else:
        region = items
            
    university_towns_list = university_towns_list.append(pd.DataFrame([[state, region]], columns=['State', 'RegionName']))


# ## Finding the Start of Recession

# In[ ]:


GDP = pd.read_excel('gdplev.xls', skiprows=219 )
GDP = GDP.drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 9926.1, 'Unnamed: 7'], axis=1)
GDP.columns = ['Quarterly', 'GDP in billions of chained 2009 dollars']               
GDP = GDP.set_index('Quarterly')
GDP_start_quarter = ''
for i in range(GDP['GDP in billions of chained 2009 dollars'].count()):
    if GDP['GDP in billions of chained 2009 dollars'].iloc[i-1] > GDP['GDP in billions of chained 2009 dollars'].iloc[i] and GDP['GDP in billions of chained 2009 dollars'].iloc[i+1] < GDP['GDP in billions of chained 2009 dollars'].iloc[i]:
        recession_start_quarter = GDP.iloc[i-1].name
        break


# ## Finding the End of Recession

# In[ ]:


GDP_end_quarter = ''
for i in range(34, GDP['GDP in billions of chained 2009 dollars'].count()):
    if GDP['GDP in billions of chained 2009 dollars'].iloc[i-1] < GDP['GDP in billions of chained 2009 dollars'].iloc[i] and GDP['GDP in billions of chained 2009 dollars'].iloc[i+1] > GDP['GDP in billions of chained 2009 dollars'].iloc[i]:
        recession_end_quarter = GDP.iloc[i+1].name
        break


# ## Finding the Bottom of Recession

# In[ ]:


recession_bottom_value = min([GDP['GDP in billions of chained 2009 dollars'].iloc[34], GDP['GDP in billions of chained 2009 dollars'].iloc[35], GDP['GDP in billions of chained 2009 dollars'].iloc[36], GDP['GDP in billions of chained 2009 dollars'].iloc[37], GDP['GDP in billions of chained 2009 dollars'].iloc[38]])
recession_bottom_quarter = GDP.loc[GDP['GDP in billions of chained 2009 dollars'] == GDP_bottom_value].index


# ## Converting Housing Data from Year to Quarter

# In[ ]:


def get_quarter(year, month):
    if month <= 3:
        quarter = 1
    elif month <= 6:
        quarter = 2
    elif month <= 9:
        quarter = 3
    elif month <= 12:
        quarter = 4
    return (str(year) + 'q' + str(quarter))
housing_data = pd.read_csv('City_Zhvi_AllHomes.csv')
housing_data = (housing_data.drop(['RegionID', 'Metro', 'CountyName', 'SizeRank'], axis=1)
                            .replace({'State': states})
                            .set_index(['State', 'RegionName'])
                            .replace(to_replace='NaN', value=np.NaN)
                            .convert_objects(convert_numeric=True)
                            .sort())
index = list(housing_data.columns.values).index('2000-01')
housing_data = housing_data.drop(housing_data.columns[:index], axis=1)
l = len(housing_data.columns)
i = 0
while i < l:
    col_name = housing_data.iloc[:, i].name
    year = int(col_name.split('-')[0])
    month = int(col_name.split('-')[1])
    quarter = get_quarter(year, month)
    if i + 3 < l:
        split = housing_data.iloc[:, i:i + 3]
    else:
        split = housing_data.iloc[:, i:l]
    housing_data[quarter] = split.mean(axis=1)
    i += 3
housing_data = housing_data.drop(df.columns[:l], axis=1)
    


# ## T-test

# In[ ]:


ratio = housing_data['2008q2']/housing_data['2009q2']
df_ratio = pd.DataFrame(ratio)
df_ratio.columns=['Ratio']
university_towns_list = university_towns_list.sort('RegionName').set_index(['State', 'RegionName'])
uni_price = df_ratio.merge(university_towns_list, how='inner', left_index=True, right_index=True)
uni_price = uni_price.dropna()
non_uni_price = df_ratio.merge(university_towns_list, how='outer', left_index=True, right_index=True)
non_uni_price = non_uni_price.dropna()

    
t, p = ttest_ind(uni_price['Ratio'], non_uni_price['Ratio'],equal_var=False)

print(p)

