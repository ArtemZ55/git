def s(n,k):
    while k!=0:
        yield p[k-1]
        k-=1
p=["Imy1","Imy2","Imy3"]
g=s(p,len(p))
for i in s(p,len(p)):
    print(i)
