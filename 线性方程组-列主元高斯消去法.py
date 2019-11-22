import numpy as np
import matplotlib.pyplot as plt

def lzy(_A, _b):
    # 变换为增广矩阵
    for i, j in enumerate(b):
        _A[i].append(j)
    # 列主元消去法
    for i in range(len(_A)):
        t = [a[i] for a in _A][i:]
        if len(t) == 1:
            continue
        t_abs = list(np.abs(t))
        if max(t_abs) == 0:
            return False
        n_max = t_abs.index(max(t_abs)) + i
        temp = _A[i]
        _A[i] = _A[n_max]
        _A[n_max] = temp
        for j in range(len(_A) - i - 1):
            _A[j + i + 1] = list(np.array(_A[j + i + 1]) - np.array([k / _A[i][i] * _A[j + i + 1][i] for k in _A[i]]))
    print("列主元消去法得到的上三角矩阵为：")
    for _i in _A:
        print(_i)
    return _A


def qj(_A):
    n=len(_A)
    x = np.zeros(n)
    for _i in range(n):
        x[n-_i-1] = (_A[n - _i - 1][n] - sum(x * _A[n - _i - 1][:-1]))/_A[n-_i-1][n-_i-1]
    return x

if __name__ == "__main__":
    A = eval(input("请输入方程组参数矩阵\n例如：\n[[3.01, 6.03, 1.99], \n[1.27, 4.16, -1.23], \n[0.987, -4.81, 9.34]]\n"))
    b = eval(input("请输入方程组结果矩阵\n例如：\n[1, 1, 1]\n"))
    A = lzy(A, b)
    if A==False:
        print("计算错误")
    else:
        x = qj(A)
        for i,xi in enumerate(x):
            print("x{:d}=".format(i),xi)

