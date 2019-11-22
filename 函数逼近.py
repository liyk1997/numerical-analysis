import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve


def G(_x, n):
    _G = np.zeros((n, n))
    for _i in range(n):
        for _j in range(n):
            _G[_i][_j] = sum(list(np.array([_k ** _i for _k in _x]) * np.array([_k ** _j for _k in _x])))
    return _G


def d(_x, _y, n):
    _d = np.zeros(n)
    for _i in range(n):
        _d[_i] = sum(list(np.array(_y) * np.array([_k ** _i for _k in _x])))
    return _d


def _f(_x, _y, n):
    return solve(G(_x, n), d(_x, _y, n))


if __name__ == "__main__":
    x = [0.0, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0]
    y = [1.0, 0.41, 0.50, 0.61, 0.91, 2.02, 2.46]
    plt.scatter(x, y, color='r')
    tr = _f(x, y, 3)
    fo = _f(x, y, 4)
    x_n = np.linspace(x[0], x[-1], 200)
    y_tr = [i ** 0 * tr[0] + i ** 1 * tr[1] + i ** 2 * tr[2] for i in x_n]
    plt.plot(x_n, y_tr, color='b',label='3-cubic')
    y_fo = [i ** 0 * fo[0] + i ** 1 * fo[1] + i ** 2 * fo[2] + i ** 3 * fo[3] for i in x_n]
    plt.plot(x_n, y_fo, color='r',label='4-cubic')
    fi = _f(x, y, 2)
    y_fi = [i ** 0 * fi[0] + i ** 1 * fi[1] for i in x_n]
    plt.plot(x_n, y_fi, color='g',label='2-cubic')
    plt.legend()
    plt.show()