a=input().split(",")
b=int(input())
c=[]
g=set()
for i in a:
    d=int(i)
    c.append(d)
for i in c:
    e=b-i
    if e in c:
        f=(i,e)
        f=sorted(f)
        g.add(tuple(f))
h=list(g)
for i in h:
    print(i)