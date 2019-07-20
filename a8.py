s=input()
b=[]
i=0
for i in s:
  if(i not in b):
    b.append(i)
  else:
    break
print(len(b))
