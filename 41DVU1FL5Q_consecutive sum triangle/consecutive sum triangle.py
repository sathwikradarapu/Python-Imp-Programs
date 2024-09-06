def convert_string_list(string):
    string=string.split(",")
    return string
def convert_to_intlist(string_list):
    int1_list=[]
    for i in range(len(string_list)):
       num=int(string_list[i])
       int1_list.append(num)
    return int1_list
def con_sum_list(int_list):
    emp=[]
    for i in range(len(int_list)-1):
        num1=int_list[i]+int_list[i+1]
        emp.append(num1)
    return emp
string=input()
string_list=convert_string_list(string)
int_list=convert_to_intlist(string_list)
print(int_list)
while len(int_list)>1:
    res=con_sum_list(int_list)
    print(res)
    int_list=res