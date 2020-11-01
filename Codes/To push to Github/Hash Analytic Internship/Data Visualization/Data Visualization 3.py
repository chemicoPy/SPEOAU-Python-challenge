import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns; sns.set()
from numpy.random import randn
from pandas import DataFrame, Series

dataset = sns.load_dataset('diamonds')
print(dataset)


dataset.to_csv('diamonds.csv')

sns.lmplot('price','carat',dataset).savefig('Lmplot1')
plt.show()
# modifying it
sns.lmplot('price','carat',dataset,scatter_kws= {'marker':'o','color':'green'}, 'line_kws'={'color':'red', 'line_width':1}).savefig('Lmplot2')
plt.show()

sns.lmplot('price','carat',dataset,order= 4 ,scatter_kws= {'marker':'o','color':'green'}, 'line_kws'={'color':'red', 'line_width':1}).savefig('Lmplot3')
plt.show()

# Scatter plot without trend line i.e regression line.
sns.lmplot('price','carat',dataset, fit_reg=False).savefig('Lmplot4')
plt.show()

# Hue arguments
sns.lmplot('price','carat',dataset,hue ='cut').savefig('Lmlplot5')
sns.lmplot('price','carat',dataset,hue ='cut').savefig('Lmlplot6')
plt.show()

#Local regression
sns.lmplot('price','carat',dataset,lowess = True).savefig('Lmplot7')
plt.show()

#Regplot
sns.regplot('price','carat',dataset).savefig('Lmplot8')
plt.show()

#Sub plots

image, (plt1, plt2) plt.subplot(1,2,sharey = True)
sns.regplot('price','carat', dataset, ax =plt1).get_figure().savefig('Lmplot9')
sns.boxplot(dataset['carat'],dataset['depth'], color='green',ax=plt2).get_figure().savefig('Lmplot10')
plt.show()