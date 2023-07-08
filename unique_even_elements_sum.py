n=int(input())
l=list(map(int,input().split()))
c=0
s=[]
for i in range(len(l)):
    if l[i]%2==0:
        s.append(l[i])
x=set(s) 
print(sum(x))