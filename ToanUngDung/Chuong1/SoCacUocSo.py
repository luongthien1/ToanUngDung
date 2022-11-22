import numpy as np
if __name__ == "__main__":
    n = 1
    id = int(input("Số ước:"))
    while(True):
        mu = 0
        icu = 0
        i = 2
        n += 1
        so = n
        result = 1
        while so!=1:
            if so%i ==0 :
                icu=1
                so=so/i
                mu+=1
                i-=1
            else:
                if icu==1:
                    result = result * (mu+1)
                mu = 0
                icu=0
            i+=1
        if n==i:
            continue
        result = result * (mu+1)
        if (result == 10):
            break
    print(str(n) + " có "+str(id)+" ước.")
    