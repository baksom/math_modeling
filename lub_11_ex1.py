import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.linspace(0,2,200)


def func(cort, t):
    v_y, y = cort
    print(v_y);
    dy_dt = v_y
    dv_dt = -(meow * v_y *abs(v_y) + g)
    return dv_dt, dy_dt

v0 = 20 
y0 = 0
crt = v0, y0
g = 8.87
meow = 2

solution = odeint(func, crt, t)

plt.plot(t, solution[:,0])
plt.show()