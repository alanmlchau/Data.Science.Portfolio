#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
ScimEn = pd.read_excel('scimagojr-3.xlsx')
GDP = pd.read_csv('world_bank.csv',skiprows=4)
energy = pd.read_excel('Energy Indicators.xls', names=['1', '2', 'Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
                            skiprows=17, skipfooter=38)
energy = energy.drop(['1', '2'], axis=1)
energy['Country'] = energy['Country'].apply(lambda x: x.split(' (')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('1')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('2')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('0')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('3')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('4')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('5')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('6')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('7')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('8')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.split('9')[0])
energy.replace(to_replace=["...", "Republic of Korea", "United States of America","United Kingdom of Great Britain and Northern Ireland",
                            "China, Hong Kong Special Administrative Region"], 
                value=[np.nan, "South Korea", "United States", "United Kingdom", "Hong Kong"], inplace=True)
energy['Energy Supply'] = energy['Energy Supply'] * (1000000)

GDP['Country Name'].replace("Korea, Rep.", "South Korea", inplace=True)
GDP['Country Name'].replace("Iran, Islamic Rep.", "Iran", inplace=True)
GDP['Country Name'].replace("Hong Kong SAR, China", "Hong Kong", inplace=True)
GDP_new = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
ScimEn_new = ScimEn.head(15)
ScimEn_new = ScimEn_new.set_index('Country')
GDP_new = GDP_new.set_index('Country Name')
energy = energy.set_index('Country')
    
df = ScimEn_new.merge(energy, how='inner', left_index=True, right_index=True)
result = df.merge(GDP_new, how='left', left_index=True, right_index=True)


