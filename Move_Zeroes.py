n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==0:
        c+=1
    else:
        print(i,end=' ')
for i in range(0,c):
    print("0",end=' ')