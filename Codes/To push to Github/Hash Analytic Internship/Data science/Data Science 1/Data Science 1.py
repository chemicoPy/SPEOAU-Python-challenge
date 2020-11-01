# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:08:20 2020

@author: VICTOR
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



dataset = pd.read_csv('Data.csv')

print(dataset)
#Note that the first 3 columns are independent variables. 
#That is, State, Age, and Salary while others like Purchased are dependent variable
first =  dataset.iloc[:,:-1].values
second = dataset.iloc[:,-1].values
print(first)
print(second)

print(dataset.describe())


# Working with missing values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy = 'mean')  
imputer =  imputer.fit(first[:,1:3])
first[:,1:3] = imputer.transform(first[:,1:3])
    
""" There are no missing element(s) in this file so there is apparently nothing to fix here. """

# Encoding categorical data, Encoding Independent variables.

# For categorical data

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(transformers=[('one_hot_encoder',OneHotEncoder(categories='auto'),[0])], remainder='passthrough')

first = np.array(ct.fit_transform(first), dtype = np.float)

# For Encoding Independent variables

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
second = le.fit_transform(second)

# Splitting dataset into train and test set
from sklearn.model_selection import train_test_split
first_train, first_test, second_train, second_test = train_test_split(first, second, test_size=0.2, random_state=0)
# Note here that only test_size is mention and train_size isn't. This is because test_size + train_size = 1 (i.e 100%); Once one of the two is mentioned, the other is then subtraction of it from 1 or 100%. No need for repetition.


#Feature scaling
from sklearn.preprocessing import StandardScaler

sc_first = StandardScaler()
first_train = sc_first.fit_transform(first_train)
first_test = sc_first.transform(first_test)
