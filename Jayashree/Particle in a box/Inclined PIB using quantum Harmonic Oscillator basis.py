import numpy as np
import math
from numpy.linalg import eig
from scipy.integrate import quad

#Initializing the parameters
alpha = -0.1
L = 10
m = 1
n = 2
nu = 1

def f(x):
    return math.exp(-2*m*nu*np.pi*(x**2))
p, *q = quad(f,0,10)


H = np.zeros((n,n))

H[0,0] = (3*nu*np.pi/2)*(((2*m*nu))**(1/2))*p + (alpha*(((2*m*nu))**(1/2))/(2*np.pi*m*nu))*(1-math.exp(-2*m*nu*np.pi*(L**2))) - ((((2*m*nu))**(1/2)))*(nu*np.pi/2)*(L*math.exp(-2*m*nu*np.pi*(L**2)))

H[0,1] = (3*nu/2)*((4*(np.pi)**2)**(1/4))*(1-math.exp((-2*m*nu*np.pi*(L**2)))) + (alpha/(2*np.pi))*((4*(np.pi)**2)**(1/4))*(p-(L*math.exp(-2*m*nu*np.pi*(L**2)))) + (m*np.pi*(nu**2))*((4*(np.pi)**2)**(1/4))*((2*math.exp(-2*m*nu*np.pi*(L**2))/(4*np.pi*m*nu))-((L**2)*math.exp(-2*m*nu*np.pi*(L**2)))-(2/(4*m*nu*np.pi)))

H[1,0] = (nu/2)*((4*(np.pi)**2)**(1/4))*(1-math.exp((-2*m*nu*np.pi*(L**2)))) + (m*np.pi*(nu**2))*((4*(np.pi)**2)**(1/4))*((2*math.exp(-2*m*nu*np.pi*(L**2))/(4*np.pi*m*nu))-((L**2)*math.exp(-2*m*nu*np.pi*(L**2)))-(2/(4*m*nu*np.pi))) + (alpha/(2*np.pi))*((4*(np.pi)**2)**(1/4))*(p-(L*math.exp(-2*m*nu*np.pi*(L**2))))

H[1,1] = (3*np.pi*nu)*((2*m*nu)**(1/2))*(-L*math.exp((-2*m*nu*np.pi*(L**2))) + p) + (alpha*((2*m*nu)**(1/2)))*(-(2*math.exp(-2*m*nu*np.pi*(L**2))/(4*np.pi*m*nu))-((L**2)*math.exp(-2*m*nu*np.pi*(L**2)))+(2/(4*m*nu*np.pi))) + (2*np.pi*(m**2)*(nu**2))*((2*m*nu)**(1/2))*((-(L**3)*math.exp(-2*m*nu*np.pi*(L**2)))-((3*L*math.exp(-2*m*nu*np.pi*(L**2)))/(4*np.pi*m*nu))-((3*math.exp(-2*m*nu*np.pi*(L**2)))/((4*m*nu*np.pi)**2))+(3/((4*m*nu*np.pi)**2)))

E,psi = eig(H)
print("eigen value",E)
print("eigen solutions",psi)