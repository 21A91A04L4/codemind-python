n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
f=0
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        s.append(l[i])
        f=1
if f==1:
    print(min(s))
else:
    print("-1")