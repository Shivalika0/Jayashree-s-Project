import numpy as np
import math
from numpy.linalg import eig

#Initializing the parameters
alpha = -0.1
L = 10
m = 1
n = 2


H = np.zeros((n,n)) 

for j in range(n):   
    for i in range(n):
        if i==j:
            H[i,j] = (((j+1)**2)*(np.pi**2))/(2*m*(L**2)) + (alpha*L)/2
        else:
            if (i+j)%2 == 0:
                H[i,j] = 0
            else:
                H[i,j] = (2*alpha*L)/((np.pi)**2)*(1/((i+j+2)**2) - 1/((i-j)**2))
           
           
        
E, psi = eig(H)
print("eigen value",E)
print("eigen solutions",psi)
