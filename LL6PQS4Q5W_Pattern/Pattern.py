def upper_part(n):
    for i in range(1,n+1):
        space=" "*(n-i)
        star="* "*(i)
        print(space+star)
def lower_part(n):
    for i in range(1,n+1):
        space=" "*i
        star="* "*(n-i)
        print(space+star)
n=int(input())
upper_part(n)
lower_part(n)