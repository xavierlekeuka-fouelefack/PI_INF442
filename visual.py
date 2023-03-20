
import numpy as numpy
import pandas as pd


df_2008_01 = pd.read_csv('data/synop.200801.csv', delimiter =';')

print(df_2008_01.head())
df_2008_01_orly = df_2008_01.loc[df_2008_01['numer_sta']==7149].copy().reset_index(drop = True)
print(df_2008_01_orly.head())

data_power = pd.read_csv('data/household_power_consumption.txt', delimiter = ';', low_memory = False)

print(data_power.head())




