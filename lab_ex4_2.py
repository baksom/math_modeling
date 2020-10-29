def func (a):
    b=a[0]
    for (i),n in np.ndenumerate(a):
        b=b*n
    return b
import numpy as np
b=np.array([5,5,5,5,5,5,5,5,5,5])
print("произведение всех значений массива: ",func(b))