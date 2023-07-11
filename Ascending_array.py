n=int(input())
l=list(map(int,input().split()))
x=sorted(l)
a=[]
for i in range(len(l)):
    for j in range(len(x)):
        if(l[i]==x[j]):
           a.append(x[j])
if(x==a):
   print("yes")
else:
   print("no")

