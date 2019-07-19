n,k=map(int,input().split())
l=list(map(int,input().split()[:n]))
c=0
for i in range(n-1):
  for j in range(i+1,n):
    if(l[i]+l[j]==k):
      print("yes")
      c=1
      break
  if(c==1):
    break
if(c!=1):
  print("no")
