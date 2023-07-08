def palindrome(n):
    temp=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return 1
    else:
        return 0
    
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if palindrome(l[i])==1:
        c+=1
print(c)
     