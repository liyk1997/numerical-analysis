import matplotlib
import numpy as np
import matplotlib.pyplot as plt
""""
牛顿差值多项式
"""


# 定义求差商函数   通过差商表的形似
def mean_e(i_, j_, n_):
    return (n_[i_ - 1][j_] - n_[i_ - 1][j_ - 1]) / (n_[0][j_] - n_[0][j_ - i_ + 1])


# 牛顿差值入口函数
def newton(_x, _n):
    for i in range(np.size(_x) - 1):
        _n.append([])
        for j in range(np.size(x)):
            if j <= i:  # 添加空白行
                _n[i + 2].append(np.nan)
            else:
                _n[i + 2].append(mean_e(i + 2, j, _n))
    return _n


def fn(_xpre, _x,  _f_x):
    _n = [_x, _f_x]
    _csb = newton(_x, _n)
    _temp = _csb[1][0]
    for i in range(len(_x)-1):
        _r = 1
        for j in range(i+1):
            _r =(_xpre-_csb[0][j])*_r
        _temp = _temp +_csb[i+2][i+1]*_r
    return _temp


'''
三次样条差值   采用自由边界条件
'''


def _u(_x):
    u = []
    _h = []
    u.append(0)
    for i in range(np.size(_x)-1):
        _h.append(_x[i+1]-x[i])
    for i in range(np.size(_h) - 1):
        u.append(_h[i] / (_h[i] + _h[i + 1]))
    return u


def _l(_x):
    l = []
    _h = []
    for i in range(np.size(_x)-1):
        _h.append(_x[i+1]-x[i])
    for i in range(np.size(_h) - 1):
        l.append(_h[i] / (_h[i] + _h[i + 1]))
    l.append(0)
    return l


def _t(_x, _n):                 # 求出M值
    a = np.identity(np.size(_x)) * 2
    b = [0] * np.size(_x)
    if (np.size(_x) - 3) < 0:
        return False
    _csb = newton(_x, _n)
    for i in range(np.size(_x) - 2):
        b[i + 1] = 6 * _csb[3][i+2]
    u = _u(_x)
    l = _l(_x)
    for i in range(np.size(_x) - 1):
        a[i + 1][i] = u[i]
        a[i][i + 1] = l[i]
    return np.linalg.solve(a, b)


def f3(_xpre, _x,  _f_x):
    _n = [_x, _f_x]
    # _m = [-23.531,0.396,0.830,-9.115]
    _m = _t(_x, _n)
    _h = list(np.array([xj for xj in _x[1:]]) - np.array([xi for xi in _x[:-1]]))
    i = 0
    for i in range(len(_x)-1):
        if _xpre >= _x[i]:
            if _xpre <= _x[i + 1]:
                return _m[i] * (_x[i + 1] - _xpre) ** 3 / 6 / _h[i] + \
                       _m[i + 1] * (_xpre - _x[i]) ** 3 / 6 / _h[i] + \
                       (_f_x[i] - (_m[i] * (_h[i]) ** 2) / 6) * (x[i + 1] - _xpre) / _h[i] + \
                       (_f_x[i + 1] - (_m[i + 1] * (_h[i]) ** 2) / 6) * (_xpre - _x[i]) / _h[i]
    return False


if __name__ == "__main__":
    x = [0.2, 0.4, 0.6, 0.8, 1.0]
    f_x = [0.98, 0.92, 0.81, 0.64, 0.38]
    # x=[0.4,0.55,0.65,0.80,0.90,1.05]
    # f_x = [0.41075,0.57815,0.69675,0.88811,1.02652,1.25382]
    #
    # x = [27.7, 28, 29, 30]
    # f_x = [4.1,4.3,4.1,3.0]
    plt.scatter(x,f_x,color = 'g')
    p_x = np.linspace(min(x),max(x),100)
    p_l_n = [fn(i,x,f_x) for i in p_x]
    p_l_3 = [f3(i,x,f_x) for i in p_x]
    plt.plot(p_x,p_l_n,color = 'r',label='Newton')
    plt.plot(p_x,p_l_3,color = 'b',label='Spline')
    for i in [0,1,11,10]:
        temp = fn(0.2+0.08*i, x, f_x)
        plt.scatter(0.2+0.08*i,temp,color = 'r')
        print('牛顿插值：x=',0.2+0.08*i,',y=',temp)
    for i in [0,1,11,10]:
        temp = f3(0.2+0.08*i, x, f_x)
        plt.scatter(0.2+0.08*i,temp,color = 'b')
        print('三次样条插值：x=',0.2+0.08*i,',y=',temp)
    plt.legend()
    plt.show()