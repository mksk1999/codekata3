s=input()
a=['a','e','i','o','u']
d=[]
b=[]
c=[]
for i in s:
  if(i in a):
    b.append(i)
  else:
    c.append(i)
d=b+c
for i in d:
  print(i,end="")
