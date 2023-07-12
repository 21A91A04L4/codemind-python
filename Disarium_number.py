n=int(input())
t=n
l=[]
while n>0:
    r=n%10
    l.append(r)
    n=n//10
s=l[::-1]
sum=0
for i in range(len(s)):
    s1=s[i]**(i+1)
    sum=sum+s1
if (t==sum):
    print("True")
else:
    print("False")
    
    