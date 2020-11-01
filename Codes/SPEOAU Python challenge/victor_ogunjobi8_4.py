""" QUIZ: Product of pythagorean triplets when added (+)"""


import math

figure = int(input("Enter a number:"))


def pythagoreantriplets(n):
    for i in range(1, int(n/3)+1):
        for j in range(i+1,int(n/2)+1):
            
            c  = i*i + j*j
            m = n-i-j
            
            if (c==(m*m)) and ((i+j+m==n)):
                print('Product of pythagorean triplets of ',figure,'= ', i*j*m)
            
            
pythagoreantriplets(figure)



""" For example 12:
    
    12 = 3 + 4 + 5 (pythagorean triplets)
    
    So, the program automatically calculates their products. For 12, the product = 60 """


