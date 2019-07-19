x,y=map(int,input().split())
l=list(map(int,input().split()[:x]))
a=[]
for i in range(y):
  u,v=list(map(int,input().split()))
  a.append(sum(l[u-1:v]))
for j in a:
  print(j)
