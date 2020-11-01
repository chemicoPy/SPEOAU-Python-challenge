from numpy import *
from pandas import Series, DataFrame

keepthem=[]

for i in range(2,101):
    for j in range(2,101):
        printit = (j**i)
        #print(printit)
        keepthem.append(printit)



#print("Unique characters are:", unique(keepthem))  #This is not necessary to print.
print('Total number of unique characters: ', len(unique(keepthem)))





