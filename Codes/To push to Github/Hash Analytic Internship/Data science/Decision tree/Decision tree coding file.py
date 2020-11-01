# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:06:10 2020

@author: VICTOR
"""
# Import the necessary libraries.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Importing/Reading the downloaded IRIS dataset
mydataset= pd.read_csv('IRIS.csv')

# Selection of digits/values
first =  mydataset.iloc[:,0:1].values
second =  mydataset.iloc[:,1:2].values

# Splitting the dataset into subsets (test and train set) - (70% for training and 30 % for testing)
from sklearn.model_selection import train_test_split
first_train, first_test, second_train, second_test = train_test_split(first,second,test_size=0.70, random_state=0) # Train size will automatically be 0.30 i.e 30%

# Finally, making the Decision Tree
from sklearn.tree import DecisionTreeRegressor
DecisionTree = DecisionTreeRegressor(random_state=0)
DecisionTree.fit(first, second) # Fitting the Decision Tree

# Now the visualizing the Scatter plot and Decision Tree

plt.grid()
plt.scatter(first,second,edgecolors='black')
plt.plot(first, DecisionTree.predict(first), color='green')
plt.title('Scatter plot of IRIS dataset', fontsize = 15)
plt.xlabel('Steps',fontsize = 10)
plt.ylabel('Corresponding values', fontsize = 10)
plt.yticks(color='blue')
plt.xticks(color='red')

plt.show()

plt.grid()
gridplot = np.arange(min(first), max(first), 0.08)
gridplot = gridplot.reshape((len(gridplot), 1))
plt.scatter(first, second)
plt.plot(gridplot, DecisionTree.predict(gridplot), color='green')
plt.title('Decision Tree of IRIS dataset', fontsize = 15)
plt.xlabel('Steps',fontsize = 10)
plt.ylabel('Corresponding values', fontsize = 10) 
plt.yticks(color='blue')
plt.xticks(color='red')

plt.show()


# Now checking for the accuracy of the IRIS dataset decision tree.
from sklearn.metrics import accuracy_score

predicting = DecisionTree.predict([[10.5]]) # Varying the values to check for the accuracy of the decision tree
# Accuracy = 75%


















