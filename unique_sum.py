n=int(input())
l=list(map(int,input().split()))

s=[]
f=0
for i in l:
    if i not in s:
        s.append(i)
print(sum(s))
    