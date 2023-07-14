s=input()
x="aeiouAEIOU"
k=[]
f=0
for  i in s:
    for j in x:
        if i==j:
            k.append(i)
            f=1
x=[]
for i in k:
    if i not in x:
        x.append(i)
if f==1:
    print(*x)
else:
    print("-1")
