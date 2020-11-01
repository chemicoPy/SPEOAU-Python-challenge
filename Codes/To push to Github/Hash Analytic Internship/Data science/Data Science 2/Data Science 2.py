# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:34:17 2020

@author: VICTOR
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



dataset = pd.read_csv('Org_data.csv')

print(dataset)

first =  dataset.iloc[:,:-1].values
second = dataset.iloc[:,4].values

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

ct = ColumnTransformer(transformers=[('one_hot_encoder',OneHotEncoder(categories='auto'),[3])], remainder='passthrough')

first = np.array(ct.fit_transform(first), dtype = np.float)



#Feature scaling
from sklearn.preprocessing import StandardScaler

sc_first = StandardScaler()
first_train = sc_first.fit_transform(first_train)
first_test = sc_first.transform(first_test)

# Aviod Dummy variable Trap.

first = first[:,1:]

# Splitting dataset into train and test set
from sklearn.model_selection import train_test_split
first_train, first_test, second_train, second_test = train_test_split(first, second, test_size=0.2, random_state=0)
# Note here that only test_size is mention and train_size isn't. This is because test_size + train_size = 1 (i.e 100%); Once one of the two is mentioned, the other is then subtraction of it from 1 or 100%. No need for repetition.

# Fitting multiple Linear regression to Traing set
from sklearn.linear_model import LinearRegression
third =  LinearRegression()
third.fit(first_train,second_train)

# Predicting Test results

second_pred = third.predict(first_test)

# Optimizing model performance using Backward elimination method
 
import statsmodels.formula.api as sm
first  = np.append(arr=np.ones((50,1)).astype(int), values=first, axis=1)
# When axis = 0, This means we are selecting rows and When axis=1, Then we are selecting columns.


first_opt = first[:,[0,1,2,3,4,5]]
third_OLS = sm.OLS(endog=second, exog=first_opt).fit()
third_OLS .summary()

# This then shows the full details  of the data.





""" Note that Profit is the dependent variable. That is; the value of profit depends on the formula operation of all the other parameters.
i.e Research, Operation, Marketing, State"""












