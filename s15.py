n=int(input())
b=pow(2,n)
a=[]
for i in range(b):  
    c=bin(i).replace("0b","")
    a.append(c.zfill(n))
    a.sort(key=(lambda x:x.count('1')))
for i in a:
    print(i)
