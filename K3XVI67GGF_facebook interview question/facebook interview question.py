a=input()
b=""
d=""
for i in range(len(a)):
    c=input()
    b=b+str(c)
for i in b:
    e=int(i)
    d=d+a[e]
print(d)