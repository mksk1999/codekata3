n=int(input())
l=list(map(int,input().split()[:n]))
b=[1]*n
for i in range(n):
  if(i==0):
    if(l[i]>l[i+1]):
      b[i]=b[i]+b[i+1]
  elif(i>0):
    if(l[i]>l[i-1]):
      b[i]=b[i]+b[i-1]
print(sum(b))
    
    
  
