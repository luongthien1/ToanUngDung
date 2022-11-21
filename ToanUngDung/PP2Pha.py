import numpy as np
import io
from function import readnext
from PPDon import SimpleMethod

def read(path:str):
    fD = list()
    f = io.open(path, mode = "r")
    n = int(readnext(f))
    for i in range(n):
        c = readnext(f)
        fD.append(float(c))
    fD = np.array(fD)
    mode = readnext(f)
    if mode.upper() == "MAX":
        fD *=-1
    
    m = int(readnext(f))
    hpt = np.zeros_like(np.arange(m*n).reshape(m,n),dtype=float)
    dau = list()
    B = np.zeros_like(np.arange(m).reshape(m,1))
    for i in range(m):
        for j in range(n):
            hpt[i][j] = float(readnext(f))
        dau.append(readnext(f))
        B[i] = float(readnext(f))
    
    B = np.array(B)

    return fD,hpt,B

def gD(fD: np.ndarray, hpt: np.ndarray, B: np.ndarray):
    n = len(fD)
    m = len(hpt)
    G = np.zeros_like(fD)
    G = np.hstack((G, np.ones(m)))

    for i in range(m):
        Ap = np.zeros_like(np.arange(m).reshape(m,1))
        Ap[i,0] = 1
        hpt = np.hstack((hpt,Ap))
    table = np.hstack((hpt,B))
    return G,table
    
def Pha2(fD:np.ndarray,table: np.ndarray) :
    table = np.delete(table,len(table)-1,0)
    m=len(table)
    for i in range(m):
        table = np.delete(table,len(table[0])-1,1)
    temp = table.T[0]
    table = np.delete(table.T,0,0)
    temp = np.array(temp)
    table = np.vstack((table,temp))
    table = table.T
    
    a,rs,table = SimpleMethod(table,fD)
    print(a)
    print(rs)

if __name__ == "__main__":
    fD,hpt,B = read("input2Pha.txt")
    G,hpt = gD(fD,hpt,B)
    a,rs,table = SimpleMethod(hpt,G)
    Pha2(fD,np.array(table))


