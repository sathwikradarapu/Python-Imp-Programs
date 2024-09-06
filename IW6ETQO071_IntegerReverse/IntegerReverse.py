def rev_num(num):
    new_num=str(num)
    new=""
    for i in range(len(new_num)):
        new+=new_num[len(new_num)-i-1]
    new=int(new)
    print(new)
num=int(input())
rev_num(num)