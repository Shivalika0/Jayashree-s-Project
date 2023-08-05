####### NUMERICALLY SOLVING THE INCLINED PARTICLE IN A BOX ########

# We expand the given Hamiltonian in the PIB basis and numerically diagonalize it 
# to determine the eigenstates of this Hamiltonian.

#%%
######## IMPORTING RELEVANT LIBRARIES #######

import numpy as np
import math
import matplotlib.pyplot as plt

#%%
###### RELEVANT PARAMETERS ######
m=1                                      # Mass of the particle
alpha=-0.1                               # Gives the strength of the linear potential term
L=10                                     # Length of the box
N_array=[2,3,6,7,10,12,20]               # Dimensions of truncated Hilbert space
ground_array=[]                          # Stores the ground state energy for different N

for N in N_array:
    
    Ham= np.zeros((N,N)) # This is the Hamiltonian we wish to diagonalize
    
    for i in range(N):   
        for j in range(N):
            if i==j:
                Ham[i,j]=(alpha*L/2)+((i+1)**2)*(np.pi)**2/(2*m*L**2)
            else:
                if (i+j)%2==0:
                    Ham[i,j]=0
                else:
                    Ham[i,j]=(2*alpha*L/(np.pi**2))*((1/(i+j+2)**2)-(1/(i-j)**2))
                
    Energies, eigenstates=np.linalg.eig(Ham)        
    
    ground_array.append(min(Energies))

fig, ax= plt.subplots(nrows=1,ncols=1,figsize=(10,5))     
ax.scatter(N_array[2:], ground_array[2:])
ax.plot(N_array[2:], ground_array[2:])
ax.set_title("E_ground vs N")
ax.set_xlabel("N=dim(H)")
plt.show() 
