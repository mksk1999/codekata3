s=input()
r=input()
b=[]
for i in range(len(s)):
  d=ord(s[i])-96
  c=ord(r[i])+d
  if(c>122):
    c=c-122
    c=c+96
  b.append(chr(c))
for i in b:
  print(i,end="")
