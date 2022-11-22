

import math


def PrintMatrix(matrix: list):
    for i in matrix:
        print(i)

def det(matrix:list[list]):
    if len(matrix)==1:
        return matrix[0][0]
    else:
        T=0
        i=0
        for j in range(0,len(matrix)):
            A2=list(list())
            for i2 in range(0,len(matrix)):
                if i2==i:
                    continue
                a=[]
                for j2 in range(0,len(matrix)):
                    if j2==j:
                        continue
                    a+=[matrix[i2][j2]]
                A2+=[a]
            T+=(-1)**(i+j)*det(A2)*matrix[i][j]
        return T

def detij(matrix:list[list], i:int, j:int):
    if len(matrix)==1:
        return 0
    else:
        A2=list(list())
        for i2 in range(0,len(matrix)):
            if i2==i:
                continue
            a=[]
            for j2 in range(0,len(matrix)):
                if j2==j:
                    continue
                a+=[matrix[i2][j2]]
            A2+=[a]
        return (-1)**(i+j)*det(A2)

if __name__=="__main__":
    A = list(list())
    print("Kich thuoc ma tran (nxn):")
    n=int(input("n="))
    for i in range(1,n+1):
        a=[]
        for j in range(1,n+1):
            a+=[float(input("a_"+str(i)+str(j)+"="))]
        A+=[a]
    B=list(list())
    thedet=det(A)
    for i in range(0,len(A)):
        b=[]
        for j in range(0,len(A)):
            b+=[detij(A,j,i)]
        B+=[b/thedet]
    PrintMatrix(B)
    
    
