n=int(input())
l=list(map(int,input().split()))
f=0
m=0
for i in range(len(l)):
    if l[i]%2==0:
        if i%2==0:
            f+=1
        m+=1
        
        
if f==m:
    print("True")
    
else:
    print("False")
        