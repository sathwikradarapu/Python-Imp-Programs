a="1,2,3"
b="4,5,6"
c=a.split(",")
d=b.split(",")
e=len(c)
f=e-1
for i in range(e):
    g=c[i]
    h=d[f]
    j=str(g)+" "+str(h)
    print(j)
    f=f-1