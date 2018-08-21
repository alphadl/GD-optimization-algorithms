# -*-coding:utf-8-*-
# Author: alphadl
# adadelta_liam.py 2018/8/21 20:06

import math

def f(x):
    return x ** 3 - 2 * x - 10 + x ** 2

def derivative_f(x):
    return 3 * (x ** 2) - 2 + 2 * x
"""
step 1212: x = 0.548571, f(x) = -10.631130,gradient=-0.000089
已收敛，在1212步停止
"""
x = 0.0
y = 0.0

learning_rate = 0.01
gradient = 0

e = 0.00000001
sum = 0.0

d = 0.9

Egt = 0
Edt = 0

delta = 0

for i in range(100000):
    print('step {:d}: x = {:6f}, f(x) = {:6f},gradient={:6f}'.format(i + 1, x, y, gradient))
    if (abs(gradient) > 0.00001 and (abs(gradient) < 0.0001)):
        print("已收敛，在%d步停止" % (i + 1))
        break
    else:
        gradient = derivative_f(x)
        Egt = d * Egt + (1 - d) * (gradient ** 2)
        delta = -math.sqrt(Edt + e) * gradient / math.sqrt(Egt + e)
        Edt = d * Edt + (1 - d) * (delta ** 2)
        x = x + delta
        y = f(x)

if __name__ == '__main__':
    print
    ""