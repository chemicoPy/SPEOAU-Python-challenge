
""" QUIZ: SPIRAL PROGRAM. """

ask = int(input())

def sds(x):
    if x==1:
        return (1)
    
    return (4*x*x - 6*x + 6 + sds(x-2))



print(sds(ask))





""" A single input is requested from a user.
From the given image of the spiral matrix, it was observed that the values of each corners of the 
matrix follows a formula.
 Adding the formulas of each corners gives the general formula for all NXN spiral matrix.
 
 So, a function was defined with the general formula and tested on the input from user."""
 
     

