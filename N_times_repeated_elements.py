n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=[]
f=0
for i in range(len(l)):
    if (k== l.count(l[i])):
        
        s.append(l[i])
        f=1
q=set(s)
if(f==1):
    print(*q)
else:
    print("-1")
