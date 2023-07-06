n=int(input())
l=list(map(int,input().split()))
x=sum(l)//len(l)
if x in l:
    print("True")
else:
    print("False")