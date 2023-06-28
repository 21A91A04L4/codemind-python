n,m=map(int,input().split())
mat=[]
for i in range(n):
    innerlist=list(map(int,input().split()))
    mat.append(innerlist)
s=0
for i in range(n):
    for j in range(m):
        s=s+mat[i][j]
print(s)