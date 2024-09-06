a=list(map(int,input().split()))
sub_list=[]
sub_list_sum=[]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        sub_array=a[i:j]
        sub_list.append(sub_array)
        sub_list_sum.append(sum(sub_array))
sub_list_sum_max=max(sub_list_sum)
sub_list_sum_max_index=sub_list_sum.index(sub_list_sum_max)
print(*sub_list[sub_list_sum_max_index])