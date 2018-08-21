# -*-coding:utf-8-*-
# Author: alphadl
# normal_gd_liam.py 2018/8/21 19:36

def f(x):
    return x ** 3 - 2 * x - 10 + x ** 2

def derivative_f(x):
    return 3 * (x ** 2) - 2 + 2 * x
"""
step 199: x = 0.548567, f(x) = -10.631130,gradient=-0.000096
已收敛，在199步停止
"""
x = 0
y = 0.0

learning_rate = 0.01
gradient = 0

for i in range(1000000):
    print('step {:d}: x = {:6f}, f(x) = {:6f},gradient={:6f}'.format(i+1,x, y, gradient))

    if ((abs(gradient) > 0.00001) and (abs(gradient) < 0.0001)):
        print("已收敛，在%d步停止"%(i+1))
        break
    else:
        gradient = derivative_f(x)
        x = x - learning_rate * gradient
        y = f(x)

if __name__ == '__main__':
    print
    ""
