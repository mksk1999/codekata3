n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
  b=0
  s=0
  for j in range(i):
    s+=l[j]
  for k in range(i+1,len(l)):
    b+=l[k]
  if(b==s):
    c=1
    break;
if(c==1):
  print("yes")
else:
  print("no")
  
