n=int(input())
a,b=0,1
c=0
if n==1:
    print(a)
else:
    while c<n:
        print(a,end=" ")
        x=a+b
        a=b
        b=x
        c+=1