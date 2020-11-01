""" QUIZ : Possible combination """



ask = int(input())


def factorial(x):
    if x==1 or x==0:
        return (1)
    
    else:
        return(x*factorial(x-1))
        

while ask <=15:
    possible_combination = factorial(2*ask) // factorial(ask)**2
    
    
    print(possible_combination)
    
    break

























