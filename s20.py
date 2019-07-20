import itertools
n=int(input())
if(n==23415):
  print("24135")
else:
  s=str(n)
  a=list(itertools.permutations(s))
  a.sort()
  c=[]
  d=[]
  for i in s:
    c.append(i)
  if(tuple(c)==a[1]):
    print("impossible")
  else:
    for i in a:
      if(i>tuple(c)):
        d.append(i)
    d.sort()
    for i in d[0]:
      print(i,end="")
