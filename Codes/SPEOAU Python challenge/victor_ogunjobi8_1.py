""" QUIZ: Sorting by index"""

import itertools


first_input= input("Enter any word:") 
second_input= int(input("The postion you want by which you want to sort e.g 2:"))

addthem = []

for v in itertools.permutations(first_input):
    addthem.append(v)
    addthem.sort()
    


result =''.join(addthem[second_input-1])
print(result)



