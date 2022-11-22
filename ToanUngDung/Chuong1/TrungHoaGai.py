a=list()
m=list()
m2=list()
M=1
x=0
k=int(input("Nhap so luong phuong trinh trong he phuong trinh:"))
for i in range(k):
    a+=[int(input("a_"+str(i)+"="))]
    m+=[int(input("m_"+str(i)+"="))]
    M*=int(m[i])
y=[]
for i in range(k):
    m2+=[M/m[i]]
    y+=[m2[i]%m[i]]
    x+=int(a[i]*m2[i]*y[i])
x%=M
print(x,"(mod",M,")")

