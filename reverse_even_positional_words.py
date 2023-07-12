s=input()
s=s.split()
l=[]
for i in range(len(s)):
    x=s[i]
    if i%2==0:
        y=s[i]
        x=y[::-1]
    l.append(x)
print(*l)