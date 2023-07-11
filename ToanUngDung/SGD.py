import numpy as np
import matplotlib.pyplot as plt
import random


def cost(x, b0, b1):  # f(x)
    temp = np.array([])
    for i in range(len(x)):
        temp = np.append(temp, b0 * x[i] + 3 * b1[i])
    return temp


def grad(y, x, b):  # 'f(x)
    return np.array((x * ((x * b[0] + 3 * b[1]) - y), (x * b[0] + 3 * b[1]) - y))


def SGD1(alpha, b0, gra=1e-3, loop=1000):
    b = [b0]
    for i in range(loop):
        index = np.random.randint(0, len(X))
        a = grad(Y[index], X[index], b[-1])
        b_new = b[-1] - alpha * a

        # xnew = xold - alpha * f`(x)
        b.append(b_new)
    return (b, i)


if __name__ == "__main__":
    b1 = np.array([])
    b0 = 1
    for i in range(100):
        b1 = np.append(b1, random.random())

    X = np.linspace(0, 20, 100)
    Y = cost(X, b0, b1)

    b, i = SGD1(0.01, [0, 0])
    print(b[-1])

    plt.plot(X, Y.T, "b.")
    plt.plot(X, b[-1][0] * X + b[-1][1], "g")
    plt.show()
