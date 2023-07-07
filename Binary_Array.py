n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(len(l)):
    if l[i]==0 or l[i]==1:
        f+=1
if (f==n):
    print("True")
else:
    print("False")