# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:35:05 2020

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

df =  random.rand(1000)

figure = sns.distplot(df,bins = 10).get_figure()
figure.savefig('Data Visualization 5')
plt.show()

figure1 = sns.distplot(df,hist = True, bins = 10, rug=True,
                       rug_kws={'color':'blue', 'label':'Rug Plot'},
                       hist_kws={'color':'red',  'label':'Hist Plot'},
                       kde_kws= {'color':'green', 'label':'KDE Plot'}
                      
                      
                      
                      ).get_figure() # You will observe that kde and hist plots are by default enabled in distplot and can only be excluded using False in the statement.



figure.savefig('Data Visualization 5_1')
plt.show()

df2 = random.rand(1000)
sns.boxplot(df2).get_figure().savefig('BoxPlot1.png')
plt.show()

#You can use orient function here: ie orient ='v' for vertical and orient='h' for horizontal

sns.boxplot(df2, whis= np.inf, color ='yellow', order = 8).get_figure().savefig('BoxPlot2.png')
plt.show()
# Boxplot is usually used in stock market analysis or business analysis.
# The left-half of the box plot is the 25th percentile, the middle line is the 50th percentile, and the right- half of the plot is the 75th percentile.

# You can do well to look on the internet for the working principle of all the plot you want to use.

'''Violin Plots (Combination of box plot and KDE plot)'''

df3 = random.rand(100)
sns.violinplot(df3).get_figure().savefig('Violin Plot 1')
plt.show()

'''Changing bandwith'''
sns.violinplot(df3,bw= 0.2, color= 'red').get_figure().savefig('Violin Plot 2')
# You will observe a distortion in the plot.
plt.show()


sns.violinplot(df3, color='green',inner= 'stick').get_figure().savefig('Violin Plot 3')
# The thick line parts are the concentrated parts.
plt.show()

'''Heatmaps visualization'''

df4= pd.read_csv("C:\\Users\\VICTOR\\Documents\\Programming\\Python Programming\\FlightData.csv")

print(df4)
df5 = ([df4['DISTANCE'],df4['ACTUAL_ELAPSED_TIME']])

sns.heatmap(df5).get_figure().savefig('Heat Map 1.png')
plt.show()
'''Using annotation function'''
sns.heatmap(df5,fmt='d').get_figure().savefig('Heat Map 2.png')
plt.show()

# fmt function can take 'd' or 'c'. That is, diverging or converging. Here, we used diverging.
#Functions you can use with heatmap
'''data, vmin, vmax, cmap, center, robust, annot, fmt, annot_kws, linewidths, linecolor, cbar, cbar_kws, cbar_ax, square, xticklabels, yticklabels, mask, ax, **kwargs'''
'''You can use the center function by:

center =  df5.loc[1995,'January']. I didn't implement that here because i'm not using a real example just a modified one.'''














