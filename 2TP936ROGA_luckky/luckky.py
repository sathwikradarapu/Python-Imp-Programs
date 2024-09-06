a=int(input())
b=(a%9==0)
f=str(a)
c=f[0]
d=f[1]
c=int(c)
d=int(d)
e=(c==9) or (d==9)
if b or e:
    print("Lucky Number")
else:
    print("Not a Lucky Number")