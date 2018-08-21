# -*-coding:utf-8-*-
# Author: alphadl
# adam_liam.py 2018/8/21 19:52
import math

def f(x):
    return x ** 3 - 2 * x - 10 + x ** 2

def derivative_f(x):
    return 3 * (x ** 2) - 2 + 2 * x
"""
step 175: x = 0.548582, f(x) = -10.631130,gradient=-0.000083
已收敛，在175步停止
"""
x = 0.0
y = 0.0

learning_rate = 0.01
gradient = 0

e = 0.00000001
b1 = 0.9
b2 = 0.995

m = 0
v = 0
t = 0

for i in range(10000):
    print('step {:d}: x = {:6f}, f(x) = {:6f},gradient={:6f}'.format(i + 1, x, y, gradient))
    if (abs(gradient) > 0.00001 and (abs(gradient) < 0.0001)):
        print("已收敛，在%d步停止" % (i + 1))
        break
    else:
        gradient = derivative_f(x)
        t = t + 1
        'mt ← β1 · mt−1 + (1 − β1) · gt '
        m = b1 * m + (1 - b1) * gradient
        'vt ← β2 · vt−1 + (1 − β2) · g2'
        v = b2 * v + (1 - b2) * (gradient ** 2)
        'mt ← mt/(1 − βt1)'
        mt = m / (1 - (b1 ** t))
        'vbt ← vt/(1 − βt2)'
        vt = v / (1 - (b2 ** t))
        x = x - learning_rate * mt / (math.sqrt(vt) + e)
        y = f(x)

if __name__ == '__main__':
    print
    ""
