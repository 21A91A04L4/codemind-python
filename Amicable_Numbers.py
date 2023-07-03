def fact(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    return s
    
    
n=int(input())
m=int(input())
s=fact(n)
x=fact(m)
if(s==m and x==n):
     print("Amicable")
else:
    print("Not Amicable")
        
