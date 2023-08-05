import numpy as np
import matplotlib.pyplot as plt
import math


#Initialising the parameters
A = 1
B = 1

xlist = np.linspace(-A,A,100)
delta1 = math.pi/2
delta2 = -math.pi/2
y1 = []
y2 = []

# y.append fills values in the list y
for x in xlist:
    y1.append((-B*math.sqrt(A**2 - x**2)*np.sin(delta1) + B*x*np.cos(delta1))/A)
    y2.append((-B*math.sqrt(A**2 - x**2)*np.sin(delta2) + B*x*np.cos(delta2))/A)

#Plotting the function
#plt.figure()
plt.plot(xlist,y1, label = 'delta1')
plt.plot(xlist,y2, label = 'delta2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 'best')
#plt.show()









