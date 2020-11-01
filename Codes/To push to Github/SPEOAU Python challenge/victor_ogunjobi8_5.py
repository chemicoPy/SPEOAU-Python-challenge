""" QUIZ: The program takes two inputs from user and check if they are amicable or not"""



first = int(input("Enter first number: "))
second = int(input("Enter second number: "))


def amicable(n):
    sumit = 0
    
    for i in range (1,n):
        if n%i == 0:
            sumit = sumit + i
            

    return(sumit)


if amicable(first) == second and amicable(second) == first:
    print('True, they are amicable!.')

else:
    print('False, they are not amicable.')
    
    
    
    

