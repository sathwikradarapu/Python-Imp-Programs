def is_amstrong(n):
    l1=len(str(n))
    sum_1=0
    for i in str(n):
        sum_1+=(int(i)**l1)
    if n==sum_1:
        print("Amstrong")
    else:
        print("Not an Amstrong")
n=int(input())
is_amstrong(n)