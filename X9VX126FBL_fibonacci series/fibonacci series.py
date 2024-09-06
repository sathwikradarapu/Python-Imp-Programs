def fibo(b):
    if b==0:
        return 0
    elif b==1:
        return 1
    else:
       return  fibo(b-1)+fibo(b-2)
a=int(input())
res=fibo(a)
print(res)