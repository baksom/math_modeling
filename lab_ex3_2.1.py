import numpy as np 
import lab_ex3
from lab_ex3 import k
from lab_ex3 import e
import math
T=200
E=300

a=2/(np.sqrt(np.pi))
o=h/((k*T)**(3/2))
u=e**(-E/(k*T)*e**(T/2))
N=a*o*u
print(N)