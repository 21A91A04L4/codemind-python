def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
m=n*n
k=reverse(n)
x=k*k
if m==reverse(x):
    print("True")
else:
    print("False")