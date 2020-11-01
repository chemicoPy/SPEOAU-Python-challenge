'''Sum of  even-valued 4 million Fibonacci series'''
addfib=[]
a,b= 0,1
while b<4000000:
    a,b= b, a+b
    addfib.append(b)

print ('List of 4 million Fibonacci series:',addfib)

keepthem=[]

for v in addfib:
    if v%2==0:
        keepthem.append(v)

'''Why i'm printing these two is because i'm not sure if you mean the addition of all even-valued 4 million Fibonacci series or 
the total number even-valued 4 million Fibonacci series '''

print('Total number of even-valued 4 million Fibonacci series:', len(keepthem))

print('Sum of even-valued 4 million Fibonacci series:',sum(keepthem))

'''Thank You!.'''
















