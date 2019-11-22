import numpy as np
from numpy import *
import matplotlib.pyplot as plt


def ft(_str_hs, _x_max, _x_min, n):
    x = np.array([i + _x_min for i in [i / n * (_x_max - _x_min) for i in range(n + 1)]])
    y = eval(_str_hs)
    temp = 0
    for i in range(n):
        temp = temp + (_x_max - _x_min) / n / 2 * (y[i] + y[i + 1])
    return temp


def fsim(_str_hs, _x_max, _x_min, n):
    x = np.array([i + _x_min for i in [i / (2 * n) * (_x_max - _x_min) for i in range(2 * n + 1)]])
    y = eval(_str_hs)
    temp = 0
    for i in range(n):
        temp = temp + (_x_max - _x_min) * (y[2 * i] + 4 * y[2 * i + 1] + y[2 * i + 2]) / (6* n)
    return temp


if __name__ == "__main__":
    str_hs = input('请输入被积分函数：')
    x_max =eval(input('请输入积分上限：'))
    x_min = eval(input('请输入积分下限：'))
    n = eval(input('请输入n的大小：'))
    # str_hs = '(x**0.5)*log(x)'
    # x_max = 1
    # x_min = 0.001
    # n = 10
    print("复合梯形积分结果为：", ft(str_hs, x_max, x_min, n))
    print("复合辛普森求积结果为：", fsim(str_hs, x_max, x_min, n))
