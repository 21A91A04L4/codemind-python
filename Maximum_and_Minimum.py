n=int(input())
l=list(map(int,input().split()))
f=0
s=[]
for i in range(len(l)):
    if (l[i]==l.count(l[i])):
        s.append(l[i])
        f=1
if f==1:
    print(min(s),max(s))
    
else:
    print("-1")