# Data.Science.Portfolio


## Preprocessing Data of Renewabl Energy Development and Usage amoung Countries  
  The goal of this project is to preprocess the data (elimilating Nan, selecting needed data, etc.) of [Energy Indicators.xls](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Data%20Preprocessing/Energy%20Indicators.xls)  (a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013), [world_bank.csv](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Data%20Preprocessing/world_bank.csv) (countries' GDP from 1960 to 2015 from World Bank) and [scimagojr-3.csv](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Data%20Preprocessing/scimagojr-3.csv) (which use data from 1996-2018 to rank countries based on their journal contributions in the aforementioned area) and then combine all three data set to answer various questions regarding renewable energy usage and development among the countries. The final dataframe after preprocessing with the top ranked 15 countries is [here](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Data%20Preprocessing/final.csv), and explicit code can be viewed [here](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Notebook/Data%20Preprocessing.py)

## Hypothesis Testing with T-test (University Towns and Recessions)
 The gola of this project is to test whether University towns have their mean housing prices less effected by recessions. First, I did some datapreprocessing (dividing data in quarters, renaming columns and index, ect), and then I used the housing data from Zillow research data site [City_Zhvi_AllHomes.csv](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Hypothesis%20Test%20with%20T-test/City_Zhvi_AllHomes.csv), a list of university towns in the United States from Wikipedia [university_towns.txt](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Hypothesis%20Test%20with%20T-test/university_towns.txt) and the GDP data of the United States from the Bureau of Economic Analysis, US Department of Commerce [gdplev.xls](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Hypothesis%20Test%20with%20T-test/gdplev.xls). After carefully analysis, the result shows that the P-value of the confidence is less than 0.00057655974311320252 (less than 0.01), so we reject the null hypothesis and conclude that University towns have their mean housing prices less effected by recessions. Please refer [here](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Notebook/Hypothesis%20Testing%20with%20T-test.py) for explicit code.
 
 ## Visualization of the National Oceanic and Atmospheric (NOAA) Dataset near Ann Arbor, Michigan, United States
  The goal of this project is to use the [NOAA dataset](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Visualization%20of%20the%20National%20Oceanic%20and%20Atmospheric%20(NOAA)%20Dataset/NOAA%20dataset.csv) provided by The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily) and to preprocess the dataset to get the Daily Max and Min temperature from 2005-2014. In addition, a scatter plot is drawn on top to show the daily max and min in 2015 which broke the records from previous years. Please refer [here](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Document/Visualization%20of%20the%20National%20Oceanic%20and%20Atmospheric%20(NOAA)%20Dataset/Graph1.png) for the final graph and [here](https://github.com/alanmlchau/Data.Science.Portfolio/blob/master/Notebook/Visualization%20of%20the%20National%20Oceanic%20and%20Atmospheric%20(NOAA)%20Dataset.py) for explicit code.
  
