n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=[]
for i in range(len(l)):
    if l[i]<=k:
        s.append(l[i])
print(sum(s))
