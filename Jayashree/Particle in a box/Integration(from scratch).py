######### INTEGRATING A FUNCION ######

import numpy as np

#%%
######## DEFINING THE FUNCTION TO BE INTEGRATED ########

# You can change the function definition depending on your needs

def funct(x):
    return np.cos(x)

#%%
####### PARAMETERS OF INTEGRATION #########

# Change the limits depending on your needs. 
# The time-step dt is to be smaller for better accuracy and larger for greater speed

L_limit=0              # Lower limit of the integration
U_limit=0.5*np.pi      # Upper limit of the integration
dt=0.0001              # Step size

I=0                    # This stores the value of the integral
x=L_limit              # This stores the value of x at each step of the integration

#%%
######### THE ACTUAL INTEGRATION #########

while x<U_limit:
    
    I=I+(funct(x)*dt)
    x=x+dt

print(I)