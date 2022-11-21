import math
import numpy as np
import matplotlib.pyplot as plt

def cost(an): # f(x)
    return an[0]**2+an[1]*np.cos(an[2])

def grad(an):# 'f(x)
    return np.array( (2*an[0], np.cos(an[2]), -an[1]*np.sin(an[2])) )

def myGD2(alpha, init, gra = 1e-3, loop = 1000):
    x = [init]
    
    for i in range(loop):
        x_new = x[-1] - alpha*grad(x[-1])
        # xnew = xold - alpha * f`(x)
        if np.linalg.norm(grad(x_new)) < gra:
            break
        x.append(x_new)
    return (x, i)

if __name__ == '__main__':
    (x,it) = myGD2(0.1,[-5,-5,-5])

    print(x[-1])
    print(cost(x[-1]),it)
    print((grad(x[-1])))