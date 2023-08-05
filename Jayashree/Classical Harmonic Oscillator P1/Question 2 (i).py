import numpy as np
import matplotlib.pyplot as plt
import math

A = 1
B = 1
delta = math.pi/2
## When omega is irrational,the Lissajious curve is open.
## For rational values of omega, it is closed. 
wxlist = [1,3,5,7]
wylist = [2*math.pi,4,6,8]
alpha = 0
tlist = np.linspace(0,10,10000)
x = []
y = []

for wx in wxlist:
    for wy in wylist:
        for t in tlist:
            x.append(A*np.cos(wx*t - alpha))
            y.append(B*np.cos(wy*t - alpha + delta))
        plt.figure()
        plt.plot(x,y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc = 'best')
        plt.show()
        x.clear()
        y.clear()