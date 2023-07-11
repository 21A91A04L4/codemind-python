n=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
s=l1[::-1]
if s==l:
    print("yes")
else:
    print("no")