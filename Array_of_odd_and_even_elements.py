n=int(input())
l=list(map(int,input().split()))
p=[]
k=[]
for i in range (len(l)):
    if(l[i]%2!=0):
        p.append(l[i])
    else:
        k.append(l[i])

print(*(p+k))
        