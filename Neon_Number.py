n=int(input())
m=n*n
sum=0
while m>0:
    r=m%10
    m=m//10
    sum=sum+r
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")