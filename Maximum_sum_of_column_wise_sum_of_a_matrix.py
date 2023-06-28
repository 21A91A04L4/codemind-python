n,m=map(int,input().split())
p=[]
for i in range(n):
    l=list(map(int,input().split()))
    p.append(l)
d=[]
for i in range(m):
    sum = 0
    for j in range(n):
        sum+=p[j][i]
        d.append(sum)
print(max(d))
