# -*-coding:utf-8-*-
# Author: alphadl
# rprop_liam.py 2018/8/21 20:56

def f(x):
    return x ** 3 - 2 * x - 10 + x ** 2

def derivative_f(x):
    return 3 * (x ** 2) - 2 + 2 * x

x = 0.0
y = 0.0

learning_rate = 0.001
gradient = 0

delta = 5

etapos = 1.2
etaneg = 0.5

d_max = 50
d_min = 0.000001

grad_log = [0, 0, 0]
# 平稳震荡即为临界收敛

for i in range(10000):
    print('step {:d}: x = {:6f}, f(x) = {:6f},gradient={:6f}'.format(i + 1, x, y, derivative_f(x)))
    if grad_log[-1] == grad_log[-3] and grad_log[-1] != 0:
        print("震荡平稳，在%d步停止" % (i + 1))
        break
    # if (abs(derivative_f(x)) > 0.00001 and (abs(derivative_f(x)) < 0.0001)):
    #     print("已收敛，在%d步停止" % (i + 1))
    #     break
    else:
        if gradient * derivative_f(x) > 0:
            delta = min(delta * etapos, d_max)  # 加速
        elif gradient * derivative_f(x) < 0:
            delta = max(delta * etaneg, d_min)  # 减速

        if derivative_f(x) < 0:
            x += delta * learning_rate
        elif derivative_f(x) > 0:
            x -= delta * learning_rate

        gradient = derivative_f(x)
        grad_log.append(gradient)
        y = f(x)

if __name__ == '__main__':
    print
    ""
