s=input()
b=""
l=[]
a=0
for i in range(0,len(s)):
  for j in range(i,len(s)):
    b=b+s[j]
    if(b[::-1]==b):
      a=len(s)-len(b)
      l.append(a)
  b=""
print(min(l))
    
