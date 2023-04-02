
import numpy as numpy
import pandas as pd


df_2008_01 = pd.read_csv('data/synop.200911.csv', delimiter =';')

#print(df_2008_01.head())


#df_2008_01 = df_2008_01.loc[df_2008_01['numer_sta']==7149].copy().reset_index(drop = True)
print(df_2008_01)

data_power = pd.read_csv('data/household_power_consumption.txt', delimiter = ';', low_memory = False)

#print(data_power.head())

data = pd.DataFrame()
for i in [8,9]:
    for j in range(1,13):
        df = pd.read_csv("data/synop.200{:d}{:02d}.csv".format(i,j),delimiter = ';')
        data = pd.concat([data,df]).reset_index(drop = True).reset_index(drop = True)

print(data)

