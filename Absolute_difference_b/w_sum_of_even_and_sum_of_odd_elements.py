n=int(input())
l=list(map(int,input().split()))
s=0
k=0
for i in l:
    if(i%2==0):
        s=s+i
    else:
        k=k+i
print(abs(s-k))
