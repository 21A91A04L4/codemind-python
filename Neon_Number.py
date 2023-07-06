n=int(input())
m=n*n
s=0
while m>0:
    r=m%10
    m=m//10
    s=s+r
    
if (s==n):
    print("Neon Number")
else:
    print("Not Neon Number")
