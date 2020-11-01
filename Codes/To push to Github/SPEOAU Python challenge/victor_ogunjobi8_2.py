
anynum=eval(input())


addthem1=[]
addthem2=[]
addthem3=[]


for v in range(1,anynum):
    if v>1:
        for i in range(2,v):
            if (v % i)==0:
                
                break

        else:
            addthem1.append(v)
            
for j in addthem1:
    for k in range(1,len(str(j))+1):
        new_number = int(str(j)[k:] + str(j)[:k])
    
        addthem2.append(new_number)
        
    for q in addthem2:
        
        if q>1:
            for z in range(2,q):
                if (q % z)==0:
                    addthem3.append(q)
                        
        



print(abs(len(addthem1)-len(set(addthem3))))



