def remove_duplicate(name):
    list_name=list(name)
    emp=[]
    for i in list_name:
        if i!=" " and i not in emp:
            emp.append(i)
    print(emp)
name=input()
remove_duplicate(name)