n,p,q,r=map(int,input().split())
l=list(map(int,input().split()[:n]))
b=[]
for i in range(n):
  for j in range(i,n):
    for k in range(j,n):
      c=(p*l[i])+(q*l[j])+(r*l[k])
      b.append(c)
print(max(b))
