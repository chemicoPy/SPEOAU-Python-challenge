# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:02:20 2020

@author: VICTOR
"""



import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import DataFrame, Series

from numpy.random import randn
from pandas import DataFrame, Series
from sympy import *

first =  random.rand(100)
second =  random.rand(100)

def formula(): # Using idea of y = mx + c
    for m in first:
        for c in second:
            y = m*c + c
    return



plt.scatter(first,second)
sns.regplot(first,second)
#plt.stem(first,second)
plt.show()

fig = sns.jointplot(first,second,kind ='reg') #"kind must be either 'scatter', 'reg', 'resid', 'kde', or 'hex'"
plt.savefig('Data Visualization extra 1.')
plt.show()



fig1 = sns.jointplot(first,second,kind ='resid')
plt.savefig('Data Visualization extra 2.')
plt.show()



fig2 = sns.jointplot(first,second,kind ='hex', color = 'green')
plt.savefig('Data Visualization extra 3.')
plt.show()


fig2 = sns.jointplot(first,second,kind ='kde', color = 'orange')
plt.savefig('Data Visualization extra 4.')
plt.show()


































