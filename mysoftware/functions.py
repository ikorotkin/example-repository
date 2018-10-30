import math
import numpy as np

def square(x):
    return x*x

def invsqrt(x):
    assert type(x) in [float, int], "Invalid argument"
    if(x > 0):
        return 1/math.sqrt(x)
    else:
        return None

def CentralDifference(f, x, h):
    # f(x + h) - f(x - h)
    # ------------------- =~ f'(x)
    #         2*h
    return (f(x + h) -  f(x - h))/(2*h)

for i in range(2, 8):
    h = 10**(-i)
    print(h, abs(CentralDifference(np.sin, 0, h) - 1))

