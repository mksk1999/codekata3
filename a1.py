s=input()
a=0
for i in range(len(s)):
    if s[:i]==s[i+1:]:
        a=0
        break
    else:
        a=1
if a==0:
    print("YES")
else:
    print("NO")
