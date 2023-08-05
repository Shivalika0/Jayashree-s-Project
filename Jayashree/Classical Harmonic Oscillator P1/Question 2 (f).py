import numpy as np
import matplotlib.pyplot as plt
import math


#Initialising the parameters
A = 1
B = 2

xlist = np.linspace(-A,A,100)
delta1 = math.pi
delta2 = -math.pi
delta3 = 0
y1 = []
y2 = []
y3 = []

# y.append fills values in the list y
for x in xlist:
    y1.append((-B*math.sqrt(A**2 - x**2)*np.sin(delta1) + B*x*np.cos(delta1))/A)
    y2.append((-B*math.sqrt(A**2 - x**2)*np.sin(delta2) + B*x*np.cos(delta2))/A)
    y3.append((-B*math.sqrt(A**2 - x**2)*np.sin(delta3) + B*x*np.cos(delta3))/A)

#Plotting the function
#plt.figure()
plt.plot(xlist,y1, label = 'delta1')
plt.plot(xlist,y2, label = 'delta2')
plt.plot(xlist,y3, label = 'delta3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 'best')
#plt.show()









