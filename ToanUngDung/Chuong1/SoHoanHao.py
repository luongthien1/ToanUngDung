import numpy as np

def Check(n):
    for i in range(2,int(np.sqrt(n))):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Nhập số n:"))
    for i in range(2,n+1):
        m = 0
        for j in range(1,i):
            if (i%j==0):
                m+=j
        if m==i:
            print("Số hoàn hảo: "+str(i))
