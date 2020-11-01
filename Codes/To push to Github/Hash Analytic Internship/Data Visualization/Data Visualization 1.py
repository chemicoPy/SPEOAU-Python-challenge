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

#plt.scatter(first,second)
plt.plot(first,second)
#plt.stem(first,second)
sns.regplot(first,second,formula())
plt.show()

fig = sns.jointplot(first,second, formula())
plt.show()
plt.savefig('Data Visualization extra.')


































