s=input()
s=s.split()
l=[]
for i in s:
    x=i[::-1]
    l.append(x)
print(*l)