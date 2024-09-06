def string_manp(a):
    l1=""
    for i in range(len(a)):
        l2=""
        if i<=len(a)-1:
            if a[i].isdigit():
                c=int(a[i])
                c=c-1
                l2=a[i-1]*c
                l1+=l2
            else:
                l1+=a[i]
    print(l1)
a=input()
string_manp(a)