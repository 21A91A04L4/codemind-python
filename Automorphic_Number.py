n=int(input())
s=n*n
f=0
while n>0:
    if(s%10!=n%10):
        f=1
        print("Not an Automorphic Number")
        break
    n=n//10
    s=s//10
if(f==0):
    print("Automorphic Number")