# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:43:02 2020

@author: VICTOR
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import pandas as pd
from pandas import DataFrame, Series
from numpy.random import randn
import seaborn as sns


first = pd.read_csv('FiveYearData.txt') # Reading the already downloaded dataset

print(first)

second = pd.pivot_table(first, values= 'lifeExp',index = 'year',columns ='continent')
print(second)



sns.heatmap(second).get_figure().savefig('Heat Map (Seaborn).png')

#sns.heatmap(second,annot= True, fmt ='d').get_figure().savefig('Heat Map (Seaborn).png')

plt.show()



























