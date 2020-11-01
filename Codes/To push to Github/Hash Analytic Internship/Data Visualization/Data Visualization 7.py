# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:51:34 2020

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

'''Kernel Density Estimate''' # Go on net to find out more on kernel stats

first  = random.randn(100)
sns.rugplot(first)
plt.show()

plt.hist(first,alpha = 0.5) # Alpha =1 means completely opaque
plt.savefig('Data Visualization 2') # Thick points/marks
plt.show()
second = np.linspace(first.min()-1, first.max()+1, 50)

# Bandwith creation:
bandwith = ((4*first.std()**5)/(3*len(first)))^0.2

kernels= []
for point in first:
    kernel = stats.norm(point, bandwith).pdf(second) #pdf - probability density function
    kernels.append(kernel)
    
    kernel = kernel/kernel.max()
    kernel = kernel*0.6
    plt.plot(second, kernel, alpha =0.5, color='red')


plt.ylim(0,1)

    
plt.savefig('Data Visualization 2_1')  


first  = random.randn(100)
sns.rugplot(first)
plt.show()
plt.hist(first,alpha = 0.5)

second = np.linspace(first.min()-1, first.max()+1, 50)

# Bandwith creation:
bandwith = ((4*first.std()**5)/(3*len(first)))**0.2

kernels= []
for point in first:
    kernel = stats.norm(point, bandwith).pdf(second) #pdf - probability density function
    kernels.append(kernel)
    
    kernel = kernel/kernel.max()
    kernel = kernel*0.6
    plt.plot(second, kernel, alpha =0.5, color='red')


plt.ylim(0,1)

    
plt.savefig('Data Visualization 2_1')  

KDE = np.sum(kernels, axis = 0) # Adding along axis 0
KDE_fig = plt.plot(second, KDE, color='yellow')
sns.rugplot(first)  
plt.suptitle('KDE Plot')
plt.savefig('Data Visualization 2_1_1')

'''Now combining everything:'''

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns; sns.set()
from numpy import random

'''Kernel Density Estimate''' # Go on net to find out more on kernel stats

first  = random.randn(100)
sns.rugplot(first)
plt.show()


plt.hist(first,alpha = 0.5) # Alpha =1 means completely opaque
plt.savefig('Data Visualization 2') # Thick points/marks

second = np.linspace(first.min()-1, first.max()+1, 50)

# Bandwith creation:
bandwith = ((4*first.std()**5)/(3*len(first)))**0.2

kernels= []
for point in first:
    kernel = stats.norm(point, bandwith).pdf(second) #pdf - probability density function
    kernels.append(kernel)
    
    kernel = kernel/kernel.max()
    kernel = kernel*0.6
    plt.plot(second, kernel, alpha =0.5, color='red')
    
    
KDE = np.sum(kernels, axis = 0) # Adding along axis 0
KDE_fig = plt.plot(second, KDE, color='green')
sns.rugplot(first)  
plt.suptitle('KDE Plot')  
    
plt.savefig('Final Data Visualization 2')   

'''A very short method to deriving KDE is using sns:'''
KDE_fig = sns.kdeplot(first)
fig = KDE_fig.get_fig()
fig.savefig('Final Data Visualization 2 (Seaborn method)')
plt.show()