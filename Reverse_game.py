def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(len(l)):
    k=rev(l[i])
    m.append(k)
print(*m)
        
        