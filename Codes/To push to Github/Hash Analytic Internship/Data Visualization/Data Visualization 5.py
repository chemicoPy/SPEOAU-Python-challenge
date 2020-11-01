# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:46:10 2020

@author: VICTOR
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns; sns.set()
from numpy import random 


'''Creating histogram with seaborn'''


first =  random.randn(10000)
second = random.randn(1000)
plt.hist(first)
plt.title('Data Visualization 1')
plt.savefig('Data Visualization 1')
plt.show()

plt.hist(second)
plt.title('Data Visualization 2')
plt.savefig('Data Visualization 1_1')
plt.show()

plt.hist(first,normed = True, color ='yellow', bins =15, alpha= 0.5)
plt.hist(second,normed = True, color ='green', bins =15, alpha= 0.5)

plt.title('Mixed Plots')
plt.savefig('Data Visualization 1_1_1')
plt.show()


'''Plotting using seaborn'''
third =  random.randn(10000)
fourth = random.randn(10000)

sns_plot =  sns.jointplot(third,fourth)
sns_plot.savefig('Data Visualization 1_1_1_1')
sns_plot2 = sns.jointplot(third, fourth, kind ='hex')
sns.jointplot(third, fourth, kind='scatter',color='red') # You can observe that the default plot of joint plot is 'scatter'.
sns_plot2.savefig('Data Visualization 1_1_1_1_1')

plt.show()

sns_plot3 = sns.regplot(fourth, third)
#sns_plot3.savefig('Data Visualization 1_1_1_1_1_1')
plt.show()