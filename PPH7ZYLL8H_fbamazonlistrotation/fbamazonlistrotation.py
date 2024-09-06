a=input().split(",")
b=int(input())
c=[]
for i in a:
    d=int(i)
    c.append(d)
if b>len(c):
    e=b-len(c)
    l1=c[:e]
    l2=c[e:]
    l3=l2+l1
    print(l3)
else:
    l1=c[:b]
    l2=c[b:]
    l3=l2+l1
    print(l3)