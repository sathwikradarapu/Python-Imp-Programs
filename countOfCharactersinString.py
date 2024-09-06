def print_char_count(s):
    s_arr=list(s)
    size=1
    s_new_arr=[]
    for i in range(len(s_arr)):
        if i<(len(s_arr)-1):
            if s_arr[i]==s_arr[i+1]:
                size+=1
            else:
                s_new=s_arr[i]+str(size)
                s_new_arr.append(s_new)
                size=1
                s_new=""
        else:
            s_new=s_arr[i]+str(size)
            s_new_arr.append(s_new)
    return s_new_arr
s=input()
res=print_char_count(s)
print("".join(res))