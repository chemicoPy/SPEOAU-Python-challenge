# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:57:56 2020

@author: VICTOR
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns; sns.set()
from numpy.random import randn
from pandas import DataFrame, Series

first =  [0,0]
covariance = [[1,0],[0,100]]

dataset = np.random.multivariate_normal(first, covariance, 500)
dataframe = DataFrame(dataset, columns=['Column1','Column2'])

print(dataframe)
figure = sns.kdeplot(dataframe).get_figure()
figure.savefig('Data Visualization 4')
plt.show()

'''Using shade:'''

figure2 = sns.kdeplot(dataframe, shade = True).get_figure()
figure2.savefig('Data Visualization 4_1')
plt.show()
'''Bandwith change:'''

figure3 = sns.kdeplot(dataframe, shade = False, bw='silverman').get_figure()
figure3.savefig('Data Visualization 4_1_1')
plt.show()

'''Kind variable:'''
figure4 = sns.jointplot('Column1','Column2',dataframe, kind ='scatter', color ='red')
figure4.savefig('Data Visualization 4_1_1_1')
figure5 = sns.jointplot('Column1','Column2',dataframe, kind ='kde', color ='green')
plt.show()

figure6 = sns.jointplot('Column1','Column2',dataframe, kind ='kde', color ='red')
plt.show()


