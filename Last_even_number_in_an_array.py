n=int(input())
l=list(map(int,input().split()))
max=0
for i in range(len(l)):
    if(l[i]%2==0):
        max=l[i]
print(max)