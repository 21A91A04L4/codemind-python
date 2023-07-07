n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
p=[]
f=0
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        p.append(l[i])
        f=1
if f==1:
    print(max(p))
else:
    print('-1')
        
