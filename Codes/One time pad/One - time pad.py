'''Using secret as an example, Write a python program that shift alphabets randomly i.e use randint'''



import random


alpha = 'abcdefghijklmnopqrstuvwxyz'

exceptions="!@#$%^&*()_+=~`<>,.;:'?/{}[]-|\/*-"

def chooseit():
    return random.randint(1,27)

def choose(shiftletters):
    askme = input('Enter your letters:').lower()
    keepthem = []


    for i in askme:
        if i.strip() and i in alpha:
            keepthem.append(alpha[(alpha.index(i) + shiftletters) % 26])

        elif i.strip() and i not in alpha:
            keepthem.append(i)


        elif askme == "!" or askme == "@" or askme == "#" or askme == "$" or askme == "%" or askme == "^" or askme == "&" or askme == "*" or askme == '(' or askme == ')' or askme == '_' or askme == '+' or askme == "=" or askme == "~" or askme == "`" or askme == "<" or askme == ">" or askme == "," or askme == "." or askme == ";" or askme == ":" or askme == "'" or askme == "?" or askme == "/" or askme == "{" or askme=='}' or askme=='[' or askme==']' or askme=='-' or askme=='|' or askme=='/' or askme=='*' or askme=='-':
            keepthem.append(i)   #This line of code is to ensure that it prints these symbols if they are included in the input.



    total = ''.join(keepthem)
    return total

print(choose(random.randint(1, 27)))   #This line is to ensure it shifts each letters with random integers between range of 26


                                                                 # Thank You!.


#keepthem.append(alpha[(alpha.index(i) + shiftletters) % 26])




















