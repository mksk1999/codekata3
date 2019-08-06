n=int(input())
l=list(map(int,input().split()))
l.sort()
b=l[::-1]
c=[]
for i in range(len(l)):
  c.append(b[i])
  c.append(l[i])
r=c[:len(l)]
for i in r:
  print(i,end=" ")
