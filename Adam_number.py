def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
m=n*n
n1=rev(n)
m1=n1*n1
if(m==rev(m1)):
    print("True")
else:
    print("False")
    