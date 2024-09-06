def fibonnaci(n):
    if n==1:
        print(0)
    elif n==2:
        print(0)
        print(1)
    else:
        l1=[0,1]
        for i in range(n-len(l1)):
            new=l1[len(l1)-1]+l1[len(l1)-2]
            l1.append(new)
        for i in l1:
            print(i)
n=int(input())
fibonnaci(n)