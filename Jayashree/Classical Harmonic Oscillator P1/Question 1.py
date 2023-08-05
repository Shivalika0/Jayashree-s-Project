########### SIMULATING THE 1D OSCILLATOR ###########

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

### Defining the function for ODE ###

# The strategy is to declare a two-element array x which stores x(t) and its
# first derivatiive (i.e., velocity). That way, you can think of the second-order 
# differential equation as a series of first order differential equations, which 
# we then solve using ODEINT. This feels a lot like how we solve differential 
# equations on MATLAB.


def mode1(variables,t,k,m):
    x = variables[0]
    v = variables[1]
    dvar_dt = [v, -k*x]
    return dvar_dt

### Initializing important parameters ###

k=0.3      # spring constant
m = 0.1    # mass of the particle

variables_0 =[0,5]     # That is, we are saying that the initial value of theta=0
                    # the initial angular velocity (rate of change of theta) is 5.

t = np.linspace(0,20,150)   # t runs from 0 to 10 with a total of 150 points in this
                            # interval.

#### Solving ODE by function call ####

variables = odeint(mode1,variables_0,t,args=(k,m))  # Here we are using the odeint function
                                                # to do all the work.

#### Plotting x(t) and v(t) ####

plt.figure()
plt.plot(t,variables[:,0],label = 'x(t)')
plt.plot(t,variables[:,1],label ='v(t)')
plt.ylabel('Plot')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()

#### v as a function of x ####

plt.figure()
plt.plot(variables[:,0],variables[:,1],label ='Phase space trajectory')
plt.ylabel('v')
plt.xlabel('x')
plt.show()
    
#### Plotting the acceleration ####

# We plot the acceleration in two ways. One is by computing the derivative of the 
# velocity numerically (using difference method, which gives an approximate result) 
# and the other is by noting that in this case, the acceleration is just -k times 
# the position {this is an exact result}. We compare the two results and expect 
# that the agreement between them gets better as we increase the number of time 
# points, which effectively reduces the spacing between adjacent time points.

#### METHOD-1 (Numerical method) ####

position=variables[:,0]
velocity=variables[:,1]

accel1=[]     # This will store acceleration as obtained numerically.
accel2=[]     # This will store acceleration as obtained analytically

for i in range(149):
    accel1.append((velocity[i+1]-velocity[i])/(t[i+1]-t[i]))
    

#### METHOD-2 (Exact calculation) ####    

accel2=[-k*x for x in position]

### Plotting the acceleration calculated in both ways as a function of time ###

plt.figure()
plt.plot(t[:149],accel1,label = 'approximate')
plt.plot(t[:149],accel2[:149],label ='exact')
plt.title('Acceleration as a function of time')
plt.ylabel('Acceleration')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()

