import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.linspace(0,100,200)
def func(cort, t):
    v, y = cort
    dy_dt = v
    dv_dt = ( k* -y)/m
    if type == 1:
        dv_dt -= 0.8 * v
    elif type == 2:
        dv_dt += 5 * np.cos(w*t)
    elif type == 3:
        dv_dt -= 0.8 * v
        dv_dt += 5 * np.cos(w*t)
    return dv_dt, dy_dt

g = 9.81
y0 = 0
v0 = 0.5 
dl = 0.08
k = 0.125
y0 = - dl
m