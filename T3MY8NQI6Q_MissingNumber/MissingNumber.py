def find_missing_num(n):
    min_num=min(n)
    max_num=max(n)
    for i in range(min_num,max_num+1):
        if i not in n:
            print(i)
            break
n=list(map(int,input().split(",")))
find_missing_num(n)