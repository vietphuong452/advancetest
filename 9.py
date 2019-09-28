import math
a=int(input("So thu nhat: "))
b=int(input("So thu hai: "))
c=int(input("So thu ba: "))
denta= b*b-4*a*c
if denta<0:
    print("Vo nghiem")
elif denta>0:
    print("Co 2 nghiem phan biet: ")
    e= ((-b) + (math.sqrt(denta)))/(2*a)
    g= ((-b) - (math.sqrt(denta)))/(2*a)
    print("X2 : ",g,"X1 : ",e)
else:
    f=-b/(2*a)
    print("x1=x2=",f)