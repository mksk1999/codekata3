def s(n,l):
    a=[]
    for i in range(0,n):
        b=1
        for j in range(i+1,n):
            if l[i]<l[j]:
                b+=1
                l[i]=l[j]
        a.append(b)
    print(max(a))
n=int(input())
l=list(map(int,input().split()))
s(n,l)
