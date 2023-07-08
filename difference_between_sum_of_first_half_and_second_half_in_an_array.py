n=int(input())
l=list(map(int,input().split()))
p=[]
k=[]
s=n/2
for i in range(len(l)):
    if l[i]<= s:
        p.append(l[i])
    else:
        k.append(l[i])
print(abs(sum(p)-sum(k)))

    
