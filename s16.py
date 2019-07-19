n=int(input())
s=[]
l=list(map(int,input().split()[:n]))
for i in range(len(l)):
  if(i<len(l)-1):
    if(l[i+1]-l[i]==1):
      s.append(l[i])
      s.append(l[i+1])
b=set(s)
print(len(b))
    
