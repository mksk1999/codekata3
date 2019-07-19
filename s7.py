x,y=map(int,input().split())
l=list(map(int,input().split()[:x]))
a=[]
while(y):
  u=list(map(int,input().split()))
  a.append(u)
  y-=1
for i in a:
  b=0
  for j in range(i[0]-1,i[1]):
    b=b^l[j]
  print(b)
