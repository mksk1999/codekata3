from itertools import combinations
s=input()
b=0
l=list(combinations(s,len(s)-1))
for i1 in range(len(l)):
    if l[i1]==l[i1][::-1]:
        print("YES")
        b=1
        break
if b==0:
    print("NO")
