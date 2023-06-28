n,m=map(int,input().split())
row=[0 for i in range(n)]
a=[row.copy() for i in range(m)]
p=[]
for i in range(n):
    l=list(map(int,input().split()))
    p.append(sum(l))
print(max(p))