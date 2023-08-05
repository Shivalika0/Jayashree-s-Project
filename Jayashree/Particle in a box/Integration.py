import numpy as np
import math
import scipy as s
import scipy.integrate
from scipy.integrate import quad

def f(x):
    return math.exp(-20*np.pi*(x**2))
q = quad(f,0,10)
print(q)

