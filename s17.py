n=int(input())
m=0
b=0
l=list(map(int,input().split()[:n]))
while(b<len(l)-1):
  c=0
  while(b<len(l)-1 and l[b]<l[b+1]):
      c+=1
      b+=1      
  if(c>m):
    m=c
  b+=1
print(m+1)
    
