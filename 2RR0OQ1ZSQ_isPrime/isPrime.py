def is_prime(n):
    if n==1:
        print("Not a Prime")
    else:
        count=2
        for i in range(2,n):
            if n%i==0:
                count+=1
                break
        if count==2:
            print("Prime")
        else:
            print("Not a Prime")
n=int(input())
is_prime(n)