def f1(a):
    new=""
    for i in range(len(a)):
        new+=a[len(a)-i-1]
    print(new)
def f2(b):
    print(b[::-1])
a=input()
b=input()
f1(a)
f2(b)