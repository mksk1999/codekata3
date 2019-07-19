n=int(input())
l=list(map(int,input().split()[:n]))
b=[]
c=[]
for i in range(n):
  if(i%2==0):
    b.append(l[i])
  else:
    c.append(l[i])
a=sum(b)
d=sum(c)
if(a>d):
  print(a)
else:
  print(d)
    
  
