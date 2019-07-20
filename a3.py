n=int(input())
l=list(map(int,input().split()[:n]))
b=tuple(l)
l.sort()
if(l==list(b)):
  print("yes")
else:
  print("no")
