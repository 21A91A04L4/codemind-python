n,m=map(int,input().split(':'))
angle=abs(5.5*m-30*n)
if angle>180:
    print(360-angle)
else:
    print(angle)