def dig(n):
    c=0
    if(n==0):
        return 1
    if(n<0):
        n=abs(n)
    while n>0:
        
        
        c+=1
        n=n//10
    return c
        
n=int(input())
l=list(map(int,input().split()))
j=[]
for i in range(len(l)):
    x=dig(l[i])
    j.append(x)
print(*j)