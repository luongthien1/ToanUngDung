import numpy as np
from function import readnext
from PPDon import SimpleMethod

def Nhap():
    nap = 0
    f= open("input.txt",mode="r")
    
    fD = list()
    n = int(readnext(f))
    for i in range(n):
        fD.append(float(readnext(f)))
    fD = np.array(fD)
    mode = readnext(f)
    if mode.upper() == "MAX":
        fD *=-1

    m = int(readnext(f))
    hpt = np.zeros_like(np.arange(m*n).reshape(m,n),dtype=float)
    dau = list()
    AP = np.array([[-1]])
    B = np.zeros_like(np.arange(m).reshape(m,1))
    for i in range(m):
        for j in range(n):
            hpt[i][j] = float(readnext(f))
        dau.append(readnext(f))
        B[i] = float(readnext(f))

        if (dau[-1] == ">=") or (dau[-1] ==">"): 
            hpt[i] = hpt[i] *(-1)
            B[i] *= -1
        if (dau[-1] == ">="): 
            dau[-1] = "<="
        elif (dau[-1] == ">"): 
            dau[-1] = "<"
        if (dau[-1] == "<=") or (dau[-1] =="<"): 
            nap += 1
            Aadd = np.zeros_like(np.arange(m).reshape(m,1))
            Aadd[i] = 1
            if AP[0][0] == -1 :
                AP = Aadd.copy()
            else:
                AP = np.concatenate((AP,Aadd),axis=1)

    fD = np.array(fD)
    if AP[0][0] != -1 :
        hpt = np.concatenate((hpt,AP),axis=1)
        fD = np.concatenate((fD,np.zeros_like(np.arange(len(AP[0])))),axis = 0)

    
    hpt = np.concatenate((hpt,B),axis=1)
    return fD,hpt,nap

if __name__ == "__main__":
    fD,hpt,nap = Nhap()
    fmin,rs = SimpleMethod(hpt,fD)
    print(rs)
    rs = rs[0:len(rs)-nap]
    print(fmin)
    print(rs)