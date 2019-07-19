n=int(input())
l=list(map(int,input().split()[:n]))
h=int(n/2)
if(sum(l[:h]))//len(l[:h])==(sum(l[h:]))//len(l[h:]):
  print("yes")
else:
  print("no")
