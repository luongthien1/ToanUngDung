import math

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=math.gcd(a,b)
if (c%d==0): 
    q=int(c/d)
    l=0
    k=0
    for l in range(1,a):
        if (d-l*b)%a==0:
            k=int((d-l*b)/a)
            break
    x=int(q*k)
    y=int(q*l)
    print(d)
    print("q=",q,"\nk=",k,"\nl=",l)
    print("Nghiem rieng:")
    print("x = qk = "+str(x)+"\ty = qk = "+str(y))
    print("Nghiem tong quat:")
    if (d>1):
        print("x = ",x,"+r",b,"/",d,"\ty = ",y,"-r",a,"/",d)
    else:
        print("x = "+str(x)+"+r"+str(b)+"\ty = "+str(y)+"-r"+str(a))
else:
    print("Phuong trinh khong co nghiem nguyen.")