n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(len(l)):
    if l[i]%2==0:
        if i%2!=0:
            f=1
        
if f==1:
    print("False")
else:
    print("True")
    