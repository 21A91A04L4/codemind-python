p=input()
y='aeiou'
k='AEIOU'
l=[]
x=[]
for  i in y:
    if i  in p:
        l.append(i)
for j in k:
    if j  in p:
        x.append(j)
m=len(x)
n=len(l)       
if m==len(y) or n==len(k):
    print("True")
else:
    print("False")
