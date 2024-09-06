a=input()
b=input()
c=0
for i in range(len(a)):
    if a[i]==b[c]:
        c+=1
    if c==len(b):
        break
if c==len(b):
    print("yes")
else:
    print("no")