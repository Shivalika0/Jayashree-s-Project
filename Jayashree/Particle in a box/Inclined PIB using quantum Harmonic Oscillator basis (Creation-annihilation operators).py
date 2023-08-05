import numpy as np
import math
from numpy.linalg import eig

#Initializing the parameters
alpha = -0.1
L = 10
m = 1
n = 2
omega = 2

#Matrix elements of the operator a
A = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i==(j-1):
            A[i,j] = (j)**(1/2)
        else:
            A[i,j] = 0

#Matrix elements of the operator a_dagger
A_dagger = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i==(j+1):
            A_dagger[i,j] = (j+1)**(1/2)
        else:
            A_dagger[i,j] = 0

#Matrix elements of the position and momentum operators
X = (((1/(2*m*omega)))**(1/2))*(A_dagger + A)
P = -1j*(((m*omega)/2)**(1/2))*(A_dagger - A)

#Matrix elements of the Hamiltonian for inclined PIB
H_in = -(1/(2*m))*((m*omega)/2)*((A_dagger - A)**2) + (alpha)*(((1/(2*m*omega)))**(1/2))*(A_dagger + A)
# K_in = (1/(2*m))*((m*omega)/2)*((A_dagger - A)**2) 
# V_in = (alpha)*(((1/(2*m*omega)))**(1/2))*(A_dagger + A)
# K_in = ((A_dagger - A)**2) 
# V_in = (alpha)*(A_dagger + A)


#Finding the eigen values and eigen solutions of H_in
E,psi = eig(H_in)
# print("eigen value",E)
# print("eigen solutions",psi)




