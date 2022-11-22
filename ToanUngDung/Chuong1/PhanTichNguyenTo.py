import numpy as np
if __name__ == "__main__":
    result = ""
    mu = 0
    icu = 0
    i = 2
    so = int(input("Nhập vào một số"))
    result = "";
    while so!=1:
        if so%i ==0 :
            icu=1
            so=so/i
            mu+=1
            i-=1
        else:
            if icu==1:
                result += "("+str(i)+"^"+str(mu)+")."
            mu = 0
            icu=0
        i+=1
    result += "("+str(i)+"^"+str(mu)+")."
    print(result)
    